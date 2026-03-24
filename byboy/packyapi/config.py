from __future__ import annotations

import os
from dataclasses import dataclass

from byboy.env_loader import ensure_dotenv_loaded


def _packy_api_key_from_env() -> str:
    """与旧 BYboy ``tests/web_clean`` / ``tests/link_choose`` 的 ``PACKYAPI_API_KEY`` 对齐。"""
    return (
        os.environ.get("PACKY_API_KEY")
        or os.environ.get("PACKYAPI_API_KEY")
        or os.environ.get("ANTHROPIC_AUTH_TOKEN")
        or os.environ.get("OPENAI_API_KEY")
        or os.environ.get("ANTHROPIC_API_KEY")
        or ""
    ).strip()


def _vision_api_key_from_env() -> str:
    return (
        os.environ.get("PACKY_VISION_API_KEY")
        or os.environ.get("PACKY_VISION_OPENAI_API_KEY")
        or os.environ.get("PACKY_VISION_ANTHROPIC_API_KEY")
        or _packy_api_key_from_env()
    ).strip()


def _openai_compat_base_v1_from_env() -> str:
    raw = (
        os.environ.get("PACKY_BASE_URL")
        or os.environ.get("PACKYAPI_BASE_URL")
        or "https://www.packyapi.com"
    ).strip().rstrip("/")
    return raw if raw.endswith("/v1") else f"{raw}/v1"


def _vision_openai_compat_base_v1_from_env() -> str:
    raw = (
        os.environ.get("PACKY_VISION_BASE_URL")
        or os.environ.get("PACKY_VISION_OPENAI_BASE_URL")
        or os.environ.get("PACKY_BASE_URL")
        or os.environ.get("PACKYAPI_BASE_URL")
        or "https://www.packyapi.com"
    ).strip().rstrip("/")
    return raw if raw.endswith("/v1") else f"{raw}/v1"


def _anthropic_messages_root_from_env() -> str:
    """
    Anthropic SDK 的 ``base_url``：网关根，**不要**带 ``/v1``。

    未配置 ``PACKY_ANTHROPIC_BASE_URL`` 时，与脚本 ``PACKY_BASE_URL`` / ``PACKYAPI_BASE_URL``
    保持一致（并剥掉末尾 ``/v1``），行为对齐 ``run_link_choose.py`` / ``run_web_clean.py``。
    """
    explicit = (os.environ.get("PACKY_ANTHROPIC_BASE_URL") or "").strip().rstrip("/")
    if explicit:
        return explicit[:-3].rstrip("/") if explicit.endswith("/v1") else explicit
    shared = (
        os.environ.get("PACKY_BASE_URL")
        or os.environ.get("PACKYAPI_BASE_URL")
        or "https://www.packyapi.com"
    ).strip().rstrip("/")
    if shared.endswith("/v1"):
        shared = shared[:-3].rstrip("/")
    return shared or "https://www.packyapi.com"


def _vision_anthropic_messages_root_from_env() -> str:
    explicit = (
        os.environ.get("PACKY_VISION_ANTHROPIC_BASE_URL") or ""
    ).strip().rstrip("/")
    if explicit:
        return explicit[:-3].rstrip("/") if explicit.endswith("/v1") else explicit
    shared = (
        os.environ.get("PACKY_VISION_BASE_URL")
        or os.environ.get("PACKY_VISION_OPENAI_BASE_URL")
        or os.environ.get("PACKY_BASE_URL")
        or os.environ.get("PACKYAPI_BASE_URL")
        or "https://www.packyapi.com"
    ).strip().rstrip("/")
    if shared.endswith("/v1"):
        shared = shared[:-3].rstrip("/")
    return shared or "https://www.packyapi.com"


@dataclass(frozen=True, slots=True)
class PackyConfig:
    """
    Packy 连接信息。

    - ``base_url``：OpenAI 兼容接口根路径（一般以 ``/v1`` 结尾）。
    - ``anthropic_base_url``：Anthropic Messages API 根路径（**不要**带 ``/v1``，SDK 会自动拼接）。
    """

    api_key: str
    base_url: str = "https://www.packyapi.com/v1"
    anthropic_base_url: str = "https://www.packyapi.com"

    @classmethod
    def from_env(cls) -> PackyConfig:
        ensure_dotenv_loaded()
        api_key = _packy_api_key_from_env()
        base_url = _openai_compat_base_v1_from_env()
        raw_anthropic = _anthropic_messages_root_from_env()
        return cls(
            api_key=api_key,
            base_url=base_url,
            anthropic_base_url=raw_anthropic,
        )

    @classmethod
    def from_vision_env(cls) -> PackyConfig:
        """读取视觉链路专用配置，未设置时回退到通用 Packy 配置。"""
        ensure_dotenv_loaded()
        api_key = _vision_api_key_from_env()
        base_url = _vision_openai_compat_base_v1_from_env()
        raw_anthropic = _vision_anthropic_messages_root_from_env()
        return cls(
            api_key=api_key,
            base_url=base_url,
            anthropic_base_url=raw_anthropic,
        )
