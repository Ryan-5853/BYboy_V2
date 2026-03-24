"""
验证 Firecrawl 云 API：``byboy.Firecrawl.FirecrawlClient``（v2：``/scrape``、``/map``、``/search`` 等）。

用法（在仓库根目录执行，且已安装依赖）::

    python -m byboy.test.test_firecrawl_api
    python -m byboy.test.test_firecrawl_api --only scrape
    python -m byboy.test.test_firecrawl_api --url https://example.com
    python -m byboy.test.test_firecrawl_api --only search --query "Firecrawl API"

环境变量（``FirecrawlConfig.from_env()`` 会经 ``byboy.env_loader`` 加载 ``.env``）::

    FIRECRAWL_API_KEY（必填）
    FIRECRAWL_BASE_URL（可选，默认 https://api.firecrawl.dev）
    FIRECRAWL_API_VERSION（可选，默认 v2）
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from byboy.env_loader import ensure_dotenv_loaded
from byboy.Firecrawl import FirecrawlAPIError, FirecrawlClient, FirecrawlConfig


def _print_ok(name: str, detail: str = "") -> None:
    extra = f" {detail}" if detail else ""
    print(f"[OK] {name}{extra}")


def _print_fail(name: str, err: BaseException) -> None:
    print(f"[FAIL] {name}: {err}")


def _mask_key(key: str) -> str:
    k = key.strip()
    if len(k) <= 8:
        return "(已设置)"
    return f"{k[:4]}…{k[-4:]}"


def test_config() -> FirecrawlConfig:
    ensure_dotenv_loaded()
    cfg = FirecrawlConfig.from_env()
    if not cfg.api_key:
        raise RuntimeError("未设置 FIRECRAWL_API_KEY，请配置 .env 或环境变量")
    _print_ok(
        "FirecrawlConfig",
        f"api_root={cfg.api_root()!r} key={_mask_key(cfg.api_key)}",
    )
    return cfg


def _require_success(resp: dict, *, stage: str) -> None:
    if resp.get("success") is False:
        raise RuntimeError(f"{stage} success=false: {resp.get('error') or resp}")


def _markdown_from_scrape(resp: dict) -> str:
    _require_success(resp, stage="scrape")
    data = resp.get("data") or {}
    md = data.get("markdown")
    if md is None or not str(md).strip():
        raise RuntimeError("scrape 响应中缺少非空 data.markdown")
    return str(md)


def test_scrape(client: FirecrawlClient, url: str) -> None:
    resp = client.scrape(
        url,
        formats=["markdown"],
        onlyMainContent=True,
    )
    md = _markdown_from_scrape(resp)
    preview = md.replace("\n", " ")[:160]
    _print_ok("scrape", f"len={len(md)} preview={preview!r}")


def test_map(client: FirecrawlClient, url: str) -> None:
    resp = client.map_site(url, limit=20)
    _require_success(resp, stage="map")
    links = resp.get("links")
    if links is None:
        # 部分部署返回 data.links
        data = resp.get("data")
        if isinstance(data, dict):
            links = data.get("links")
    n = len(links) if isinstance(links, list) else "?"
    _print_ok("map", f"links≈{n}")


def test_search(client: FirecrawlClient, query: str) -> None:
    resp = client.search(query, limit=3)
    _require_success(resp, stage="search")
    data = resp.get("data")
    _print_ok("search", f"keys={list(resp.keys())} data_type={type(data).__name__}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Firecrawl API 透测（byboy.Firecrawl）")
    parser.add_argument(
        "--only",
        choices=("all", "config", "scrape", "map", "search"),
        default="all",
        help="只跑指定阶段（默认 all；可先 config 确认环境）",
    )
    parser.add_argument(
        "--url",
        default="https://example.com",
        help="scrape / map 使用的 URL（默认 example.com）",
    )
    parser.add_argument(
        "--query",
        default="Firecrawl scrape API",
        help="search 使用的查询串",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=120.0,
        help="单次 HTTP 超时秒数（默认 120）",
    )
    args = parser.parse_args()
    ensure_dotenv_loaded()

    failed = 0
    cfg: FirecrawlConfig | None = None

    try:
        cfg = test_config()
    except Exception as e:
        failed += 1
        _print_fail("FirecrawlConfig", e)

    if args.only == "config":
        if failed:
            return 1
        print("\n全部通过")
        return 0

    if failed or cfg is None:
        return 1

    try:
        client = FirecrawlClient(cfg, timeout=args.timeout)
    except Exception as e:
        failed += 1
        _print_fail("FirecrawlClient", e)
        return 1

    if args.only in ("all", "scrape"):
        try:
            test_scrape(client, args.url)
        except FirecrawlAPIError as e:
            failed += 1
            _print_fail("scrape", e)
        except Exception as e:
            failed += 1
            _print_fail("scrape", e)

    if args.only in ("all", "map"):
        try:
            test_map(client, args.url)
        except FirecrawlAPIError as e:
            failed += 1
            _print_fail("map", e)
        except Exception as e:
            failed += 1
            _print_fail("map", e)

    if args.only in ("all", "search"):
        try:
            test_search(client, args.query)
        except FirecrawlAPIError as e:
            failed += 1
            _print_fail("search", e)
        except Exception as e:
            failed += 1
            _print_fail("search", e)

    if failed:
        print(f"\n完成：{failed} 项失败")
        return 1
    print("\n全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
