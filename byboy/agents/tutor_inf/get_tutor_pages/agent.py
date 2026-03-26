"""
导师页面链接抓取编排：
维护三类 URL 列表（待处理/导师页/已处理），串联 web_clean 与 link_choose 做迭代。
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import json
import os
import re
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.link_choose import LinkChooseAgent, LinkChoosePayload
from byboy.agents.tutor_inf.logging_utils import AgentLogger
from byboy.agents.tutor_inf.transient_errors import (
    run_with_transient_llm_retries,
    try_switch_fast_slot_pair,
)
from byboy.agents.tutor_inf.web_clean import FirecrawlError, WebCleanAgent, WebCleanPayload
from byboy.llm.dispatcher import LLMDispatcher

_ROOT_DIR = Path.cwd().resolve()


class GetTutorPagesError(RuntimeError):
    """抓取编排阶段性失败。"""


@dataclass(frozen=True, slots=True)
class GetTutorPagesPayload:
    """学院站点 URL + 输出目录 + 最大迭代深度。"""

    academy_url: str
    output_dir: str | Path
    max_depth: int = 2
    resume_state_path: str | Path | None = None
    #: 传给 link_choose：True 每条链接都经 LLM；False 仅低置信链接经 LLM。
    link_choose_refine_all_links: bool = True
    #: 本任务所属学院/单位名称（供链接分类防串院）；须由调用方传入，勿依赖进程级环境变量。
    academy_scope_hint: str | None = None
    #: 同一大轮（同一 ``round``）内，「名录下一页」类链接最多追加清洗次数；不计入 ``max_depth``。0 表示关闭。
    listing_pagination_max_passes: int = 80
    #: 单页 link_choose 内多批 LLM（每批约 50 条链接）并行 worker；1 为串行。总并发约 ``choice_max_workers * 本值``。
    link_choose_refine_batch_parallel_workers: int = 1


@dataclass(frozen=True, slots=True)
class GetTutorPagesResult:
    output_dir: Path
    cache_dir: Path
    cleaned_dir: Path
    choice_dir: Path
    state_path: Path
    round_count: int
    list1_pending_count: int
    list2_tutor_profile_count: int
    list3_processed_count: int


_PAGINATION_QS_KEYS = frozenset(
    {
        "page",
        "pageno",
        "pagenum",
        "p",
        "pn",
        "offset",
        "start",
        "startrow",
        "curpage",
        "currentpage",
        "currpage",
        "pageindex",
        "pi",
        "nowpage",
        "pagesize",
        "size",
        "limit",
        "rows",
    }
)

# 树形/栏目导航类站点（如东大 faculty.neu xyjslb.jsp?wbtreeid=&id=）靠 query 区分不同列表，不可剥掉。
_TREE_NAV_QS_KEYS = frozenset(
    {
        "id",
        "wbtreeid",
        "treeid",
        "urltype",
        "nodeid",
        "menuid",
        "cid",
        "catid",
        "columnid",
    }
)

_KEEP_QUERY_KEYS = _PAGINATION_QS_KEYS | _TREE_NAV_QS_KEYS


def _normalize_url(url: str) -> str:
    """抓取状态去重主键：默认同 path；若 query 含分页或树形导航参数则保留规范化后的 query。"""
    return _crawl_url_key(url)


def _crawl_url_key(url: str) -> str:
    u = (url or "").strip()
    if not u:
        return ""
    parts = urlsplit(u)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        return ""
    path = parts.path or "/"
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    q_pairs = [(k.strip().lower(), v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k]
    if any(k in _KEEP_QUERY_KEYS for k, _ in q_pairs):
        q_norm = sorted(q_pairs)
        query = urlencode(q_norm)
        return urlunsplit((scheme, netloc, path, query, ""))
    # 其它 query 仍忽略，避免追踪参数导致重复爬同一正文页。
    return urlunsplit((scheme, netloc, path, "", ""))


def _resolve_url(raw_url: str, source_url: str) -> str:
    s = (raw_url or "").strip()
    if not s:
        return ""
    if s.startswith(("mailto:", "tel:", "javascript:", "#")):
        return ""
    abs_u = urljoin(source_url, s)
    return _crawl_url_key(abs_u)


def _is_choice_listing_pagination_next(item: dict[str, Any]) -> bool:
    """是否名录「下一页」专道：仅认 link_choose 产出的 listing_pagination_next（由 LLM 判定）。"""
    v = str(item.get("listing_pagination_next") or "").strip().lower()
    return v == "1"


def _safe_slug_from_url(url: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", url.strip()).strip("_")
    if len(s) > 80:
        s = s[:80]
    return s or "url"


def _cleaned_filename(url: str, seq: int) -> str:
    return f"{seq:05d}_{_safe_slug_from_url(url)}_cleaned.md"


_CLEANED_SEQ_PREFIX_RE = re.compile(r"^(\d{5})_", re.ASCII)


def _max_seq_from_cleaned_basename(name: str) -> int | None:
    m = _CLEANED_SEQ_PREFIX_RE.match(name)
    if not m:
        return None
    try:
        return int(m.group(1), 10)
    except ValueError:
        return None


def _max_cleaned_seq_from_records(records: object) -> int:
    m = 0
    if not isinstance(records, list):
        return 0
    for rec in records:
        if not isinstance(rec, dict):
            continue
        cf = str(rec.get("cleaned_file") or "").strip()
        if not cf:
            continue
        base = Path(cf.replace("\\", "/")).name
        n = _max_seq_from_cleaned_basename(base)
        if n is not None:
            m = max(m, n)
    return m


def _max_cleaned_seq_from_dir(cleaned_dir: Path) -> int:
    m = 0
    if not cleaned_dir.is_dir():
        return 0
    try:
        for p in cleaned_dir.iterdir():
            if not p.is_file():
                continue
            n = _max_seq_from_cleaned_basename(p.name)
            if n is not None:
                m = max(m, n)
    except OSError:
        return m
    return m


def _reconcile_cleaned_seq(
    state: dict[str, Any],
    cleaned_dir: Path,
    *,
    log: AgentLogger,
) -> bool:
    """
    中断可能发生在 web_clean 落盘之后、state.json 更新 seq 之前，重启后 seq 偏小会
    生成重复编号甚至覆盖文件。用 records 与 cleaned 目录中已有 ``#####_`` 前缀抬升 seq。
    """
    cur = int(state.get("seq") or 0)
    floor = max(
        _max_cleaned_seq_from_records(state.get("records")),
        _max_cleaned_seq_from_dir(cleaned_dir),
    )
    if floor > cur:
        state["seq"] = floor
        log.step("已对齐 cleaned 序号", detail=f"seq {cur} -> {floor}（避免中断后编号回退）")
        return True
    return False


def _choice_filename(cleaned_filename: str) -> str:
    stem = Path(cleaned_filename).stem
    return f"{stem}.choice.json"


def _to_root_relative(path: str | Path) -> str:
    p = Path(path).resolve()
    try:
        return p.relative_to(_ROOT_DIR).as_posix()
    except ValueError:
        return os.path.relpath(str(p), str(_ROOT_DIR)).replace("\\", "/")


def _to_workspace_relative(path: str | Path, workspace: Path) -> str:
    """将路径存为相对工作目录（output_dir），避免与 base_dir 拼接时错位。"""
    p = Path(path).resolve()
    w = workspace.resolve()
    try:
        return p.relative_to(w).as_posix()
    except ValueError:
        return _to_root_relative(p)


def _resolve_cleaned_markdown(
    path_text: str,
    *,
    out_dir: Path,
    cleaned_dir: Path,
) -> Path | None:
    """
    解析 state 里记录的 cleaned markdown 路径。
    兼容：相对 workdir、仅 basename、旧版相对仓库根、以及当前工作目录。
    """
    s = (path_text or "").strip()
    if not s:
        return None
    p = Path(s)
    if p.is_absolute():
        r = p.resolve()
        return r if r.is_file() else None
    cand = (out_dir / p).resolve()
    if cand.is_file():
        return cand
    norm = s.replace("\\", "/")
    mark = "cache/cleaned/"
    if mark in norm:
        tail = norm.split(mark, 1)[-1].lstrip("/")
        if tail:
            c2 = (out_dir / "cache" / "cleaned" / tail).resolve()
            if c2.is_file():
                return c2
    c3 = (cleaned_dir / p.name).resolve()
    if c3.is_file():
        return c3
    c4 = p.resolve()
    if c4.is_file():
        return c4
    return None


def _resolve_existing_choice_path(
    rec_choice_text: str,
    *,
    out_dir: Path,
    choice_dir: Path,
    choice_filename: str,
) -> Path | None:
    """若 choice JSON 已存在于标准路径或 state 记录的路径，返回绝对路径。"""
    default_p = (choice_dir / choice_filename).resolve()
    if default_p.is_file():
        return default_p
    s = (rec_choice_text or "").strip()
    if not s:
        return None
    p = Path(s)
    if p.is_absolute() and p.is_file():
        return p.resolve()
    cand = (out_dir / p).resolve()
    if cand.is_file():
        return cand
    norm = s.replace("\\", "/")
    mark = "cache/choice/"
    if mark in norm:
        tail = norm.split(mark, 1)[-1].lstrip("/")
        if tail:
            c2 = (out_dir / "cache" / "choice" / tail).resolve()
            if c2.is_file():
                return c2
    c3 = (choice_dir / p.name).resolve()
    if c3.is_file():
        return c3
    c4 = p.resolve()
    if c4.is_file():
        return c4
    return None


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


def _acquire_file_lock(lock_path: Path, *, timeout_sec: float = 30.0, poll_sec: float = 0.2) -> int:
    """通过原子创建 lock 文件实现轻量互斥，避免并发重复处理。"""
    deadline = time.time() + timeout_sec
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    while True:
        try:
            fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            payload = {"pid": os.getpid(), "ts": time.time()}
            os.write(fd, (json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8"))
            return fd
        except FileExistsError:
            if time.time() >= deadline:
                raise GetTutorPagesError(f"获取锁超时: {lock_path}")
            time.sleep(poll_sec)


def _release_file_lock(lock_fd: int | None, lock_path: Path) -> None:
    if lock_fd is not None:
        try:
            os.close(lock_fd)
        except OSError:
            pass
    try:
        if lock_path.exists():
            lock_path.unlink()
    except OSError:
        pass


def _init_state(academy_url: str) -> dict[str, Any]:
    init_url = _normalize_url(academy_url)
    if not init_url:
        raise ValueError(f"academy_url 需要是 http(s) URL，当前为 {academy_url!r}")
    return {
        "round": 0,
        "seq": 0,
        "list1_possible_pages": [init_url],
        "list2_tutor_profiles": [],
        "list3_processed_pages": [],
        "records": [],
    }


def _as_set(values: list[str]) -> set[str]:
    return {v for v in values if isinstance(v, str) and v.strip()}


def _validate_state_shape(state: dict[str, Any]) -> None:
    required = {
        "round": int,
        "seq": int,
        "list1_possible_pages": list,
        "list2_tutor_profiles": list,
        "list3_processed_pages": list,
        "records": list,
    }
    for key, typ in required.items():
        if key not in state:
            raise GetTutorPagesError(f"state 缺少字段: {key}")
        if not isinstance(state[key], typ):
            raise GetTutorPagesError(f"state.{key} 类型错误，期望 {typ.__name__}")


def _validate_choice_schema(obj: dict[str, Any]) -> None:
    links = obj.get("clickable_links")
    if not isinstance(links, list):
        raise GetTutorPagesError("link_choose 输出缺少 clickable_links 数组")
    for i, item in enumerate(links):
        if not isinstance(item, dict):
            raise GetTutorPagesError(f"clickable_links[{i}] 必须为对象")
        for k in ("url", "category", "category_confidence"):
            if not isinstance(item.get(k), str) or not str(item.get(k)).strip():
                raise GetTutorPagesError(f"clickable_links[{i}].{k} 必须为非空字符串")


def _resolve_cache_layout(
    output_dir: str | Path,
    resume_state_path: str | Path | None,
) -> tuple[Path, Path, Path, Path]:
    if resume_state_path is not None:
        state_path = Path(resume_state_path).resolve()
        if state_path.name.lower() != "state.json":
            raise ValueError("resume_state_path 必须指向 state.json")
        if not state_path.is_file():
            raise FileNotFoundError(f"resume_state_path 不存在: {state_path}")
        cache_dir = state_path.parent.resolve()
        cleaned_dir = (cache_dir / "cleaned").resolve()
        choice_dir = (cache_dir / "choice").resolve()
        out_dir = cache_dir.parent.resolve()
        return out_dir, cache_dir, cleaned_dir, choice_dir

    out_dir = Path(output_dir).resolve()
    cache_dir = (out_dir / "cache").resolve()
    cleaned_dir = (cache_dir / "cleaned").resolve()
    choice_dir = (cache_dir / "choice").resolve()
    return out_dir, cache_dir, cleaned_dir, choice_dir


def _pick_high_confidence_urls(
    *,
    choice_json: dict[str, Any],
    source_url: str,
) -> tuple[set[str], set[str], list[tuple[str, str, dict[str, Any]]]]:
    """返回 (list1 高置信 URL, list2 导师主页, tutor_expansion+high 边列表供分页拆分)。"""
    list1_add: set[str] = set()
    list2_add: set[str] = set()
    expansion_edges: list[tuple[str, str, dict[str, Any]]] = []
    links = choice_json.get("clickable_links")
    if not isinstance(links, list):
        return list1_add, list2_add, expansion_edges
    for item in links:
        if not isinstance(item, dict):
            continue
        cat = str(item.get("category") or "").strip()
        conf = str(item.get("category_confidence") or "").strip()
        if conf != "high":
            continue
        resolved = _resolve_url(str(item.get("url") or ""), source_url)
        if not resolved:
            continue
        if cat in {"tutor_profile", "tutor_expansion"}:
            list1_add.add(resolved)
        if cat == "tutor_profile":
            list2_add.add(resolved)
        elif cat == "tutor_expansion":
            expansion_edges.append((resolved, source_url, item))
    return list1_add, list2_add, expansion_edges


def _has_choice_pending_for_round(state: dict[str, Any], *, round_no: int) -> bool:
    """
    检测是否处于“已完成页面清洗，但链接分类尚未完成”的中断场景。

    触发条件：
    - records 中存在指定 round_no 的条目
    - cleaned_file 存在（说明 webclean 已完成）
    - choice_file 缺失或为空（说明 link_choose 尚未完成）
    """
    records = state.get("records")
    if not isinstance(records, list):
        return False
    for rec in records:
        if not isinstance(rec, dict):
            continue
        try:
            rno = int(rec.get("round") or 0)
        except (TypeError, ValueError):
            rno = 0
        if rno != round_no:
            continue
        cleaned_file = str(rec.get("cleaned_file") or "").strip()
        if not cleaned_file:
            continue
        choice_file = str(rec.get("choice_file") or "").strip()
        if not choice_file:
            return True
    return False


def _list2_tutor_urls_missing_cleaned_markdown(
    state: dict[str, Any],
    *,
    out_dir: Path,
    cleaned_dir: Path,
) -> set[str]:
    """
    list2 中的导师主页 URL 若尚无对应 records + 磁盘 cleaned .md，则须进 list1 做 web_clean。
    修复历史 state：list2 已满而 list1 空时续跑不再空转。
    """
    records = state.get("records")
    if not isinstance(records, list):
        records = []
    have: set[str] = set()
    for rec in records:
        if not isinstance(rec, dict):
            continue
        url = _normalize_url(str(rec.get("url") or ""))
        if not url:
            continue
        cleaned_rel = str(rec.get("cleaned_file") or "").strip()
        if not cleaned_rel:
            continue
        fp = _resolve_cleaned_markdown(cleaned_rel, out_dir=out_dir, cleaned_dir=cleaned_dir)
        if fp is not None and fp.is_file():
            have.add(url)
    out: set[str] = set()
    list2 = state.get("list2_tutor_profiles")
    if not isinstance(list2, list):
        return out
    list3_set = _as_set(state.get("list3_processed_pages"))
    for raw in list2:
        u = _normalize_url(str(raw or "").strip())
        if not u or u in have:
            continue
        if u in list3_set:
            continue
        out.add(u)
    return out


class GetTutorPagesAgent:
    def run(
        self,
        inv: AgentInvocation[GetTutorPagesPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 8192,
        choice_max_workers: int = 4,
        restart_on_transient_llm_error: bool = True,
        transient_retry_initial_sec: float = 15.0,
        transient_retry_max_sec: float = 120.0,
        transient_swap_fast_slot_pair: bool = True,
    ) -> GetTutorPagesResult:
        log = AgentLogger("GetTutorPagesAgent")
        if max_tokens <= 0:
            raise ValueError("max_tokens 必须为正整数")
        slot_token = [inv.model.token]

        def _on_retry(attempt: int, wait_sec: float, e: BaseException) -> None:
            log.warn(
                "LLM 网关/模型暂时不可用，抓取编排将从断点重试",
                detail=f"attempt={attempt} sleep={wait_sec:.1f}s err={e!s}",
            )
            try_switch_fast_slot_pair(
                dispatcher,
                slot_token,
                log=log,
                enabled=transient_swap_fast_slot_pair,
            )

        return run_with_transient_llm_retries(
            lambda: self._run_impl(
                AgentInvocation(ModelRef(slot_token[0]), inv.llm_part),
                dispatcher,
                max_tokens=max_tokens,
                choice_max_workers=choice_max_workers,
                log=log,
            ),
            restart_on_transient_llm_error=restart_on_transient_llm_error,
            transient_retry_initial_sec=transient_retry_initial_sec,
            transient_retry_max_sec=transient_retry_max_sec,
            on_retry=_on_retry,
        )

    def _run_impl(
        self,
        inv: AgentInvocation[GetTutorPagesPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int,
        choice_max_workers: int,
        log: AgentLogger,
    ) -> GetTutorPagesResult:
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        academy_url = _normalize_url(p.academy_url)
        log.start("开始导师页面抓取编排", detail=f"url={academy_url} depth={p.max_depth}")
        if not academy_url:
            raise ValueError(f"academy_url 需要是 http(s) URL，当前为 {p.academy_url!r}")
        if not isinstance(p.max_depth, int) or p.max_depth <= 0:
            raise ValueError("max_depth 必须为正整数")
        if p.max_depth > 20:
            raise ValueError("max_depth 过大，建议不超过 20")
        if p.listing_pagination_max_passes > 500:
            raise ValueError("listing_pagination_max_passes 过大，建议不超过 500")
        if not str(Path(p.output_dir)).strip():
            raise ValueError("output_dir 不能为空")
        out_dir, cache_dir, cleaned_dir, choice_dir = _resolve_cache_layout(
            p.output_dir,
            p.resume_state_path,
        )
        state_path = (cache_dir / "state.json").resolve()
        state_lock_path = (cache_dir / "state.lock").resolve()
        choice_summary_path = (choice_dir / "url_choice.md").resolve()
        cleaned_dir.mkdir(parents=True, exist_ok=True)
        choice_dir.mkdir(parents=True, exist_ok=True)
        lock_fd: int | None = None
        try:
            lock_fd = _acquire_file_lock(state_lock_path)
            if state_path.is_file():
                state = _read_json(state_path, default_obj=_init_state(academy_url))
                if not isinstance(state, dict):
                    state = _init_state(academy_url)
            else:
                state = _init_state(academy_url)

            for key, default_value in {
                "round": 0,
                "seq": 0,
                "list1_possible_pages": [],
                "list2_tutor_profiles": [],
                "list3_processed_pages": [],
                "records": [],
            }.items():
                state.setdefault(key, default_value)

            _validate_state_shape(state)
            if _reconcile_cleaned_seq(state, cleaned_dir, log=log):
                _write_json(state_path, state)

            wc = WebCleanAgent()
            chooser = LinkChooseAgent()

            pag_max = max(0, int(p.listing_pagination_max_passes))
            for _depth_slot in range(p.max_depth):
                list1_accum: set[str] = set(_as_set(state["list1_possible_pages"]))
                list1_accum |= _list2_tutor_urls_missing_cleaned_markdown(
                    state, out_dir=out_dir, cleaned_dir=cleaned_dir
                )
                state["list1_possible_pages"] = []
                pagination_queue: list[str] = []
                pag_passes = 0
                aggregated_links_slot: list[dict[str, Any]] = []

                while True:
                    choice_only_resume = False
                    from_pagination = False
                    batch: list[str] = []

                    # 同轮若仍有「已 web_clean、choice_file 未写入」的 records，必须先补跑 link_choose。
                    # 否则 list1/分页队列会先走 web_clean，断在 link_choose 后重启会像「又从清洗开始」。
                    cr_loop = int(state["round"])
                    pending_choice = _has_choice_pending_for_round(state, round_no=cr_loop)

                    if pagination_queue:
                        if pending_choice:
                            choice_only_resume = True
                        else:
                            batch = list(dict.fromkeys(pagination_queue))
                            pagination_queue.clear()
                            from_pagination = True
                    elif list1_accum:
                        if pending_choice:
                            choice_only_resume = True
                        else:
                            batch = list(dict.fromkeys(list1_accum))
                            list1_accum.clear()
                    elif pending_choice:
                        choice_only_resume = True
                    else:
                        break

                    ran_clean = bool(batch) and not choice_only_resume
                    if ran_clean:
                        if not from_pagination:
                            state["round"] = int(state["round"]) + 1
                            current_round = int(state["round"])
                            log.step(
                                "开始新一轮迭代",
                                detail=f"round={current_round} batch={len(batch)}",
                            )
                        else:
                            current_round = int(state["round"])
                            if pag_max > 0:
                                log.step(
                                    "名录分页续洗(不占 max_depth 轮次)",
                                    detail=(
                                        f"round={current_round} pass={pag_passes + 1}/{pag_max} "
                                        f"batch={len(batch)}"
                                    ),
                                )
                            else:
                                log.step(
                                    "名录分页(已关闭分页专道，按普通页处理)",
                                    detail=f"round={current_round} batch={len(batch)}",
                                )

                        processed_set = _as_set(state["list3_processed_pages"])
                        records = state["records"] if isinstance(state["records"], list) else []
                        existing_record_urls = {
                            _normalize_url(str(rec.get("url") or ""))
                            for rec in records
                            if isinstance(rec, dict)
                        }
                        existing_record_urls.discard("")

                        urls_to_clean = [
                            u
                            for u in batch
                            if u not in processed_set and u not in existing_record_urls
                        ]
                        skipped_clean = len(batch) - len(urls_to_clean)
                        if skipped_clean:
                            log.step(
                                "网页清洗·跳过已处理",
                                detail=f"round={current_round} 本批 {skipped_clean} 条已在 records/已处理列表",
                            )
                        if (
                            from_pagination
                            and pag_max > 0
                            and batch
                            and len(urls_to_clean) == 0
                        ):
                            log.warn(
                                "名录分页专道本批无需清洗（均已处理），将仅重跑链接聚合；"
                                "若反复出现请检查 URL 去重或删除旧 choice 缓存",
                                detail=f"round={current_round} batch_n={len(batch)}",
                            )
                        if urls_to_clean:
                            n_clean = len(urls_to_clean)
                            log.step(
                                "网页清洗阶段",
                                detail=f"round={current_round} 本批待清洗 {n_clean} 条",
                            )
                        for ci, url in enumerate(urls_to_clean, start=1):
                            next_seq = int(state["seq"]) + 1
                            cleaned_name = _cleaned_filename(url, next_seq)
                            log.step(
                                "网页清洗进度",
                                detail=f"round={current_round} [{ci}/{n_clean}] {url}",
                            )
                            try:
                                cleaned_path = wc.run(
                                    AgentInvocation(
                                        model=inv.model,
                                        llm_part=WebCleanPayload(
                                            url=url,
                                            output_dir=cleaned_dir,
                                            output_filename=cleaned_name,
                                            progress_index=ci,
                                            progress_total=n_clean,
                                        ),
                                    ),
                                    dispatcher,
                                )
                            except FirecrawlError as e:
                                log.warn(
                                    "网页清洗失败已跳过(Firecrawl)",
                                    detail=(
                                        f"round={current_round} [{ci}/{n_clean}] {url} "
                                        f"mark=FIRECRAWL_SKIP err={e!s}"
                                    ),
                                )
                                continue
                            state["seq"] = next_seq
                            processed_set.add(url)
                            existing_record_urls.add(url)
                            records.append(
                                {
                                    "url": url,
                                    "round": current_round,
                                    "cleaned_file": _to_workspace_relative(cleaned_path, out_dir),
                                }
                            )
                            log.info("网页清洗完成", detail=f"[{ci}/{n_clean}] {cleaned_name}")

                        for url in batch:
                            processed_set.add(url)

                        state["list3_processed_pages"] = sorted(processed_set)
                        state["records"] = records
                        _write_json(state_path, state)
                    elif choice_only_resume:
                        log.step(
                            "继续链接分类(未完成)",
                            detail=f"round={int(state['round'])} pending_choice=1",
                        )

                    cr_choice = int(state["round"])
                    need_choice = (
                        ran_clean
                        or choice_only_resume
                        or _has_choice_pending_for_round(state, round_no=cr_choice)
                    )
                    if not need_choice:
                        break

                    all_records = state["records"] if isinstance(state["records"], list) else []
                    list1_candidate_add: set[str] = set()
                    list2_candidate_add: set[str] = set()
                    expansion_edges_all: list[tuple[str, str, dict[str, Any]]] = []
                    ready_choice_items: list[tuple[dict[str, Any], str, dict[str, Any], Path]] = []
                    choice_jobs: list[tuple[dict[str, Any], str, Path, str]] = []

                    for rec in all_records:
                        if not isinstance(rec, dict):
                            continue
                        source_url = str(rec.get("url") or "").strip()
                        cleaned_file = _resolve_cleaned_markdown(
                            str(rec.get("cleaned_file") or ""),
                            out_dir=out_dir,
                            cleaned_dir=cleaned_dir,
                        )
                        if not source_url or cleaned_file is None:
                            continue
                        choice_name = _choice_filename(cleaned_file.name)
                        existing_choice = _resolve_existing_choice_path(
                            str(rec.get("choice_file") or ""),
                            out_dir=out_dir,
                            choice_dir=choice_dir,
                            choice_filename=choice_name,
                        )
                        one: dict[str, Any] | None = None
                        choice_path: Path
                        if existing_choice is not None:
                            cached = _read_json(existing_choice, default_obj={})
                            try:
                                if isinstance(cached, dict):
                                    _validate_choice_schema(cached)
                                    one = cached
                            except GetTutorPagesError:
                                one = None
                                log.warn(
                                    "已有 choice 缓存无效，将重新分类",
                                    detail=f"{source_url} -> {existing_choice.name}",
                                )
                        if one is None:
                            choice_jobs.append((rec, source_url, cleaned_file, choice_name))
                        else:
                            choice_path = existing_choice
                            rec["choice_file"] = _to_workspace_relative(choice_path, out_dir)
                            log.info(
                                "跳过链接分类(已有缓存)",
                                detail=f"{source_url} -> {choice_path.name}",
                            )
                            if isinstance(one, dict):
                                ready_choice_items.append((rec, source_url, one, choice_path))

                    if choice_jobs:
                        workers = max(1, int(choice_max_workers))
                        n_choice = len(choice_jobs)
                        log.step(
                            "链接分类阶段",
                            detail=f"round={int(state['round'])} 待分类 {n_choice} 页 workers={workers}",
                        )

                        def _run_one_choice(
                            job_idx: int,
                            job: tuple[dict[str, Any], str, Path, str],
                        ) -> tuple[dict[str, Any], str, dict[str, Any], Path]:
                            rec0, src0, cleaned0, choice_name0 = job
                            tmp_name = f"{Path(choice_name0).stem}.{uuid.uuid4().hex}.tmp.json"
                            tmp_path = (choice_dir / tmp_name).resolve()
                            final_path = (choice_dir / choice_name0).resolve()
                            try:
                                out_tmp = chooser.run(
                                    AgentInvocation(
                                        model=inv.model,
                                        llm_part=LinkChoosePayload(
                                            markdown_path=cleaned0,
                                            output_dir=choice_dir,
                                            output_filename=tmp_name,
                                            refine_all_links=p.link_choose_refine_all_links,
                                            refine_batch_parallel_workers=max(
                                                1, int(p.link_choose_refine_batch_parallel_workers)
                                            ),
                                            progress_index=job_idx,
                                            progress_total=n_choice,
                                            task_root_url=academy_url,
                                            scope_hint=(
                                                (p.academy_scope_hint or "").strip() or None
                                            ),
                                        ),
                                    ),
                                    dispatcher,
                                    max_tokens=max_tokens,
                                ).resolve()
                                one0 = _read_json(out_tmp, default_obj={"clickable_links": []})
                                if isinstance(one0, dict):
                                    _validate_choice_schema(one0)
                                else:
                                    raise GetTutorPagesError("link_choose 输出不是 JSON 对象")
                                return rec0, src0, one0, final_path
                            except Exception:
                                try:
                                    if tmp_path.exists():
                                        tmp_path.unlink()
                                except OSError:
                                    pass
                                raise

                        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
                            fut_map = {
                                ex.submit(_run_one_choice, idx, j): j
                                for idx, j in enumerate(choice_jobs, start=1)
                            }
                            choice_done = 0
                            for fut in concurrent.futures.as_completed(fut_map):
                                rec0, src0, _cleaned0, choice_name0 = fut_map[fut]
                                try:
                                    rec_ret, src_ret, one_ret, final_path = fut.result()
                                except Exception as e:
                                    choice_done += 1
                                    log.warn(
                                        "链接分类失败，丢弃该 worker 结果",
                                        detail=f"[{choice_done}/{n_choice}] {src0} -> {choice_name0} err={e!s}",
                                    )
                                    continue
                                tmp_candidates = list(
                                    choice_dir.glob(f"{Path(choice_name0).stem}.*.tmp.json")
                                )
                                if not tmp_candidates:
                                    choice_done += 1
                                    log.warn(
                                        "链接分类结果临时文件丢失，丢弃",
                                        detail=f"[{choice_done}/{n_choice}] {src_ret} -> {choice_name0}",
                                    )
                                    continue
                                tmp_choice = sorted(tmp_candidates, key=lambda p0: p0.stat().st_mtime)[-1]
                                try:
                                    tmp_choice.replace(final_path)
                                except OSError as e:
                                    choice_done += 1
                                    log.warn(
                                        "链接分类结果落盘失败，丢弃",
                                        detail=f"[{choice_done}/{n_choice}] {src_ret} -> {choice_name0} err={e!s}",
                                    )
                                    continue
                                rec_ret["choice_file"] = _to_workspace_relative(final_path, out_dir)
                                choice_done += 1
                                log.step(
                                    "链接分类进度",
                                    detail=(
                                        f"round={int(state['round'])} [{choice_done}/{n_choice}] "
                                        f"{src_ret} -> {final_path.name}"
                                    ),
                                )
                                ready_choice_items.append((rec_ret, src_ret, one_ret, final_path))

                    for _rec, source_url, one, _choice_path in ready_choice_items:
                        links = one.get("clickable_links")
                        if isinstance(links, list):
                            for item in links:
                                if isinstance(item, dict):
                                    row = dict(item)
                                    row["source_url"] = source_url
                                    aggregated_links_slot.append(row)
                        add1, add2, edges = _pick_high_confidence_urls(
                            choice_json=one, source_url=source_url
                        )
                        list1_candidate_add |= add1
                        list2_candidate_add |= add2
                        expansion_edges_all.extend(edges)

                    list2_set = _as_set(state["list2_tutor_profiles"])
                    list3_set = _as_set(state["list3_processed_pages"])
                    for u in list2_candidate_add:
                        if u not in list2_set:
                            list2_set.add(u)
                    state["list2_tutor_profiles"] = sorted(list2_set)

                    pag_urls: set[str] = set()
                    if pag_max > 0:
                        for resolved, src_u, item in expansion_edges_all:
                            if _is_choice_listing_pagination_next(item):
                                pag_urls.add(resolved)
                    # 已处理页、已收录导师页不得再进分页专道，否则会出现「跳过清洗」仍反复 continue 的空转。
                    pag_urls = {u for u in pag_urls if u not in list3_set and u not in list2_set}

                    spill_pag = False
                    if pag_urls and pag_max > 0:
                        if pag_passes >= pag_max:
                            spill_pag = True
                            log.warn(
                                "名录分页追加次数已达上限，余页并入普通待爬队列",
                                detail=f"cap={pag_max} round={int(state['round'])}",
                            )
                        else:
                            pagination_queue.extend(sorted(pag_urls))
                            pag_passes += 1
                    elif pag_urls:
                        spill_pag = True

                    # list2 仅表示「导师主页候选」；仍需经 web_clean 写入 records 后 analyse 才能消费。
                    # 若此处再排除 list2_set，tutor_profile 会只进 list2、永不进 list1，形成无 cleaned 的死局。
                    norm_list1 = set(list1_candidate_add) - pag_urls
                    for u in norm_list1:
                        if u not in list3_set:
                            list1_accum.add(u)
                    if spill_pag:
                        for u in pag_urls:
                            if u not in list3_set:
                                list1_accum.add(u)

                    state["list1_possible_pages"] = sorted(list1_accum)
                    state["records"] = all_records
                    _write_json(state_path, state)

                    if pagination_queue:
                        continue

                    _write_json(
                        choice_summary_path,
                        {
                            "round": int(state["round"]),
                            "academy_url": academy_url,
                            "clickable_links": aggregated_links_slot,
                        },
                    )
                    log.step(
                        "轮次状态已保存",
                        detail=(
                            f"round={state['round']} pending={len(state['list1_possible_pages'])} "
                            f"tutors={len(state['list2_tutor_profiles'])}"
                        ),
                    )
                    break

                state["list1_possible_pages"] = sorted(list1_accum)
                _write_json(state_path, state)
        finally:
            _release_file_lock(lock_fd, state_lock_path)
        log.done(
            "抓取编排完成",
            detail=(
                f"round={state['round']} pending={len(state['list1_possible_pages'])} "
                f"tutors={len(state['list2_tutor_profiles'])}"
            ),
        )

        return GetTutorPagesResult(
            output_dir=Path(_to_root_relative(out_dir)),
            cache_dir=Path(_to_root_relative(cache_dir)),
            cleaned_dir=Path(_to_root_relative(cleaned_dir)),
            choice_dir=Path(_to_root_relative(choice_dir)),
            state_path=Path(_to_root_relative(state_path)),
            round_count=int(state["round"]),
            list1_pending_count=len(_as_set(state["list1_possible_pages"])),
            list2_tutor_profile_count=len(_as_set(state["list2_tutor_profiles"])),
            list3_processed_count=len(_as_set(state["list3_processed_pages"])),
        )

    async def arun(
        self,
        inv: AgentInvocation[GetTutorPagesPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 8192,
        choice_max_workers: int = 4,
        restart_on_transient_llm_error: bool = True,
        transient_retry_initial_sec: float = 15.0,
        transient_retry_max_sec: float = 120.0,
        transient_swap_fast_slot_pair: bool = True,
    ) -> GetTutorPagesResult:
        return await asyncio.to_thread(
            self.run,
            inv,
            dispatcher,
            max_tokens=max_tokens,
            choice_max_workers=choice_max_workers,
            restart_on_transient_llm_error=restart_on_transient_llm_error,
            transient_retry_initial_sec=transient_retry_initial_sec,
            transient_retry_max_sec=transient_retry_max_sec,
            transient_swap_fast_slot_pair=transient_swap_fast_slot_pair,
        )


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "GetTutorPagesAgent",
    "GetTutorPagesError",
    "GetTutorPagesPayload",
    "GetTutorPagesResult",
]
