"""
对单张导师页相关图片做多模态识别，输出与 ``tutor_analyse`` 同风格的结构化 JSON（侧车文件）。
"""

from __future__ import annotations

import asyncio
import base64
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from byboy.agent.invoke import AgentInvocation, ModelRef, slot_complete
from byboy.agents.tutor_inf.link_choose import LinkChooseError, parse_llm_json_object
from byboy.agents.tutor_inf.logging_utils import (
    AgentLogger,
    log_llm_wait_done,
    log_llm_wait_start,
    run_with_periodic_wait_log,
)
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.route_spec import ChatMessage


class PicRecogError(RuntimeError):
    """视觉模型输出解析失败。"""


@dataclass(frozen=True, slots=True)
class PicRecogPayload:
    """单张图片路径 + 导师中文名（与 ``tutor_analyse`` 对齐上下文）。"""

    image_path: str | Path
    tutor_name_cn: str


@dataclass(frozen=True, slots=True)
class PicRecogResult:
    """写入磁盘后的侧车 JSON 路径。"""

    json_path: Path


VISION_SYSTEM_PROMPT = """你是高校导师个人主页信息整理助手（**视觉**）。用户会提供：
1) 目标导师的中文姓名（用于判断画面/文字是否主要介绍该人；若图中含多人，请分别标注与谁相关）。
2) **一张**从导师个人主页上保存下来的图片（可能是头像、简介横幅、招生海报、履历表截图、办公信息图等）。

【硬性要求】
- 你必须**穷尽**该图片中可见的**全部**事实性、描述性文字与可辨认的结构化信息，不得因主观认为「次要」「常见」而删减。
- 包括但不限于：姓名与别名、职称职务、行政级别、所属单位、联系方式、办公地址、招生/研究方向、教育经历、工作/科研经历、项目、论文、专利、获奖、课程、社会兼职、简介段落、表格与列表、页脚小字、水印旁文字等——只要图上可读，就要以某种形式进入输出。
- 若图为装饰/校徽/与具体导师无关的模板图，仍请用标签标明性质，并**保留**可见文字要点，不要随意整段丢弃。
- 输出必须是**单个 JSON 对象**（可任意嵌套、任意键名），用**标签/分类**组织信息：例如多组 { "tags": ["标签1","标签2"], "content": "…" }；「标签」可用中文或英文。
- **禁止**输出 Markdown 代码围栏；**禁止**在 JSON 外附加解释文字。

请只输出 JSON。"""


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


def _user_text(tutor_name_cn: str, image_filename: str) -> str:
    return "\n".join(
        [
            f"目标导师中文姓名（查询键）：{tutor_name_cn.strip() or '（未提供，请据画面文字推断并注明不确定性）'}",
            f"来源图片文件名：{image_filename}",
            "请根据上图抽取信息，只输出 JSON。",
        ]
    )


class PicRecogAgent:
    """单图视觉结构化；``content`` 使用 OpenAI 风格 ``image_url`` data URL（Claude 通道会经网关转换）。"""

    def run(
        self,
        inv: AgentInvocation[PicRecogPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
    ) -> PicRecogResult:
        log = AgentLogger("PicRecogAgent")
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        path = Path(p.image_path).resolve()
        log.start("开始单图识别", detail=path.name)
        if not path.is_file():
            raise FileNotFoundError(f"图片不存在: {path}")
        raw_bytes = path.read_bytes()
        if not raw_bytes:
            raise PicRecogError(f"图片为空: {path}")
        mime = _mime_for_path(path)
        b64 = base64.standard_b64encode(raw_bytes).decode("ascii")
        data_url = f"data:{mime};base64,{b64}"

        messages: list[ChatMessage] = [
            {"role": "system", "content": VISION_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": _user_text(p.tutor_name_cn, path.name)},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            },
        ]
        t0 = log_llm_wait_start(
            log,
            model=inv.model.token,
            payload=messages,
            max_tokens=max_tokens,
            stage="pic_recog_extract",
        )
        out = run_with_periodic_wait_log(
            log=log,
            stage="pic_recog_extract",
            wait_message="等待模型响应中",
            every_sec=5.0,
            fn=lambda: slot_complete(
                dispatcher,
                inv.model.token,
                messages,
                max_tokens=max_tokens,
            ),
        )
        log_llm_wait_done(log, stage="pic_recog_extract", started_at=t0)
        try:
            obj = parse_llm_json_object(out)
        except LinkChooseError as e:
            raise PicRecogError(str(e)) from e
        if not isinstance(obj, dict):
            raise PicRecogError("模型输出 JSON 根节点必须是对象")

        sidecar = {
            "source_image": path.name,
            "source_image_path": str(path),
            "tutor_name_cn": p.tutor_name_cn.strip(),
            "extracted": obj,
        }
        json_path = path.with_suffix(".json")
        json_path.write_text(
            json.dumps(sidecar, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        log.done("写入单图识别结果", detail=str(json_path))
        return PicRecogResult(json_path=json_path)

    async def arun(
        self,
        inv: AgentInvocation[PicRecogPayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
    ) -> PicRecogResult:
        return await asyncio.to_thread(self.run, inv, dispatcher, max_tokens=max_tokens)


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "PicRecogAgent",
    "PicRecogError",
    "PicRecogPayload",
    "PicRecogResult",
]
