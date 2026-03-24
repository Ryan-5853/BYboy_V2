"""
从环境变量（含 ``.env``）读取 LLM 路由与模型名。

与 ``PackyConfig`` 中的 Packy 网关地址、API Key 一起，构成完整配置面。
"""

from __future__ import annotations

import os

from byboy.env_loader import ensure_dotenv_loaded
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.model_ref import parse_route_spec_token
from byboy.llm.registry import ModelSlotRegistry
from byboy.llm.route_spec import RouteSpec
from byboy.packyapi.claude import PackyClaudeClient
from byboy.packyapi.client import PackyAPIClient
from byboy.packyapi.config import PackyConfig


def _parse_opt_float(name: str) -> float | None:
    raw = os.environ.get(name)
    if raw is None or not str(raw).strip():
        return None
    return float(str(raw).strip())


def _parse_opt_int(name: str) -> int | None:
    raw = os.environ.get(name)
    if raw is None or not str(raw).strip():
        return None
    return int(str(raw).strip(), 10)


def _strip_optional_anthropic_prefix(model_id: str) -> str:
    s = model_id.strip()
    if s.startswith("anthropic/"):
        return s[len("anthropic/") :].lstrip()
    return s


def _legacy_model_from_env(*, prefer_analyst: bool) -> str | None:
    """
    旧 BYboy ``config.settings``：MODEL_ANALYST / MODEL_OPERATOR / MODEL；
    与 ``run_link_choose.py`` 优先级一致（analyst 路径用 MODEL_ANALYST 优先）。
    """
    ensure_dotenv_loaded()
    keys = (
        ("MODEL_ANALYST", "MODEL_OPERATOR", "MODEL")
        if prefer_analyst
        else ("MODEL_OPERATOR", "MODEL_ANALYST", "MODEL")
    )
    for key in keys:
        raw = (os.environ.get(key) or "").strip()
        if raw:
            return _strip_optional_anthropic_prefix(raw)
    return None


def openai_model_from_env() -> str:
    ensure_dotenv_loaded()
    explicit = (
        os.environ.get("BYBOY_OPENAI_MODEL")
        or os.environ.get("BYBOY_TEST_OPENAI_MODEL")
        or ""
    ).strip()
    if explicit:
        return explicit
    legacy = _legacy_model_from_env(prefer_analyst=False)
    if legacy:
        low = legacy.lower()
        if low.startswith("gpt-") or low.startswith("o1") or low.startswith("o3"):
            return legacy
    return "gpt-4o-mini"


def claude_model_from_env() -> str:
    ensure_dotenv_loaded()
    return _strip_optional_anthropic_prefix(
        (
            os.environ.get("BYBOY_CLAUDE_MODEL")
            or os.environ.get("BYBOY_TEST_CLAUDE_MODEL")
            or _legacy_model_from_env(prefer_analyst=True)
            or "claude-3-5-haiku-20241022"
        ).strip()
    )


def llm_default_route_from_env() -> str:
    ensure_dotenv_loaded()
    v = (os.environ.get("BYBOY_LLM_DEFAULT_ROUTE") or "claude").strip().lower()
    if v not in ("claude", "openai"):
        raise ValueError(
            "BYBOY_LLM_DEFAULT_ROUTE 必须是 claude 或 openai，"
            f"当前为 {v!r}"
        )
    return v


def route_spec_with_channel_defaults(spec: RouteSpec) -> RouteSpec:
    """把 ``BYBOY_OPENAI_*`` / ``BYBOY_CLAUDE_*`` 上的温度、max_tokens 合入 ``RouteSpec``。"""
    if spec.backend == "openai":
        t_def = _parse_opt_float("BYBOY_OPENAI_TEMPERATURE")
        m_def = _parse_opt_int("BYBOY_OPENAI_MAX_TOKENS")
    else:
        t_def = _parse_opt_float("BYBOY_CLAUDE_TEMPERATURE")
        m_def = _parse_opt_int("BYBOY_CLAUDE_MAX_TOKENS")
    return RouteSpec(
        model=spec.model,
        backend=spec.backend,
        temperature=spec.temperature if spec.temperature is not None else t_def,
        max_tokens=spec.max_tokens if spec.max_tokens is not None else m_def,
        extra=dict(spec.extra),
    )


def _channel_route_specs() -> dict[str, RouteSpec]:
    """底层 ``openai`` / ``claude`` 通道（仍可作为显式路由键使用）。"""
    ensure_dotenv_loaded()
    return {
        "openai": RouteSpec(
            model=openai_model_from_env(),
            backend="openai",
            temperature=_parse_opt_float("BYBOY_OPENAI_TEMPERATURE"),
            max_tokens=_parse_opt_int("BYBOY_OPENAI_MAX_TOKENS"),
        ),
        "claude": RouteSpec(
            model=claude_model_from_env(),
            backend="claude",
            temperature=_parse_opt_float("BYBOY_CLAUDE_TEMPERATURE"),
            max_tokens=_parse_opt_int("BYBOY_CLAUDE_MAX_TOKENS"),
        ),
    }


def slot_routes_from_env() -> dict[str, RouteSpec]:
    """读取 ``BYBOY_SLOT_<NAME>=openai:…`` / ``claude:…`` 等，NAME 转为小写槽位名。"""
    ensure_dotenv_loaded()
    prefix = "BYBOY_SLOT_"
    out: dict[str, RouteSpec] = {}
    for k, v in os.environ.items():
        if not k.startswith(prefix):
            continue
        raw = str(v).strip()
        if not raw:
            continue
        slot = k[len(prefix) :].lower()
        if not slot:
            continue
        out[slot] = parse_route_spec_token(raw)
    return out


def llm_routes_from_env() -> tuple[dict[str, RouteSpec], str]:
    """返回 ``(openai/claude 通道表, BYBOY_LLM_DEFAULT_ROUTE 通道键)``。兼容旧调用。"""
    return _channel_route_specs(), llm_default_route_from_env()


def _merged_slots_and_routes() -> tuple[dict[str, RouteSpec], ModelSlotRegistry]:
    """构造显式 ``routes`` 表与语义槽位注册表（含 default / reasoning / code / fast 默认值）。"""
    primary = llm_default_route_from_env()
    routes = _channel_route_specs()
    slots = slot_routes_from_env()
    for k, v in list(slots.items()):
        slots[k] = route_spec_with_channel_defaults(v)
    routes = {k: route_spec_with_channel_defaults(v) for k, v in routes.items()}
    if "default" not in slots:
        slots["default"] = routes["claude" if primary == "claude" else "openai"]
    for name, fb in (
        ("reasoning", "claude"),
        ("code", "openai"),
        ("fast", "openai"),
    ):
        if name not in slots:
            slots[name] = routes[fb]
    return routes, ModelSlotRegistry(slots)


def llm_dispatcher_from_env(
    *,
    packy_config: PackyConfig | None = None,
    openai_client: PackyAPIClient | None = None,
    claude_client: PackyClaudeClient | None = None,
) -> LLMDispatcher:
    """使用同一 ``PackyConfig`` 构造客户端；默认路由键为槽位 ``default``。"""
    cfg = packy_config or PackyConfig.from_env()
    routes, registry = _merged_slots_and_routes()
    return LLMDispatcher(
        routes=routes,
        slot_registry=registry,
        default_route="default",
        openai_client=openai_client or PackyAPIClient(cfg),
        claude_client=claude_client or PackyClaudeClient(cfg),
    )
