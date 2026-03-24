"""
命令行：读取 analysed 目录内导师 JSON，LLM 抽取固定字段并增量写入 CSV。

示例（仓库根目录，已配置 .env）::

    python -m byboy.agents.tutor_inf.output_to_csv \
        ./byboy/test/get_tutor_pages_kzgc/cache/analysed \
        --route BYBOY_SLOT_DEFAULT
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.output_to_csv.agent import OutputToCsvAgent, OutputToCsvPayload
from byboy.llm.dispatcher import LLMDispatcher


def _to_root_relative(path: str | Path) -> str:
    root = Path.cwd().resolve()
    p = Path(path).resolve()
    try:
        return p.relative_to(root).as_posix()
    except ValueError:
        return os.path.relpath(str(p), str(root)).replace("\\", "/")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="analysed JSON -> LLM 抽取 -> CSV 增量写入")
    p.add_argument("analysed_dir", type=Path, help="导师 analysed JSON 目录")
    p.add_argument(
        "--csv-path",
        type=Path,
        default=None,
        help="CSV 输出路径；默认 analysed_dir 同级 tutor_summary.csv",
    )
    p.add_argument(
        "--route",
        default="BYBOY_SLOT_DEFAULT",
        help="LLM 路由键（推荐传 BYBOY_SLOT_* 代号）",
    )
    p.add_argument("--max-tokens", type=int, default=2048, help="抽取阶段 max_tokens")
    p.add_argument(
        "--repair-max-tokens",
        type=int,
        default=4096,
        help="JSON 修复阶段 max_tokens",
    )
    p.add_argument(
        "--resume-state-path",
        type=Path,
        default=None,
        help="断点状态文件路径；默认 analysed 同级 cache/output_to_csv.resume.json",
    )
    p.add_argument(
        "--run-log-path",
        type=Path,
        default=None,
        help="逐文件处理日志 jsonl 路径；默认 analysed 同级 cache/run_output_to_csv.jsonl",
    )
    args = p.parse_args(argv)
    if args.max_tokens <= 0 or args.repair_max_tokens <= 0:
        raise SystemExit("--max-tokens 与 --repair-max-tokens 必须为正整数")

    analysed_dir = args.analysed_dir
    csv_path = (
        args.csv_path
        if args.csv_path is not None
        else (analysed_dir.parent / "tutor_summary.csv")
    )

    dispatcher = LLMDispatcher.from_env()
    agent = OutputToCsvAgent()
    inv = AgentInvocation(
        model=ModelRef(args.route),
        llm_part=OutputToCsvPayload(
            analysed_dir=analysed_dir,
            csv_path=csv_path,
            resume_state_path=args.resume_state_path,
            run_log_path=args.run_log_path,
        ),
    )
    result = agent.run(
        inv,
        dispatcher,
        max_tokens=args.max_tokens,
        repair_max_tokens=args.repair_max_tokens,
    )
    print(_to_root_relative(result.csv_path))
    print(f"scanned_count={result.scanned_count}")
    print(f"parsed_count={result.parsed_count}")
    print(f"appended_count={result.appended_count}")
    print(f"updated_count={result.updated_count}")
    print(f"skipped_count={result.skipped_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
