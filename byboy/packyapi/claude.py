from __future__ import annotations

import base64
import os
import re
from collections.abc import AsyncIterator, Iterator, Sequence
from typing import Any, cast

from anthropic import AsyncAnthropic, Anthropic
from anthropic.types import MessageParam

from byboy.packyapi.config import PackyConfig

ChatMessage = dict[str, Any]

_DATA_IMAGE_RE = re.compile(
    r"^data:(image/[-+.\w]+);base64,(.+)$",
    re.IGNORECASE | re.DOTALL,
)


def _stringify_message_content(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text" and "text" in block:
                    parts.append(str(block["text"]))
                elif "text" in block:
                    parts.append(str(block["text"]))
            else:
                parts.append(str(block))
        return "\n".join(parts)
    return str(content)


def _normalize_anthropic_media_type(mime: str) -> str:
    m = mime.strip().lower()
    if m == "image/jpg":
        return "image/jpeg"
    return m


def _openai_image_block_to_anthropic(block: dict[str, Any]) -> dict[str, Any] | None:
    iu = block.get("image_url")
    url = ""
    if isinstance(iu, dict):
        url = str(iu.get("url") or "")
    elif iu is not None:
        url = str(iu)
    if not url:
        return None
    dm = _DATA_IMAGE_RE.match(url.strip())
    if dm:
        mime = _normalize_anthropic_media_type(dm.group(1))
        b64 = dm.group(2).strip()
        try:
            base64.b64decode(b64, validate=True)
        except (ValueError, TypeError):
            return None
        return {
            "type": "image",
            "source": {"type": "base64", "media_type": mime, "data": b64},
        }
    u = url.strip()
    if u.startswith("http://") or u.startswith("https://"):
        return {"type": "image", "source": {"type": "url", "url": u}}
    return None


def _openai_content_list_to_anthropic(parts: list[Any]) -> str | list[dict[str, Any]]:
    """OpenAI 多模态 ``content`` 列表 -> Anthropic ``content``（字符串或 block 列表）。"""
    ablocks: list[dict[str, Any]] = []
    for block in parts:
        if not isinstance(block, dict):
            ablocks.append({"type": "text", "text": str(block)})
            continue
        t = block.get("type")
        if t == "text" or (t is None and "text" in block):
            ablocks.append({"type": "text", "text": str(block.get("text", ""))})
            continue
        if t == "image_url":
            img = _openai_image_block_to_anthropic(block)
            if img is not None:
                ablocks.append(img)
            continue
        ablocks.append({"type": "text", "text": str(block)})

    has_image = any(b.get("type") == "image" for b in ablocks)
    texts = [str(b.get("text", "")) for b in ablocks if b.get("type") == "text"]
    if not has_image:
        return "\n\n".join(x for x in texts if x).strip()
    out_blocks: list[dict[str, Any]] = []
    for b in ablocks:
        if b.get("type") == "text":
            tx = str(b.get("text", ""))
            if tx:
                out_blocks.append({"type": "text", "text": tx})
        else:
            out_blocks.append(b)
    return out_blocks


def _anthropic_user_or_assistant_content(role: str, content: Any) -> str | list[dict[str, Any]]:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        if role == "user":
            return _openai_content_list_to_anthropic(content)
        return _stringify_message_content(content)
    return str(content)


def openai_style_messages_to_anthropic(
    messages: Sequence[ChatMessage],
) -> tuple[str | None, list[MessageParam]]:
    """将常见 OpenAI 风格 ``role/content`` 列表转为 Anthropic 的 ``system`` + ``messages``。"""
    system_chunks: list[str] = []
    out: list[MessageParam] = []
    for m in messages:
        role = m.get("role")
        content = m.get("content")
        if role == "system":
            system_chunks.append(_stringify_message_content(content))
            continue
        if role in ("user", "assistant"):
            ac = _anthropic_user_or_assistant_content(str(role), content)
            out.append(
                cast(
                    MessageParam,
                    {
                        "role": role,
                        "content": ac,
                    },
                )
            )
    system = "\n\n".join(system_chunks) if system_chunks else None
    return system, out


def _message_text_blocks(resp: Any) -> str:
    texts: list[str] = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            texts.append(getattr(block, "text", "") or "")
    return "".join(texts)


def _is_streaming_required_value_error(err: ValueError) -> bool:
    """Anthropic SDK：非流式 ``max_tokens`` 过大时会拒绝并提示改用 stream。"""
    return "Streaming is required" in str(err)


class PackyClaudeClient:
    """
    经 Packy 转发调用 **Anthropic Messages API**（与 Claude Code 相同网关域名时可共用令牌）。

    环境变量与控制台文档一致时可使用：``ANTHROPIC_AUTH_TOKEN`` 或 ``PACKY_API_KEY``。
    """

    def __init__(self, config: PackyConfig | None = None) -> None:
        self._config = config or PackyConfig.from_env()
        if not self._config.api_key:
            raise ValueError(
                "缺少 API Key：请设置 PACKY_API_KEY、PACKYAPI_API_KEY、"
                "ANTHROPIC_AUTH_TOKEN、OPENAI_API_KEY 或 ANTHROPIC_API_KEY"
            )
        # 与旧 BYboy tests/link_choose、web_clean 中 _link_choose_llm / _web_clean_llm 一致：
        # CrewAI / 其它读 ANTHROPIC_* 的栈与裸 Anthropic SDK 使用同一 Packy 端点。
        os.environ["ANTHROPIC_API_KEY"] = self._config.api_key
        os.environ["ANTHROPIC_BASE_URL"] = self._config.anthropic_base_url
        self._sync = Anthropic(
            api_key=self._config.api_key,
            base_url=self._config.anthropic_base_url,
        )
        self._async = AsyncAnthropic(
            api_key=self._config.api_key,
            base_url=self._config.anthropic_base_url,
        )

    @property
    def config(self) -> PackyConfig:
        return self._config

    def messages_create(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        system: str | None = None,
        max_tokens: int = 4096,
        temperature: float | None = None,
        **kwargs: Any,
    ) -> str:
        sys_text, anth_msgs = openai_style_messages_to_anthropic(messages)
        merged_system = sys_text if system is None else (sys_text + "\n\n" + system if sys_text else system)
        kw: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": anth_msgs,
            **kwargs,
        }
        if merged_system:
            kw["system"] = merged_system
        if temperature is not None:
            kw["temperature"] = temperature
        try:
            resp = self._sync.messages.create(**kw)
            return _message_text_blocks(resp)
        except ValueError as e:
            if not _is_streaming_required_value_error(e):
                raise
            buf: list[str] = []
            with self._sync.messages.stream(**kw) as stream:
                for chunk in stream.text_stream:
                    buf.append(chunk)
            return "".join(buf)

    async def amessages_create(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        system: str | None = None,
        max_tokens: int = 4096,
        temperature: float | None = None,
        **kwargs: Any,
    ) -> str:
        sys_text, anth_msgs = openai_style_messages_to_anthropic(messages)
        merged_system = sys_text if system is None else (sys_text + "\n\n" + system if sys_text else system)
        kw: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": anth_msgs,
            **kwargs,
        }
        if merged_system:
            kw["system"] = merged_system
        if temperature is not None:
            kw["temperature"] = temperature
        try:
            resp = await self._async.messages.create(**kw)
            return _message_text_blocks(resp)
        except ValueError as e:
            if not _is_streaming_required_value_error(e):
                raise
            buf: list[str] = []
            async with self._async.messages.stream(**kw) as stream:
                async for chunk in stream.text_stream:
                    buf.append(chunk)
            return "".join(buf)

    def messages_stream(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        system: str | None = None,
        max_tokens: int = 4096,
        temperature: float | None = None,
        **kwargs: Any,
    ) -> Iterator[str]:
        sys_text, anth_msgs = openai_style_messages_to_anthropic(messages)
        merged_system = sys_text if system is None else (sys_text + "\n\n" + system if sys_text else system)
        kw: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": anth_msgs,
            **kwargs,
        }
        if merged_system:
            kw["system"] = merged_system
        if temperature is not None:
            kw["temperature"] = temperature
        with self._sync.messages.stream(**kw) as stream:
            yield from stream.text_stream

    async def amessages_stream(
        self,
        *,
        model: str,
        messages: Sequence[ChatMessage],
        system: str | None = None,
        max_tokens: int = 4096,
        temperature: float | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[str]:
        sys_text, anth_msgs = openai_style_messages_to_anthropic(messages)
        merged_system = sys_text if system is None else (sys_text + "\n\n" + system if sys_text else system)
        kw: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": anth_msgs,
            **kwargs,
        }
        if merged_system:
            kw["system"] = merged_system
        if temperature is not None:
            kw["temperature"] = temperature
        async with self._async.messages.stream(**kw) as stream:
            async for text in stream.text_stream:
                yield text

    def raw_sync(self) -> Anthropic:
        return self._sync

    def raw_async(self) -> AsyncAnthropic:
        return self._async
