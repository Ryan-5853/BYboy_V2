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

from byboy.agent.invoke import AgentInvocation, ModelRef, agent_complete, slot_complete
from byboy.agents.tutor_inf.logging_utils import (
    AgentLogger,
    log_llm_wait_done,
    log_llm_wait_start,
    run_with_periodic_wait_log,
)
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
    if Path(name).suffix.lower() != ".json":
        raise ValueError("output_filename 必须以 .json 结尾")
    base = Path(payload.output_dir)
    if not str(base).strip():
        raise ValueError("output_dir 不能为空")
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
    required = ("clickable_links",)
    for k in required:
        if k not in obj:
            raise LinkChooseError(f"JSON 缺少必填键 {k!r}")
    if not isinstance(obj["clickable_links"], list):
        raise LinkChooseError("clickable_links 必须是数组")
    for i, item in enumerate(obj["clickable_links"]):
        if not isinstance(item, dict):
            raise LinkChooseError(f"clickable_links[{i}] 必须是对象")
        required_item_keys = (
            "url",
            "anchor_text",
            "scope",
            "category",
            "category_confidence",
            "category_reason",
            "guessed_target_content",
        )
        for k in required_item_keys:
            if k not in item:
                raise LinkChooseError(f"clickable_links[{i}] 缺少必填键 {k!r}")
            if not isinstance(item[k], str):
                raise LinkChooseError(f"clickable_links[{i}].{k} 必须是字符串")
        if item["scope"] not in {"internal", "external", "unknown"}:
            raise LinkChooseError(f"clickable_links[{i}].scope 非法: {item['scope']!r}")
        if item["category"] not in {
            "tutor_profile",
            "tutor_expansion",
            "irrelevant",
        }:
            raise LinkChooseError(f"clickable_links[{i}].category 非法: {item['category']!r}")
        if item["category_confidence"] not in {"high", "medium", "low"}:
            raise LinkChooseError(f"clickable_links[{i}].category_confidence 非法: {item['category_confidence']!r}")


SYSTEM_PROMPT = """你是链接三分类助手。请只根据给出的 URL 与锚文本，将每条链接分类为以下之一：
- tutor_profile（导师个人信息页）
- tutor_expansion（可能包含更多导师信息的页面，如导师名录、分页、学院导航到师资栏目）
- irrelevant（无关网页）

你必须输出一个 JSON 对象：{"results":[...]}。
results 中每项必须含：
- idx: 整数（对应输入索引）
- category: 上述四类之一
- category_confidence: high|medium|low
- category_reason: 不超过30字

禁止输出 JSON 以外的任何内容。"""

SYSTEM_JSON_REPAIR = """你是 JSON 语法修复助手。用户会给你一段本应是单个 JSON 对象的文本，
其中可能有未转义引号、尾逗号、代码围栏或夹杂说明文字。

请只输出一个可被标准 json.loads 解析的 JSON 对象，尽量保留原字段与语义。
禁止输出 JSON 以外的任何内容。"""


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


