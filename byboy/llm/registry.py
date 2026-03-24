"""语义槽位（推理、代码等）→ ``RouteSpec``，供 ``LLMDispatcher`` 做本地解析。"""

from __future__ import annotations

from collections.abc import Mapping

from byboy.llm.route_spec import RouteSpec
from byboy.llm.model_ref import looks_like_api_model_id, parse_route_spec_token


class ModelSlotRegistry:
    """
    分发模块认可的「模型标注」表：键为槽位名（小写），值为固定 ``RouteSpec``。

    解析顺序在 ``LLMDispatcher.resolve`` 中：显式 ``routes`` 表优先，再到本注册表槽位，
    再到 ``openai:…`` / ``claude:…`` / 裸模型 id。
    """

    __slots__ = ("_slots",)

    def __init__(self, slots: Mapping[str, RouteSpec | str] | None = None) -> None:
        self._slots: dict[str, RouteSpec] = {}
        if slots:
            for name, spec in slots.items():
                self.set_slot(name, spec)

    def set_slot(self, name: str, spec: RouteSpec | str) -> None:
        key = name.strip().lower()
        if isinstance(spec, str):
            self._slots[key] = parse_route_spec_token(spec.strip())
        else:
            self._slots[key] = spec

    def get_slot(self, name: str) -> RouteSpec | None:
        return self._slots.get(name.strip().lower())

    def resolve_adhoc(self, token: str) -> RouteSpec | None:
        """
        在已排除 ``routes`` 显式表项之后，尝试解析 ``token``。

        返回 None 表示既非已知槽位，也非可解析的直连模型引用。
        """
        t = token.strip()
        if not t:
            return None
        hit = self.get_slot(t)
        if hit is not None:
            return hit
        if ":" in t:
            return parse_route_spec_token(t)
        if looks_like_api_model_id(t):
            return parse_route_spec_token(t)
        return None

    def all_slots(self) -> dict[str, RouteSpec]:
        return dict(self._slots)
