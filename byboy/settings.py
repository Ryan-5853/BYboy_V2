"""
从环境变量（含 ``.env``）读取 LLM 路由与模型名。

与 ``PackyConfig`` 中的 Packy 网关地址、API Key 一起，构成完整配置面。
"""

from __future__ import annotations

import os
from dataclasses import replace

from byboy.env_loader import ensure_dotenv_loaded
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.local_deadline_retry import llm_local_deadline_config_from_env
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


def vision_model_from_env() -> str:
    ensure_dotenv_loaded()
    return (
        os.environ.get("BYBOY_VISION_MODEL")
        or os.environ.get("BYBOY_TEST_VISION_MODEL")
        or openai_model_from_env()
    ).strip()


def vision_backend_from_env() -> str:
    ensure_dotenv_loaded()
    raw = (os.environ.get("BYBOY_VISION_BACKEND") or "openai").strip().lower()
    if raw not in ("openai", "claude"):
        raise ValueError(
            "BYBOY_VISION_BACKEND 必须是 openai 或 claude，"
            f"当前为 {raw!r}"
        )
    return raw


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
    elif spec.backend == "claude":
        t_def = _parse_opt_float("BYBOY_CLAUDE_TEMPERATURE")
        m_def = _parse_opt_int("BYBOY_CLAUDE_MAX_TOKENS")
    else:
        t_def = _parse_opt_float("BYBOY_VISION_TEMPERATURE")
        m_def = _parse_opt_int("BYBOY_VISION_MAX_TOKENS")
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


def _vision_route_spec() -> RouteSpec:
    ensure_dotenv_loaded()
    backend = vision_backend_from_env()
    mapped_backend = "openai_vision" if backend == "openai" else "claude_vision"
    return RouteSpec(
        model=vision_model_from_env(),
        backend=mapped_backend,  # type: ignore[arg-type]
        temperature=_parse_opt_float("BYBOY_VISION_TEMPERATURE"),
        max_tokens=_parse_opt_int("BYBOY_VISION_MAX_TOKENS"),
    )


def slot_routes_from_env() -> dict[str, RouteSpec]:
    """
    读取 slot 模型配置（推荐）：
    - BYBOY_SLOT_<NAME>_MODEL=<backend:model 或裸模型id>

    兼容旧写法：
    - BYBOY_SLOT_<NAME>=<backend:model 或裸模型id>
    """
    ensure_dotenv_loaded()
    prefix = "BYBOY_SLOT_"
    out: dict[str, RouteSpec] = {}
    model_suffix = "_MODEL"
    # 新写法优先：BYBOY_SLOT_<NAME>_MODEL
    for k, v in os.environ.items():
        if not k.startswith(prefix) or not k.endswith(model_suffix):
            continue
        raw = str(v).strip()
        if not raw:
            continue
        slot = k[len(prefix) : -len(model_suffix)].lower()
        if not slot:
            continue
        out[slot] = parse_route_spec_token(raw)
    # 兼容旧写法：BYBOY_SLOT_<NAME>，并排除 *_MODEL / *_API_KEY / *_PACKY_*
    for k, v in os.environ.items():
        if not k.startswith(prefix):
            continue
        tail = k[len(prefix) :]
        if (
            tail.endswith("_MODEL")
            or tail.endswith("_API_KEY")
            or tail.endswith("_PACKY_API_KEY")
            or tail.endswith("_PACKY_BASE_URL")
            or tail.endswith("_PACKY_ANTHROPIC_BASE_URL")
            or tail.endswith("_HTTP_TIMEOUT")
        ):
            continue
        raw = str(v).strip()
        if not raw:
            continue
        slot = tail.lower()
        if not slot or slot in out:
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
    routes["vision"] = _vision_route_spec()
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
    if "vision" not in slots:
        slots["vision"] = routes["vision"]
    return routes, ModelSlotRegistry(slots)


def _slot_env_prefix(slot_name: str) -> str:
    return f"BYBOY_SLOT_{slot_name.strip().upper()}_"


def _base_v1(raw: str) -> str:
    r = raw.strip().rstrip("/")
    return r if r.endswith("/v1") else f"{r}/v1"


def _anthropic_root(raw: str) -> str:
    r = raw.strip().rstrip("/")
    return r[:-3].rstrip("/") if r.endswith("/v1") else r


def _slot_http_timeout_sec(slot_name: str) -> float | None:
    """
    槽位 HTTP 请求超时（秒）。环境变量：BYBOY_SLOT_<NAME>_HTTP_TIMEOUT

    单次 LLM 的墙钟控制见 ``BYBOY_LLM_LOCAL_DEADLINE_SEC``（``byboy.llm.local_deadline_retry``）。
    """
    prefix = _slot_env_prefix(slot_name)
    raw = (os.environ.get(prefix + "HTTP_TIMEOUT") or "").strip()
    if raw:
        v = float(raw)
        if v <= 0:
            raise ValueError(f"{prefix}HTTP_TIMEOUT 必须为正数秒，当前为 {raw!r}")
        return v
    return None


