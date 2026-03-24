"""
导师主页分析：先经 ``web_clean`` 将 URL 落盘到本包 ``cache/``，再用 LLM 将 Markdown
全文结构化为带标签的 JSON（不预设固定 schema，但要求穷尽正文信息）。
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from byboy.agent.invoke import AgentInvocation, ModelRef, agent_complete
from byboy.agents.tutor_inf.link_choose import LinkChooseError, parse_llm_json_object
from byboy.agents.tutor_inf.web_clean import WebCleanAgent, WebCleanPayload
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.route_spec import ChatMessage


class TutorAnalyseError(RuntimeError):
    """解析或校验 LLM 输出失败。"""


_CACHE_DIR = Path(__file__).resolve().parent / "cache"


def _markdown_cache_filename(url: str) -> str:
    h = hashlib.sha256(url.strip().encode("utf-8")).hexdigest()
    return f"{h}.md"


def _read_markdown_source_declaration(md: str) -> str | None:
    for line in md.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^>\s*抓取来源：\s*(\S+)\s*$", s)
        if m:
            return m.group(1).strip()
        break
    return None


def _output_path(output_dir: str | Path, output_filename: str) -> Path:
    name = output_filename.strip()
    if not name:
        raise ValueError("output_filename 不能为空")
    return (Path(output_dir) / name).resolve()


@dataclass(frozen=True, slots=True)
class TutorAnalysePayload:
    """单次分析：导师页 URL、中文姓名（用于上下文对齐）、结构化 JSON 的输出位置。"""

    url: str
    tutor_name_cn: str
    output_dir: str | Path
    output_filename: str
    #: 若指定则**不**调用 Firecrawl，直接读取该 Markdown；仍会写入本包 ``cache/`` 标准文件名以便留痕。
    markdown_path: str | Path | None = None


SYSTEM_PROMPT = """你是高校导师个人主页信息整理助手。用户会提供：
1) 目标导师的中文姓名（用于判断页面是否主要介绍该人；若页面含多人，请分别标注与谁相关）。
2) 一整页由工具从 HTML 转成的 Markdown（可能含标题、列表、表格、链接等）。

【硬性要求】
- 你必须**穷尽**该 Markdown 正文中出现的**全部**事实性、描述性信息，不得因主观认为「次要」「常见」而删减。
- 包括但不限于：姓名与别名、职称职务、行政级别、所属单位、联系方式、办公地址、招生/研究方向、教育经历、工作/科研经历、项目、论文、专利、获奖、课程、社会兼职、个人简介原文段落、图片说明文字、页脚声明等——只要正文里有，就要以某种形式进入输出。
- 导航栏、纯站点模板文案若与具体导师无关，可归入单独标签（如 site_chrome），但仍需保留原文要点，不要随意整段丢弃。
- 链接请保留为 Markdown 形式或拆成 url + anchor_text；表格请保留为结构化数组或逐行文本，勿省略单元格。
- 输出必须是**单个 JSON 对象**（可任意嵌套、任意键名），用**标签/分类**组织信息：例如多组 { "tags": ["标签1","标签2"], "content": "…" }，或按章节分对象；「标签」可用中文或英文，但要能说明信息类别。
- **禁止**输出 Markdown 代码围栏；**禁止**在 JSON 外附加解释文字。

【输出形态建议（不强制，仅示例）】
- 可用 "blocks" / "sections" / "fields" 等数组列出带 tags 的条目；
- 可用 "tables" 数组还原表格；
- 可用 "links" 数组列出文中链接；
- 若某段原文难以归类，仍须放入 "uncategorized" 或类似键并附全文摘录。

请只输出 JSON。"""

SYSTEM_JSON_REPAIR = """你是 JSON 语法修复助手。用户会给你一段**本应**是单个 JSON 对象的内容，其中可能有：
未转义的引号或换行、尾逗号、夹杂说明文字、Markdown 代码围栏等。

