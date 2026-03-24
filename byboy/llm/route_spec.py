from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Backend = Literal["claude", "openai"]
ChatMessage = dict[str, Any]


@dataclass
class RouteSpec:
    """单条路由：逻辑名 -> 模型与后端（默认 Claude / Anthropic 通道）。"""

    model: str
    backend: Backend = "claude"
    temperature: float | None = None
    max_tokens: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)
