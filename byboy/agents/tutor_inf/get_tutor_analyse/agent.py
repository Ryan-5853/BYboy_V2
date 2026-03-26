"""
批量导师页分析编排：
读取 get_tutor_pages 工作空间中的 state / cleaned，
调用 tutor_analyse 生成 cache/analysed/{导师名}_{序号}.json。
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from byboy.agent.invoke import AgentInvocation, ModelRef, slot_complete
from byboy.agents.tutor_inf.get_tutor_pages.agent import _resolve_cleaned_markdown
from byboy.agents.tutor_inf.link_choose import LinkChooseError, parse_llm_json_object
from byboy.agents.tutor_inf.logging_utils import AgentLogger
from byboy.agents.tutor_inf.tutor_analyse import TutorAnalyseAgent, TutorAnalyseError, TutorAnalysePayload
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.route_spec import ChatMessage

_ROOT_DIR = Path.cwd().resolve()

# 常见栏目/导航，形式上像「2～8 个汉字」但不是人名（启发式与 LLM 结果均需过滤）
_NOT_A_PERSON_NAME: frozenset[str] = frozenset(
    {
        "更多",
        "首页",
        "科学研究",
        "教学研究",
        "社会兼职",
        "研究方向",
        "研究领域",
        "教育经历",
        "工作经历",
        "个人简介",
        "个人简历",
        "团队成员",
        "主讲课程",
        "授课信息",
        "教学成果",
        "获奖信息",
        "招生信息",
        "学生信息",
        "我的相册",
        "教师博客",
        "联系我们",
        "联系方式",
        "论文成果",
        "专利",
        "著作成果",
        "科研项目",
        "教学资源",
        "研究成果",
        "荣誉奖励",
        "讲授课程",
        "英文主页",
        "教师主页",
        "导师简介",
        "基本信息",
        "学院概况",
        "师资队伍",
        "人才招聘",
        "新闻动态",
        "通知公告",
    }
)


class GetTutorAnalyseError(RuntimeError):
    """批量分析失败。"""


@dataclass(frozen=True, slots=True)
class GetTutorAnalysePayload:
    workspace_dir: str | Path
    analysed_subdir: str = "cache/analysed"


@dataclass(frozen=True, slots=True)
class GetTutorAnalyseResult:
    workspace_dir: Path
    analysed_dir: Path
    manifest_path: Path
    success_count: int
    skipped_count: int


def _read_json(path: Path, default_obj: Any) -> Any:
    if not path.is_file():
        return default_obj
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError:
        return default_obj


def _write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _normalize_url(url: str) -> str:
    return (url or "").strip()


def _as_set(values: list[str]) -> set[str]:
    return {str(v).strip() for v in values if isinstance(v, str) and str(v).strip()}


def _safe_filename_stem(name: str) -> str:
    x = re.sub(r'[\\/:*?"<>|]+', "_", (name or "").strip())
    x = re.sub(r"\s+", "", x)
    x = x.strip("._")
    return x or "unknown_tutor"


def _to_root_relative(path: str | Path) -> str:
    p = Path(path).resolve()
    try:
        return p.relative_to(_ROOT_DIR).as_posix()
    except ValueError:
        return os.path.relpath(str(p), str(_ROOT_DIR)).replace("\\", "/")


def _strip_heading_hashes(s: str) -> str:
    t = s.strip()
    return t.lstrip("#").strip()


def _extract_bold_cn_name(markdown_text: str, *, scan_chars: int = 6000) -> str | None:
    """常见教师页：简介区「**唐其鹏**」加粗姓名。"""
    chunk = markdown_text[:scan_chars] if len(markdown_text) > scan_chars else markdown_text
    for m in re.finditer(r"\*\*([\u4e00-\u9fff]{2,4})\*\*", chunk):
        s = m.group(1)
        if s not in _NOT_A_PERSON_NAME:
            return s
    return None


def _extract_h1_name(markdown_text: str) -> str | None:
    """从 Markdown 标题中猜姓名；跳过链接标题、栏目黑名单，并在多个标题中继续尝试。"""
    for line in markdown_text.splitlines():
        s = line.strip()
        if not s.startswith("#"):
            continue
        t = _strip_heading_hashes(s)
        if not t or "](" in t:
            continue
        compact = t.replace(" ", "")
        if compact in _NOT_A_PERSON_NAME:
            continue
        if re.fullmatch(r"[\u4e00-\u9fff]{2,8}", compact):
            return compact
    return None


_SYSTEM_NAME_FALLBACK = """你是文本提取助手。用户给出一页高校**教师个人主页**的 Markdown（常由 HTML 转换）及 URL。
请提取页面**主体介绍的一位**教师的中文姓名（多为 2～4 个汉字）。

