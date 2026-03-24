from __future__ import annotations

import os
from dataclasses import dataclass

from byboy.env_loader import ensure_dotenv_loaded


@dataclass(frozen=True, slots=True)
class FirecrawlConfig:
    """
    Firecrawl 云 API 连接信息。

    - ``base_url``：API 主机根路径，不含版本段（默认 ``https://api.firecrawl.dev``）。
    - ``api_version``：路径前缀，如 ``v2``，实际请求为 ``{base_url}/{api_version}/…``。
    """

    api_key: str
    base_url: str = "https://api.firecrawl.dev"
    api_version: str = "v2"

    def api_root(self) -> str:
        return f"{self.base_url.rstrip('/')}/{self.api_version.strip().strip('/')}"

    @classmethod
    def from_env(cls) -> FirecrawlConfig:
        ensure_dotenv_loaded()
        api_key = (os.environ.get("FIRECRAWL_API_KEY") or "").strip()
        base = (
            os.environ.get("FIRECRAWL_BASE_URL") or "https://api.firecrawl.dev"
        ).strip().rstrip("/")
        version = (os.environ.get("FIRECRAWL_API_VERSION") or "v2").strip().strip("/")
        return cls(api_key=api_key, base_url=base, api_version=version)
