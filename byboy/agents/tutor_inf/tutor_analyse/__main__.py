"""
命令行：抓取导师页为 Markdown（写入本包 cache/），再输出结构化 JSON。

示例（仓库根目录，已配置 .env）::

    python -m byboy.agents.tutor_inf.tutor_analyse \\
        "https://example.edu/faculty/zhang" 张三 ./out zhang.json --route default
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.tutor_analyse.agent import TutorAnalyseAgent, TutorAnalysePayload
from byboy.llm.dispatcher import LLMDispatcher


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="导师主页：web_clean 缓存 + LLM 全文结构化 JSON")
    p.add_argument("url", help="导师主页 http(s) URL")
    p.add_argument("tutor_name_cn", help="导师中文姓名（上下文对齐）")
    p.add_argument("output_dir", type=Path, help="结构化 JSON 输出目录")
    p.add_argument("output_filename", help="JSON 文件名，如 result.json")
    p.add_argument(
        "--route",
        default="default",
        help="LLM 路由键（槽位名或 openai:… / claude:…），默认 default",
    )
    p.add_argument(
        "--max-tokens",
        type=int,
        default=16384,
        help="补全 max_tokens，默认 16384",
    )
    p.add_argument(
        "--markdown-path",
        type=Path,
        default=None,
        help="跳过 Firecrawl，直接使用已有 webclean 风格 .md（仍会复制到本包 cache/）",
    )
    args = p.parse_args(argv)

    dispatcher = LLMDispatcher.from_env()
    agent = TutorAnalyseAgent()
    inv = AgentInvocation(
        model=ModelRef(args.route),
        llm_part=TutorAnalysePayload(
            url=args.url,
            tutor_name_cn=args.tutor_name_cn,
            output_dir=args.output_dir,
            output_filename=args.output_filename,
            markdown_path=args.markdown_path,
        ),
    )
    result = agent.run(inv, dispatcher, max_tokens=args.max_tokens)
    print(str(result.json_path))
    print(f"markdown_cache={result.markdown_cache_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
