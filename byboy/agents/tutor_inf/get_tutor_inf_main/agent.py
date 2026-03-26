"""
导师信息主流程编排：
接收学院起始页 URL、模型/槽位 token、工作目录，
顺序执行 get_tutor_pages 与 get_tutor_analyse。
"""

from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.get_tutor_analyse import (
    GetTutorAnalyseAgent,
    GetTutorAnalysePayload,
    GetTutorAnalyseResult,
)
from byboy.agents.tutor_inf.get_tutor_pages import (
    GetTutorPagesAgent,
    GetTutorPagesPayload,
    GetTutorPagesResult,
)
from byboy.agents.tutor_inf.logging_utils import AgentLogger
from byboy.agents.tutor_inf.transient_errors import (
    run_with_transient_llm_retries,
    try_switch_fast_slot_pair,
)
from byboy.agents.tutor_inf.output_to_csv import (
    OutputToCsvAgent,
    OutputToCsvPayload,
    OutputToCsvResult,
)
from byboy.llm.dispatcher import LLMDispatcher


@dataclass(frozen=True, slots=True)
class GetTutorInfMainPayload:
    workdir: str | Path
    academy_url: str | None = None
    #: 学院/单位名称，传入 link_choose；与 academy_url 一样可写入 state 续跑时复用。
    academy_scope_hint: str | None = None
    max_depth: int = 2
    #: 同一大轮内名录「下一页」最多追加清洗次数（不计入 max_depth）；0 表示关闭专道。
    listing_pagination_max_passes: int = 80
    pages_resume_state_path: str | Path | None = None
    main_resume_state_path: str | Path | None = None
    analysed_subdir: str = "cache/analysed"
    csv_path: str | Path | None = None
    csv_resume_state_path: str | Path | None = None
    csv_run_log_path: str | Path | None = None
    link_choose_refine_all_links: bool = True
    #: 单页 link_choose 内 LLM 批次并行度（与 get_tutor_pages 一致）；总 LLM 并发约 pages_choice_max_workers × 本值。
    link_choose_refine_batch_parallel_workers: int = 1
    resume_from_round: int | None = None
    resume_from_stage: str = "auto"


@dataclass(frozen=True, slots=True)
class GetTutorInfMainResult:
    workdir: Path
    pages_result: GetTutorPagesResult
    analyse_result: GetTutorAnalyseResult
    csv_result: OutputToCsvResult


