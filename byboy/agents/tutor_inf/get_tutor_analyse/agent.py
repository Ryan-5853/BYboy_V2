"""
批量导师页分析编排：
读取 get_tutor_pages 工作空间中的 state / cleaned，
调用 tutor_analyse 生成 cache/analysed/{导师名}_{序号}.json。
"""

from __future__ import annotations

import asyncio
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.logging_utils import AgentLogger
from byboy.agents.tutor_inf.tutor_analyse import TutorAnalyseAgent, TutorAnalyseError, TutorAnalysePayload
from byboy.llm.dispatcher import LLMDispatcher

_ROOT_DIR = Path.cwd().resolve()


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


def _resolve_maybe_relative(path_text: str | Path, *, base_dir: Path) -> Path:
    p = Path(path_text)
    if p.is_absolute():
        return p.resolve()
    c1 = (base_dir / p).resolve()
    if c1.exists():
        return c1
    return p.resolve()


def _extract_h1_name(markdown_text: str) -> str | None:
    for line in markdown_text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            t = s.lstrip("#").strip()
            # 常见中文姓名长度 2-8；允许中间空格。
            if re.fullmatch(r"[\u4e00-\u9fff]{2,8}", t.replace(" ", "")):
                return t.replace(" ", "")
            return None
    return None


class GetTutorAnalyseAgent:
    def run(
        self,
        inv: AgentInvocation[GetTutorAnalysePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
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
            fp = _resolve_maybe_relative(cleaned_file, base_dir=workspace_dir)
            if fp.is_file():
                record_map[url] = fp
                record_ref_map[url] = rec

        analyser = TutorAnalyseAgent()
        per_name_counter: dict[str, int] = {}
        success_items: list[dict[str, Any]] = []
        skipped_items: list[dict[str, Any]] = []

        total = len(list2)
        for i, raw_url in enumerate(list2, start=1):
            url = _normalize_url(str(raw_url or ""))
            if not url:
                continue
            if url in analysed_set:
                log.info("跳过已分析页面", detail=f"{i}/{total} {url}")
                continue
            log.step("处理导师页面", detail=f"{i}/{total} {url}")
            md_path = record_map.get(url)
            if md_path is None or not md_path.is_file():
                skipped_items.append(
                    {"url": url, "reason": "missing_cleaned_markdown_in_records"}
                )
                log.warn("跳过页面", detail=f"{url} missing_cleaned_markdown_in_records")
                continue

            md_text = md_path.read_text(encoding="utf-8", errors="replace")
            name_from_h1 = _extract_h1_name(md_text)
            final_name = (name_from_h1 or "").strip()
            if not final_name:
                skipped_items.append({"url": url, "reason": "cannot_resolve_unique_name"})
                log.warn("跳过页面", detail=f"{url} cannot_resolve_unique_name")
                continue

            stem = _safe_filename_stem(final_name)
            idx = per_name_counter.get(stem, 0) + 1
            per_name_counter[stem] = idx
            output_filename = f"{stem}_{idx}.json"

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
            except TutorAnalyseError as e:
                skipped_items.append(
                    {
                        "url": url,
                        "reason": "tutor_analyse_failed",
                        "error": str(e),
                    }
                )
                log.warn("跳过页面", detail=f"{url} tutor_analyse_failed")
                continue
            success_items.append(
                {
                    "url": url,
                    "tutor_name_cn": final_name,
                    "cleaned_markdown": _to_root_relative(md_path),
                    "analysed_json": _to_root_relative(result.json_path),
                }
            )
            analysed_set.add(url)
            state["list4_analysed_profiles"] = sorted(analysed_set)
            rec_ref = record_ref_map.get(url)
            if isinstance(rec_ref, dict):
                rec_ref["analysed_file"] = _to_root_relative(result.json_path)
                rec_ref["analysed_name"] = final_name
            # 每成功一个导师页就即时落盘，支持中断恢复不重复。
            _write_json(state_path, state)
            log.info("完成单页分析", detail=f"{final_name} -> {output_filename}")

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
    ) -> GetTutorAnalyseResult:
        return await asyncio.to_thread(self.run, inv, dispatcher, max_tokens=max_tokens)


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "GetTutorAnalyseAgent",
    "GetTutorAnalyseError",
    "GetTutorAnalysePayload",
    "GetTutorAnalyseResult",
]
