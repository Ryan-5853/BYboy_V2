"""
命令行：分析 webclean Markdown 中的链接并写入 JSON。

示例（在仓库根目录，已配置 .env）::

    python -m byboy.agents.tutor_inf.link_choose path/to/page.md ./out links.json --route BYBOY_SLOT_DEFAULT
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.link_choose.agent import LinkChooseAgent, LinkChoosePayload
from byboy.llm.dispatcher import LLMDispatcher


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="从 webclean Markdown 中提取导师主页链接与可迭代链接（LLM）")
    p.add_argument("markdown_path", type=Path, help="webclean 产出的 .md 文件路径")
    p.add_argument("output_dir", type=Path, help="JSON 输出目录")
    p.add_argument("output_filename", help="JSON 文件名，如 result.json")
    p.add_argument(
        "--route",
        default="BYBOY_SLOT_DEFAULT",
        help="LLM 路由键（推荐传 BYBOY_SLOT_* 代号；也支持 openai:… / claude:…）",
    )
    p.add_argument(
        "--max-tokens",
        type=int,
        default=8192,
        help="补全 max_tokens",
    )
    args = p.parse_args(argv)

    dispatcher = LLMDispatcher.from_env()
    agent = LinkChooseAgent()
    inv = AgentInvocation(
        model=ModelRef(args.route),
        llm_part=LinkChoosePayload(
            markdown_path=args.markdown_path,
            output_dir=args.output_dir,
            output_filename=args.output_filename,
        ),
    )
    out = agent.run(inv, dispatcher, max_tokens=args.max_tokens)
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
