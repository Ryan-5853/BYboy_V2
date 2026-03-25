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
    p.add_argument("academy_url", nargs="?", default=None, help="学院起始页面 URL（http/https，可省略以复用历史状态）")
    p.add_argument("--workdir", type=Path, required=False, default=Path.cwd(), help="统一工作目录（默认当前目录）")
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
    p.add_argument(
        "--pages-choice-max-workers",
        type=int,
        default=4,
        help="页面阶段链接分类并行 worker 数（默认 4）",
    )
    p.add_argument(
        "--link-choose-uncertain-only-llm",
        action="store_true",
        help="link_choose 仅对规则低置信链接调 LLM（默认每条链接都过 LLM）",
    )
    p.add_argument("--analyse-max-tokens", type=int, default=16384, help="导师分析阶段 max_tokens")
    p.add_argument(
        "--analyse-max-workers",
        type=int,
        default=4,
        help="导师分析阶段并行 worker 数（默认 4）",
    )
    p.add_argument(
        "--analyse-name-resolve-max-tokens",
        type=int,
        default=512,
        help="LLM 推断导师姓名的 max_tokens（默认 512；默认先 LLM 再标题/加粗兜底）",
    )
    p.add_argument(
        "--no-analyse-name-resolve-llm-first",
        action="store_true",
        help="改为先标题/加粗启发式，失败后再 LLM（默认先 LLM）",
    )
    p.add_argument("--csv-max-tokens", type=int, default=2048, help="CSV 抽取阶段 max_tokens")
    p.add_argument(
        "--csv-repair-max-tokens",
        type=int,
        default=4096,
        help="CSV JSON 修复阶段 max_tokens",
    )
    p.add_argument(
        "--main-resume-state",
        type=Path,
        default=None,
        help="主流程状态文件路径（默认 workdir/cache/state.json）",
    )
    p.add_argument(
        "--resume-round",
        type=int,
        default=None,
        help="从指定轮次重新开始（可配合 --resume-stage）",
    )
    p.add_argument(
        "--resume-stage",
        choices=["auto", "pages", "analyse", "csv"],
        default="auto",
        help="从哪个阶段开始：auto/pages/analyse/csv",
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
    p.add_argument(
        "--no-restart-on-transient-llm-error",
        action="store_true",
        help="关闭：遇模型/网关暂时不可用时自动整任务重试（默认开启）",
    )
    p.add_argument(
        "--transient-retry-initial-sec",
        type=float,
        default=15.0,
        help="首次重试前等待秒数（默认 15）",
    )
    p.add_argument(
        "--transient-retry-max-sec",
        type=float,
        default=120.0,
        help="重试等待上限秒数，指数退避封顶（默认 120）",
    )
    p.add_argument(
        "--no-transient-swap-fast-slot-pair",
        action="store_true",
        help="关闭：瞬时故障时在 BYBOY_SLOT_FAST / BYBOY_SLOT_FAST2 间切换（默认开启）",
    )
    args = p.parse_args(argv)
    if args.resume_round is not None and args.resume_round <= 0:
        raise SystemExit("--resume-round 必须为正整数")
    if args.depth <= 0:
        raise SystemExit("--depth 必须为正整数")
    if (
        args.pages_max_tokens <= 0
        or args.analyse_max_tokens <= 0
        or args.analyse_name_resolve_max_tokens <= 0
        or args.csv_max_tokens <= 0
        or args.csv_repair_max_tokens <= 0
    ):
        raise SystemExit("所有 max-tokens 参数都必须为正整数")
    if args.pages_choice_max_workers <= 0 or args.analyse_max_workers <= 0:
        raise SystemExit("并行 worker 数必须为正整数")
    if args.transient_retry_initial_sec <= 0 or args.transient_retry_max_sec <= 0:
        raise SystemExit("transient-retry 秒数必须为正数")

    dispatcher = LLMDispatcher.from_env()
    agent = GetTutorInfMainAgent()
    inv = AgentInvocation(
        model=ModelRef(args.slot),
        llm_part=GetTutorInfMainPayload(
            academy_url=args.academy_url,
            workdir=args.workdir,
            max_depth=args.depth,
            pages_resume_state_path=args.pages_resume_state,
            main_resume_state_path=args.main_resume_state,
            analysed_subdir=args.analysed_subdir,
            csv_path=args.csv_path,
            csv_resume_state_path=args.csv_resume_state,
            csv_run_log_path=args.csv_run_log,
            link_choose_refine_all_links=not args.link_choose_uncertain_only_llm,
            resume_from_round=args.resume_round,
            resume_from_stage=args.resume_stage,
        ),
    )
    result = agent.run(
        inv,
        dispatcher,
        pages_max_tokens=args.pages_max_tokens,
        pages_choice_max_workers=args.pages_choice_max_workers,
        analyse_max_tokens=args.analyse_max_tokens,
        analyse_max_workers=args.analyse_max_workers,
        analyse_name_resolve_max_tokens=args.analyse_name_resolve_max_tokens,
        analyse_name_resolve_llm_first=not args.no_analyse_name_resolve_llm_first,
        csv_max_tokens=args.csv_max_tokens,
        csv_repair_max_tokens=args.csv_repair_max_tokens,
        restart_on_transient_llm_error=not args.no_restart_on_transient_llm_error,
        transient_retry_initial_sec=args.transient_retry_initial_sec,
        transient_retry_max_sec=args.transient_retry_max_sec,
        transient_swap_fast_slot_pair=not args.no_transient_swap_fast_slot_pair,
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
