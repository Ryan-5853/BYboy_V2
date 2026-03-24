# WebClean Agent（网页转 Markdown）

## 模块作用

- 调用 Firecrawl `POST /v2/scrape`，将 `http(s)` 页面转换为 Markdown。
- 不调用 LLM，但仍走统一的 `AgentInvocation` / `ModelRef` 入口，便于与其他 agent 编排。
- 输出 Markdown 时会在首行插入来源声明：
  - `> 抓取来源：<url>`

## 依赖与环境变量

| 变量 | 说明 |
|------|------|
| `FIRECRAWL_API_KEY` | 必填，Firecrawl Token |
| `FIRECRAWL_BASE_URL` | 可选，默认 `https://api.firecrawl.dev` |

## 入参 / 出参

### `WebCleanPayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `url` | `str` | 待抓取 URL（仅支持 `http/https`） |
| `output_dir` | `str \| Path` | 输出目录 |
| `output_filename` | `str` | 输出文件名，必须 `.md` 结尾 |

### 返回值

- `Path`：生成的 Markdown 文件路径。

### 关键函数

- `scrape_url_to_markdown(...)`：仅返回 Firecrawl 原始 Markdown（不含来源声明行）。
- `firecrawl_api_key_from_env()` / `firecrawl_base_url_from_env()`：读取并校验环境变量。

## 调用链路

`URL` -> `web_clean` -> `cache/cleaned/*.md` -> `link_choose` / `tutor_analyse`

## 代码示例

```python
from pathlib import Path
from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.web_clean import WebCleanAgent, WebCleanPayload
from byboy.llm.dispatcher import LLMDispatcher

dispatcher = LLMDispatcher.from_env()
out = WebCleanAgent().run(
    AgentInvocation(
        model=ModelRef("BYBOY_SLOT_DEFAULT"),
        llm_part=WebCleanPayload(
            url="https://example.edu/faculty",
            output_dir=Path("./cache/cleaned"),
            output_filename="00001_xxx_cleaned.md",
        ),
    ),
    dispatcher,
)
print(out)
```

## 异常

- `FirecrawlError`：请求失败、响应非法或缺少 `markdown`。
- `ValueError`：URL 非法、输出文件名非法等。
