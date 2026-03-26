from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Sequence
from typing import Any

from openai import AsyncOpenAI, OpenAI

from byboy.packyapi.config import PackyConfig

# OpenAI SDK 接受的 message 结构（与 Chat Completions 一致）
ChatMessage = dict[str, Any]


class PackyAPIClient:
    """
    PackyAPI 调用封装：使用 OpenAI 兼容的 ``/v1/chat/completions`` 等端点。

    鉴权：``Authorization: Bearer <api_key>``，与官方 OpenAI 客户端一致。
    """

    def __init__(self, config: PackyConfig | None = None) -> None:
        self._config = config or PackyConfig.from_env()
        if not self._config.api_key:
            raise ValueError(
                "缺少 API Key：请设置 PACKY_API_KEY、PACKYAPI_API_KEY、OPENAI_API_KEY 等"
            )
        _client_kw: dict[str, object] = {
            "api_key": self._config.api_key,
            "base_url": self._config.base_url,
        }
        if self._config.http_timeout_sec is not None:
            _client_kw["timeout"] = float(self._config.http_timeout_sec)
        self._sync = OpenAI(**_client_kw)
        self._async = AsyncOpenAI(**_client_kw)

    @property
    def config(self) -> PackyConfig:
        return self._config

    def chat_completion(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        temperature: float | None = None,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> str:
        """同步聊天补全，返回 assistant 的文本内容（非流式）。"""
        resp = self._sync.chat.completions.create(
            model=model,
            messages=list(messages),
            temperature=temperature,
            max_tokens=max_tokens,
            stream=False,
            **kwargs,
        )
        choice = resp.choices[0]
        content = choice.message.content
        if content is None:
            return ""
        return content

    async def achat_completion(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        temperature: float | None = None,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> str:
        """异步聊天补全，返回 assistant 的文本内容（非流式）。"""
        resp = await self._async.chat.completions.create(
            model=model,
            messages=list(messages),
            temperature=temperature,
            max_tokens=max_tokens,
            stream=False,
            **kwargs,
        )
        choice = resp.choices[0]
        content = choice.message.content
        if content is None:
            return ""
        return content

    def chat_completion_stream(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        temperature: float | None = None,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> Iterator[str]:
        """同步流式增量文本（delta）。"""
        stream = self._sync.chat.completions.create(
            model=model,
            messages=list(messages),
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
            **kwargs,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                yield delta.content

    async def achat_completion_stream(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        temperature: float | None = None,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[str]:
        """异步流式增量文本（delta）。"""
        stream = await self._async.chat.completions.create(
            model=model,
            messages=list(messages),
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
            **kwargs,
        )
        async for chunk in stream:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                yield delta.content

    def raw_sync(self) -> OpenAI:
        """需要调用 embeddings、images 等其它 OpenAI 兼容接口时，使用底层客户端。"""
        return self._sync

    def raw_async(self) -> AsyncOpenAI:
        """异步版底层客户端。"""
        return self._async
