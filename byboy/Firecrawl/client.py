from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Mapping

from .config import FirecrawlConfig
from .errors import FirecrawlAPIError


class FirecrawlClient:
    """
    Firecrawl REST API（当前按官方 ``v2`` 文档：``/scrape``、``/map``、``/search``、``/crawl``）。

    鉴权：``Authorization: Bearer <FIRECRAWL_API_KEY>``。
    """

    def __init__(
        self,
        config: FirecrawlConfig | None = None,
        *,
        timeout: float = 120.0,
    ) -> None:
        self._config = config or FirecrawlConfig.from_env()
        if not self._config.api_key:
            raise ValueError("缺少 API Key：请设置环境变量 FIRECRAWL_API_KEY")
        self._timeout = timeout

    @property
    def config(self) -> FirecrawlConfig:
        return self._config

    def _url(self, path: str) -> str:
        p = path if path.startswith("/") else f"/{path}"
        return f"{self._config.api_root()}{p}"

    def _request_json(
        self,
        method: str,
        path_or_url: str,
        *,
        body: Mapping[str, Any] | None = None,
        use_full_url: bool = False,
    ) -> dict[str, Any]:
        url = path_or_url if use_full_url else self._url(path_or_url)
        headers = {
            "Authorization": f"Bearer {self._config.api_key}",
            "Accept": "application/json",
        }
        data: bytes | None = None
        m = method.upper()
        if body is not None and m not in ("GET", "HEAD"):
            headers["Content-Type"] = "application/json"
            data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method=m)
        try:
            with urllib.request.urlopen(req, timeout=self._timeout) as resp:
                raw = resp.read().decode("utf-8")
                if not raw.strip():
                    return {}
                try:
                    out = json.loads(raw)
                except json.JSONDecodeError as e:
                    raise FirecrawlAPIError(
                        f"Firecrawl 响应非 JSON：{raw[:200]!r}",
                        status_code=getattr(resp, "status", None),
                        body=raw,
                    ) from e
                if not isinstance(out, dict):
                    raise FirecrawlAPIError(
                        "Firecrawl 响应 JSON 根类型应为 object",
                        status_code=getattr(resp, "status", None),
                        body=raw,
                    )
                return out
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", errors="replace")
            raise FirecrawlAPIError(
                f"Firecrawl HTTP {e.code}: {raw[:800]}",
                status_code=e.code,
                body=raw,
            ) from e

    def scrape(self, url: str, **options: Any) -> dict[str, Any]:
        """``POST /scrape``：单页抓取（``options`` 与官方 ScrapeOptions 对齐，如 ``formats``）。"""
        body: dict[str, Any] = {"url": url, **options}
        return self._request_json("POST", "/scrape", body=body)

    def map_site(self, url: str, **options: Any) -> dict[str, Any]:
        """``POST /map``：站点 URL 发现（避免与内置 ``map`` 同名）。"""
        body: dict[str, Any] = {"url": url, **options}
        return self._request_json("POST", "/map", body=body)

    def search(self, query: str, **options: Any) -> dict[str, Any]:
        """``POST /search``：联网搜索并可附带 ``scrapeOptions`` 等。"""
        body: dict[str, Any] = {"query": query, **options}
        return self._request_json("POST", "/search", body=body)

    def crawl(self, url: str, **options: Any) -> dict[str, Any]:
        """``POST /crawl``：提交站点爬取任务。"""
        body: dict[str, Any] = {"url": url, **options}
        return self._request_json("POST", "/crawl", body=body)

    def crawl_status(self, job_id: str, **query: Any) -> dict[str, Any]:
        """``GET /crawl/{id}``：查询爬取任务状态；``query`` 会序列化为查询串。"""
        path = f"/crawl/{urllib.parse.quote(job_id, safe='')}"
        if query:
            path = f"{path}?{urllib.parse.urlencode(query)}"
        return self._request_json("GET", path)

    def get_json(self, full_url: str) -> dict[str, Any]:
        """
        ``GET`` 任意完整 URL（例如 ``crawl_status`` 返回的分页字段 ``next``）。

        仍携带与 Firecrawl 一致的 Bearer 头。
        """
        return self._request_json("GET", full_url, use_full_url=True)


def firecrawl_client_from_env(**kwargs: Any) -> FirecrawlClient:
    """使用 ``FirecrawlConfig.from_env()`` 构造客户端。"""
    return FirecrawlClient(FirecrawlConfig.from_env(), **kwargs)
