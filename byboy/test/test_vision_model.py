"""
最小可运行的视觉模型测试脚本：读取本地图片，经 BYboy 的 ``vision`` 路由调用模型并打印结果。

用法（仓库根目录）::

    python -m byboy.test.test_vision_model
    python -m byboy.test.test_vision_model --image byboy/test/image.png --route vision
"""

from __future__ import annotations

import argparse
import base64
from pathlib import Path

from byboy.llm.dispatcher import LLMDispatcher
from byboy.settings import vision_model_from_env


def _mime_for_path(path: Path) -> str:
    m = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".bmp": "image/bmp",
        ".svg": "image/svg+xml",
    }
    return m.get(path.suffix.lower(), "image/png")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="测试视觉模型：输入图片并输出识别文本")
    parser.add_argument(
        "--image",
        default="byboy/test/image.png",
        help="测试图片路径，默认 byboy/test/image.png",
    )
    parser.add_argument(
        "--route",
        default="vision",
        help="路由键，默认 vision（推荐）",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=2048,
        help="输出 token 上限，默认 2048",
    )
    parser.add_argument(
        "--save",
        default=None,
        help="可选：把模型输出保存到文件（如 byboy/test/vision_output.txt）",
    )
    args = parser.parse_args(argv)

    image_path = Path(args.image).resolve()
    if not image_path.is_file():
        raise FileNotFoundError(f"图片不存在: {image_path}")

    raw = image_path.read_bytes()
    if not raw:
        raise ValueError(f"图片为空: {image_path}")

    mime = _mime_for_path(image_path)
    b64 = base64.standard_b64encode(raw).decode("ascii")
    data_url = f"data:{mime};base64,{b64}"

    messages = [
        {
            "role": "system",
            "content": "你是图像理解助手。请准确描述图片中可见内容，优先提取文字信息。",
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "请输出这张图的主要内容，并尽量完整识别图中文字。",
                },
                {"type": "image_url", "image_url": {"url": data_url}},
            ],
        },
    ]

    disp = LLMDispatcher.from_env()
    resolved = disp.resolve(args.route)
    text = disp.complete(args.route, messages, max_tokens=args.max_tokens, temperature=0)

    output_text = text.strip() if text else ""
    print(f"[route] {args.route}")
    print(f"[backend] {resolved.backend}")
    print(f"[model] {resolved.model or vision_model_from_env()}")
    print("\n===== model output =====\n")
    print(output_text)

    if args.save:
        out_path = Path(args.save).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_text + "\n", encoding="utf-8", newline="\n")
        print(f"\n[saved] {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
