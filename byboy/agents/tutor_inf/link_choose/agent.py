"""
从 webclean 产出的 Markdown 中，用 LLM 归类链接：导师主页链接 vs 可迭代扩展的站内链接，
并写入 JSON。正文为 Markdown（由 HTML 转换而来），链接以 ``[锚文本](url)`` 等形式保留。
"""

from __future__ import annotations

import asyncio
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from byboy.agent.invoke import AgentInvocation, ModelRef, agent_complete
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.route_spec import ChatMessage


class LinkChooseError(RuntimeError):
    """解析或校验 LLM 输出失败。"""


@dataclass(frozen=True, slots=True)
class LinkChoosePayload:
    """单次分析：webclean Markdown 路径 + JSON 输出目录与文件名。"""

    markdown_path: str | Path
    output_dir: str | Path
    output_filename: str


def _read_markdown_source_declaration(md: str) -> str | None:
    """读取首行 ``> 抓取来源：URL``（webclean 约定），若无则返回 None。"""
    for line in md.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^>\s*抓取来源：\s*(\S+)\s*$", s)
        if m:
            return m.group(1).strip()
        break
    return None


def _output_path(payload: LinkChoosePayload) -> Path:
    name = payload.output_filename.strip()
    if not name:
        raise ValueError("output_filename 不能为空")
    base = Path(payload.output_dir)
    return (base / name).resolve()


def _strip_json_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```(?:json)?\s*", "", t, flags=re.IGNORECASE)
        t = re.sub(r"\s*```\s*$", "", t)
    return t.strip()


def parse_llm_json_object(text: str) -> dict[str, Any]:
    """从模型回复中取出单个 JSON 对象并 ``json.loads``。"""
    raw = _strip_json_fence(text)
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError as e:
        raise LinkChooseError(f"模型输出不是合法 JSON: {e}") from e
    if not isinstance(obj, dict):
        raise LinkChooseError("模型输出 JSON 根节点必须是对象")
    return obj


def _validate_schema(obj: dict[str, Any]) -> None:
    required = ("tutor_homepage_links", "iteration_links", "debug")
    for k in required:
        if k not in obj:
            raise LinkChooseError(f"JSON 缺少必填键 {k!r}")
    if not isinstance(obj["tutor_homepage_links"], list):
        raise LinkChooseError("tutor_homepage_links 必须是数组")
    if not isinstance(obj["iteration_links"], list):
        raise LinkChooseError("iteration_links 必须是数组")
    if not isinstance(obj["debug"], dict):
        raise LinkChooseError("debug 必须是对象")


SYSTEM_PROMPT = """你是高校院系网站爬虫规划助手。用户会给你一整页由工具从 HTML 转成的 Markdown，
其中链接通常以 [锚文本](URL "可选标题") 等形式出现。请通读全文，识别并分类链接。

【任务】
1) tutor_homepage_links：直接指向**某位导师个人主页/简介页**的链接。每条须尽量给出：
   - url（完整 URL）
   - anchor_text（Markdown 中的可见锚文本，若无则 ""）
   - tutor_name（推断的导师姓名；若锚文本即姓名可直接采用；不确定可 ""）
   - department_or_unit（从上下文推断的院系、研究所、职称栏等，无则 ""）
   - evidence（一两句说明为何判定为导师主页）
   - confidence：\"high\" | \"medium\" | \"low\"

2) iteration_links：不指向具体某位导师主页，但**在同一学校/同一学院体系内**、抓取后**很可能列出更多导师或分页**的链接。例如：教师名录下一页、博导/硕导子列表、同院其他系师资页、本站点内「师资」「导师介绍」等导航。每条给出：
   - url
   - anchor_text
   - purpose（简短说明用途）
   - why_in_scope（为何认为是本站内扩展而非外链）
   - confidence：\"high\" | \"medium\" | \"low\"

3) 必须排除的外链/无关链：
   - 其他大学、其他学院域名、政府/新闻/商业网站
   - 邮箱 mailto:、纯下载文件、仅登录/注册
   - 与师资/导师名录明显无关的栏目（除非用户 Markdown 几乎只有导航且你只能列可疑项，此时放入 iteration_links 并标低 confidence）

若用户消息中提供了「页面来源 URL」，请以其域名/路径为**站内**判断依据；同主域或明显同一站点的子路径视为站内。

4) debug：对象，可包含任意子字段，用于你的判断备注，**至少**包含：
   - notes：字符串数组，简要记录分类依据或歧义
   - suspicions：字符串数组，页面异常怀疑、内容过少、可能未列全导师、分页未出现等

【输出要求】
- 只输出一个 JSON 对象，不要 Markdown 代码块、不要前后解释文字。
- 键名固定为：tutor_homepage_links、iteration_links、debug（英文键）。
- 两类链接数组中的元素均为对象；没有合适项时用 []。"""


def _user_content(markdown_text: str, declared_source_url: str | None) -> str:
    parts = [
        "以下为一页内容的 Markdown（由网页转换而来）。请按系统说明输出 JSON。",
    ]
    if declared_source_url:
        parts.append(f"页面来源 URL（用于判断站内/站外）：{declared_source_url}")
    parts.append("----- 正文开始 -----")
    parts.append(markdown_text)
    parts.append("----- 正文结束 -----")
    return "\n".join(parts)


class LinkChooseAgent:
    """``LlmCallingAgent`` 形态：``llm_part`` 为 ``LinkChoosePayload``，结果写入 JSON 文件。"""

    def run(
        self,
        inv: AgentInvocation[LinkChoosePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 8192,
    ) -> Path:
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        md_path = Path(p.markdown_path).resolve()
        if not md_path.is_file():
            raise FileNotFoundError(f"Markdown 文件不存在: {md_path}")
        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        declared = _read_markdown_source_declaration(md_text)
        messages: list[ChatMessage] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _user_content(md_text, declared)},
        ]
        inv_chat = AgentInvocation(model=inv.model, llm_part=messages)
        raw = agent_complete(
            dispatcher,
            inv_chat,
            max_tokens=max_tokens,
        )
        obj = parse_llm_json_object(raw)
        _validate_schema(obj)
        meta = {
            "markdown_path": str(md_path),
            "declared_source_url": declared,
            "page_host": urlsplit(declared).netloc if declared else None,
        }
        out_obj = {
            "meta": meta,
            "tutor_homepage_links": obj["tutor_homepage_links"],
            "iteration_links": obj["iteration_links"],
            "debug": obj["debug"],
        }
        out = _output_path(p)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(out_obj, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return out

    async def arun(
        self,
        inv: AgentInvocation[LinkChoosePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 8192,
    ) -> Path:
        return await asyncio.to_thread(self.run, inv, dispatcher, max_tokens=max_tokens)


__all__ = [
    "LinkChooseAgent",
    "LinkChooseError",
    "LinkChoosePayload",
    "ModelRef",
    "AgentInvocation",
    "parse_llm_json_object",
]