规则：
- 只输出一个 JSON 对象：{"tutor_name_cn":"张三"}；无法唯一确定时 {"tutor_name_cn":null}。
- 姓名不要含职称、职务、空格与标点；若标题为「李四 教授」则只取「李四」。
- **禁止**把章节小标题当作姓名，例如：社会兼职、研究方向、教育经历、工作经历、团队成员、招生信息、获奖信息、专利、论文成果、首页、更多 等。
- 姓名常见于：加粗行（如 **王某某**）、简介首段、页眉姓名区，而不是「## 社会兼职」这类栏目。
- 若为名录/导航页、多人并列且无明确主人物，输出 null。

禁止输出 JSON 以外的任何内容。"""

# 单次兜底请求的 Markdown 节选上限（字符）
_NAME_FALLBACK_MD_CAP = 24_000


def _normalize_cn_name_candidate(raw: object) -> str | None:
    if raw is None:
        return None
    if not isinstance(raw, str):
        return None
    t = raw.strip()
    if not t or t.lower() in {"null", "none", "无", "未知"}:
        return None
    compact = re.sub(r"\s+", "", t)
    if re.fullmatch(r"[\u4e00-\u9fff]{2,8}", compact):
        if compact in _NOT_A_PERSON_NAME:
            return None
        return compact
    # 「姓名：张三」「教师: 李四」等：优先取分隔符右侧片段
    for sep in ("：", ":"):
        if sep in t:
            right = t.split(sep, 1)[-1].strip()
            rc = re.sub(r"\s+", "", right)
            if re.fullmatch(r"[\u4e00-\u9fff]{2,8}", rc) and rc not in _NOT_A_PERSON_NAME:
                return rc
    m = re.search(r"[\u4e00-\u9fff]{2,8}", t)
    cand = m.group(0) if m else None
    if cand is not None and cand in _NOT_A_PERSON_NAME:
        return None
    return cand


def _llm_resolve_tutor_name_cn(
    *,
    url: str,
    markdown_text: str,
    dispatcher: LLMDispatcher,
    slot_token: str,
    max_tokens: int,
    log: AgentLogger,
) -> str | None:
    excerpt = markdown_text if len(markdown_text) <= _NAME_FALLBACK_MD_CAP else markdown_text[:_NAME_FALLBACK_MD_CAP]
    messages: list[ChatMessage] = [
        {"role": "system", "content": _SYSTEM_NAME_FALLBACK},
        {
            "role": "user",
            "content": f"URL:\n{url}\n\n----- Markdown（节选） -----\n{excerpt}",
        },
    ]
    try:
        raw = slot_complete(
            dispatcher,
            slot_token,
            messages,
            max_tokens=max_tokens,
        )
    except Exception as e:
        log.warn(
            "LLM 姓名兜底调用失败",
            detail=f"{url[:100]} err={e!s}",
        )
        return None
    try:
        obj = parse_llm_json_object(raw)
    except LinkChooseError:
        log.warn("LLM 姓名兜底输出非合法 JSON", detail=url[:120])
        return None
    if not isinstance(obj, dict):
        return None
    return _normalize_cn_name_candidate(obj.get("tutor_name_cn"))


class GetTutorAnalyseAgent:
    def run(
        self,
        inv: AgentInvocation[GetTutorAnalysePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
        name_resolve_max_tokens: int = 512,
        name_resolve_llm_first: bool = True,
        max_workers: int = 4,
    ) -> GetTutorAnalyseResult:
        log = AgentLogger("GetTutorAnalyseAgent")
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        workspace_dir = Path(p.workspace_dir).resolve()
        log.start("开始批量导师分析", detail=str(workspace_dir))
        cache_dir = (workspace_dir / "cache").resolve()
        state_path = (cache_dir / "state.json").resolve()
        cleaned_dir = (cache_dir / "cleaned").resolve()
        analysed_dir = (workspace_dir / p.analysed_subdir).resolve()
        analysed_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = (analysed_dir / "manifest.json").resolve()

        if not state_path.is_file():
            raise FileNotFoundError(f"state.json 不存在: {state_path}")
        if not cleaned_dir.is_dir():
            raise FileNotFoundError(f"cleaned 目录不存在: {cleaned_dir}")

        state = _read_json(state_path, default_obj={})
        if not isinstance(state, dict):
            raise GetTutorAnalyseError("state.json 不是 JSON 对象")

        list2 = state.get("list2_tutor_profiles")
        records = state.get("records")
        if not isinstance(list2, list):
            raise GetTutorAnalyseError("state.list2_tutor_profiles 缺失或类型错误")
        if not isinstance(records, list):
            raise GetTutorAnalyseError("state.records 缺失或类型错误")
        if name_resolve_max_tokens <= 0:
            raise ValueError("name_resolve_max_tokens 必须为正整数")
        list4_analysed = state.get("list4_analysed_profiles")
        if not isinstance(list4_analysed, list):
            list4_analysed = []
            state["list4_analysed_profiles"] = list4_analysed
        analysed_set = _as_set(list4_analysed)

        record_map: dict[str, Path] = {}
        record_ref_map: dict[str, dict[str, Any]] = {}
        for rec in records:
            if not isinstance(rec, dict):
                continue
            url = _normalize_url(str(rec.get("url") or ""))
            cleaned_file = str(rec.get("cleaned_file") or "").strip()
            if not url or not cleaned_file:
                continue
            fp = _resolve_cleaned_markdown(
                cleaned_file, out_dir=workspace_dir, cleaned_dir=cleaned_dir
            )
            if fp is not None:
                record_map[url] = fp
                record_ref_map[url] = rec

        # 交替轮次模式下，list2_tutor_profiles 可能包含“本轮刚被 choice 发现，但还没来得及清洗生成 records”的 URL。
        # 直接遍历会造成大量 missing_cleaned_markdown_in_records 跳过。
        # 这里改为只分析 record_map 中已存在 cleaned markdown 的 URL，避免无效跳过并让轮次输出更稳定。
        list2_analysable: list[str] = []
        missing_cleaned_urls: list[str] = []
        for raw_url in list2:
            url = _normalize_url(str(raw_url or ""))
            if not url:
                continue
            if url in record_map:
                list2_analysable.append(url)
            else:
                missing_cleaned_urls.append(url)
        if missing_cleaned_urls:
            log.step(
                "过滤无 cleaned 的导师页",
                detail=f"analysable={len(list2_analysable)}/{len(list2)} missing_cleaned={len(set(missing_cleaned_urls))}",
            )

        analyser = TutorAnalyseAgent()
        success_items: list[dict[str, Any]] = []
        skipped_items: list[dict[str, Any]] = []

        pending_urls: list[str] = []
        total_all = len(list2_analysable)
        for i, raw_url in enumerate(list2_analysable, start=1):
            url = _normalize_url(str(raw_url or ""))
            if not url:
                continue
            if url in analysed_set:
                log.info("跳过已分析页面", detail=f"{i}/{total_all} {url}")
                continue
            pending_urls.append(url)

        def _worker(url: str) -> tuple[str, dict[str, Any]]:
            md_path = record_map.get(url)
            if md_path is None or not md_path.is_file():
                return ("skipped", {"url": url, "reason": "missing_cleaned_markdown_in_records"})
            md_text = md_path.read_text(encoding="utf-8", errors="replace")
            final_name = ""
            if name_resolve_llm_first:
                final_name = (
                    _llm_resolve_tutor_name_cn(
                        url=url,
                        markdown_text=md_text,
                        dispatcher=dispatcher,
                        slot_token=inv.model.token,
                        max_tokens=name_resolve_max_tokens,
                        log=log,
                    )
                    or ""
                ).strip()
            if not final_name:
                final_name = (_extract_h1_name(md_text) or "").strip()
            if not final_name:
                final_name = (_extract_bold_cn_name(md_text) or "").strip()
            if not final_name and not name_resolve_llm_first:
                final_name = (
                    _llm_resolve_tutor_name_cn(
                        url=url,
                        markdown_text=md_text,
                        dispatcher=dispatcher,
                        slot_token=inv.model.token,
                        max_tokens=name_resolve_max_tokens,
                        log=log,
                    )
                    or ""
                ).strip()
            if not final_name:
                return ("skipped", {"url": url, "reason": "cannot_resolve_unique_name"})

            stem = _safe_filename_stem(final_name)
            suffix = hashlib.sha1(url.encode("utf-8", errors="replace")).hexdigest()[:10]
            output_filename = f"{stem}_{suffix}.json"
            output_path = (analysed_dir / output_filename).resolve()
            try:
                result = analyser.run(
                    AgentInvocation(
                        model=ModelRef(inv.model.token),
                        llm_part=TutorAnalysePayload(
                            url=url,
                            tutor_name_cn=final_name,
                            output_dir=analysed_dir,
                            output_filename=output_filename,
                            markdown_path=md_path,
                        ),
                    ),
                    dispatcher,
                    max_tokens=max_tokens,
                )
            except Exception as e:
                try:
                    if output_path.exists():
                        output_path.unlink()
                except OSError:
                    pass
                return ("skipped", {"url": url, "reason": "tutor_analyse_failed", "error": str(e)})

            return (
                "success",
                {
                    "url": url,
                    "tutor_name_cn": final_name,
                    "cleaned_markdown": _to_root_relative(md_path),
                    "analysed_json": _to_root_relative(result.json_path),
                },
            )

        workers = max(1, int(max_workers))
        if pending_urls:
            log.step(
                "导师分析阶段",
                detail=f"待分析 {len(pending_urls)} 页 workers={workers}",
            )
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            fut_map = {ex.submit(_worker, u): u for u in pending_urls}
            done_i = 0
            for fut in concurrent.futures.as_completed(fut_map):
                done_i += 1
                url = fut_map[fut]
                log.step("导师分析进度", detail=f"[{done_i}/{len(pending_urls)}] {url}")
                try:
                    kind, payload_item = fut.result()
                except Exception as e:
                    skipped_items.append({"url": url, "reason": "worker_failed", "error": str(e)})
                    log.warn("跳过页面", detail=f"{url} worker_failed")
                    continue
                if kind != "success":
                    skipped_items.append(payload_item)
                    log.warn("跳过页面", detail=f"{url} {payload_item.get('reason', 'unknown')}")
                    continue
                success_items.append(payload_item)
                analysed_set.add(url)
                state["list4_analysed_profiles"] = sorted(analysed_set)
                rec_ref = record_ref_map.get(url)
                if isinstance(rec_ref, dict):
                    rec_ref["analysed_file"] = payload_item["analysed_json"]
                    rec_ref["analysed_name"] = payload_item["tutor_name_cn"]
                # 仅在 worker 成功完成后，由主线程同步状态，避免半成品污染断点。
                _write_json(state_path, state)
                log.info("完成单页分析", detail=f"{payload_item['tutor_name_cn']} -> {Path(payload_item['analysed_json']).name}")

        manifest = {
            "workspace_dir": _to_root_relative(workspace_dir),
            "state_path": _to_root_relative(state_path),
            "analysed_dir": _to_root_relative(analysed_dir),
            "success_count": len(success_items),
            "skipped_count": len(skipped_items),
            "success_items": success_items,
            "skipped_items": skipped_items,
        }
        _write_json(manifest_path, manifest)
        log.done(
            "批量分析完成",
            detail=f"success={len(success_items)} skipped={len(skipped_items)}",
        )

        return GetTutorAnalyseResult(
            workspace_dir=Path(_to_root_relative(workspace_dir)),
            analysed_dir=Path(_to_root_relative(analysed_dir)),
            manifest_path=Path(_to_root_relative(manifest_path)),
            success_count=len(success_items),
            skipped_count=len(skipped_items),
        )

    async def arun(
        self,
        inv: AgentInvocation[GetTutorAnalysePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
        name_resolve_max_tokens: int = 512,
        name_resolve_llm_first: bool = True,
        max_workers: int = 4,
    ) -> GetTutorAnalyseResult:
        return await asyncio.to_thread(
            self.run,
            inv,
            dispatcher,
            max_tokens=max_tokens,
            name_resolve_max_tokens=name_resolve_max_tokens,
            name_resolve_llm_first=name_resolve_llm_first,
            max_workers=max_workers,
        )


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "GetTutorAnalyseAgent",
    "GetTutorAnalyseError",
    "GetTutorAnalysePayload",
    "GetTutorAnalyseResult",
]