请只输出**一个**可被标准 json.loads 解析的 JSON 对象，尽量保留原意与全部字段，不要主观删减信息。
禁止代码围栏，禁止任何 JSON 外的文字。"""


def _user_content(tutor_name_cn: str, markdown_text: str, declared_source_url: str | None) -> str:
    parts = [
        f"目标导师中文姓名（查询键）：{tutor_name_cn.strip() or '（未提供，请据正文推断并注明不确定性）'}",
    ]
    if declared_source_url:
        parts.append(f"页面声明来源 URL：{declared_source_url}")
    parts.append("----- Markdown 正文开始 -----")
    parts.append(markdown_text)
    parts.append("----- Markdown 正文结束 -----")
    return "\n".join(parts)


def _parse_extracted_json(
    raw: str,
    dispatcher: LLMDispatcher,
    route_token: str,
    *,
    repair_max_tokens: int,
) -> dict[str, Any]:
    try:
        obj = parse_llm_json_object(raw)
    except LinkChooseError:
        repair_messages: list[ChatMessage] = [
            {"role": "system", "content": SYSTEM_JSON_REPAIR},
            {
                "role": "user",
                "content": "以下内容无法被 json.loads 解析，请修复为合法 JSON 对象：\n\n" + raw.strip()[:240_000],
            },
        ]
        inv_repair = AgentInvocation(model=ModelRef(route_token), llm_part=repair_messages)
        fixed = agent_complete(dispatcher, inv_repair, max_tokens=repair_max_tokens)
        obj = parse_llm_json_object(fixed)
    if not isinstance(obj, dict):
        raise TutorAnalyseError("模型输出 JSON 根节点必须是对象")
    return obj


@dataclass(frozen=True, slots=True)
class TutorAnalyseResult:
    """一次完整跑完：结构化 JSON 路径 + 本 agent 缓存中的 Markdown 路径。"""

    json_path: Path
    markdown_cache_path: Path


class TutorAnalyseAgent:
    """串联 WebClean（缓存于 ``tutor_analyse/cache``）与 LLM 全文结构化。"""

    def run(
        self,
        inv: AgentInvocation[TutorAnalysePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
        repair_max_tokens: int = 32768,
    ) -> TutorAnalyseResult:
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        cache_dir = _CACHE_DIR
        cache_dir.mkdir(parents=True, exist_ok=True)
        md_name = _markdown_cache_filename(p.url)
        if p.markdown_path is not None:
            src = Path(p.markdown_path).resolve()
            if not src.is_file():
                raise FileNotFoundError(f"Markdown 文件不存在: {src}")
            body = src.read_text(encoding="utf-8", errors="replace")
            if _read_markdown_source_declaration(body) is None:
                u = p.url.strip()
                body = f"> 抓取来源：{u}\n\n" + body.lstrip("\n\r")
            md_path = (cache_dir / md_name).resolve()
            md_path.write_text(body, encoding="utf-8", newline="\n")
        else:
            wc = WebCleanAgent()
            md_path = wc.run(
                AgentInvocation(
                    model=inv.model,
                    llm_part=WebCleanPayload(
                        url=p.url.strip(),
                        output_dir=cache_dir,
                        output_filename=md_name,
                    ),
                ),
                dispatcher,
            )
            md_path = Path(md_path).resolve()
        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        declared = _read_markdown_source_declaration(md_text)
        messages: list[ChatMessage] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _user_content(p.tutor_name_cn, md_text, declared)},
        ]
        inv_chat = AgentInvocation(model=inv.model, llm_part=messages)
        raw = agent_complete(dispatcher, inv_chat, max_tokens=max_tokens)
        try:
            obj = _parse_extracted_json(
                raw,
                dispatcher,
                inv.model.token,
                repair_max_tokens=repair_max_tokens,
            )
        except LinkChooseError as e:
            raise TutorAnalyseError(str(e)) from e

        meta = {
            "tutor_name_cn": p.tutor_name_cn.strip(),
            "request_url": p.url.strip(),
            "declared_source_url": declared,
            "page_host": urlsplit(declared).netloc if declared else None,
            "markdown_cache_path": str(md_path),
            "markdown_source": "local_file" if p.markdown_path is not None else "firecrawl",
        }
        out_obj = {"meta": meta, "extracted": obj}
        out = _output_path(p.output_dir, p.output_filename)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(out_obj, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return TutorAnalyseResult(json_path=out, markdown_cache_path=md_path)

    async def arun(
        self,
        inv: AgentInvocation[TutorAnalysePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 16384,
        repair_max_tokens: int = 32768,
    ) -> TutorAnalyseResult:
        return await asyncio.to_thread(
            self.run,
            inv,
            dispatcher,
            max_tokens=max_tokens,
            repair_max_tokens=repair_max_tokens,
        )


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "TutorAnalyseAgent",
    "TutorAnalyseError",
    "TutorAnalysePayload",
    "TutorAnalyseResult",
]
