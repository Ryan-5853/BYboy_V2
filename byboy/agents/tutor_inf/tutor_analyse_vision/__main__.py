"""
命令行：HTML 找图（写入本包 cache/<sha256>/images/），逐张视觉识别并合并为结构化 JSON。

示例（仓库根目录，已配置 .env）::

    python -m byboy.agents.tutor_inf.tutor_analyse_vision \\
        "https://example.edu/faculty/zhang" 张三 ./out zhang_vision.json --route openai
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.tutor_analyse import TutorAnalysePayload
from byboy.agents.tutor_inf.tutor_analyse_vision.agent import TutorAnalyseVisionAgent
from byboy.llm.dispatcher import LLMDispatcher


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="导师主页：HTML 抽图 + 视觉结构化 + JSON 合并")
    p.add_argument("url", help="导师主页 http(s) URL")
    p.add_argument("tutor_name_cn", help="导师中文姓名（上下文对齐）")
    p.add_argument("output_dir", type=Path, help="最终结构化 JSON 输出目录")
    p.add_argument("output_filename", help="JSON 文件名，如 result.json")
    p.add_argument(
        "--route",
        default="default",
        help="LLM 路由键（须为支持视觉的模型；槽位名或 openai:… / claude:…）",
    )
    p.add_argument(
        "--max-tokens",
        type=int,
        default=16384,
        help="单图识别 max_tokens，默认 16384",
    )
    p.add_argument(
        "--merge-max-tokens",
        type=int,
        default=None,
        help="合并阶段 max_tokens，默认与 --max-tokens 相同",
    )
    p.add_argument(
        "--markdown-path",
        type=Path,
        default=None,
        help="与 tutor_analyse 参数对齐；视觉流水线仍从 url 拉取 HTML 找图，仅写入占位 md 说明",
    )
    args = p.parse_args(argv)

    dispatcher = LLMDispatcher.from_env()
    agent = TutorAnalyseVisionAgent()
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
    result = agent.run(
        inv,
        dispatcher,
        max_tokens=args.max_tokens,
        merge_max_tokens=args.merge_max_tokens,
    )
    print(str(result.json_path))
    print(f"markdown_cache={result.markdown_cache_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
