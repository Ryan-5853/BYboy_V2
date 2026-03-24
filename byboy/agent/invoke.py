"""
Agent 调用契约：「模型引用」与「进入 LLM 的载荷」分离。

- ``ModelRef`` / ``AgentInvocation.model``：仅用于 ``LLMDispatcher.resolve``，不得写入用户消息。
- ``AgentInvocation.llm_part``：由 Agent 原样交给 ``complete*`` / ``acomplete*``。
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Sequence
from dataclasses import dataclass
from typing import Any, Generic, Protocol, TypeVar

from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.route_spec import ChatMessage

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class ModelRef:
    """分发模块认可的标记：槽位名、``openai:…`` / ``claude:…``、或裸 API 模型 id。"""

    token: str

    def __str__(self) -> str:
        return self.token


@dataclass(frozen=True, slots=True)
class AgentInvocation(Generic[T]):
    """单次 Agent 入口：本地路由信息 + 进入 LLM 的业务载荷。"""

    model: ModelRef
    llm_part: T


class LlmCallingAgent(Protocol[T]):
    """持有 ``ModelRef``，在需要时向 ``LLMDispatcher`` 要一次补全。"""

    def run(self, inv: AgentInvocation[T], dispatcher: LLMDispatcher) -> Any:
        ...


def agent_complete(
    dispatcher: LLMDispatcher,
    inv: AgentInvocation[Sequence[ChatMessage]],
    **kwargs: Any,
) -> str:
    return dispatcher.complete(inv.model.token, inv.llm_part, **kwargs)


async def agent_acomplete(
    dispatcher: LLMDispatcher,
    inv: AgentInvocation[Sequence[ChatMessage]],
    **kwargs: Any,
) -> str:
    return await dispatcher.acomplete(inv.model.token, inv.llm_part, **kwargs)


def agent_complete_stream(
    dispatcher: LLMDispatcher,
    inv: AgentInvocation[Sequence[ChatMessage]],
    **kwargs: Any,
) -> Iterator[str]:
    return dispatcher.complete_stream(inv.model.token, inv.llm_part, **kwargs)


async def agent_acomplete_stream(
    dispatcher: LLMDispatcher,
    inv: AgentInvocation[Sequence[ChatMessage]],
    **kwargs: Any,
) -> AsyncIterator[str]:
    async for part in dispatcher.acomplete_stream(inv.model.token, inv.llm_part, **kwargs):
        yield part
