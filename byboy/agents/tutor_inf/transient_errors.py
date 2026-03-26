"""
识别 LLM 网关/模型侧暂时不可用（如渠道无实例、503），用于整任务安全重试。

断点续跑由各阶段 state 文件保证；此处只判断「是否值得整段重跑」。
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

import time

from byboy.agents.tutor_inf.logging_utils import AgentLogger
from byboy.llm.dispatcher import LLMDispatcher
from byboy.llm.registry import ModelSlotRegistry

_T = TypeVar("_T")


def _collect_exception_text(exc: BaseException) -> str:
    parts: list[str] = [str(exc)]
    body = getattr(exc, "body", None)
    if body is not None:
        parts.append(str(body))
    response = getattr(exc, "response", None)
    if response is not None:
        text = getattr(response, "text", None)
        if isinstance(text, str) and text.strip():
            parts.append(text)
    return "\n".join(parts)


def is_transient_llm_unavailable(exc: BaseException) -> bool:
    """
    是否为「稍后重试同一任务」类错误。

    覆盖 PackyAPI 返回的 model_not_found / 无可用渠道，以及常见网关 502/503/429。
    """
    if isinstance(exc, (KeyboardInterrupt, SystemExit)):
        return False

    text = _collect_exception_text(exc)
    lower = text.lower()

    # Packy：分组下模型无 distributor（与 503 常同时出现）
    if "model_not_found" in lower:
        return True
    if "无可用渠道" in text:
        return True

    status = getattr(exc, "status_code", None)
    if status is None:
        response = getattr(exc, "response", None)
        if response is not None:
            status = getattr(response, "status_code", None)
    if status in (502, 503, 429):
        return True

    try:
        import openai

        if isinstance(
            exc,
            (openai.APIConnectionError, openai.APITimeoutError, openai.RateLimitError),
        ):
            return True
    except Exception:
        pass

    try:
        import anthropic

        if isinstance(
            exc,
            (
                anthropic.APIConnectionError,
                anthropic.APITimeoutError,
            ),
        ):
            return True
        if hasattr(anthropic, "RateLimitError") and isinstance(
            exc,
            anthropic.RateLimitError,
        ):
            return True
    except Exception:
        pass

    try:
        import concurrent.futures

        if isinstance(exc, concurrent.futures.TimeoutError):
            return True
    except Exception:
        pass

    try:
        import httpx

        if isinstance(exc, httpx.TimeoutException):
            return True
    except Exception:
        pass

    return False


def partner_byboy_fast_slot(token: str) -> str | None:
    """
    若 ``token`` 为 FAST / FAST2 语义槽（含 ``BYBOY_SLOT_FAST``、``fast`` 等），
    返回配对的 ``BYBOY_SLOT_*`` 代号；否则返回 ``None``。
    """
    key = ModelSlotRegistry._normalize_slot_name(token)
    if key == "fast":
        return "BYBOY_SLOT_FAST2"
    if key == "fast2":
        return "BYBOY_SLOT_FAST"
    return None


def try_switch_fast_slot_pair(
    dispatcher: LLMDispatcher,
    slot_token: list[str],
    *,
    log: AgentLogger | None = None,
    enabled: bool = True,
) -> None:
    """
    在 ``BYBOY_SLOT_FAST`` / ``BYBOY_SLOT_FAST2`` 之间切换（若当前槽位属于该对）。

    ``slot_token`` 为单元素列表，成功时改写 ``slot_token[0]``。
    配对槽位未配置时保持原值并打日志。
    """
    if not enabled or not slot_token:
        return
    cur = slot_token[0].strip()
    nxt = partner_byboy_fast_slot(cur)
    if nxt is None or nxt == cur:
        return
    try:
        dispatcher.resolve(nxt)
    except KeyError:
        if log is not None:
            log.warn(
                "未能切换到配对 FAST 槽位（未配置或无法解析），保持当前槽位",
                detail=f"tried={nxt}",
            )
        return
    slot_token[0] = nxt
    if log is not None:
        log.step("瞬时故障：在 FAST / FAST2 槽位间切换", detail=f"{cur} -> {nxt}")


def run_with_transient_llm_retries(
    fn: Callable[[], _T],
    *,
    on_retry: Callable[[int, float, BaseException], None] | None = None,
    restart_on_transient_llm_error: bool = True,
    transient_retry_initial_sec: float = 15.0,
    transient_retry_max_sec: float = 120.0,
) -> _T:
    """
    执行 ``fn``；若抛出 :func:`is_transient_llm_unavailable` 为真的异常则等待后重试。

    ``on_retry(attempt, sleep_sec, exc)`` 在每次重试前调用（attempt 从 1 起）。
    """
    if not restart_on_transient_llm_error:
        return fn()

    wait_sec = max(1.0, float(transient_retry_initial_sec))
    cap = max(wait_sec, float(transient_retry_max_sec))
    attempt = 0
    while True:
        try:
            return fn()
        except BaseException as e:
            if not is_transient_llm_unavailable(e):
                raise
            attempt += 1
            if on_retry is not None:
                on_retry(attempt, wait_sec, e)
            time.sleep(wait_sec)
            wait_sec = min(wait_sec * 1.5, cap)
