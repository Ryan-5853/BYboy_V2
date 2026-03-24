"""
命令行：导师信息主流程（抓取页面 + 批量分析）。

示例（在仓库根目录，已配置 .env）::

    python -m byboy.agents.tutor_inf.get_tutor_inf_main \
        "https://example.edu/college" \
        --workdir ./byboy/test/get_tutor_pages_kzgc \
        --slot BYBOY_SLOT_DEFAULT
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.get_tutor_inf_main.agent import (
    GetTutorInfMainAgent,
    GetTutorInfMainPayload,
)
from byboy.llm.dispatcher import LLMDispatcher


def _to_root_relative(path: str | Path) -> str:
    root = Path.cwd().resolve()
    p = Path(path).resolve()
    try:
        return p.relative_to(root).as_posix()
    except ValueError:
        return os.path.relpath(str(p), str(root)).replace("\\", "/")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="导师信息主流程：get_tutor_pages + get_tutor_analyse + output_to_csv"
    )
    p.add_argument("academy_url", help="学院起始页面 URL（http/https）")
    p.add_argument("--workdir", type=Path, required=True, help="统一工作目录")
    p.add_argument("--depth", type=int, default=2, help="get_tutor_pages 最大迭代轮数")
    p.add_argument(
        "--slot",
        "--route",
        "--model",
        dest="slot",
        default="BYBOY_SLOT_DEFAULT",
        help="统一模型/槽位 token（支持 BYBOY_SLOT_* 或直传模型 token）",
    )
    p.add_argument("--pages-max-tokens", type=int, default=8192, help="页面抓取阶段 max_tokens")
    p.add_argument("--analyse-max-tokens", type=int, default=16384, help="导师分析阶段 max_tokens")
    p.add_argument("--csv-max-tokens", type=int, default=2048, help="CSV 抽取阶段 max_tokens")
    p.add_argument(
        "--csv-repair-max-tokens",
        type=int,
        default=4096,
        help="CSV JSON 修复阶段 max_tokens",
    )
    p.add_argument(
        "--pages-resume-state",
        type=Path,
        default=None,
        help="可选：get_tutor_pages 恢复用 state.json 路径",
    )
    p.add_argument(
        "--analysed-subdir",
        default="cache/analysed",
        help="分析结果子目录（相对 workdir），默认 cache/analysed",
    )
    p.add_argument(
        "--csv-path",
        type=Path,
        default=None,
        help="CSV 输出路径；默认 workdir/cache/tutor_summary.csv",
    )
    p.add_argument(
        "--csv-resume-state",
        type=Path,
        default=None,
        help="CSV 阶段断点状态文件路径",
    )
    p.add_argument(
        "--csv-run-log",
        type=Path,
        default=None,
        help="CSV 阶段运行日志 jsonl 路径",
    )
    args = p.parse_args(argv)
    if args.depth <= 0:
        raise SystemExit("--depth 必须为正整数")
    if (
        args.pages_max_tokens <= 0
        or args.analyse_max_tokens <= 0
        or args.csv_max_tokens <= 0
        or args.csv_repair_max_tokens <= 0
    ):
        raise SystemExit("所有 max-tokens 参数都必须为正整数")

    dispatcher = LLMDispatcher.from_env()
    agent = GetTutorInfMainAgent()
    inv = AgentInvocation(
        model=ModelRef(args.slot),
        llm_part=GetTutorInfMainPayload(
            academy_url=args.academy_url,
            workdir=args.workdir,
            max_depth=args.depth,
            pages_resume_state_path=args.pages_resume_state,
            analysed_subdir=args.analysed_subdir,
            csv_path=args.csv_path,
            csv_resume_state_path=args.csv_resume_state,
            csv_run_log_path=args.csv_run_log,
        ),
    )
    result = agent.run(
        inv,
        dispatcher,
        pages_max_tokens=args.pages_max_tokens,
        analyse_max_tokens=args.analyse_max_tokens,
        csv_max_tokens=args.csv_max_tokens,
        csv_repair_max_tokens=args.csv_repair_max_tokens,
    )

    print(f"workdir={_to_root_relative(result.workdir)}")
    print(f"state_path={_to_root_relative(result.pages_result.state_path)}")
    print(f"analysed_manifest={_to_root_relative(result.analyse_result.manifest_path)}")
    print(f"pages_round_count={result.pages_result.round_count}")
    print(f"tutor_profile_count={result.pages_result.list2_tutor_profile_count}")
    print(f"analysed_success_count={result.analyse_result.success_count}")
    print(f"analysed_skipped_count={result.analyse_result.skipped_count}")
    print(f"csv_path={_to_root_relative(result.csv_result.csv_path)}")
    print(f"csv_scanned_count={result.csv_result.scanned_count}")
    print(f"csv_appended_count={result.csv_result.appended_count}")
    print(f"csv_updated_count={result.csv_result.updated_count}")
    print(f"csv_skipped_count={result.csv_result.skipped_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