def _packy_floor_http_timeout_for_local(
    p: PackyConfig,
    local_deadline_sec: float | None,
) -> PackyConfig:
    """保证 httpx 读超时大于本地 deadline，由本地计时先触发放弃当前请求。"""
    if local_deadline_sec is None:
        return p
    floor = float(local_deadline_sec) + 90.0
    cur = p.http_timeout_sec
    if cur is not None and cur >= floor:
        return p
    return replace(p, http_timeout_sec=floor)


def _slot_route_packy_config(slot_name: str, fallback: PackyConfig) -> PackyConfig | None:
    """
    若槽位配置了独立 API Key，和/或需要独立 HTTP 超时，则返回专用 ``PackyConfig``。
    """
    key_cfg = _slot_specific_config(slot_name, fallback)
    timeout = _slot_http_timeout_sec(slot_name)
    if key_cfg is None:
        if timeout is None:
            return None
        return PackyConfig(
            api_key=fallback.api_key,
            base_url=fallback.base_url,
            anthropic_base_url=fallback.anthropic_base_url,
            http_timeout_sec=timeout,
        )
    if timeout is not None:
        return replace(key_cfg, http_timeout_sec=timeout)
    return key_cfg


def _slot_specific_config(slot_name: str, fallback: PackyConfig) -> PackyConfig | None:
    """
    每个 slot 独立 API Key（base 统一走全局 PACKY_BASE_URL）：
    - BYBOY_SLOT_<NAME>_API_KEY

    兼容旧名：
    - BYBOY_SLOT_<NAME>_PACKY_API_KEY
    """
    prefix = _slot_env_prefix(slot_name)
    api_key = (
        os.environ.get(prefix + "API_KEY")
        or os.environ.get(prefix + "PACKY_API_KEY")
        or ""
    ).strip()
    if not api_key:
        return None
    return PackyConfig(
        api_key=api_key,
        base_url=fallback.base_url,
        anthropic_base_url=fallback.anthropic_base_url,
    )


def llm_dispatcher_from_env(
    *,
    packy_config: PackyConfig | None = None,
    openai_client: PackyAPIClient | None = None,
    claude_client: PackyClaudeClient | None = None,
) -> LLMDispatcher:
    """构造分发器；支持 slot 独立 PACKY key/base，默认路由键为槽位 ``default``。"""
    cfg = packy_config or PackyConfig.from_env()
    vision_cfg = PackyConfig.from_vision_env()
    ldc = llm_local_deadline_config_from_env()
    cfg = _packy_floor_http_timeout_for_local(cfg, ldc.deadline_sec)
    vision_cfg = _packy_floor_http_timeout_for_local(vision_cfg, ldc.deadline_sec)
    routes, registry = _merged_slots_and_routes()
    slot_specs = registry.all_slots()

    route_openai_clients: dict[str, PackyAPIClient] = {}
    route_claude_clients: dict[str, PackyClaudeClient] = {}
    route_vision_openai_clients: dict[str, PackyAPIClient] = {}
    route_vision_claude_clients: dict[str, PackyClaudeClient] = {}

    for slot_name, spec in slot_specs.items():
        fallback = vision_cfg if spec.backend in ("openai_vision", "claude_vision") else cfg
        slot_cfg = _slot_route_packy_config(slot_name, fallback)
        if slot_cfg is None:
            continue
        slot_cfg = _packy_floor_http_timeout_for_local(slot_cfg, ldc.deadline_sec)
        if spec.backend == "openai":
            route_openai_clients[slot_name] = PackyAPIClient(slot_cfg)
        elif spec.backend == "claude":
            route_claude_clients[slot_name] = PackyClaudeClient(slot_cfg)
        elif spec.backend == "openai_vision":
            route_vision_openai_clients[slot_name] = PackyAPIClient(slot_cfg)
        else:
            route_vision_claude_clients[slot_name] = PackyClaudeClient(slot_cfg)

    return LLMDispatcher(
        routes=routes,
        slot_registry=registry,
        default_route="default",
        openai_client=openai_client or PackyAPIClient(cfg),
        claude_client=claude_client or PackyClaudeClient(cfg),
        vision_openai_client=PackyAPIClient(vision_cfg),
        vision_claude_client=PackyClaudeClient(vision_cfg),
        route_openai_clients=route_openai_clients,
        route_claude_clients=route_claude_clients,
        route_vision_openai_clients=route_vision_openai_clients,
        route_vision_claude_clients=route_vision_claude_clients,
        llm_local_deadline=ldc,
    )
