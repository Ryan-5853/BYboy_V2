"""
从导师页完整 HTML 中收集可能含导师信息的图片 URL，下载并按序编号落盘。
"""

from __future__ import annotations

import asyncio
import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit, urlunsplit

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.llm.dispatcher import LLMDispatcher


class PicFindError(RuntimeError):
    """抓取 HTML 或下载图片失败。"""


@dataclass(frozen=True, slots=True)
class PicFindPayload:
    """目标页 URL + 图片输出目录（由调用方保证为本 agent 缓存子目录）。"""

    url: str
    output_dir: str | Path


@dataclass(frozen=True, slots=True)
class PicFindResult:
    """已保存的本地图片路径（按序号排序）及清单 JSON 路径。"""

    image_paths: tuple[Path, ...]
    manifest_path: Path


_DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)
_MAX_BODY_BYTES = 12 * 1024 * 1024
_READ_CHUNK = 65536

_SRCSET_PART = re.compile(
    r"^\s*(\S+?)(?:\s+[\d.w]+)?\s*$",
    re.IGNORECASE,
)
_BG_URL = re.compile(
    r"background-image\s*:\s*url\(\s*[\"']?([^\"')]+)[\"']?\s*\)",
    re.IGNORECASE,
)


def _validate_http_url(url: str) -> None:
    u = url.strip()
    parts = urlsplit(u)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        raise ValueError(f"需要 http(s) URL，当前为 {url!r}")


def _strip_fragment(u: str) -> str:
    p = urlsplit(u)
    return urlunsplit((p.scheme, p.netloc, p.path, p.query, ""))


class _ImageURLCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.raw_urls: list[str] = []
        self._base_href: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k.lower(): (v or "") for k, v in attrs}
        if tag.lower() == "base" and ad.get("href"):
            self._base_href = ad["href"].strip()
            return
        t = tag.lower()
        if t == "img":
            for key in ("src", "data-src", "data-original", "data-lazy-src", "data-lazyload"):
                raw = ad.get(key)
                if raw and raw.strip() and not raw.strip().lower().startswith("data:"):
                    self.raw_urls.append(raw.strip())
            ds = ad.get("data-srcset") or ad.get("srcset")
            if ds:
                self._push_srcset(ds)
            return
        if t == "source":
            ds = ad.get("srcset") or ad.get("data-srcset")
            if ds:
                self._push_srcset(ds)
            if ad.get("src") and not ad["src"].strip().lower().startswith("data:"):
                self.raw_urls.append(ad["src"].strip())
            return
        if t == "meta" and ad.get("property", "").lower() == "og:image" and ad.get("content"):
            self.raw_urls.append(ad["content"].strip())
            return
        if t == "link" and ad.get("rel", "").lower() in ("image_src", "thumbnail"):
            href = ad.get("href")
            if href and href.strip():
                self.raw_urls.append(href.strip())
            return
        style = ad.get("style")
        if style:
            for m in _BG_URL.finditer(style):
                self.raw_urls.append(m.group(1).strip())

    def _push_srcset(self, srcset: str) -> None:
        for piece in srcset.split(","):
            m = _SRCSET_PART.match(piece)
            if m:
                u = m.group(1).strip()
                if u and not u.lower().startswith("data:"):
                    self.raw_urls.append(u)


def _collect_urls_from_html(html: str, page_url: str) -> list[str]:
    col = _ImageURLCollector()
    try:
        col.feed(html)
        col.close()
    except Exception:
        pass
    base_for_join = page_url
    if col._base_href:
        base_for_join = urljoin(page_url, col._base_href)
    seen: set[str] = set()
    out: list[str] = []
    for raw in col.raw_urls:
        for m in _BG_URL.finditer(raw):
            raw = m.group(1).strip()
        if raw.startswith("//"):
            raw = urlsplit(page_url).scheme + ":" + raw
        abs_u = urljoin(base_for_join, raw)
        parts = urlsplit(abs_u)
        if parts.scheme not in ("http", "https"):
            continue
        norm = _strip_fragment(abs_u)
        if norm in seen:
            continue
        seen.add(norm)
        out.append(norm)
    for m in _BG_URL.finditer(html):
        raw = m.group(1).strip()
        if raw.startswith("//"):
            raw = urlsplit(page_url).scheme + ":" + raw
        abs_u = urljoin(base_for_join, raw)
        parts = urlsplit(abs_u)
        if parts.scheme not in ("http", "https"):
            continue
        norm = _strip_fragment(abs_u)
        if norm in seen:
            continue
        seen.add(norm)
        out.append(norm)
    return out


def _ext_from_content_type(ct: str | None) -> str | None:
    if not ct:
        return None
    main = ct.split(";")[0].strip().lower()
    return {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/bmp": ".bmp",
        "image/svg+xml": ".svg",
    }.get(main)


