"""
导师页面链接抓取编排：
维护三类 URL 列表（待处理/导师页/已处理），串联 web_clean 与 link_choose 做迭代。
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit, urlunsplit

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.link_choose import LinkChooseAgent, LinkChoosePayload
from byboy.agents.tutor_inf.logging_utils import AgentLogger
from byboy.agents.tutor_inf.web_clean import WebCleanAgent, WebCleanPayload
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


def _normalize_url(url: str) -> str:
    u = (url or "").strip()
    if not u:
        return ""
    parts = urlsplit(u)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        return ""
    path = parts.path or "/"
    # 为避免同一页面仅 query 不同而被重复处理，统一忽略 query 与 fragment。
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def _resolve_url(raw_url: str, source_url: str) -> str:
    s = (raw_url or "").strip()
    if not s:
        return ""
    if s.startswith(("mailto:", "tel:", "javascript:", "#")):
        return ""
    abs_u = urljoin(source_url, s)
    return _normalize_url(abs_u)


def _safe_slug_from_url(url: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", url.strip()).strip("_")
    if len(s) > 80:
        s = s[:80]
    return s or "url"


def _cleaned_filename(url: str, seq: int) -> str:
    return f"{seq:05d}_{_safe_slug_from_url(url)}_cleaned.md"


def _choice_filename(cleaned_filename: str) -> str:
    stem = Path(cleaned_filename).stem
    return f"{stem}.choice.json"


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
) -> tuple[set[str], set[str]]:
    list1_add: set[str] = set()
    list2_add: set[str] = set()
    links = choice_json.get("clickable_links")
    if not isinstance(links, list):
        return list1_add, list2_add
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
    return list1_add, list2_add


class GetTutorPagesAgent:
    def run(
        self,
        inv: AgentInvocation[GetTutorPagesPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 8192,
    ) -> GetTutorPagesResult:
        log = AgentLogger("GetTutorPagesAgent")
        if max_tokens <= 0:
            raise ValueError("max_tokens 必须为正整数")
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

            wc = WebCleanAgent()
            chooser = LinkChooseAgent()

            for _ in range(p.max_depth):
                list1 = list(dict.fromkeys(_as_set(state["list1_possible_pages"])))
                if not list1:
                    break
                log.step(
                    "开始新一轮迭代",
                    detail=f"round={int(state['round']) + 1} batch={len(list1)}",
                )

                state["round"] = int(state["round"]) + 1
                current_round = int(state["round"])

                batch = list1[:]
                state["list1_possible_pages"] = []

                processed_set = _as_set(state["list3_processed_pages"])
                records = state["records"] if isinstance(state["records"], list) else []
                existing_record_urls = {
                    _normalize_url(str(rec.get("url") or ""))
                    for rec in records
                    if isinstance(rec, dict)
                }
                existing_record_urls.discard("")

                for url in batch:
                    # 已处理过或已有记录都跳过，避免异常场景重复生成 cleaned。
                    if url in processed_set or url in existing_record_urls:
                        processed_set.add(url)
                        continue
                    seq = int(state["seq"]) + 1
                    state["seq"] = seq
                    cleaned_name = _cleaned_filename(url, seq)
                    cleaned_path = wc.run(
                        AgentInvocation(
                            model=inv.model,
                            llm_part=WebCleanPayload(
                                url=url,
                                output_dir=cleaned_dir,
                                output_filename=cleaned_name,
                            ),
                        ),
                        dispatcher,
                    )
                    processed_set.add(url)
                    existing_record_urls.add(url)
                    records.append(
                        {
                            "url": url,
                            "round": current_round,
                            "cleaned_file": _to_root_relative(cleaned_path),
                        }
                    )
                    log.info("完成页面清洗", detail=f"{url} -> {cleaned_name}")

                state["list3_processed_pages"] = sorted(processed_set)
                state["records"] = records
                _write_json(state_path, state)

                all_records = state["records"] if isinstance(state["records"], list) else []
                aggregated_links: list[dict[str, Any]] = []
                list1_candidate_add: set[str] = set()
                list2_candidate_add: set[str] = set()
                for rec in all_records:
                    if not isinstance(rec, dict):
                        continue
                    source_url = str(rec.get("url") or "").strip()
                    cleaned_file = _resolve_maybe_relative(
                        str(rec.get("cleaned_file") or ""),
                        base_dir=out_dir,
                    )
                    if not source_url or not cleaned_file.is_file():
                        continue
                    choice_name = _choice_filename(cleaned_file.name)
                    choice_path = chooser.run(
                        AgentInvocation(
                            model=inv.model,
                            llm_part=LinkChoosePayload(
                                markdown_path=cleaned_file,
                                output_dir=choice_dir,
                                output_filename=choice_name,
                            ),
                        ),
                        dispatcher,
                        max_tokens=max_tokens,
                    )
                    rec["choice_file"] = _to_root_relative(choice_path)
                    log.info("完成链接分类", detail=f"{source_url} -> {Path(choice_path).name}")
                    one = _read_json(Path(choice_path), default_obj={"clickable_links": []})
                    if isinstance(one, dict):
                        _validate_choice_schema(one)
                        links = one.get("clickable_links")
                        if isinstance(links, list):
                            for item in links:
                                if isinstance(item, dict):
                                    row = dict(item)
                                    row["source_url"] = source_url
                                    aggregated_links.append(row)
                        add1, add2 = _pick_high_confidence_urls(choice_json=one, source_url=source_url)
                        list1_candidate_add |= add1
                        list2_candidate_add |= add2

                list1_set = _as_set(state["list1_possible_pages"])
                list2_set = _as_set(state["list2_tutor_profiles"])
                list3_set = _as_set(state["list3_processed_pages"])

                for u in list1_candidate_add:
                    if u not in list1_set and u not in list2_set and u not in list3_set:
                        list1_set.add(u)
                for u in list2_candidate_add:
                    if u not in list2_set:
                        list2_set.add(u)

                state["list1_possible_pages"] = sorted(list1_set)
                state["list2_tutor_profiles"] = sorted(list2_set)
                state["records"] = all_records

                _write_json(
                    choice_summary_path,
                    {
                        "round": int(state["round"]),
                        "academy_url": academy_url,
                        "clickable_links": aggregated_links,
                    },
                )
                _write_json(state_path, state)
                log.step(
                    "轮次状态已保存",
                    detail=(
                        f"round={state['round']} pending={len(state['list1_possible_pages'])} "
                        f"tutors={len(state['list2_tutor_profiles'])}"
                    ),
                )
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
    ) -> GetTutorPagesResult:
        return await asyncio.to_thread(self.run, inv, dispatcher, max_tokens=max_tokens)


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "GetTutorPagesAgent",
    "GetTutorPagesError",
    "GetTutorPagesPayload",
    "GetTutorPagesResult",
]