def _parse_with_repair(
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
            log=log if log is not None else AgentLogger("LinkChooseAgent"),
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
        raise LinkChooseError("模型输出 JSON 根节点必须是对象")
    return obj


_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\((\S+?)(?:\s+\"[^\"]*\")?\)")
_AUTO_LINK_RE = re.compile(r"<(https?://[^>\s]+)>", flags=re.IGNORECASE)


def _normalize_url(url: str) -> str:
    return url.strip().strip("()[]<>")


def _link_scope(url: str, declared_source_url: str | None) -> str:
    u = _normalize_url(url)
    if not declared_source_url:
        return "unknown"
    if u.startswith(("mailto:", "tel:", "javascript:")):
        return "unknown"
    target = urlsplit(u)
    src = urlsplit(declared_source_url)
    if not target.netloc:
        return "internal"
    return "internal" if target.netloc == src.netloc else "external"


def _category_to_guess(category: str) -> str:
    mapping = {
        "tutor_profile": "教师/导师个人信息页面",
        "tutor_expansion": "可能包含更多导师信息的页面",
        "irrelevant": "无关网页或低相关页面",
    }
    return mapping.get(category, "站点普通信息页面")


def _rule_category(url: str, anchor_text: str, scope: str) -> tuple[str, str, str, bool]:
    u = url.lower()
    a = anchor_text.strip().lower()
    text = f"{a} {u}"
    score = {
        "tutor_profile": 0,
        "tutor_expansion": 0,
        "irrelevant": 0,
    }
    reason_parts: list[str] = []

    if u.startswith("mailto:"):
        return ("irrelevant", "high", "mailto 链接", False)
    if u.startswith("tel:"):
        return ("irrelevant", "high", "tel 链接", False)
    if u.startswith("javascript:"):
        return ("tutor_expansion", "medium", "javascript 站内动作", False)

    if any(k in text for k in ("个人主页", "homepage", "profile", "faculty", "教师主页", "导师主页")):
        score["tutor_profile"] += 4
        reason_parts.append("命中个人主页关键词")
    if any(k in text for k in ("导师", "教师", "名录", "师资", "people", "faculty-list", "teachers")):
        score["tutor_expansion"] += 3
        reason_parts.append("命中名录关键词")
    if any(k in text for k in ("list", "index", "page=", "栏目", "导航", "通知", "新闻", "研究生", "本科")):
        score["tutor_expansion"] += 2
    if scope == "external":
        score["irrelevant"] += 2
    if scope == "internal":
        score["tutor_expansion"] += 1
    if any(k in text for k in ("pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip", ".rar")):
        score["irrelevant"] += 3
        reason_parts.append("文件下载链接")
    if any(k in text for k in ("login", "signin", "注册", "登录")):
        score["irrelevant"] += 2

    ranked = sorted(score.items(), key=lambda x: x[1], reverse=True)
    top_label, top_score = ranked[0]
    second_score = ranked[1][1]
    gap = top_score - second_score

    if top_score >= 4 and gap >= 2:
        conf = "high"
    elif top_score >= 2 and gap >= 1:
        conf = "medium"
    else:
        conf = "low"
    uncertain = conf == "low"
    reason = "；".join(reason_parts[:2]) if reason_parts else "关键词信号较弱"
    return (top_label, conf, reason, uncertain)


def _llm_refine_uncertain(
    *,
    items: list[dict[str, str]],
    dispatcher: LLMDispatcher,
    model: ModelRef,
    batch_size: int = 50,
    max_tokens: int = 2048,
    log: AgentLogger | None = None,
) -> dict[int, dict[str, str]]:
    if not items:
        return {}
    refined: dict[int, dict[str, str]] = {}
    for i in range(0, len(items), batch_size):
        batch = items[i : i + batch_size]
        user_data = {
            "links": [
                {
                    "idx": int(x["idx"]),
                    "url": x["url"],
                    "anchor_text": x["anchor_text"],
                    "scope": x["scope"],
                    "rule_category": x["category"],
                    "rule_confidence": x["category_confidence"],
                }
                for x in batch
            ]
        }
        messages: list[ChatMessage] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(user_data, ensure_ascii=False)},
        ]
        inv = AgentInvocation(model=model, llm_part=messages)
        t1 = None
        if log is not None:
            t1 = log_llm_wait_start(
                log,
                model=model.token,
                payload=messages,
                max_tokens=max_tokens,
                stage=f"refine_batch_{i // batch_size + 1}",
            )
        raw = run_with_periodic_wait_log(
            log=log if log is not None else AgentLogger("LinkChooseAgent"),
            stage=f"refine_batch_{i // batch_size + 1}",
            wait_message="等待模型响应中",
            every_sec=5.0,
            fn=lambda: agent_complete(dispatcher, inv, max_tokens=max_tokens),
        )
        if log is not None and t1 is not None:
            log_llm_wait_done(log, stage=f"refine_batch_{i // batch_size + 1}", started_at=t1)
        parsed = _parse_with_repair(
            raw,
            dispatcher,
            model.token,
            repair_max_tokens=max_tokens,
            log=log,
            stage=f"json_repair_batch_{i // batch_size + 1}",
        )
        results = parsed.get("results")
        if not isinstance(results, list):
            continue
        for r in results:
            if not isinstance(r, dict):
                continue
            idx = r.get("idx")
            category = r.get("category")
            category_confidence = r.get("category_confidence")
            category_reason = r.get("category_reason")
            if not isinstance(idx, int):
                continue
            if category not in {"tutor_profile", "tutor_expansion", "irrelevant"}:
                continue
            if category_confidence not in {"high", "medium", "low"}:
                continue
            if not isinstance(category_reason, str):
                continue
            refined[idx] = {
                "category": category,
                "category_confidence": category_confidence,
                "category_reason": category_reason[:60],
            }
    return refined


