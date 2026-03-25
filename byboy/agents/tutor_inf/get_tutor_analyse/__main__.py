"""
命令行：读取 get_tutor_pages 工作空间，批量调用 tutor_analyse 输出 analysed/*.json。

示例（仓库根目录，已配置 .env）::

    python -m byboy.agents.tutor_inf.get_tutor_analyse \
        ./byboy/test/get_tutor_pages_kzgc --route BYBOY_SLOT_DEFAULT
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.get_tutor_analyse.agent import (
    GetTutorAnalyseAgent,
    GetTutorAnalysePayload,
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
    p = argparse.ArgumentParser(description="批量导师页分析：state/cleaned -> cache/analysed")
    p.add_argument(
        "workspace_dir",
        nargs="?",
        type=Path,
        help="get_tutor_pages 工作空间目录；可用 --workdir 传入",
    )
    p.add_argument(
        "--workdir",
        type=Path,
        default=None,
        help="统一工作目录（等价 workspace_dir）",
    )
    p.add_argument(
        "--slot",
        "--route",
        "--model",
        dest="slot",
        default="BYBOY_SLOT_DEFAULT",
        help="统一模型/槽位 token（支持 BYBOY_SLOT_* 或直传模型 token）",
    )
    p.add_argument("--max-tokens", type=int, default=16384, help="tutor_analyse max_tokens")
    p.add_argument(
        "--name-resolve-max-tokens",
        type=int,
        default=512,
        help="LLM 推断导师姓名的 max_tokens（默认 512；默认先 LLM）",
    )
    p.add_argument(
        "--no-name-resolve-llm-first",
        action="store_true",
        help="改为先标题/加粗启发式，失败后再 LLM（默认先 LLM）",
    )
    p.add_argument(
        "--analysed-subdir",
        default="cache/analysed",
        help="分析结果子目录（相对 workspace_dir），默认 cache/analysed",
    )
    args = p.parse_args(argv)
    if args.max_tokens <= 0 or args.name_resolve_max_tokens <= 0:
        raise SystemExit("--max-tokens 与 --name-resolve-max-tokens 必须为正整数")
    workdir = args.workdir or args.workspace_dir
    if workdir is None:
        raise SystemExit("必须提供 workspace_dir 或 --workdir")

    dispatcher = LLMDispatcher.from_env()
    agent = GetTutorAnalyseAgent()
    inv = AgentInvocation(
        model=ModelRef(args.slot),
        llm_part=GetTutorAnalysePayload(
            workspace_dir=workdir,
            analysed_subdir=args.analysed_subdir,
        ),
    )
    result = agent.run(
        inv,
        dispatcher,
        max_tokens=args.max_tokens,
        name_resolve_max_tokens=args.name_resolve_max_tokens,
        name_resolve_llm_first=not args.no_name_resolve_llm_first,
    )
    print(_to_root_relative(result.manifest_path))
    print(f"success_count={result.success_count}")
    print(f"skipped_count={result.skipped_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
