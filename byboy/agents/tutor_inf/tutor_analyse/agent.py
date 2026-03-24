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

from byboy.agent.invoke import AgentInvocation, ModelRef, slot_complete
from byboy.agents.tutor_inf.link_choose import LinkChooseError, parse_llm_json_object
from byboy.agents.tutor_inf.logging_utils import (
    AgentLogger,
    log_llm_wait_done,
    log_llm_wait_start,
    run_with_periodic_wait_log,
)
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

【信息覆盖硬性要求】
- 你必须穷尽该 Markdown 正文中出现的全部事实性、描述性信息，不得因主观认为“次要/常见”而删减。
- 包括但不限于：姓名与别名、职称职务、行政级别、所属单位、联系方式、办公地址、招生/研究方向、教育经历、工作/科研经历、项目、论文、专利、获奖、课程、社会兼职、个人简介段落、图片说明、页脚声明等。
- 导航栏、模板文案、面包屑等若与导师无关，可归入 site_chrome（或同义键），但仍要保留核心要点，不可整段丢弃。
- 链接需保留（Markdown 形式或 {url, anchor_text}）；表格需保留（结构化数组或逐行文本，不能漏单元格）。

【JSON 语法硬约束（必须全部满足）】
1) 只输出一个 JSON 对象（根节点必须是 object）。
2) 第一字符必须是 {，最后字符必须是 }。
3) 严禁输出任何 JSON 之外的文字（包括“说明/注释/前后缀/道歉/思考”）。
4) 严禁 Markdown 代码围栏（```）和任何 markdown 格式包装。
5) 所有键名必须使用双引号。
6) 所有字符串值必须使用双引号，并正确转义内部双引号、反斜杠与控制字符（尤其换行）。
7) 严禁尾逗号，严禁使用注释（// 或 /* */）。
8) 布尔值只能是 true/false，空值只能是 null（不得写 True/False/None）。
9) 若内容含引号或多行文本，必须做 JSON 合法转义后再写入。

【结构组织要求】
- 输出仍然是“单个 JSON 对象”，但对象内部可自由嵌套、自由键名。
- 必须使用“标签/分类”组织信息（如 blocks/sections/fields 任一风格均可）。
- 若某段信息难以归类，放入 uncategorized（或同义键），不得遗漏。

【输出前自检（在脑中执行，不要输出自检过程）】
- 我输出的是不是从 { 开始、以 } 结束？
- 能否被标准 json.loads 直接解析？
- 有没有代码围栏或 JSON 外文本？
- 有没有未转义引号、非法换行、尾逗号？
- 原文事实是否有明显遗漏？

只输出最终 JSON 对象。"""

SYSTEM_JSON_REPAIR = """你是 JSON 语法修复助手。用户会给你一段**本应**是单个 JSON 对象的内容，其中可能有：
未转义的引号或换行、尾逗号、夹杂说明文字、Markdown 代码围栏等。

请只输出**一个**可被标准 json.loads 解析的 JSON 对象，尽量保留原意与全部字段，不要主观删减信息。
禁止代码围栏，禁止任何 JSON 外的文字。"""

SYSTEM_INFO_QUALITY_PROMPT = """你是网页正文信息质量判定助手。用户会提供导师主页的 Markdown 全文。

请判断该 Markdown 是否“疑似没有多少有效文字信息”，用于决定是否要调用视觉模型兜底。

判定为 true 的典型情况：
- 正文几乎全是导航、页眉页脚、模板文案、免责声明、空白占位；
- 与导师相关的可提取事实极少，难以形成有价值的文字结构化结果；
- 大量内容是无意义重复、碎片符号、乱码或仅有很少几行有效句子。

判定为 false 的典型情况：
- 虽然有噪声，但仍包含可观的导师相关文本信息（简介、经历、方向、成果、联系方式等）；
- 能够从文字中提取出多条事实。

你必须只输出单个 JSON 对象，格式严格为：
{
  "suspect_no_text_info": true/false,
  "reason": "一句话中文理由，<=60字"
}

禁止输出代码围栏，禁止在 JSON 外输出任何文字。"""

SYSTEM_REGEN_STRICT_JSON = """上一轮输出不是可解析 JSON。请重新生成，并严格满足：
1) 只输出单个 JSON 对象，且第一字符是 {、最后字符是 }；
2) 禁止任何 JSON 外文字（解释、前后缀、致歉、思考）；
3) 禁止代码围栏（```）和注释；
4) 键名/字符串必须双引号，内部引号和换行必须合法转义；
5) 禁止尾逗号，布尔值仅 true/false，空值仅 null；
6) 保持信息尽量完整，不要省略原文事实。
只输出 JSON。"""


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


def _parse_info_quality_flag(
    raw: str,
    dispatcher: LLMDispatcher,
    slot_token: str,
    *,
    repair_max_tokens: int,
) -> tuple[bool, str]:
    try:
        obj = _parse_extracted_json(
            raw,
            dispatcher,
            slot_token,
            repair_max_tokens=repair_max_tokens,
        )
    except (LinkChooseError, TutorAnalyseError):
        return False, "信息质量判定解析失败，默认按可用文本处理"

    val = obj.get("suspect_no_text_info")
    if isinstance(val, bool):
        flag = val
    else:
        flag = False
    reason = obj.get("reason")
    if not isinstance(reason, str):
        reason = ""
    return flag, reason.strip()


def _parse_extracted_json(
    raw: str,
    dispatcher: LLMDispatcher,
    slot_token: str,
    *,
    repair_max_tokens: int,
    log: AgentLogger | None = None,
    stage: str = "json_repair",
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
        t0 = None
        if log is not None:
            t0 = log_llm_wait_start(
                log,
                model=slot_token,
                payload=repair_messages,
                max_tokens=repair_max_tokens,
                stage=stage,
            )
        fixed = run_with_periodic_wait_log(
            log=log if log is not None else AgentLogger("TutorAnalyseAgent"),
            stage=stage,
            wait_message="等待模型响应中",
            every_sec=5.0,
            fn=lambda: slot_complete(
                dispatcher,
                slot_token,
                repair_messages,
                max_tokens=repair_max_tokens,
            ),
        )
        if log is not None and t0 is not None:
            log_llm_wait_done(log, stage=stage, started_at=t0)
        obj = parse_llm_json_object(fixed)
    if not isinstance(obj, dict):
        raise TutorAnalyseError("模型输出 JSON 根节点必须是对象")
    return obj


@dataclass(frozen=True, slots=True)
class TutorAnalyseResult:
    """一次完整跑完：结构化 JSON 路径 + 本 agent 缓存中的 Markdown 路径。"""

    json_path: Path
    markdown_cache_path: Path
    suspect_no_text_info: bool | None = None


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
        log = AgentLogger("TutorAnalyseAgent")
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        log.start("开始导师页分析", detail=f"name={p.tutor_name_cn.strip()} url={p.url.strip()}")
        cache_dir = _CACHE_DIR
        cache_dir.mkdir(parents=True, exist_ok=True)
        md_name = _markdown_cache_filename(p.url)
        if p.markdown_path is not None:
            log.step("使用本地 markdown 输入", detail=str(Path(p.markdown_path).resolve()))
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
            log.step("调用 WebClean 抓取 markdown")
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
        log.step("完成 markdown 准备", detail=str(md_path))

        quality_messages: list[ChatMessage] = [
            {"role": "system", "content": SYSTEM_INFO_QUALITY_PROMPT},
            {"role": "user", "content": _user_content(p.tutor_name_cn, md_text, declared)},
        ]
        t_quality = log_llm_wait_start(
            log,
            model=inv.model.token,
            payload=quality_messages,
            max_tokens=512,
            stage="quality_check",
        )
        quality_raw = run_with_periodic_wait_log(
            log=log,
            stage="quality_check",
            wait_message="等待模型响应中",
            every_sec=5.0,
            fn=lambda: slot_complete(
                dispatcher,
                inv.model.token,
                quality_messages,
                max_tokens=512,
            ),
        )
        log_llm_wait_done(log, stage="quality_check", started_at=t_quality)
        suspect_no_text_info, suspect_reason = _parse_info_quality_flag(
            quality_raw,
            dispatcher,
            inv.model.token,
            repair_max_tokens=2048,
        )
        log.step(
            "完成文本质量判定",
            detail=f"suspect_no_text_info={suspect_no_text_info}",
        )

        messages: list[ChatMessage] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _user_content(p.tutor_name_cn, md_text, declared)},
        ]
        obj: dict[str, Any] | None = None
        last_err: Exception | None = None
        total_attempts = 3
        cur_messages = messages
        for attempt in range(1, total_attempts + 1):
            t_extract = log_llm_wait_start(
                log,
                model=inv.model.token,
                payload=cur_messages,
                max_tokens=max_tokens,
                stage=f"main_extract_attempt_{attempt}",
            )
            raw = run_with_periodic_wait_log(
                log=log,
                stage=f"main_extract_attempt_{attempt}",
                wait_message="等待模型响应中",
                every_sec=5.0,
                fn=lambda: slot_complete(
                    dispatcher,
                    inv.model.token,
                    cur_messages,
                    max_tokens=max_tokens,
                ),
            )
            log_llm_wait_done(log, stage=f"main_extract_attempt_{attempt}", started_at=t_extract)
            log.step("完成主结构化抽取", detail=f"attempt={attempt}/{total_attempts}")
            try:
                obj = _parse_extracted_json(
                    raw,
                    dispatcher,
                    inv.model.token,
                    repair_max_tokens=repair_max_tokens,
                    log=log,
                    stage=f"json_repair_attempt_{attempt}",
                )
                break
            except (LinkChooseError, TutorAnalyseError) as e:
                last_err = e
                if attempt >= total_attempts:
                    break
                log.warn("JSON 解析失败，准备重试生成", detail=f"attempt={attempt} err={e}")
                cur_messages = [
                    *cur_messages,
                    {"role": "assistant", "content": raw[:120_000]},
                    {"role": "user", "content": SYSTEM_REGEN_STRICT_JSON},
                ]
        if obj is None:
            raise TutorAnalyseError(str(last_err or "结构化抽取失败"))

        meta = {
            "tutor_name_cn": p.tutor_name_cn.strip(),
            "request_url": p.url.strip(),
            "declared_source_url": declared,
            "page_host": urlsplit(declared).netloc if declared else None,
            "markdown_cache_path": str(md_path),
            "markdown_source": "local_file" if p.markdown_path is not None else "firecrawl",
            "suspect_no_text_info": suspect_no_text_info,
            "suspect_no_text_info_reason": suspect_reason or None,
        }
        out_obj = {
            "meta": meta,
            "suspect_no_text_info": suspect_no_text_info,
            "extracted": obj,
        }
        out = _output_path(p.output_dir, p.output_filename)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(out_obj, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        log.done("写入分析结果", detail=str(out))
        return TutorAnalyseResult(
            json_path=out,
            markdown_cache_path=md_path,
            suspect_no_text_info=suspect_no_text_info,
        )

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
