"""
命令行：迭代抓取学院站内导师相关页面链接。

示例（在仓库根目录，已配置 .env）::

    python -m byboy.agents.tutor_inf.get_tutor_pages \
        "https://example.edu/college" ./out --depth 3 --route BYBOY_SLOT_DEFAULT
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.get_tutor_pages.agent import GetTutorPagesAgent, GetTutorPagesPayload
from byboy.llm.dispatcher import LLMDispatcher


def _to_root_relative(path: str | Path) -> str:
    root = Path.cwd().resolve()
    p = Path(path).resolve()
    try:
        return p.relative_to(root).as_posix()
    except ValueError:
        return os.path.relpath(str(p), str(root)).replace("\\", "/")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="导师页面抓取编排：web_clean + link_choose 迭代")
    p.add_argument("academy_url", help="学院网站 URL（http/https）")
    p.add_argument(
        "output_dir",
        nargs="?",
        type=Path,
        help="输出目录（含 cache 子目录）；可用 --workdir 传入",
    )
    p.add_argument(
        "--workdir",
        type=Path,
        default=None,
        help="统一工作目录（等价 output_dir）",
    )
    p.add_argument("--depth", type=int, default=2, help="最大迭代轮数，默认 2")
    p.add_argument(
        "--slot",
        "--route",
        "--model",
        dest="slot",
        default="BYBOY_SLOT_DEFAULT",
        help="统一模型/槽位 token（支持 BYBOY_SLOT_* 或直传模型 token）",
    )
    p.add_argument("--max-tokens", type=int, default=8192, help="link_choose max_tokens")
    p.add_argument(
        "--link-choose-uncertain-only-llm",
        action="store_true",
        help="link_choose 仅对规则低置信链接调 LLM（默认每条链接都过 LLM）",
    )
    p.add_argument(
        "--resume-state",
        type=Path,
        default=None,
        help="断点续跑状态文件路径（state.json），指定后按该文件所在 cache 目录恢复上下文",
    )
    p.add_argument(
        "--no-restart-on-transient-llm-error",
        action="store_true",
        help="关闭：遇模型/网关暂时不可用时自动从断点重试（默认开启）",
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
        help="重试等待上限秒数（默认 120）",
    )
    p.add_argument(
        "--no-transient-swap-fast-slot-pair",
        action="store_true",
        help="关闭：瞬时故障时在 BYBOY_SLOT_FAST / BYBOY_SLOT_FAST2 间切换（默认开启）",
    )
    args = p.parse_args(argv)
    if args.depth <= 0:
        raise SystemExit("--depth 必须为正整数")
    if args.max_tokens <= 0:
        raise SystemExit("--max-tokens 必须为正整数")
    if args.transient_retry_initial_sec <= 0 or args.transient_retry_max_sec <= 0:
        raise SystemExit("transient-retry 秒数必须为正数")
    workdir = args.workdir or args.output_dir
    if workdir is None:
        raise SystemExit("必须提供 output_dir 或 --workdir")

    dispatcher = LLMDispatcher.from_env()
    agent = GetTutorPagesAgent()
    inv = AgentInvocation(
        model=ModelRef(args.slot),
        llm_part=GetTutorPagesPayload(
            academy_url=args.academy_url,
            output_dir=workdir,
            max_depth=args.depth,
            resume_state_path=args.resume_state,
            link_choose_refine_all_links=not args.link_choose_uncertain_only_llm,
        ),
    )
    result = agent.run(
        inv,
        dispatcher,
        max_tokens=args.max_tokens,
        restart_on_transient_llm_error=not args.no_restart_on_transient_llm_error,
        transient_retry_initial_sec=args.transient_retry_initial_sec,
        transient_retry_max_sec=args.transient_retry_max_sec,
        transient_swap_fast_slot_pair=not args.no_transient_swap_fast_slot_pair,
    )
    print(_to_root_relative(result.state_path))
    print(f"round_count={result.round_count}")
    print(f"list1_pending_count={result.list1_pending_count}")
    print(f"list2_tutor_profile_count={result.list2_tutor_profile_count}")
    print(f"list3_processed_count={result.list3_processed_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
