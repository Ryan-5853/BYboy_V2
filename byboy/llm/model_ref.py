"""
将「模型引用」解析为 ``RouteSpec``。

支持：

- ``openai:<模型 id>`` / ``claude:<模型 id>``（显式通道）
- 裸 API 模型 id（按前缀启发式选择后端，见 ``_looks_like_api_model_id``）

槽位名（如 ``reasoning``）由 ``ModelSlotRegistry`` 单独解析，不在此函数内查表。
"""

from __future__ import annotations

from byboy.llm.route_spec import Backend, RouteSpec


def parse_route_spec_token(token: str) -> RouteSpec:
    """把 ``backend:model`` 或裸模型 id 转为 ``RouteSpec``。"""
    t = token.strip()
    if not t:
        raise ValueError("模型引用为空")
    if ":" in t:
        backend_raw, _, model_raw = t.partition(":")
        backend_s = backend_raw.strip().lower()
        model_s = model_raw.strip()
        if not model_s:
            raise ValueError(f"模型 id 为空：{token!r}")
        if backend_s not in ("openai", "claude", "openai_vision", "claude_vision"):
            raise ValueError(
                "backend 必须是 openai / claude / openai_vision / claude_vision，"
                f"当前为 {backend_raw.strip()!r}"
            )
        return RouteSpec(model=model_s, backend=backend_s)  # type: ignore[arg-type]
    return _bare_model_to_spec(t)


def _bare_model_to_spec(model_id: str) -> RouteSpec:
    low = model_id.strip().lower()
    if low.startswith("claude"):
        backend: Backend = "claude"
    else:
        backend = "openai"
    return RouteSpec(model=model_id.strip(), backend=backend)


def looks_like_api_model_id(token: str) -> bool:
    """
    判断 ``token`` 是否更像直连 API 的模型 id，而非业务槽位名。

    未命中时返回 False，交由注册表报「未知槽位」。
    """
    t = token.strip()
    if not t or " " in t or ":" in t:
        return False
    low = t.lower()
    if low.startswith("claude-"):
        return True
    if low.startswith("gpt-") or low.startswith("o1") or low.startswith("o3"):
        return True
    if len(t) >= 16 and all(c.isalnum() or c in "-_." for c in t):
        return True
    return False
