"""按 slot 单链路验证：每次只测一个 BYBOY_SLOT_*。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# 支持直接 ``python byboy/test/test_llmapi_chain.py`` 运行
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from byboy.llm.dispatcher import LLMDispatcher, RouteSpec
from byboy.packyapi.config import PackyConfig

PROMPT = "只回复一个字：好。不要其它内容。"

def _messages() -> list[dict[str, str]]:
    return [
        {"role": "system", "content": "你是简洁助手。"},
        {"role": "user", "content": PROMPT},
    ]


def _print_ok(name: str, detail: str = "") -> None:
    extra = f" {detail}" if detail else ""
    print(f"[OK] {name}{extra}")


def _print_fail(name: str, err: BaseException) -> None:
    print(f"[FAIL] {name}: {err}")


def _mask_key(v: str) -> str:
    s = (v or "").strip()
    if len(s) <= 8:
        return "*" * len(s)
    return f"{s[:4]}...{s[-4:]}"


def _used_client_info(disp: LLMDispatcher, slot: str, backend: str) -> tuple[str, str]:
    # 测试用途：读取 dispatcher 内部已选客户端，便于确认 slot 实际命中哪个 key/base
    norm = disp._normalize_slot_key(slot)  # type: ignore[attr-defined]
    if backend == "openai":
        cli = disp._route_openai_clients.get(norm) or disp._openai  # type: ignore[attr-defined]
    elif backend == "claude":
        cli = disp._route_claude_clients.get(norm) or disp._claude  # type: ignore[attr-defined]
    elif backend == "openai_vision":
        cli = disp._route_vision_openai_clients.get(norm) or disp._vision_openai  # type: ignore[attr-defined]
    else:
        cli = disp._route_vision_claude_clients.get(norm) or disp._vision_claude  # type: ignore[attr-defined]
    if cli is None:
        return ("<none>", "<none>")
    cfg = cli.config
    return (cfg.base_url, _mask_key(cfg.api_key))


def test_routing_local() -> None:
    """不访问网络：槽位 + 显式路由 + openai: / 裸模型 id 解析。"""
    from byboy.llm.registry import ModelSlotRegistry

    reg = ModelSlotRegistry(
        {
            "reasoning": "claude:claude-test-model",
            "code": "openai:gpt-code-model",
        }
    )
    disp = LLMDispatcher(
        routes={
            "legacy": RouteSpec(model="legacy-m", backend="openai"),
        },
        slot_registry=reg,
        default_route="reasoning",
        openai_client=None,
        claude_client=None,
    )
    assert disp.resolve("legacy").model == "legacy-m"
    assert disp.resolve("reasoning").model == "claude-test-model"
    assert disp.resolve("BYBOY_SLOT_REASONING").model == "claude-test-model"
    assert disp.resolve("code").backend == "openai"
    assert disp.resolve("BYBOY_SLOT_CODE").backend == "openai"
    assert disp.resolve("openai:gpt-4o-mini").model == "gpt-4o-mini"
    assert disp.resolve("openai_vision:gemini-2.5-flash-image").backend == "openai_vision"
    assert disp.resolve(None).model == "claude-test-model"
    disp2 = LLMDispatcher(
        routes={"x": RouteSpec(model="m", backend="claude")},
        default_route="x",
    )
    assert disp2.resolve("claude-3-5-haiku-20241022").backend == "claude"
    _print_ok("routing_local", "槽位/代号解析")


def test_config() -> PackyConfig:
    cfg = PackyConfig.from_env()
    if not cfg.api_key:
        raise RuntimeError(
            "未检测到 API Key，请设置 PACKY_API_KEY、OPENAI_API_KEY 或 ANTHROPIC_AUTH_TOKEN 等"
        )
    _print_ok(
        "PackyConfig",
        f"base_url={cfg.base_url!r} anthropic_base_url={cfg.anthropic_base_url!r}",
    )
    return cfg


def test_dispatcher_slot(slot: str, *, stream: bool) -> None:
    disp = LLMDispatcher.from_env()
    spec = disp.resolve(slot)
    base_url, api_key_masked = _used_client_info(disp, slot, spec.backend)
    _print_ok("resolve_slot", f"{slot} -> {spec.backend}:{spec.model}")
    _print_ok(
        "slot_runtime_config",
        f"model={spec.model!r} backend={spec.backend!r} base_url={base_url!r} api_key={api_key_masked}",
    )
    text = disp.complete(slot, _messages(), temperature=0, max_tokens=256)
    if not text.strip():
        raise RuntimeError(f"LLMDispatcher.complete({slot!r}) 返回空内容")
    _print_ok("LLMDispatcher.complete(slot)", repr(text[:120]))
    if stream:
        parts = list(disp.complete_stream(slot, _messages(), temperature=0, max_tokens=256))
        joined = "".join(parts).strip()
        if not joined:
            raise RuntimeError(f"LLMDispatcher.complete_stream({slot!r}) 返回空内容")
        _print_ok("LLMDispatcher.complete_stream(slot)", repr(joined[:120]))


def main() -> int:
    parser = argparse.ArgumentParser(description="Packy LLM slot 单链路透测")
    parser.add_argument(
        "--slot",
        default="BYBOY_SLOT_DEFAULT",
        help="只测试这一个链路代号（如 BYBOY_SLOT_FAST / BYBOY_SLOT_VISION）",
    )
    parser.add_argument(
        "--no-stream",
        action="store_true",
        help="跳过流式接口",
    )
    args = parser.parse_args()
    stream = not args.no_stream

    failed = 0
    try:
        test_routing_local()
    except Exception as e:
        failed += 1
        _print_fail("routing_local", e)

    try:
        test_config()
    except Exception as e:
        failed += 1
        _print_fail("PackyConfig", e)
    try:
        test_dispatcher_slot(args.slot, stream=stream)
    except Exception as e:
        failed += 1
        _print_fail("LLMDispatcher slot 链路", e)

    if failed:
        print(f"\n完成：{failed} 项失败")
        return 1
    print("\n全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
