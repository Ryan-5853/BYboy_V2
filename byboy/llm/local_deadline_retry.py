"""
单次 LLM 调用的「本地墙钟」超时：到点即放弃当前请求（底层线程可能仍在跑），
sleep 后发起全新请求，直到成功。

不依赖远端是否遵守 HTTP read timeout；仍建议把 httpx 超时设得大于本地 deadline，
避免 HTTP 层抢先于本地计时结束。
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeoutError
from dataclasses import dataclass
from typing import Awaitable, Callable

from byboy.env_loader import ensure_dotenv_loaded

_LOG = logging.getLogger("byboy.llm.local_deadline")

_DEFAULT_DEADLINE_SEC = 300.0


@dataclass(frozen=True, slots=True)
class LlmLocalDeadlineConfig:
    deadline_sec: float | None
    retry_sleep_initial: float = 2.0
    retry_sleep_max: float = 60.0


def llm_local_deadline_config_from_env() -> LlmLocalDeadlineConfig:
    """
    - ``BYBOY_LLM_LOCAL_DEADLINE_SEC``：未设置时默认 300s；设为 0/off/false 则关闭本地超时重试。
    - ``BYBOY_LLM_LOCAL_RETRY_SLEEP_SEC``：超时后首次等待秒数，默认 2。
    - ``BYBOY_LLM_LOCAL_RETRY_SLEEP_MAX_SEC``：退避上限，默认 60。
    """
    ensure_dotenv_loaded()
    raw = (os.environ.get("BYBOY_LLM_LOCAL_DEADLINE_SEC") or "").strip()
    if not raw:
        deadline: float | None = _DEFAULT_DEADLINE_SEC
    else:
        low = raw.lower()
        if low in ("0", "off", "false", "no", "none", "disable", "disabled"):
            deadline = None
        else:
            v = float(raw)
            deadline = None if v <= 0 else v

    s0 = (os.environ.get("BYBOY_LLM_LOCAL_RETRY_SLEEP_SEC") or "").strip()
    initial = float(s0) if s0 else 2.0
    if initial <= 0:
        initial = 2.0

    sm = (os.environ.get("BYBOY_LLM_LOCAL_RETRY_SLEEP_MAX_SEC") or "").strip()
    cap = float(sm) if sm else 60.0
    if cap < initial:
        cap = initial

    return LlmLocalDeadlineConfig(
        deadline_sec=deadline,
        retry_sleep_initial=initial,
        retry_sleep_max=cap,
    )


def run_sync_call_with_deadline(fn: Callable[[], str], deadline_sec: float) -> str:
    """在独立线程中执行 ``fn``，主线程仅等待 ``deadline_sec``。"""
    ex = ThreadPoolExecutor(max_workers=1)
    try:
        fut = ex.submit(fn)
        return fut.result(timeout=deadline_sec)
    finally:
        ex.shutdown(wait=False)


async def run_async_call_with_deadline(
    coro_factory: Callable[[], Awaitable[str]],
    deadline_sec: float,
) -> str:
    """每次重试调用 ``coro_factory()`` 得到新的协程，再 ``wait_for``。"""
    return await asyncio.wait_for(coro_factory(), timeout=deadline_sec)


def run_sync_with_deadline_retries(
    fn: Callable[[], str],
    cfg: LlmLocalDeadlineConfig,
    *,
    what: str = "llm_complete",
) -> str:
    if cfg.deadline_sec is None:
        return fn()
    wait_sec = max(0.5, cfg.retry_sleep_initial)
    cap = max(wait_sec, cfg.retry_sleep_max)
    attempt = 0
    while True:
        attempt += 1
        try:
            return run_sync_call_with_deadline(fn, cfg.deadline_sec)
        except FuturesTimeoutError:
            _LOG.warning(
                "%s 本地超时 (%.1fs)，放弃当前请求，%.1fs 后重试 (attempt=%d)",
                what,
                cfg.deadline_sec,
                wait_sec,
                attempt,
            )
            time.sleep(wait_sec)
            wait_sec = min(wait_sec * 1.5, cap)


async def run_async_with_deadline_retries(
    coro_factory: Callable[[], Awaitable[str]],
    cfg: LlmLocalDeadlineConfig,
    *,
    what: str = "llm_acomplete",
) -> str:
    if cfg.deadline_sec is None:
        return await coro_factory()
    wait_sec = max(0.5, cfg.retry_sleep_initial)
    cap = max(wait_sec, cfg.retry_sleep_max)
    attempt = 0
    while True:
        attempt += 1
        try:
            return await run_async_call_with_deadline(coro_factory, cfg.deadline_sec)
        except asyncio.TimeoutError:
            _LOG.warning(
                "%s 本地超时 (%.1fs)，放弃当前请求，%.1fs 后重试 (attempt=%d)",
                what,
                cfg.deadline_sec,
                wait_sec,
                attempt,
            )
            await asyncio.sleep(wait_sec)
            wait_sec = min(wait_sec * 1.5, cap)