class GetTutorInfMainAgent:
    _MAIN_SCHEMA_VERSION = 1
    _MAIN_SCHEMA = "get_tutor_inf_main_state"
    _STAGES: tuple[str, ...] = ("pages", "analyse", "csv")

    @staticmethod
    def _read_json(path: Path, default_obj: Any) -> Any:
        if not path.is_file():
            return default_obj
        try:
            return json.loads(path.read_text(encoding="utf-8", errors="replace"))
        except json.JSONDecodeError:
            return default_obj

    @staticmethod
    def _write_json(path: Path, obj: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).isoformat(timespec="seconds")

    def _ensure_main_state(self, state: dict[str, Any]) -> dict[str, Any]:
        meta = state.get("main_task_meta")
        if not isinstance(meta, dict):
            meta = {}
            state["main_task_meta"] = meta
        meta.setdefault("schema", self._MAIN_SCHEMA)
        meta.setdefault("version", self._MAIN_SCHEMA_VERSION)
        meta.setdefault("created_at", self._now_iso())
        meta["updated_at"] = self._now_iso()
        state.setdefault("main_task_params", {})
        state.setdefault("main_task_progress", {})
        state.setdefault("main_task_rounds", [])
        return state

    @staticmethod
    def _ensure_pages_state_seed(state: dict[str, Any], academy_url: str) -> dict[str, Any]:
        """
        与 get_tutor_pages 的 state 共用同一文件时，确保抓取阶段必需字段存在。
        若是首次运行（仅主流程字段），需要把起始 URL 放入 list1_possible_pages。
        """
        if not isinstance(state.get("round"), int):
            state["round"] = 0
        if not isinstance(state.get("seq"), int):
            state["seq"] = 0
        if not isinstance(state.get("list1_possible_pages"), list):
            state["list1_possible_pages"] = [academy_url]
        if not isinstance(state.get("list2_tutor_profiles"), list):
            state["list2_tutor_profiles"] = []
        if not isinstance(state.get("list3_processed_pages"), list):
            state["list3_processed_pages"] = []
        if not isinstance(state.get("records"), list):
            state["records"] = []
        if (
            not state["list1_possible_pages"]
            and not state["list2_tutor_profiles"]
            and not state["list3_processed_pages"]
            and not state["records"]
        ):
            state["list1_possible_pages"] = [academy_url]
        return state

    @staticmethod
    def _normalize_stage(stage: str) -> str:
        s = (stage or "").strip().lower()
        if not s:
            return "auto"
        if s not in {"auto", "pages", "analyse", "csv"}:
            raise ValueError("resume_from_stage 仅支持 auto/pages/analyse/csv")
        return s

    def _mark_stage(
        self,
        state: dict[str, Any],
        *,
        round_no: int | None,
        stage: str,
        status: str,
        detail: dict[str, Any] | None = None,
    ) -> None:
        progress = state.setdefault("main_task_progress", {})
        if not isinstance(progress, dict):
            progress = {}
            state["main_task_progress"] = progress
        stages = progress.setdefault("stages", {})
        if not isinstance(stages, dict):
            stages = {}
            progress["stages"] = stages
        one = {"status": status, "updated_at": self._now_iso()}
        if isinstance(detail, dict) and detail:
            one["detail"] = detail
        stages[stage] = one
        if round_no is not None and round_no > 0:
            rounds = state.setdefault("main_task_rounds", [])
            if not isinstance(rounds, list):
                rounds = []
                state["main_task_rounds"] = rounds
            target: dict[str, Any] | None = None
            for x in rounds:
                if isinstance(x, dict) and int(x.get("round") or 0) == round_no:
                    target = x
                    break
            if target is None:
                target = {"round": round_no, "stages": {}}
                rounds.append(target)
            rs = target.setdefault("stages", {})
            if not isinstance(rs, dict):
                rs = {}
                target["stages"] = rs
            rs[stage] = one
        progress["last_round"] = round_no
        progress["last_stage"] = stage
        progress["updated_at"] = self._now_iso()

    def _save_main_only(
        self,
        *,
        state_path: Path,
        main_state: dict[str, Any],
    ) -> dict[str, Any]:
        """
        只回写 main_task_* 控制字段，避免覆盖 get_tutor_pages 实时更新的数据字段。
        """
        latest = self._read_json(state_path, default_obj={})
        if not isinstance(latest, dict):
            latest = {}
        latest["main_task_meta"] = main_state.get("main_task_meta", {})
        latest["main_task_params"] = main_state.get("main_task_params", {})
        latest["main_task_progress"] = main_state.get("main_task_progress", {})
        latest["main_task_rounds"] = main_state.get("main_task_rounds", [])
        for k in (
            "round",
            "seq",
            "list1_possible_pages",
            "list2_tutor_profiles",
            "list3_processed_pages",
            "records",
            "list4_analysed_profiles",
        ):
            if k not in latest and k in main_state:
                latest[k] = main_state[k]
        self._write_json(state_path, latest)
        return latest

    def _resolve_effective_params(
        self,
        *,
        payload: GetTutorInfMainPayload,
        model_token: str,
        state: dict[str, Any],
    ) -> dict[str, Any]:
        old = state.get("main_task_params")
        old = old if isinstance(old, dict) else {}
        academy_url = (payload.academy_url or "").strip() or str(old.get("academy_url") or "").strip()
        if not academy_url:
            raise ValueError("academy_url 不能为空（首次运行请提供；后续可从已有 state 继承）")
        pay_hint = (payload.academy_scope_hint or "").strip()
        old_hint = str(old.get("academy_scope_hint") or "").strip()
        academy_scope_hint = pay_hint or old_hint or None
        max_depth = payload.max_depth if payload.max_depth > 0 else int(old.get("max_depth") or 2)
        if max_depth <= 0:
            raise ValueError("max_depth 必须为正整数")
        lp = int(payload.listing_pagination_max_passes)
        if lp > 0:
            listing_pagination_max_passes = lp
        elif lp == 0:
            listing_pagination_max_passes = 0
        else:
            old_lp = old.get("listing_pagination_max_passes")
            listing_pagination_max_passes = int(old_lp) if old_lp is not None else 80
        if listing_pagination_max_passes > 500:
            raise ValueError("listing_pagination_max_passes 过大，建议不超过 500")
        return {
            "academy_url": academy_url,
            "academy_scope_hint": academy_scope_hint,
            "listing_pagination_max_passes": listing_pagination_max_passes,
            "workdir": str(Path(payload.workdir).resolve()),
            "slot": model_token,
            "max_depth": max_depth,
            "pages_resume_state_path": str(Path(payload.pages_resume_state_path).resolve())
            if payload.pages_resume_state_path is not None
            else None,
            "analysed_subdir": payload.analysed_subdir or str(old.get("analysed_subdir") or "cache/analysed"),
            "csv_path": str(Path(payload.csv_path).resolve()) if payload.csv_path is not None else None,
            "csv_resume_state_path": str(Path(payload.csv_resume_state_path).resolve())
            if payload.csv_resume_state_path is not None
            else None,
            "csv_run_log_path": str(Path(payload.csv_run_log_path).resolve())
            if payload.csv_run_log_path is not None
            else None,
            "link_choose_refine_all_links": bool(payload.link_choose_refine_all_links),
            "link_choose_refine_batch_parallel_workers": max(
                1, int(payload.link_choose_refine_batch_parallel_workers)
            ),
        }

    def _prepare_resume_from_round_for_analyse(self, state_path: Path, start_round: int) -> None:
        state = self._read_json(state_path, default_obj={})
        if not isinstance(state, dict):
            return
        records = state.get("records")
        if not isinstance(records, list):
            return
        analysed_urls: set[str] = set()
        for rec in records:
            if not isinstance(rec, dict):
                continue
            rno = int(rec.get("round") or 0)
            if rno >= start_round:
                u = str(rec.get("url") or "").strip()
                if u:
                    analysed_urls.add(u)
                rec.pop("analysed_file", None)
                rec.pop("analysed_name", None)
        list4 = state.get("list4_analysed_profiles")
        if isinstance(list4, list):
            kept = [u for u in list4 if str(u).strip() and str(u).strip() not in analysed_urls]
            state["list4_analysed_profiles"] = sorted(set(kept))
        self._write_json(state_path, state)

    def _prepare_resume_from_round_for_csv(
        self,
        *,
        state_path: Path,
        analysed_dir: Path,
        csv_resume_state_path: Path,
        start_round: int,
    ) -> None:
        state = self._read_json(state_path, default_obj={})
        if not isinstance(state, dict):
            return
        records = state.get("records")
        if not isinstance(records, list):
            return
        target_names: set[str] = set()
        for rec in records:
            if not isinstance(rec, dict):
                continue
            rno = int(rec.get("round") or 0)
            if rno < start_round:
                continue
            af = str(rec.get("analysed_file") or "").strip()
            if not af:
                continue
            target_names.add(Path(af).name)
        resume_obj = self._read_json(csv_resume_state_path, default_obj={})
        if not isinstance(resume_obj, dict):
            return
        files_obj = resume_obj.get("files")
        if not isinstance(files_obj, dict):
            return
        for name in list(files_obj.keys()):
            if str(name) in target_names:
                files_obj.pop(name, None)
        resume_obj["files"] = files_obj
        self._write_json(csv_resume_state_path, resume_obj)

    def _has_analyzable_profiles(self, state_path: Path) -> bool:
        """
        仅当 list2 中至少有一个 URL 在 records 中已有 cleaned_file 时，才进入 analyse 阶段。
        """
        state = self._read_json(state_path, default_obj={})
        if not isinstance(state, dict):
            return False
        list2 = state.get("list2_tutor_profiles")
        records = state.get("records")
        if not isinstance(list2, list) or not isinstance(records, list):
            return False
        list2_set = {str(x).strip() for x in list2 if isinstance(x, str) and str(x).strip()}
        if not list2_set:
            return False
        for rec in records:
            if not isinstance(rec, dict):
                continue
            url = str(rec.get("url") or "").strip()
            cleaned_file = str(rec.get("cleaned_file") or "").strip()
            if url in list2_set and cleaned_file:
                return True
        return False

    @staticmethod
    def _has_pending_list1_pages(state_path: Path) -> bool:
        """
        ``get_tutor_pages`` 单次调用内 ``max_depth=1`` 只跑一轮；link_choose 可能把新 URL 写回
        list1。若主流程仅按 ``max_depth`` 计数退出，会在仍有待爬队列时误进 CSV。
        """
        state = GetTutorInfMainAgent._read_json(state_path, default_obj={})
        if not isinstance(state, dict):
            return False
        list1 = state.get("list1_possible_pages")
        if not isinstance(list1, list):
            return False
        return any(isinstance(x, str) and str(x).strip() for x in list1)

    @staticmethod
    def _needs_more_pages_pass(state_path: Path) -> bool:
        """
        是否还应再跑一轮 ``get_tutor_pages``：待爬 list1 非空，或与子编排一致的
        「清洗完成但 choice 未落盘」中断续跑（与 ``get_tutor_pages`` 内逻辑对齐）。
        """
        if GetTutorInfMainAgent._has_pending_list1_pages(state_path):
            return True
        state = GetTutorInfMainAgent._read_json(state_path, default_obj={})
        if not isinstance(state, dict):
            return False
        try:
            current_round = int(state.get("round") or 0)
        except (TypeError, ValueError):
            current_round = 0
        if current_round <= 0:
            return False
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
            if rno != current_round:
                continue
            cleaned_file = str(rec.get("cleaned_file") or "").strip()
            if not cleaned_file:
                continue
            choice_file = str(rec.get("choice_file") or "").strip()
            if not choice_file:
                return True
        return False

    def run(
        self,
        inv: AgentInvocation[GetTutorInfMainPayload],
        dispatcher: LLMDispatcher,
        *,
        pages_max_tokens: int = 8192,
        pages_choice_max_workers: int = 4,
        analyse_max_tokens: int = 16384,
        analyse_max_workers: int = 4,
        analyse_name_resolve_max_tokens: int = 512,
        analyse_name_resolve_llm_first: bool = True,
        csv_max_tokens: int = 2048,
        csv_repair_max_tokens: int = 4096,
        restart_on_transient_llm_error: bool = True,
        transient_retry_initial_sec: float = 15.0,
        transient_retry_max_sec: float = 120.0,
        transient_swap_fast_slot_pair: bool = True,
    ) -> GetTutorInfMainResult:
        log = AgentLogger("GetTutorInfMainAgent")
        slot_token = [inv.model.token]
        p = inv.llm_part

        def _on_retry(attempt: int, wait_sec: float, e: BaseException) -> None:
            log.warn(
                "LLM 网关/模型暂时不可用，将从断点整任务重试",
                detail=f"attempt={attempt} sleep={wait_sec:.1f}s err={e!s}",
            )
            try_switch_fast_slot_pair(
                dispatcher,
                slot_token,
                log=log,
                enabled=transient_swap_fast_slot_pair,
            )

        return run_with_transient_llm_retries(
            lambda: self._run_once(
                slot_token,
                p,
                dispatcher,
                log=log,
                pages_max_tokens=pages_max_tokens,
                pages_choice_max_workers=pages_choice_max_workers,
                analyse_max_tokens=analyse_max_tokens,
                analyse_max_workers=analyse_max_workers,
                analyse_name_resolve_max_tokens=analyse_name_resolve_max_tokens,
                analyse_name_resolve_llm_first=analyse_name_resolve_llm_first,
                csv_max_tokens=csv_max_tokens,
                csv_repair_max_tokens=csv_repair_max_tokens,
            ),
            restart_on_transient_llm_error=restart_on_transient_llm_error,
            transient_retry_initial_sec=transient_retry_initial_sec,
            transient_retry_max_sec=transient_retry_max_sec,
            on_retry=_on_retry,
        )

    def _run_once(
        self,
        slot_token: list[str],
        p: GetTutorInfMainPayload,
        dispatcher: LLMDispatcher,
        *,
        log: AgentLogger,
        pages_max_tokens: int = 8192,
        pages_choice_max_workers: int = 4,
        analyse_max_tokens: int = 16384,
        analyse_max_workers: int = 4,
        analyse_name_resolve_max_tokens: int = 512,
        analyse_name_resolve_llm_first: bool = True,
        csv_max_tokens: int = 2048,
        csv_repair_max_tokens: int = 4096,
    ) -> GetTutorInfMainResult:
        tok = slot_token[0]
        workdir = Path(p.workdir).resolve()
        if (
            pages_max_tokens <= 0
            or analyse_max_tokens <= 0
            or analyse_name_resolve_max_tokens <= 0
            or csv_max_tokens <= 0
            or csv_repair_max_tokens <= 0
        ):
            raise ValueError("各阶段 max_tokens 必须为正整数")

        # 入口先做一次模型解析校验，避免跑到中途才失败。
        dispatcher.resolve(tok)
        workdir.mkdir(parents=True, exist_ok=True)
        cache_dir = (workdir / "cache").resolve()
        default_state_path = (cache_dir / "state.json").resolve()
        main_state_path = (
            Path(p.main_resume_state_path).resolve()
            if p.main_resume_state_path is not None
            else default_state_path
        )
        state_obj = self._read_json(main_state_path, default_obj={})
        if not isinstance(state_obj, dict):
            state_obj = {}
        state_obj = self._ensure_main_state(state_obj)
        eff = self._resolve_effective_params(payload=p, model_token=tok, state=state_obj)
        state_obj = self._ensure_pages_state_seed(state_obj, eff["academy_url"])
        state_obj["main_task_params"] = eff
        stage = self._normalize_stage(p.resume_from_stage)
        start_round = p.resume_from_round if (p.resume_from_round is not None and p.resume_from_round > 0) else None
        progress = state_obj.setdefault("main_task_progress", {})
        if not isinstance(progress, dict):
            progress = {}
            state_obj["main_task_progress"] = progress
        if stage == "auto":
            # 优先用“最后一轮 roundX 的 pages/analyse 是否 done”来决定起点，
            # 避免出现 main_task_progress.pages=done 但 roundX.pages 仍未完成（choice 中断）导致跳过 pages。
            last_round = progress.get("last_round")
            chosen = None
            if isinstance(last_round, int) and last_round > 0:
                rounds = state_obj.get("main_task_rounds")
                if isinstance(rounds, list):
                    round_entry = next(
                        (
                            x
                            for x in rounds
                            if isinstance(x, dict) and int(x.get("round") or -1) == last_round
                        ),
                        None,
                    )
                    if isinstance(round_entry, dict):
                        rs = round_entry.get("stages")
                        if isinstance(rs, dict):
                            pages_st = rs.get("pages")
                            if isinstance(pages_st, dict) and pages_st.get("status") != "done":
                                chosen = "pages"
                            else:
                                analyse_st = rs.get("analyse")
                                if isinstance(analyse_st, dict) and analyse_st.get("status") != "done":
                                    chosen = "analyse"
            if chosen is None:
                stages = progress.get("stages")
                if isinstance(stages, dict):
                    for candidate in self._STAGES:
                        st = stages.get(candidate)
                        if not isinstance(st, dict) or st.get("status") != "done":
                            stage = candidate
                            break
                    else:
                        stage = "pages"
                else:
                    stage = "pages"
            else:
                stage = chosen
        progress["requested_start_stage"] = stage
        progress["requested_start_round"] = start_round
        progress["status"] = "running"
        self._save_main_only(state_path=main_state_path, main_state=state_obj)

        log.start(
            "开始导师信息主流程",
            detail=(
                f"url={eff['academy_url']} workdir={workdir} slot={tok} "
                f"start_stage={stage} start_round={start_round}"
            ),
        )

        analyse_agent = GetTutorAnalyseAgent()
        pages_agent = GetTutorPagesAgent()
        pages_result: GetTutorPagesResult | None = None
        analyse_result: GetTutorAnalyseResult | None = None

        rounds_budget = int(eff["max_depth"])
        raw_state = self._read_json(main_state_path, default_obj={})
        current_round = int(raw_state.get("round") or 0) if isinstance(raw_state, dict) else 0

        def _pages_done_for_round(round_no: int) -> bool:
            rounds = state_obj.get("main_task_rounds")
            if not isinstance(rounds, list):
                return False
            for x in rounds:
                if not isinstance(x, dict):
                    continue
                try:
                    rno = int(x.get("round") or -1)
                except (TypeError, ValueError):
                    rno = -1
                if rno != round_no:
                    continue
                rs = x.get("stages")
                if not isinstance(rs, dict):
                    return False
                ps = rs.get("pages")
                if not isinstance(ps, dict):
                    return False
                return ps.get("status") == "done"
            return False

        def _analyse_terminal_for_round(round_no: int) -> bool:
            """该轮 analyse 已结束（完成或明确跳过），无需再跑。"""
            rounds = state_obj.get("main_task_rounds")
            if not isinstance(rounds, list):
                return False
            for x in rounds:
                if not isinstance(x, dict):
                    continue
                try:
                    rno = int(x.get("round") or -1)
                except (TypeError, ValueError):
                    rno = -1
                if rno != round_no:
                    continue
                rs = x.get("stages")
                if not isinstance(rs, dict):
                    return False
                an = rs.get("analyse")
                if not isinstance(an, dict):
                    return False
                st = an.get("status")
                return st in ("done", "skipped")
            return False

        # rounds_done 表示“pages 已经完成的轮次数（从 1 起连续推进时近似成立）”。
        # 为了正确续跑，先根据当前 round 的 pages 状态推断起点。
        rounds_done = current_round if _pages_done_for_round(current_round) else max(0, current_round - 1)

        if stage == "csv":
            self._mark_stage(state_obj, round_no=start_round, stage="pages", status="skipped")
            self._mark_stage(state_obj, round_no=start_round, stage="analyse", status="skipped")
            self._save_main_only(state_path=main_state_path, main_state=state_obj)
        else:
            if start_round is not None and stage == "analyse":
                self._prepare_resume_from_round_for_analyse(main_state_path, start_round)
                current_round = start_round - 1
            # 最后一轮 pages 已完成、analyse 中断时 rounds_done 已达 budget，若仅用
            #「rounds_done < budget」会整段跳过 while，从而误进 CSV；需允许补跑 analyse。
            #
            # ``max_depth``（rounds_budget）为抓取阶段**硬上限**：每调用一次 get_tutor_pages（子
            # 编排内 depth=1）计一轮；达到上限后**不再**因 list1 仍非空而加跑，否则会出现
            # 「depth=3 却跑到第 4 轮」。若需清空 list1，请增大 --depth。
            while (
                rounds_done < rounds_budget
                or (
                    _pages_done_for_round(current_round)
                    and not _analyse_terminal_for_round(current_round)
                    and self._has_analyzable_profiles(main_state_path)
                )
            ):
                if stage == "pages" and rounds_done < rounds_budget:
                    target_round = (
                        current_round + 1 if _pages_done_for_round(current_round) else current_round
                    )
                    self._mark_stage(state_obj, round_no=target_round, stage="pages", status="running")
                    self._save_main_only(state_path=main_state_path, main_state=state_obj)
                    log.step(
                        "主流程·抓取阶段",
                        detail=f"即将运行 get_tutor_pages（单轮 depth=1）workdir={workdir}",
                    )
                    pages_result = pages_agent.run(
                        AgentInvocation(
                            model=ModelRef(tok),
                            llm_part=GetTutorPagesPayload(
                                academy_url=eff["academy_url"],
                                output_dir=workdir,
                                # 每次只推进 1 轮，形成“抓取+链接分类 -> 分析主页”的轮次节奏
                                max_depth=1,
                                resume_state_path=eff["pages_resume_state_path"],
                                link_choose_refine_all_links=bool(eff["link_choose_refine_all_links"]),
                                academy_scope_hint=eff.get("academy_scope_hint"),
                                listing_pagination_max_passes=int(
                                    eff["listing_pagination_max_passes"]
                                ),
                                link_choose_refine_batch_parallel_workers=int(
                                    eff["link_choose_refine_batch_parallel_workers"]
                                ),
                            ),
                        ),
                        dispatcher,
                        max_tokens=pages_max_tokens,
                        choice_max_workers=pages_choice_max_workers,
                        restart_on_transient_llm_error=False,
                        transient_swap_fast_slot_pair=False,
                    )
                    current_round = pages_result.round_count
                    self._mark_stage(
                        state_obj,
                        round_no=current_round,
                        stage="pages",
                        status="done",
                        detail={"state_path": str(pages_result.state_path)},
                    )
                    self._save_main_only(state_path=main_state_path, main_state=state_obj)
                    log.step("轮次抓取+链接分类完成", detail=f"round={current_round} state={pages_result.state_path}")
                    rounds_done = max(rounds_done, current_round)

                if self._has_analyzable_profiles(main_state_path):
                    self._mark_stage(state_obj, round_no=current_round, stage="analyse", status="running")
                    self._save_main_only(state_path=main_state_path, main_state=state_obj)
                    log.step(
                        "主流程·分析阶段",
                        detail=f"round={current_round} get_tutor_analyse workdir={workdir}",
                    )
                    analyse_result = analyse_agent.run(
                        AgentInvocation(
                            model=ModelRef(tok),
                            llm_part=GetTutorAnalysePayload(
                                workspace_dir=workdir,
                                analysed_subdir=eff["analysed_subdir"],
                            ),
                        ),
                        dispatcher,
                        max_tokens=analyse_max_tokens,
                        name_resolve_max_tokens=analyse_name_resolve_max_tokens,
                        name_resolve_llm_first=analyse_name_resolve_llm_first,
                        max_workers=analyse_max_workers,
                    )
                    self._mark_stage(
                        state_obj,
                        round_no=current_round,
                        stage="analyse",
                        status="done",
                        detail={"manifest_path": str(analyse_result.manifest_path)},
                    )
                    self._save_main_only(state_path=main_state_path, main_state=state_obj)
                    log.step("轮次主页分析完成", detail=f"round={current_round} manifest={analyse_result.manifest_path}")
                else:
                    self._mark_stage(
                        state_obj,
                        round_no=current_round,
                        stage="analyse",
                        status="skipped",
                        detail={"note": "no_cleaned_tutor_profiles_yet"},
                    )
                    self._save_main_only(state_path=main_state_path, main_state=state_obj)
                    log.step("轮次主页分析跳过", detail=f"round={current_round} no_cleaned_tutor_profiles_yet")
                stage = "pages"

            if rounds_done >= rounds_budget and self._needs_more_pages_pass(main_state_path):
                log.warn(
                    "已达抓取深度上限，list1 仍有待爬 URL",
                    detail=(
                        f"max_depth={rounds_budget} state.round={current_round} "
                        "需继续请增大 --depth"
                    ),
                )

        if analyse_result is None:
            analysed_dir_fallback = (workdir / eff["analysed_subdir"]).resolve()
            analyse_result = GetTutorAnalyseResult(
                workspace_dir=Path(workdir),
                analysed_dir=Path(analysed_dir_fallback),
                manifest_path=Path(analysed_dir_fallback / "manifest.json"),
                success_count=0,
                skipped_count=0,
            )

        analysed_dir = analyse_result.analysed_dir
        Path(analysed_dir).mkdir(parents=True, exist_ok=True)
        csv_path = (
            Path(eff["csv_path"]).resolve()
            if eff["csv_path"] is not None
            else (analysed_dir.parent / "tutor_summary.csv").resolve()
        )
        csv_resume_state_path = (
            Path(eff["csv_resume_state_path"]).resolve()
            if eff["csv_resume_state_path"] is not None
            else (analysed_dir.parent / "cache" / "output_to_csv.resume.json").resolve()
        )
        if start_round is not None and stage == "csv":
            self._prepare_resume_from_round_for_csv(
                state_path=main_state_path,
                analysed_dir=analysed_dir,
                csv_resume_state_path=csv_resume_state_path,
                start_round=start_round,
            )
        self._mark_stage(state_obj, round_no=start_round, stage="csv", status="running")
        self._save_main_only(state_path=main_state_path, main_state=state_obj)
        log.step("主流程·CSV 阶段", detail=f"analysed_dir={analysed_dir} csv={csv_path}")
        output_to_csv_agent = OutputToCsvAgent()
        csv_result = output_to_csv_agent.run(
            AgentInvocation(
                model=ModelRef(tok),
                llm_part=OutputToCsvPayload(
                    analysed_dir=analysed_dir,
                    csv_path=csv_path,
                    resume_state_path=csv_resume_state_path,
                    run_log_path=eff["csv_run_log_path"],
                ),
            ),
            dispatcher,
            max_tokens=csv_max_tokens,
            repair_max_tokens=csv_repair_max_tokens,
        )
        self._mark_stage(
            state_obj,
            round_no=start_round,
            stage="csv",
            status="done",
            detail={"csv_path": str(csv_result.csv_path)},
        )
        progress = state_obj.setdefault("main_task_progress", {})
        if isinstance(progress, dict):
            progress["status"] = "done"
        self._save_main_only(state_path=main_state_path, main_state=state_obj)
        log.done("CSV 汇总完成", detail=f"csv={csv_result.csv_path}")

        return GetTutorInfMainResult(
            workdir=workdir,
            pages_result=pages_result if pages_result is not None else GetTutorPagesResult(
                output_dir=Path(workdir),
                cache_dir=Path(workdir / "cache"),
                cleaned_dir=Path(workdir / "cache" / "cleaned"),
                choice_dir=Path(workdir / "cache" / "choice"),
                state_path=Path(main_state_path),
                round_count=int(start_round or 0),
                list1_pending_count=0,
                list2_tutor_profile_count=0,
                list3_processed_count=0,
            ),
            analyse_result=analyse_result,
            csv_result=csv_result,
        )

    async def arun(
        self,
        inv: AgentInvocation[GetTutorInfMainPayload],
        dispatcher: LLMDispatcher,
        *,
        pages_max_tokens: int = 8192,
        pages_choice_max_workers: int = 4,
        analyse_max_tokens: int = 16384,
        analyse_max_workers: int = 4,
        analyse_name_resolve_max_tokens: int = 512,
        analyse_name_resolve_llm_first: bool = True,
        csv_max_tokens: int = 2048,
        csv_repair_max_tokens: int = 4096,
        restart_on_transient_llm_error: bool = True,
        transient_retry_initial_sec: float = 15.0,
        transient_retry_max_sec: float = 120.0,
        transient_swap_fast_slot_pair: bool = True,
    ) -> GetTutorInfMainResult:
        return await asyncio.to_thread(
            self.run,
            inv,
            dispatcher,
            pages_max_tokens=pages_max_tokens,
            pages_choice_max_workers=pages_choice_max_workers,
            analyse_max_tokens=analyse_max_tokens,
            analyse_max_workers=analyse_max_workers,
            analyse_name_resolve_max_tokens=analyse_name_resolve_max_tokens,
            analyse_name_resolve_llm_first=analyse_name_resolve_llm_first,
            csv_max_tokens=csv_max_tokens,
            csv_repair_max_tokens=csv_repair_max_tokens,
            restart_on_transient_llm_error=restart_on_transient_llm_error,
            transient_retry_initial_sec=transient_retry_initial_sec,
            transient_retry_max_sec=transient_retry_max_sec,
            transient_swap_fast_slot_pair=transient_swap_fast_slot_pair,
        )


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "GetTutorInfMainAgent",
    "GetTutorInfMainPayload",
    "GetTutorInfMainResult",
]
