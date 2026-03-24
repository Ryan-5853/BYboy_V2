from __future__ import annotations

import os
import sys
import time
import threading
from dataclasses import dataclass
from typing import Any

_RESET = "\033[0m"
_BOLD = "\033[1m"
_DIM = "\033[2m"
_BLUE = "\033[94m"
_CYAN = "\033[96m"
_GREEN = "\033[92m"
_YELLOW = "\033[93m"
_RED = "\033[91m"


def _use_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    return True


def _paint(text: str, color: str) -> str:
    if not _use_color():
        return text
    return f"{color}{text}{_RESET}"


def _now_hms() -> str:
    return time.strftime("%H:%M:%S")


@dataclass(slots=True)
class AgentLogger:
    agent: str

    def _emit(self, level: str, message: str, *, detail: str | None = None) -> None:
        level_color = {
            "START": _BLUE,
            "STEP": _CYAN,
            "INFO": _GREEN,
            "WARN": _YELLOW,
            "ERROR": _RED,
            "DONE": _GREEN,
        }.get(level, _CYAN)
        ts = _paint(_now_hms(), _DIM)
        tag = _paint(f"{self.agent}", _BOLD + _BLUE)
        lvl = _paint(f"[{level}]", level_color + _BOLD)
        line = f"{ts} {tag} {lvl} {message}"
        if detail:
            line += f" | {detail}"
        print(line, file=sys.stderr, flush=True)

    def start(self, message: str, *, detail: str | None = None) -> None:
        self._emit("START", message, detail=detail)

    def step(self, message: str, *, detail: str | None = None) -> None:
        self._emit("STEP", message, detail=detail)

    def info(self, message: str, *, detail: str | None = None) -> None:
        self._emit("INFO", message, detail=detail)

    def warn(self, message: str, *, detail: str | None = None) -> None:
        self._emit("WARN", message, detail=detail)

    def error(self, message: str, *, detail: str | None = None) -> None:
        self._emit("ERROR", message, detail=detail)

    def done(self, message: str, *, detail: str | None = None) -> None:
        self._emit("DONE", message, detail=detail)


def estimate_tokens(payload: Any) -> int:
    """粗略估算 tokens（用于日志观测，不用于计费/限额）。"""
    try:
        if isinstance(payload, str):
            n = len(payload)
        elif isinstance(payload, list):
            n = 0
            for x in payload:
                if isinstance(x, dict):
                    n += len(str(x.get("content", ""))) + len(str(x.get("role", ""))) + 8
                else:
                    n += len(str(x))
        elif isinstance(payload, dict):
            n = len(str(payload))
        else:
            n = len(str(payload))
    except Exception:
        n = 0
    # 经验估计：中文/英文混合场景，约 3~4 字符/token。
    return max(1, n // 4)


def log_llm_wait_start(
    log: AgentLogger,
    *,
    model: str,
    payload: Any,
    max_tokens: int,
    stage: str,
) -> float:
    prompt_toks = estimate_tokens(payload)
    log.step(
        f"已向模型{model}发送约{prompt_toks}tokens，等待响应中，0s",
        detail=f"stage={stage} max_tokens={max_tokens}",
    )
    return time.time()


def log_llm_wait_done(log: AgentLogger, *, stage: str, started_at: float) -> None:
    elapsed = max(0.0, time.time() - started_at)
    log.step("模型响应完成", detail=f"stage={stage} elapsed={elapsed:.1f}s")


def run_with_periodic_wait_log(
    *,
    log: AgentLogger,
    stage: str,
    wait_message: str,
    every_sec: float,
    fn: Any,
) -> Any:
    """在执行阻塞函数时，周期性输出等待时长日志。"""
    done = threading.Event()
    box: dict[str, Any] = {"value": None, "error": None}
    started = time.time()

    def _worker() -> None:
        try:
            box["value"] = fn()
        except Exception as e:  # pragma: no cover
            box["error"] = e
        finally:
            done.set()

    t = threading.Thread(target=_worker, daemon=True)
    t.start()

    tick = max(0.2, float(every_sec))
    while not done.wait(timeout=tick):
        elapsed = max(0.0, time.time() - started)
        log.step(wait_message, detail=f"stage={stage} elapsed={elapsed:.1f}s")

    if box["error"] is not None:
        raise box["error"]
    return box["value"]

