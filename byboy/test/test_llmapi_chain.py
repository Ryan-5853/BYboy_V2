"""
验证 Packy LLM 链路：环境配置 → PackyAPIClient（OpenAI 兼容）/ PackyClaudeClient → LLMDispatcher。

用法（在仓库根目录执行，且已安装依赖）::

    python -m byboy.test.test_llmapi_chain
    python -m byboy.test.test_llmapi_chain --only openai
    python -m byboy.test.test_llmapi_chain --openai-model gpt-4o-mini --claude-model claude-sonnet-4-20250514

推荐在仓库根目录放置 ``.env``（可参考 ``.env.example``），由 ``byboy.env_loader`` 自动加载。

Packy 网关（``byboy.packyapi.config.PackyConfig``）::

    PACKY_API_KEY 或 OPENAI_API_KEY 等
    PACKY_BASE_URL（可选）
    PACKY_ANTHROPIC_BASE_URL（可选）

模型与默认路由（``byboy.settings``）::

    BYBOY_OPENAI_MODEL / BYBOY_CLAUDE_MODEL
    BYBOY_LLM_DEFAULT_ROUTE（决定 ``default`` 槽位用哪条通道）
    BYBOY_SLOT_<NAME>（语义槽位，如 BYBOY_SLOT_REASONING=claude:…）
    可选 BYBOY_*_TEMPERATURE、BYBOY_*_MAX_TOKENS

``LLMDispatcher.from_env()`` 的 ``default_route`` 为槽位 ``default``。兼容：BYBOY_TEST_* 模型名。
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

# 支持直接 ``python byboy/test/test_llmapi_chain.py`` 运行
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from byboy.llm.dispatcher import LLMDispatcher, RouteSpec
from byboy.packyapi.claude import PackyClaudeClient
from byboy.packyapi.client import PackyAPIClient
from byboy.packyapi.config import PackyConfig
from byboy.settings import claude_model_from_env, openai_model_from_env

PROMPT = "只回复一个字：好。不要其它内容。"


def _default_openai_model() -> str:
    return openai_model_from_env()


def _default_claude_model() -> str:
    return claude_model_from_env()


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
    assert disp.resolve("code").backend == "openai"
    assert disp.resolve("openai:gpt-4o-mini").model == "gpt-4o-mini"
    assert disp.resolve(None).model == "claude-test-model"
    disp2 = LLMDispatcher(
        routes={"x": RouteSpec(model="m", backend="claude")},
        default_route="x",
    )
    assert disp2.resolve("claude-3-5-haiku-20241022").backend == "claude"
    _print_ok("routing_local", "槽位 / 直连模型引用解析")


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


def test_openai_chain(model: str, *, stream: bool) -> None:
    client = PackyAPIClient()
    text = client.chat_completion(
        model=model,
        messages=_messages(),
        max_tokens=64,
        temperature=0,
    )
    if not text.strip():
        raise RuntimeError("OpenAI 兼容通道返回空内容")
    _print_ok("PackyAPIClient.chat_completion", repr(text[:120]))
    if stream:
        parts: list[str] = []
        for delta in client.chat_completion_stream(
            model=model,
            messages=_messages(),
            max_tokens=64,
            temperature=0,
        ):
            parts.append(delta)
        joined = "".join(parts).strip()
        if not joined:
            raise RuntimeError("OpenAI 兼容流式返回空内容")
        _print_ok("PackyAPIClient.chat_completion_stream", repr(joined[:120]))


async def test_openai_async(model: str) -> None:
    client = PackyAPIClient()
    text = await client.achat_completion(
        model=model,
        messages=_messages(),
        max_tokens=64,
        temperature=0,
    )
    if not text.strip():
        raise RuntimeError("异步 OpenAI 兼容通道返回空内容")
    _print_ok("PackyAPIClient.achat_completion", repr(text[:120]))


def test_claude_chain(model: str, *, stream: bool) -> None:
    client = PackyClaudeClient()
    text = client.messages_create(
        model=model,
        messages=_messages(),
        max_tokens=128,
        temperature=0,
    )
    if not text.strip():
        raise RuntimeError("Claude 通道返回空内容")
    _print_ok("PackyClaudeClient.messages_create", repr(text[:120]))
    if stream:
        parts: list[str] = []
        for delta in client.messages_stream(
            model=model,
            messages=_messages(),
            max_tokens=128,
            temperature=0,
        ):
            parts.append(delta)
        joined = "".join(parts).strip()
        if not joined:
            raise RuntimeError("Claude 流式返回空内容")
        _print_ok("PackyClaudeClient.messages_stream", repr(joined[:120]))


async def test_claude_async(model: str) -> None:
    client = PackyClaudeClient()
    text = await client.amessages_create(
        model=model,
        messages=_messages(),
        max_tokens=128,
        temperature=0,
    )
    if not text.strip():
        raise RuntimeError("异步 Claude 通道返回空内容")
    _print_ok("PackyClaudeClient.amessages_create", repr(text[:120]))


def test_dispatcher(
    openai_model: str,
    claude_model: str,
    *,
    stream: bool,
) -> None:
    disp = LLMDispatcher(
        routes={
            "openai": RouteSpec(model=openai_model, backend="openai"),
            "claude": RouteSpec(model=claude_model, backend="claude"),
        },
        default_route="claude",
        openai_client=PackyAPIClient(),
        claude_client=PackyClaudeClient(),
    )
    for key in ("openai", "claude"):
        text = disp.complete(key, _messages(), temperature=0, max_tokens=128)
        if not text.strip():
            raise RuntimeError(f"LLMDispatcher.complete({key!r}) 返回空内容")
        _print_ok(f"LLMDispatcher.complete({key!r})", repr(text[:120]))
    if stream:
        for key in ("openai", "claude"):
            parts = list(disp.complete_stream(key, _messages(), temperature=0, max_tokens=128))
            joined = "".join(parts).strip()
            if not joined:
                raise RuntimeError(f"LLMDispatcher.complete_stream({key!r}) 返回空内容")
            _print_ok(f"LLMDispatcher.complete_stream({key!r})", repr(joined[:120]))


async def test_dispatcher_async(openai_model: str, claude_model: str) -> None:
    disp = LLMDispatcher(
        routes={
            "openai": RouteSpec(model=openai_model, backend="openai"),
            "claude": RouteSpec(model=claude_model, backend="claude"),
        },
        default_route="claude",
        openai_client=PackyAPIClient(),
        claude_client=PackyClaudeClient(),
    )
    for key in ("openai", "claude"):
        text = await disp.acomplete(key, _messages(), temperature=0, max_tokens=128)
        if not text.strip():
            raise RuntimeError(f"LLMDispatcher.acomplete({key!r}) 返回空内容")
        _print_ok(f"LLMDispatcher.acomplete({key!r})", repr(text[:120]))


def main() -> int:
    parser = argparse.ArgumentParser(description="Packy LLM API 链路透测")
    parser.add_argument(
        "--only",
        choices=("all", "config", "openai", "claude", "dispatcher", "routing"),
        default="all",
        help="只跑指定阶段（默认 all；routing 不访问 API）",
    )
    parser.add_argument(
        "--openai-model",
        default=None,
        help="OpenAI 兼容通道模型（默认读 BYBOY_OPENAI_MODEL / BYBOY_TEST_OPENAI_MODEL 或 gpt-4o-mini）",
    )
    parser.add_argument(
        "--claude-model",
        default=None,
        help="Claude 通道模型（默认读 BYBOY_CLAUDE_MODEL / BYBOY_TEST_CLAUDE_MODEL 或 haiku 默认）",
    )
    parser.add_argument(
        "--no-stream",
        action="store_true",
        help="跳过流式接口",
    )
    parser.add_argument(
        "--no-async",
        action="store_true",
        help="跳过异步接口",
    )
    args = parser.parse_args()
    openai_model = args.openai_model or _default_openai_model()
    claude_model = args.claude_model or _default_claude_model()
    stream = not args.no_stream
    run_async = not args.no_async

    failed = 0

    if args.only in ("all", "routing"):
        try:
            test_routing_local()
        except Exception as e:
            failed += 1
            _print_fail("routing_local", e)
        if args.only == "routing":
            return 1 if failed else 0

    try:
        if args.only in ("all", "config"):
            test_config()
    except Exception as e:
        failed += 1
        _print_fail("PackyConfig", e)
        if args.only == "config":
            return 1

    if args.only in ("all", "openai"):
        try:
            test_openai_chain(openai_model, stream=stream)
            if run_async:
                asyncio.run(test_openai_async(openai_model))
        except Exception as e:
            failed += 1
            _print_fail("OpenAI 兼容链路", e)

    if args.only in ("all", "claude"):
        try:
            test_claude_chain(claude_model, stream=stream)
            if run_async:
                asyncio.run(test_claude_async(claude_model))
        except Exception as e:
            failed += 1
            _print_fail("Claude 链路", e)

    if args.only in ("all", "dispatcher"):
        try:
            test_dispatcher(openai_model, claude_model, stream=stream)
            if run_async:
                asyncio.run(test_dispatcher_async(openai_model, claude_model))
        except Exception as e:
            failed += 1
            _print_fail("LLMDispatcher 链路", e)

    if failed:
        print(f"\n完成：{failed} 项失败")
        return 1
    print("\n全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
