"""
导师信息主流程编排：
接收学院起始页 URL、模型/槽位 token、工作目录，
顺序执行 get_tutor_pages 与 get_tutor_analyse。
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path

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
from byboy.agents.tutor_inf.output_to_csv import (
    OutputToCsvAgent,
    OutputToCsvPayload,
    OutputToCsvResult,
)
from byboy.llm.dispatcher import LLMDispatcher


@dataclass(frozen=True, slots=True)
class GetTutorInfMainPayload:
    academy_url: str
    workdir: str | Path
    max_depth: int = 2
    pages_resume_state_path: str | Path | None = None
    analysed_subdir: str = "cache/analysed"
    csv_path: str | Path | None = None
    csv_resume_state_path: str | Path | None = None
    csv_run_log_path: str | Path | None = None


@dataclass(frozen=True, slots=True)
class GetTutorInfMainResult:
    workdir: Path
    pages_result: GetTutorPagesResult
    analyse_result: GetTutorAnalyseResult
    csv_result: OutputToCsvResult


class GetTutorInfMainAgent:
    def run(
        self,
        inv: AgentInvocation[GetTutorInfMainPayload],
        dispatcher: LLMDispatcher,
        *,
        pages_max_tokens: int = 8192,
        analyse_max_tokens: int = 16384,
        csv_max_tokens: int = 2048,
        csv_repair_max_tokens: int = 4096,
    ) -> GetTutorInfMainResult:
        log = AgentLogger("GetTutorInfMainAgent")
        p = inv.llm_part
        workdir = Path(p.workdir).resolve()
        if not p.academy_url.strip():
            raise ValueError("academy_url 不能为空")
        if p.max_depth <= 0:
            raise ValueError("max_depth 必须为正整数")
        if (
            pages_max_tokens <= 0
            or analyse_max_tokens <= 0
            or csv_max_tokens <= 0
            or csv_repair_max_tokens <= 0
        ):
            raise ValueError("各阶段 max_tokens 必须为正整数")

        # 入口先做一次模型解析校验，避免跑到中途才失败。
        dispatcher.resolve(inv.model.token)
        workdir.mkdir(parents=True, exist_ok=True)

        log.start(
            "开始导师信息主流程",
            detail=f"url={p.academy_url} workdir={workdir} slot={inv.model.token}",
        )

        pages_agent = GetTutorPagesAgent()
        pages_result = pages_agent.run(
            AgentInvocation(
                model=ModelRef(inv.model.token),
                llm_part=GetTutorPagesPayload(
                    academy_url=p.academy_url,
                    output_dir=workdir,
                    max_depth=p.max_depth,
                    resume_state_path=p.pages_resume_state_path,
                ),
            ),
            dispatcher,
            max_tokens=pages_max_tokens,
        )
        log.step("导师页面抓取完成", detail=f"state={pages_result.state_path}")

        analyse_agent = GetTutorAnalyseAgent()
        analyse_result = analyse_agent.run(
            AgentInvocation(
                model=ModelRef(inv.model.token),
                llm_part=GetTutorAnalysePayload(
                    workspace_dir=workdir,
                    analysed_subdir=p.analysed_subdir,
                ),
            ),
            dispatcher,
            max_tokens=analyse_max_tokens,
        )
        log.step("导师分析完成", detail=f"manifest={analyse_result.manifest_path}")

        analysed_dir = analyse_result.analysed_dir
        csv_path = (
            Path(p.csv_path).resolve()
            if p.csv_path is not None
            else (analysed_dir.parent / "tutor_summary.csv").resolve()
        )
        output_to_csv_agent = OutputToCsvAgent()
        csv_result = output_to_csv_agent.run(
            AgentInvocation(
                model=ModelRef(inv.model.token),
                llm_part=OutputToCsvPayload(
                    analysed_dir=analysed_dir,
                    csv_path=csv_path,
                    resume_state_path=p.csv_resume_state_path,
                    run_log_path=p.csv_run_log_path,
                ),
            ),
            dispatcher,
            max_tokens=csv_max_tokens,
            repair_max_tokens=csv_repair_max_tokens,
        )
        log.done("CSV 汇总完成", detail=f"csv={csv_result.csv_path}")

        return GetTutorInfMainResult(
            workdir=workdir,
            pages_result=pages_result,
            analyse_result=analyse_result,
            csv_result=csv_result,
        )

    async def arun(
        self,
        inv: AgentInvocation[GetTutorInfMainPayload],
        dispatcher: LLMDispatcher,
        *,
        pages_max_tokens: int = 8192,
        analyse_max_tokens: int = 16384,
        csv_max_tokens: int = 2048,
        csv_repair_max_tokens: int = 4096,
    ) -> GetTutorInfMainResult:
        return await asyncio.to_thread(
            self.run,
            inv,
            dispatcher,
            pages_max_tokens=pages_max_tokens,
            analyse_max_tokens=analyse_max_tokens,
            csv_max_tokens=csv_max_tokens,
            csv_repair_max_tokens=csv_repair_max_tokens,
        )


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "GetTutorInfMainAgent",
    "GetTutorInfMainPayload",
    "GetTutorInfMainResult",
]