def _extract_clickable_links(markdown_text: str, declared_source_url: str | None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for m in _MD_LINK_RE.finditer(markdown_text):
        anchor_text = m.group(1).strip()
        url = _normalize_url(m.group(2))
        key = (url, anchor_text)
        if not url or key in seen:
            continue
        seen.add(key)
        scope = _link_scope(url, declared_source_url)
        category, category_confidence, category_reason, uncertain = _rule_category(url, anchor_text, scope)
        items.append(
            {
                "idx": str(len(items)),
                "url": url,
                "anchor_text": anchor_text,
                "scope": scope,
                "category": category,
                "category_confidence": category_confidence,
                "category_reason": category_reason,
                "guessed_target_content": _category_to_guess(category),
                "needs_llm_refine": "1" if uncertain else "0",
            }
        )

    for m in _AUTO_LINK_RE.finditer(markdown_text):
        url = _normalize_url(m.group(1))
        key = (url, "")
        if not url or key in seen:
            continue
        seen.add(key)
        scope = _link_scope(url, declared_source_url)
        category, category_confidence, category_reason, uncertain = _rule_category(url, "", scope)
        items.append(
            {
                "idx": str(len(items)),
                "url": url,
                "anchor_text": "",
                "scope": scope,
                "category": category,
                "category_confidence": category_confidence,
                "category_reason": category_reason,
                "guessed_target_content": _category_to_guess(category),
                "needs_llm_refine": "1" if uncertain else "0",
            }
        )
    return items


class LinkChooseAgent:
    """``LlmCallingAgent`` 形态：``llm_part`` 为 ``LinkChoosePayload``，结果写入 JSON 文件。"""

    def run(
        self,
        inv: AgentInvocation[LinkChoosePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 8192,
        repair_max_tokens: int = 8192,
    ) -> Path:
        log = AgentLogger("LinkChooseAgent")
        if max_tokens <= 0 or repair_max_tokens <= 0:
            raise ValueError("max_tokens 与 repair_max_tokens 必须为正整数")
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        md_path = Path(p.markdown_path).resolve()
        log.start("开始链接分类", detail=str(md_path))
        if not md_path.is_file():
            raise FileNotFoundError(f"Markdown 文件不存在: {md_path}")
        if md_path.suffix.lower() != ".md":
            raise ValueError(f"markdown_path 必须是 .md 文件: {md_path}")
        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        declared = _read_markdown_source_declaration(md_text)
        links = _extract_clickable_links(md_text, declared)
        log.step("提取可点击链接", detail=f"total={len(links)}")
        uncertain = [x for x in links if x.get("needs_llm_refine") == "1"]
        if uncertain:
            log.step("调用 LLM 细化低置信链接", detail=f"uncertain={len(uncertain)}")
        refined = _llm_refine_uncertain(
            items=uncertain,
            dispatcher=dispatcher,
            model=inv.model,
            max_tokens=repair_max_tokens,
            log=log,
        )
        for x in links:
            idx = int(x["idx"])
            if idx in refined:
                x["category"] = refined[idx]["category"]
                x["category_confidence"] = refined[idx]["category_confidence"]
                x["category_reason"] = refined[idx]["category_reason"]
                x["guessed_target_content"] = _category_to_guess(x["category"])
            x.pop("idx", None)
            x.pop("needs_llm_refine", None)

        obj = {"clickable_links": links}
        _validate_schema(obj)
        out_obj = {"clickable_links": obj["clickable_links"]}
        out = _output_path(p)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(out_obj, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        log.done("写入分类结果", detail=str(out))
        return out

    async def arun(
        self,
        inv: AgentInvocation[LinkChoosePayload],
        dispatcher: LLMDispatcher,
        *,
        max_tokens: int = 8192,
        repair_max_tokens: int = 8192,
    ) -> Path:
        return await asyncio.to_thread(
            self.run,
            inv,
            dispatcher,
            max_tokens=max_tokens,
            repair_max_tokens=repair_max_tokens,
        )


__all__ = [
    "LinkChooseAgent",
    "LinkChooseError",
    "LinkChoosePayload",
    "ModelRef",
    "AgentInvocation",
    "parse_llm_json_object",
]
