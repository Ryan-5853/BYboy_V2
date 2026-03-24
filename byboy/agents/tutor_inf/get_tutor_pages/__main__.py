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
        "--resume-state",
        type=Path,
        default=None,
        help="断点续跑状态文件路径（state.json），指定后按该文件所在 cache 目录恢复上下文",
    )
    args = p.parse_args(argv)
    if args.depth <= 0:
        raise SystemExit("--depth 必须为正整数")
    if args.max_tokens <= 0:
        raise SystemExit("--max-tokens 必须为正整数")
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
        ),
    )
    result = agent.run(inv, dispatcher, max_tokens=args.max_tokens)
    print(_to_root_relative(result.state_path))
    print(f"round_count={result.round_count}")
    print(f"list1_pending_count={result.list1_pending_count}")
    print(f"list2_tutor_profile_count={result.list2_tutor_profile_count}")
    print(f"list3_processed_count={result.list3_processed_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