def _ext_from_bytes(head: bytes) -> str:
    if len(head) >= 3 and head[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if len(head) >= 8 and head[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if len(head) >= 6 and (head[:6] in (b"GIF87a", b"GIF89a")):
        return ".gif"
    if len(head) >= 12 and head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return ".webp"
    if head.strip().startswith(b"<svg") or head.strip().startswith(b"<?xml"):
        return ".svg"
    return ".bin"


def _fetch_html(url: str, *, timeout_sec: float = 60.0) -> tuple[str, str]:
    _validate_http_url(url)
    req = urllib.request.Request(
        url.strip(),
        headers={
            "User-Agent": _DEFAULT_UA,
            "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "identity",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
            final = resp.geturl()
            raw = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
    except urllib.error.HTTPError as e:
        raise PicFindError(f"获取 HTML HTTP {e.code}: {e.reason}") from e
    except urllib.error.URLError as e:
        raise PicFindError(f"获取 HTML 失败: {e.reason}") from e
    if len(raw) > _MAX_BODY_BYTES:
        raise PicFindError("HTML 体积超过上限")
    try:
        text = raw.decode(charset, errors="replace")
    except LookupError:
        text = raw.decode("utf-8", errors="replace")
    return text, final


def _download_binary(url: str, *, timeout_sec: float = 45.0) -> tuple[bytes, str | None]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": _DEFAULT_UA,
            "Accept": "image/*,*/*;q=0.8",
            "Accept-Encoding": "identity",
        },
        method="GET",
    )
    chunks: list[bytes] = []
    total = 0
    ctype: str | None = None
    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
            ctype = resp.headers.get("Content-Type")
            while True:
                piece = resp.read(_READ_CHUNK)
                if not piece:
                    break
                total += len(piece)
                if total > _MAX_BODY_BYTES:
                    raise PicFindError("单张图片超过体积上限")
                chunks.append(piece)
    except urllib.error.HTTPError as e:
        raise PicFindError(f"下载图片 HTTP {e.code}: {url[:80]!r}") from e
    except urllib.error.URLError as e:
        raise PicFindError(f"下载图片失败 {url[:80]!r}: {e.reason}") from e
    return b"".join(chunks), ctype


def _is_image_payload(content_type: str | None, data: bytes) -> bool:
    if content_type:
        main = content_type.split(";")[0].strip().lower()
        if main.startswith("image/"):
            return True
    return _ext_from_bytes(data[: min(512, len(data))]) != ".bin"


class PicFindAgent:
    """拉取 HTML、抽取图片 URL、下载并按 ``001.*`` 顺序保存；``model`` 仅用于 ``dispatcher.resolve``。"""

    def run(
        self,
        inv: AgentInvocation[PicFindPayload],
        dispatcher: LLMDispatcher,
    ) -> PicFindResult:
        dispatcher.resolve(inv.model.token)
        p = inv.llm_part
        html, page_url = _fetch_html(p.url.strip())
        cand_urls = _collect_urls_from_html(html, page_url)
        out_dir = Path(p.output_dir).resolve()
        out_dir.mkdir(parents=True, exist_ok=True)

        saved: list[Path] = []
        manifest_rows: list[dict[str, Any]] = []
        idx = 0
        for src_url in cand_urls:
            try:
                data, ct = _download_binary(src_url)
            except PicFindError as e:
                manifest_rows.append({"source_url": src_url, "status": "error", "detail": str(e)})
                continue
            if not data or not _is_image_payload(ct, data):
                manifest_rows.append({"source_url": src_url, "status": "skipped", "reason": "not_image"})
                continue
            ext = _ext_from_content_type(ct) or _ext_from_bytes(data[: min(512, len(data))])
            idx += 1
            name = f"{idx:03d}{ext}"
            path = (out_dir / name).resolve()
            path.write_bytes(data)
            saved.append(path)
            manifest_rows.append(
                {
                    "index": idx,
                    "filename": name,
                    "source_url": src_url,
                    "status": "saved",
                    "content_type": ct,
                }
            )

        man_path = (out_dir / "pic_find_manifest.json").resolve()
        man_path.write_text(
            json.dumps(
                {
                    "request_url": p.url.strip(),
                    "resolved_page_url": page_url,
                    "output_dir": str(out_dir),
                    "entries": manifest_rows,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return PicFindResult(image_paths=tuple(saved), manifest_path=man_path)

    async def arun(
        self,
        inv: AgentInvocation[PicFindPayload],
        dispatcher: LLMDispatcher,
    ) -> PicFindResult:
        return await asyncio.to_thread(self.run, inv, dispatcher)


__all__ = [
    "AgentInvocation",
    "ModelRef",
    "PicFindAgent",
    "PicFindError",
    "PicFindPayload",
    "PicFindResult",
]