from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from byboy.packyapi.config import PackyConfig

from byboy.llm.registry import ModelSlotRegistry
from byboy.llm.route_spec import ChatMessage, RouteSpec
from byboy.packyapi.claude import PackyClaudeClient
from byboy.packyapi.client import PackyAPIClient


class LLMDispatcher:
    """
    按路由键选择 ``RouteSpec``，并调用 Packy 上的 **Claude（Anthropic）** 或 **OpenAI 兼容** 接口。

    主用 Claude 时传入 ``claude_client``，并将各路由 ``backend`` 保持默认 ``\"claude\"`` 即可。
    """

    def __init__(
        self,
        *,
        routes: Mapping[str, str | RouteSpec] | None = None,
        slot_registry: ModelSlotRegistry | None = None,
        default_route: str = "default",
        openai_client: PackyAPIClient | None = None,
        claude_client: PackyClaudeClient | None = None,
        vision_openai_client: PackyAPIClient | None = None,
        vision_claude_client: PackyClaudeClient | None = None,
        route_openai_clients: Mapping[str, PackyAPIClient] | None = None,
        route_claude_clients: Mapping[str, PackyClaudeClient] | None = None,
        route_vision_openai_clients: Mapping[str, PackyAPIClient] | None = None,
        route_vision_claude_clients: Mapping[str, PackyClaudeClient] | None = None,
    ) -> None:
        self._openai = openai_client
        self._claude = claude_client
        self._vision_openai = vision_openai_client
        self._vision_claude = vision_claude_client
        self._default_route = default_route
        self._slot_registry = slot_registry
        self._route_openai_clients = {
            self._normalize_slot_key(k): v for k, v in (route_openai_clients or {}).items()
        }
        self._route_claude_clients = {
            self._normalize_slot_key(k): v for k, v in (route_claude_clients or {}).items()
        }
        self._route_vision_openai_clients = {
            self._normalize_slot_key(k): v
            for k, v in (route_vision_openai_clients or {}).items()
        }
        self._route_vision_claude_clients = {
            self._normalize_slot_key(k): v
            for k, v in (route_vision_claude_clients or {}).items()
        }
        self._routes: dict[str, RouteSpec] = {}
        if routes:
            self.update_routes(routes)

    @staticmethod
    def _normalize_slot_key(key: str) -> str:
        k = key.strip().lower()
        if k.startswith("byboy_slot_"):
            return k[len("byboy_slot_") :]
        if k.startswith("slot_"):
            return k[len("slot_") :]
        return k

    def set_route(self, key: str, spec: str | RouteSpec) -> None:
        self._routes[key] = (
            RouteSpec(model=spec) if isinstance(spec, str) else spec
        )

    def update_routes(self, routes: Mapping[str, str | RouteSpec]) -> None:
        for k, v in routes.items():
            self.set_route(k, v)

    def _resolve_one(self, key: str) -> RouteSpec | None:
        hit = self._resolve_one_with_key(key)
        return hit[1] if hit is not None else None

    def _resolve_one_with_key(self, key: str) -> tuple[str, RouteSpec] | None:
        if key in self._routes:
            return (key, self._routes[key])
        if self._slot_registry is not None:
            slot_hit = self._slot_registry.get_slot(key)
            if slot_hit is not None:
                return (self._normalize_slot_key(key), slot_hit)
            adhoc = self._slot_registry.resolve_adhoc(key)
            if adhoc is not None:
                return (key, adhoc)
        return None

    def resolve(self, route_key: str | None) -> RouteSpec:
        """
        解析顺序：``routes`` 显式表 → 槽位注册表（推理/代码等标注）→
        ``openai:…`` / ``claude:…`` / 裸 API 模型 id。

        若当前键未命中，再回退到 ``default_route`` 对应项。
        """
        key = (route_key if route_key is not None else self._default_route).strip()
        hit = self._resolve_one_with_key(key)
        if hit is not None:
            return hit[1]
        fb = self._default_route.strip()
        if fb != key:
            hit_fb = self._resolve_one_with_key(fb)
            if hit_fb is not None:
                return hit_fb[1]
        raise KeyError(
            f"未知路由 {key!r}，且无法回退到默认 {self._default_route!r}"
        )

    def _resolve_with_key(self, route_key: str | None) -> tuple[str, RouteSpec]:
        key = (route_key if route_key is not None else self._default_route).strip()
        hit = self._resolve_one_with_key(key)
        if hit is not None:
            return hit
        fb = self._default_route.strip()
        if fb != key:
            hit_fb = self._resolve_one_with_key(fb)
            if hit_fb is not None:
                return hit_fb
        raise KeyError(
            f"未知路由 {key!r}，且无法回退到默认 {self._default_route!r}"
        )

    def _merge_kwargs(self, spec: RouteSpec, overrides: dict[str, Any]) -> dict[str, Any]:
        out: dict[str, Any] = dict(spec.extra)
        if spec.temperature is not None and "temperature" not in overrides:
            out["temperature"] = spec.temperature
        if spec.max_tokens is not None and "max_tokens" not in overrides:
            out["max_tokens"] = spec.max_tokens
        out.update(overrides)
        return out

    def _require_claude(self, route_key: str) -> PackyClaudeClient:
        rk = self._normalize_slot_key(route_key)
        c = self._route_claude_clients.get(rk)
        if c is not None:
            return c
        if self._claude is None:
            raise ValueError("该路由使用 Claude 后端，但未提供 claude_client")
        return self._claude

    def _require_openai(self, route_key: str) -> PackyAPIClient:
        rk = self._normalize_slot_key(route_key)
        c = self._route_openai_clients.get(rk)
        if c is not None:
            return c
        if self._openai is None:
            raise ValueError("该路由使用 OpenAI 兼容后端，但未提供 openai_client")
        return self._openai

    def _require_vision_claude(self, route_key: str) -> PackyClaudeClient:
        rk = self._normalize_slot_key(route_key)
        c = self._route_vision_claude_clients.get(rk)
        if c is not None:
            return c
        if self._vision_claude is None:
            raise ValueError(
                "该路由使用视觉 Claude 后端，但未提供 vision_claude_client"
            )
        return self._vision_claude

    def _require_vision_openai(self, route_key: str) -> PackyAPIClient:
        rk = self._normalize_slot_key(route_key)
        c = self._route_vision_openai_clients.get(rk)
        if c is not None:
            return c
        if self._vision_openai is None:
            raise ValueError(
                "该路由使用视觉 OpenAI 兼容后端，但未提供 vision_openai_client"
            )
        return self._vision_openai

    def complete(
        self,
        route_key: str | None,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> str:
        resolved_key, spec = self._resolve_with_key(route_key)
        call_kw = self._merge_kwargs(spec, kwargs)
        if spec.backend == "claude":
            max_t = call_kw.pop("max_tokens", None) or 4096
            return self._require_claude(resolved_key).messages_create(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            )
        if spec.backend == "claude_vision":
            max_t = call_kw.pop("max_tokens", None) or 4096
            return self._require_vision_claude(resolved_key).messages_create(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            )
        if spec.backend == "openai_vision":
            return self._require_vision_openai(resolved_key).chat_completion(
                model=spec.model,
                messages=messages,
                **call_kw,
            )
        return self._require_openai(resolved_key).chat_completion(
            model=spec.model,
            messages=messages,
            **call_kw,
        )

    async def acomplete(
        self,
        route_key: str | None,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> str:
        resolved_key, spec = self._resolve_with_key(route_key)
        call_kw = self._merge_kwargs(spec, kwargs)
        if spec.backend == "claude":
            max_t = call_kw.pop("max_tokens", None) or 4096
            return await self._require_claude(resolved_key).amessages_create(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            )
        if spec.backend == "claude_vision":
            max_t = call_kw.pop("max_tokens", None) or 4096
            return await self._require_vision_claude(resolved_key).amessages_create(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            )
        if spec.backend == "openai_vision":
            return await self._require_vision_openai(resolved_key).achat_completion(
                model=spec.model,
                messages=messages,
                **call_kw,
            )
        return await self._require_openai(resolved_key).achat_completion(
            model=spec.model,
            messages=messages,
            **call_kw,
        )

    def complete_stream(
        self,
        route_key: str | None,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> Iterator[str]:
        resolved_key, spec = self._resolve_with_key(route_key)
        call_kw = self._merge_kwargs(spec, kwargs)
        if spec.backend == "claude":
            max_t = call_kw.pop("max_tokens", None) or 4096
            yield from self._require_claude(resolved_key).messages_stream(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            )
        elif spec.backend == "claude_vision":
            max_t = call_kw.pop("max_tokens", None) or 4096
            yield from self._require_vision_claude(resolved_key).messages_stream(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            )
        elif spec.backend == "openai_vision":
            yield from self._require_vision_openai(resolved_key).chat_completion_stream(
                model=spec.model,
                messages=messages,
                **call_kw,
            )
        else:
            yield from self._require_openai(resolved_key).chat_completion_stream(
                model=spec.model,
                messages=messages,
                **call_kw,
            )

    async def acomplete_stream(
        self,
        route_key: str | None,
        messages: Sequence[ChatMessage],
        **kwargs: Any,
    ) -> AsyncIterator[str]:
        resolved_key, spec = self._resolve_with_key(route_key)
        call_kw = self._merge_kwargs(spec, kwargs)
        if spec.backend == "claude":
            max_t = call_kw.pop("max_tokens", None) or 4096
            async for part in self._require_claude(resolved_key).amessages_stream(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            ):
                yield part
        elif spec.backend == "claude_vision":
            max_t = call_kw.pop("max_tokens", None) or 4096
            async for part in self._require_vision_claude(resolved_key).amessages_stream(
                model=spec.model,
                messages=messages,
                max_tokens=max_t,
                **call_kw,
            ):
                yield part
        elif spec.backend == "openai_vision":
            async for part in self._require_vision_openai(
                resolved_key
            ).achat_completion_stream(
                model=spec.model,
                messages=messages,
                **call_kw,
            ):
                yield part
        else:
            async for part in self._require_openai(resolved_key).achat_completion_stream(
                model=spec.model,
                messages=messages,
                **call_kw,
            ):
                yield part

    @classmethod
    def from_env(
        cls,
        *,
        packy_config: PackyConfig | None = None,
        openai_client: PackyAPIClient | None = None,
        claude_client: PackyClaudeClient | None = None,
    ) -> LLMDispatcher:
        """从环境变量（及可选的 ``.env``）构建调度器，模型与默认路由见 ``byboy.settings``。"""
        from byboy.settings import llm_dispatcher_from_env

        return llm_dispatcher_from_env(
            packy_config=packy_config,
            openai_client=openai_client,
            claude_client=claude_client,
        )
