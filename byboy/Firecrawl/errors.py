from __future__ import annotations


class FirecrawlAPIError(Exception):
    """Firecrawl HTTP 非成功响应或解析失败。"""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        body: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.body = body
