"""
从 webclean 产出的 Markdown 中提取链接，默认对每条链接调用 LLM 归类（导师主页 / 可扩展名录 / 无关），
并写入 JSON；也可仅对规则低置信链接调 LLM（``LinkChoosePayload.refine_all_links=False``）。
正文为 Markdown（由 HTML 转换而来），链接以 ``[锚文本](url)`` 等形式保留。
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit, urlunsplit

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
    #: True：每条链接都经 LLM 再分类；False：仅规则标为低置信的链接调 LLM（省 token）。
    refine_all_links: bool = True
    #: 可选：编排层批次内序号（与 ``progress_total`` 成对），便于并行时日志对齐任务。
    progress_index: int | None = None
    progress_total: int | None = None
    #: 抓取任务根 URL（如学院师资入口），用于提示模型与外链「名录」降级策略。
    task_root_url: str | None = None
    #: 可选：本任务关注的学院/单位名称；由编排层传入，保证多任务并行时互不干扰。
    scope_hint: str | None = None
    #: 单页内 LLM 细化按 batch（默认 50 条一批）并行提交的最大 worker 数；1 表示串行（默认）。
    refine_batch_parallel_workers: int = 1


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


def _coerce_listing_pagination_next(raw: Any) -> str:
    """将模型或旧数据中的翻页标记规范为 \"0\" / \"1\"。"""
    v = str(raw or "").strip().lower()
    if v in {"1", "yes", "true", "y"}:
        return "1"
    return "0"


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
            "listing_pagination_next",
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
        if item["listing_pagination_next"] not in {"0", "1"}:
            raise LinkChooseError(f"clickable_links[{i}].listing_pagination_next 必须为 \"0\" 或 \"1\"")


