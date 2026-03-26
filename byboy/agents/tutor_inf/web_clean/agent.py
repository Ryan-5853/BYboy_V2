"""
网页清洗为 Markdown：Firecrawl v2 scrape，无 LLM。

调用侧仍使用 ``AgentInvocation``：``model`` 仅参与 ``LLMDispatcher.resolve``，
``llm_part`` 为 ``WebCleanPayload``（与 Chat 消息分离，符合分发契约）。

写入磁盘的 Markdown **开头**会固定加上一行源 URL 声明（见 ``_markdown_with_source_declaration``），
``scrape_url_to_markdown`` 仍只返回接口原始正文，便于程序内拼接。
"""

from __future__ import annotations

import asyncio
import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.env_loader import ensure_dotenv_loaded
from byboy.agents.tutor_inf.logging_utils import AgentLogger
from byboy.llm.dispatcher import LLMDispatcher


class FirecrawlError(RuntimeError):
    """Firecrawl API 返回错误或 HTTP 失败。"""


@dataclass(frozen=True, slots=True)
class WebCleanPayload:
    """单次抓取：目标 URL + Markdown 输出目录与文件名。"""

    url: str
    output_dir: str | Path
    output_filename: str
    #: 可选：由编排层填入，便于日志展示 ``[i/n]`` 批次进度。
    progress_index: int | None = None
    progress_total: int | None = None


def firecrawl_api_key_from_env() -> str:
    ensure_dotenv_loaded()
    key = (os.environ.get("FIRECRAWL_API_KEY") or "").strip()
    if not key:
        raise FirecrawlError("未设置环境变量 FIRECRAWL_API_KEY")
    return key


def firecrawl_base_url_from_env() -> str:
    ensure_dotenv_loaded()
    raw = (os.environ.get("FIRECRAWL_BASE_URL") or "https://api.firecrawl.dev").strip()
    return raw.rstrip("/")


def _validate_http_url(url: str) -> None:
    u = url.strip()
    parts = urlsplit(u)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        raise ValueError(f"需要 http(s) URL，当前为 {url!r}")


def scrape_url_to_markdown(
    url: str,
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    only_main_content: bool = True,
    wait_for_ms: int = 0,
    timeout_sec: float = 120.0,
) -> str:
    """调用 Firecrawl ``POST /v2/scrape``，返回 ``data.markdown``。"""
    _validate_http_url(url)
    key = api_key if api_key is not None else firecrawl_api_key_from_env()
    root = base_url if base_url is not None else firecrawl_base_url_from_env()
    endpoint = f"{root}/v2/scrape"
    def _call_scrape(only_main: bool, *, wait_ms: int) -> str:
        body: dict[str, Any] = {
            "url": url.strip(),
            "formats": ["markdown"],
            "onlyMainContent": only_main,
        }
        if wait_ms and wait_ms > 0:
            # 等待页面渲染/动态加载正文
            body["waitFor"] = int(wait_ms)
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            endpoint,
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
                raw = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            try:
                detail = e.read().decode("utf-8")
            except OSError:
                detail = str(e)
            raise FirecrawlError(f"Firecrawl HTTP {e.code}: {detail}") from e
        except urllib.error.URLError as e:
            raise FirecrawlError(f"Firecrawl 请求失败: {e.reason}") from e

        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as e:
            raise FirecrawlError(f"Firecrawl 返回非 JSON: {raw[:200]!r}") from e

        if not payload.get("success"):
            err = payload.get("error") or payload.get("message") or payload
            raise FirecrawlError(f"Firecrawl 失败: {err}")

        data_obj = payload.get("data") or {}
        md = data_obj.get("markdown")
        if md is None or not str(md).strip():
            raise FirecrawlError("Firecrawl 响应中缺少 markdown 正文")
        return str(md)

    md_main = _call_scrape(only_main_content, wait_ms=wait_for_ms)
    # 一些高校站点在 onlyMainContent=True 时会被误裁剪成仅导航。
    if only_main_content and len(md_main.strip()) < 1200:
        md_full = _call_scrape(False, wait_ms=max(0, int(wait_for_ms) * 2) if wait_for_ms else 5000)
        if len(md_full.strip()) > len(md_main.strip()) * 2:
            return md_full
    return md_main


def _markdown_with_source_declaration(source_url: str, markdown_body: str) -> str:
    """在正文前加上源 URL 声明块（引用行 + 空行），供落盘文件使用。"""
    u = source_url.strip()
    if not u:
        return markdown_body
    declaration = f"> 抓取来源：{u}\n\n"
    return declaration + markdown_body.lstrip("\n\r")


def _output_path(payload: WebCleanPayload) -> Path:
    name = payload.output_filename.strip()
    if not name:
        raise ValueError("output_filename 不能为空")
    if Path(name).suffix.lower() != ".md":
        raise ValueError("output_filename 必须以 .md 结尾")
    base = Path(payload.output_dir)
    if not str(base).strip():
        raise ValueError("output_dir 不能为空")
    return (base / name).resolve()


class WebCleanAgent:
    """
    实现与 ``LlmCallingAgent[WebCleanPayload]`` 相同的 ``run`` / ``arun`` 形态；
    内部不调用 ``dispatcher.complete*``，仅在入口执行 ``resolve`` 以校验路由键。
    """

    def run(
        self,
        inv: AgentInvocation[WebCleanPayload],
        dispatcher: LLMDispatcher,
    ) -> Path:
        log = AgentLogger("WebCleanAgent")
        p = inv.llm_part
        prog = ""
        if p.progress_index is not None and p.progress_total is not None:
            prog = f"[{p.progress_index}/{p.progress_total}] "
        log.start("网页清洗", detail=f"{prog}{p.url.strip()}")
        dispatcher.resolve(inv.model.token)
        _validate_http_url(p.url)
        log.step("Firecrawl 抓取", detail=f"{prog}{p.url.strip()[:120]}")
        # 这个站点详情页往往是空壳 HTML + JS 动态加载正文，等待后可提高命中率。
        raw = scrape_url_to_markdown(p.url, wait_for_ms=2500)
        md = _markdown_with_source_declaration(p.url, raw)
        out = _output_path(p)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8", newline="\n")
        log.done("网页清洗完成", detail=f"{prog}{out.name}")
        return out

    async def arun(
        self,
        inv: AgentInvocation[WebCleanPayload],
        dispatcher: LLMDispatcher,
    ) -> Path:
        return await asyncio.to_thread(self.run, inv, dispatcher)


__all__ = [
    "FirecrawlError",
    "ModelRef",
    "AgentInvocation",
    "WebCleanPayload",
    "WebCleanAgent",
    "firecrawl_api_key_from_env",
    "firecrawl_base_url_from_env",
    "scrape_url_to_markdown",
]