SYSTEM_PROMPT = """你是链接三分类助手。请只根据给出的 URL 与锚文本，将每条链接分类为以下之一：
- tutor_profile（**单一**教师/导师的个人信息页、个人主页入口）
- tutor_expansion（可能包含更多导师信息的页面，如**本任务相关单位**的导师名录、站内师资栏目导航）
- irrelevant（无关网页）

**名录翻页（仅由你判断，不要用额外规则）**
- 部分学校站点用 **同一 .jsp 路径 + 不同 query（如 id= / wbtreeid=）** 表示下一栏或下一页列表；若属 **同一教师列表的延续**，也应 **listing_pagination_next="1"**（可与 tutor_expansion+high 同时出现）。
- 若结合上下文可判断 **当前页是导师名录/教师列表**，且该链接是 **同一列表的「下一页」或等价分页**（继续展示更多本表教师，而非跳到其它栏目、其它学院、单条新闻等），则：
  - category 应为 tutor_expansion，category_confidence 可为 high；
  - **listing_pagination_next 必须为字符串 "1"**。
- 其它所有链接（含导师个人主页、其它栏目、兄弟学院名录、不确定是否同表分页）**listing_pagination_next 必须为 "0"**。

**防串院/串站点（重要）**
- 输入中可能带有 task_context.task_root_url（本次抓取的学院/单位入口）与 scope_hint（任务关注的院系名称）。
- 指向**其他学院、其他院系、其他二级单位**的**师资名录/教师列表/师资队伍总览**（兄弟单位导航页），**不得**标为 tutor_profile；应标为 irrelevant，或 tutor_expansion 且 **category_confidence 只能是 medium 或 low**，禁止 high；且 listing_pagination_next="0"。
- **例外**：若链接明显是**某位具体教师**的个人主页（锚文本或 URL 体现姓名+个人介绍页），即便在子域或外链上，仍可标 tutor_profile + high；listing_pagination_next="0"。
- 全校级、跨院系的「教师库」「统一师资平台」列表入口，若非本任务 scope_hint 所在单位，倾向 irrelevant 或 tutor_expansion+low/medium；listing_pagination_next="0"。

你必须输出一个 JSON 对象：{"results":[...]}。
results 中每项必须含：
- idx: 整数（对应输入索引）
- category: 上述三类之一
- category_confidence: high|medium|low
- category_reason: 不超过30字
- listing_pagination_next: 字符串 **"0"** 或 **"1"**（含义见上）

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
_BARE_URL_RE = re.compile(r"(https?://[^\s<>()\[\]\"']+)", flags=re.IGNORECASE)


def _normalize_url(url: str) -> str:
    u = url.strip().strip("()[]<>")
    # Firecrawl/Markdown 里 URL 可能带有转义字符（如 zh\_CN），需要还原后再用。
    u = (
        u.replace("\\_", "_")
        .replace("\\-", "-")
        .replace("\\.", ".")
        .replace("\\~", "~")
    )
    return u


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

    # 放宽规则：只有“非常明确”的才跳过 LLM，其它（medium/low）都尽量交给 LLM 判断。
    # 这样可在开启 `--link-choose-uncertain-only-llm` 时显著提升召回/分类准确率。
    if top_score >= 6 and gap >= 3:
        conf = "high"
    elif top_score >= 3 and gap >= 1:
        conf = "medium"
    else:
        conf = "low"
    uncertain = conf != "high"
    reason = "；".join(reason_parts[:2]) if reason_parts else "关键词信号较弱"
    return (top_label, conf, reason, uncertain)


def _registrable_domain(netloc: str) -> str:
    """粗略的「注册域」用于判断是否跨站（同校多子域通常共享同一后缀，如 uestc.edu.cn）。"""
    h = netloc.lower().strip()
    if not h:
        return ""
    if ":" in h and not h.startswith("["):
        h = h.rsplit(":", 1)[0]
    if h.startswith("www."):
        h = h[4:]
    parts = h.split(".")
    if len(parts) < 2:
        return h
    if len(parts) >= 3 and parts[-1] == "cn" and parts[-2] == "edu":
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def _absolute_url_for_policy(raw: str, base: str | None) -> str:
    """解析为绝对 http(s) URL，返回 scheme+host+path（小写 host、去 query/fragment），供域名比较。"""
    u = _normalize_url(raw)
    if not u or u.startswith("#"):
        return ""
    if u.startswith(("mailto:", "tel:", "javascript:")):
        return ""
    pr0 = urlsplit(u)
    if pr0.scheme in ("http", "https") and pr0.netloc:
        path = pr0.path or "/"
        return urlunsplit((pr0.scheme.lower(), pr0.netloc.lower(), path, "", "")).rstrip("/")
    b = (base or "").strip()
    if not b:
        return ""
    joined = urljoin(b if b.endswith("/") else b + "/", u)
    pr = urlsplit(joined)
    if pr.scheme not in ("http", "https") or not pr.netloc:
        return ""
    path = pr.path or "/"
    return urlunsplit((pr.scheme.lower(), pr.netloc.lower(), path, "", "")).rstrip("/")


def _apply_cross_domain_expansion_cap(
    links: list[dict[str, str]],
    *,
    task_root_url: str | None,
    page_base_url: str | None,
) -> None:
    """不同注册域上的 tutor_expansion 若被标为 high，降为 medium，避免进入仅采纳 high 的爬取队列。"""
    flag = (os.environ.get("BYBOY_TUTOR_LINK_SKIP_EXTERNAL_EXPANSION_CAP") or "").strip().lower()
    if flag in {"1", "true", "yes", "on"}:
        return
    root = (task_root_url or "").strip()
    if not root:
        return
    root_abs = _absolute_url_for_policy(root, root)
    if not root_abs:
        return
    root_dom = _registrable_domain(urlsplit(root_abs).netloc)
    if not root_dom:
        return
    base = (page_base_url or "").strip() or root
    for x in links:
        if x.get("category") != "tutor_expansion":
            continue
        if x.get("category_confidence") != "high":
            continue
        u_abs = _absolute_url_for_policy(x.get("url", ""), base)
        if not u_abs:
            continue
        link_dom = _registrable_domain(urlsplit(u_abs).netloc)
        if not link_dom or link_dom == root_dom:
            continue
        x["category_confidence"] = "medium"
        x["listing_pagination_next"] = "0"
        note = "跨注册域名录降级"
        prev = (x.get("category_reason") or "").strip()
        x["category_reason"] = (prev + "；" + note if prev else note)[:60]


def _fallback_refine_batch_items(
    batch_items: list[dict[str, str]], *, reason: str
) -> dict[int, dict[str, str]]:
    """LLM 失败或输出无效时，跳过该批次细化，保留规则结果并打标。"""
    out: dict[int, dict[str, str]] = {}
    for x in batch_items:
        try:
            idx = int(x.get("idx") or -1)
        except (TypeError, ValueError):
            continue
        if idx < 0:
            continue
        cat = str(x.get("category") or x.get("rule_category") or "irrelevant")
        if cat not in {"tutor_profile", "tutor_expansion", "irrelevant"}:
            cat = "irrelevant"
        out[idx] = {
            "category": cat,
            "category_confidence": "low",
            "category_reason": reason[:60],
            "listing_pagination_next": "0",
        }
    return out


def _refine_single_llm_batch(
    batch: list[dict[str, str]],
    batch_no: int,
    *,
    dispatcher: LLMDispatcher,
    model: ModelRef,
    max_tokens: int,
    log: AgentLogger | None,
    task_root_url: str | None,
    scope_hint: str | None,
) -> dict[int, dict[str, str]]:
    user_data: dict[str, Any] = {
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
    ctx: dict[str, str] = {}
    tru = (task_root_url or "").strip()
    if tru:
        ctx["task_root_url"] = tru
    sh = (scope_hint or "").strip()
    if sh:
        ctx["scope_hint"] = sh
    if ctx:
        user_data["task_context"] = ctx
    messages: list[ChatMessage] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": json.dumps(user_data, ensure_ascii=False)},
    ]
    inv = AgentInvocation(model=model, llm_part=messages)

    def _run_refine_once(stage_suffix: str) -> dict[str, Any]:
        t1 = None
        stage_name = f"refine_batch_{batch_no}{stage_suffix}"
        if log is not None:
            t1 = log_llm_wait_start(
                log,
                model=model.token,
                payload=messages,
                max_tokens=max_tokens,
                stage=stage_name,
            )
        raw = run_with_periodic_wait_log(
            log=log if log is not None else AgentLogger("LinkChooseAgent"),
            stage=stage_name,
            wait_message="等待模型响应中",
            every_sec=5.0,
            fn=lambda: agent_complete(dispatcher, inv, max_tokens=max_tokens),
        )
        if log is not None and t1 is not None:
            log_llm_wait_done(log, stage=stage_name, started_at=t1)
        return _parse_with_repair(
            raw,
            dispatcher,
            model.token,
            repair_max_tokens=max_tokens,
            log=log,
            stage=f"json_repair_batch_{batch_no}{stage_suffix}",
        )

    try:
        parsed = _run_refine_once("")
    except LinkChooseError as e1:
        if log is not None:
            log.warn(
                "LLM 首次输出不可解析，重试一次",
                detail=f"batch={batch_no} err={e1!s}",
            )
        try:
            parsed = _run_refine_once("_retry")
        except LinkChooseError as e2:
            if log is not None:
                log.warn(
                    "LLM 重试仍失败，跳过该批次细化",
                    detail=f"batch={batch_no} mark=LLM_RETRY_FAILED_SKIP err={e2!s}",
                )
            return _fallback_refine_batch_items(
                batch,
                reason="LLM_RETRY_FAILED_SKIP: 保留规则分类",
            )

    results = parsed.get("results")
    if not isinstance(results, list):
        if log is not None:
            log.warn(
                "LLM 输出缺少 results，跳过该批次细化",
                detail=f"batch={batch_no} mark=LLM_RESULTS_MISSING_SKIP",
            )
        return _fallback_refine_batch_items(
            batch,
            reason="LLM_RESULTS_MISSING_SKIP: 保留规则分类",
        )

    out: dict[int, dict[str, str]] = {}
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
        out[idx] = {
            "category": category,
            "category_confidence": category_confidence,
            "category_reason": category_reason[:60],
            "listing_pagination_next": _coerce_listing_pagination_next(
                r.get("listing_pagination_next")
            ),
        }
    return out


def _llm_refine_uncertain(
    *,
    items: list[dict[str, str]],
    dispatcher: LLMDispatcher,
    model: ModelRef,
    batch_size: int = 50,
    max_tokens: int = 2048,
    log: AgentLogger | None = None,
    task_root_url: str | None = None,
    scope_hint: str | None = None,
    parallel_workers: int = 1,
) -> dict[int, dict[str, str]]:
    if not items:
        return {}
    batches: list[tuple[list[dict[str, str]], int]] = [
        (items[i : i + batch_size], i // batch_size + 1)
        for i in range(0, len(items), batch_size)
    ]
    pw = max(1, int(parallel_workers))
    if pw <= 1 or len(batches) <= 1:
        refined: dict[int, dict[str, str]] = {}
        for batch, batch_no in batches:
            refined.update(
                _refine_single_llm_batch(
                    batch,
                    batch_no,
                    dispatcher=dispatcher,
                    model=model,
                    max_tokens=max_tokens,
                    log=log,
                    task_root_url=task_root_url,
                    scope_hint=scope_hint,
                )
            )
        return refined

    refined = {}
    cap = min(pw, len(batches))
    with concurrent.futures.ThreadPoolExecutor(max_workers=cap) as ex:
        futs = {
            ex.submit(
                _refine_single_llm_batch,
                batch,
                batch_no,
                dispatcher=dispatcher,
                model=model,
                max_tokens=max_tokens,
                log=log,
                task_root_url=task_root_url,
                scope_hint=scope_hint,
            ): batch_no
            for batch, batch_no in batches
        }
        for fut in concurrent.futures.as_completed(futs):
            refined.update(fut.result())
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
                "listing_pagination_next": "0",
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
                "listing_pagination_next": "0",
            }
        )

    # 有些页面即便包含 URL，也可能被 firecrawl 转成“裸文本”，不一定会生成 markdown link 或 <...>。
    # 为了保证这类 URL 也能进入后续队列，这里额外提取裸 URL。
    for m in _BARE_URL_RE.finditer(markdown_text):
        raw_url = m.group(1).strip()
        # 去掉句末常见标点，避免把正文标点当作 URL 一部分。
        raw_url = raw_url.rstrip(".,;:!?)\"'")
        url = _normalize_url(raw_url)
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
                "listing_pagination_next": "0",
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
        rbpw = int(p.refine_batch_parallel_workers)
        if rbpw <= 0:
            raise ValueError("refine_batch_parallel_workers 必须为正整数")
        md_path = Path(p.markdown_path).resolve()
        prog = ""
        if p.progress_index is not None and p.progress_total is not None:
            prog = f"[{p.progress_index}/{p.progress_total}] "
        log.start("链接分类", detail=f"{prog}{md_path.name}")
        if not md_path.is_file():
            raise FileNotFoundError(f"Markdown 文件不存在: {md_path}")
        if md_path.suffix.lower() != ".md":
            raise ValueError(f"markdown_path 必须是 .md 文件: {md_path}")
        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        declared = _read_markdown_source_declaration(md_text)
        links = _extract_clickable_links(md_text, declared)
        log.step("提取可点击链接", detail=f"total={len(links)}")
        if p.refine_all_links:
            uncertain = list(links)
            if uncertain:
                log.step(
                    "调用 LLM 分类全部链接",
                    detail=f"total={len(uncertain)} batch_parallel={rbpw}",
                )
        else:
            uncertain = [x for x in links if x.get("needs_llm_refine") == "1"]
            if uncertain:
                log.step(
                    "调用 LLM 细化低置信链接",
                    detail=f"uncertain={len(uncertain)} batch_parallel={rbpw}",
                )
        scope_hint_eff = (p.scope_hint or "").strip() or None
        refined = _llm_refine_uncertain(
            items=uncertain,
            dispatcher=dispatcher,
            model=inv.model,
            max_tokens=repair_max_tokens,
            log=log,
            task_root_url=(p.task_root_url or "").strip() or None,
            scope_hint=scope_hint_eff,
            parallel_workers=rbpw,
        )
        for x in links:
            idx = int(x["idx"])
            if idx in refined:
                x["category"] = refined[idx]["category"]
                x["category_confidence"] = refined[idx]["category_confidence"]
                x["category_reason"] = refined[idx]["category_reason"]
                x["listing_pagination_next"] = refined[idx].get(
                    "listing_pagination_next", "0"
                )
                if x["listing_pagination_next"] not in {"0", "1"}:
                    x["listing_pagination_next"] = _coerce_listing_pagination_next(
                        x["listing_pagination_next"]
                    )
                x["guessed_target_content"] = _category_to_guess(x["category"])
            else:
                x["listing_pagination_next"] = _coerce_listing_pagination_next(
                    x.get("listing_pagination_next")
                )
            x.pop("idx", None)
            x.pop("needs_llm_refine", None)

        page_base = (declared or "").strip() or (p.task_root_url or "").strip() or None
        _apply_cross_domain_expansion_cap(
            links,
            task_root_url=(p.task_root_url or "").strip() or None,
            page_base_url=page_base,
        )

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
        log.done("链接分类完成", detail=f"{prog}{out.name}")
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
