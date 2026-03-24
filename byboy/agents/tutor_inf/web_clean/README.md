# WebClean Agent（网页转 Markdown）

## 模块作用

- 通过 **Firecrawl v2** `POST /v2/scrape` 将指定 **http(s) URL** 抓取并转为 **Markdown**。
- **不调用 LLM**；仍使用项目统一的 `AgentInvocation` 形态，便于与 `LLMDispatcher`、其它 Agent 编排一致。
- 写入磁盘的 Markdown **正文前**会固定插入一行引用块声明源 URL（与下游 `link_choose` 约定一致）：

  `> 抓取来源：<url>`

## 依赖与环境变量

| 变量 | 说明 |
|------|------|
| `FIRECRAWL_API_KEY` | 必填，Firecrawl Bearer Token |
| `FIRECRAWL_BASE_URL` | 可选，默认 `https://api.firecrawl.dev`（不含路径，实际请求 `{BASE}/v2/scrape`） |

应用会通过 `byboy.env_loader.ensure_dotenv_loaded()` 加载 `.env`（若存在）。

## 调用流程

1. 构造 `LLMDispatcher`（任意能 `resolve(model_token)` 的实例即可；本 Agent **不会**调用 `complete*`）。
2. 构造 `AgentInvocation(model=ModelRef(路由键), llm_part=WebCleanPayload(...))`。
3. 调用 `WebCleanAgent().run(inv, dispatcher)` 或 `await WebCleanAgent().arun(inv, dispatcher)`。
4. 内部：`dispatcher.resolve(inv.model.token)` → `scrape_url_to_markdown(url)` → 拼接来源声明 → 写入 `output_dir / output_filename`。
5. 返回值为输出文件的 **`Path`**。

与 **LinkChoose** 串联时：先用本模块得到 `.md`，再将该路径作为 LinkChoose 的 `markdown_path`。

## 入参 / 出参（接口）

### `WebCleanPayload`（即 `AgentInvocation.llm_part`）

| 字段 | 类型 | 说明 |
|------|------|------|
| `url` | `str` | 待抓取的 http(s) URL |
| `output_dir` | `str \| Path` | 输出目录（不存在会创建） |
| `output_filename` | `str` | 输出文件名，如 `page.md` |

### `AgentInvocation.model`（`ModelRef`）

- **仅用于** `dispatcher.resolve(token)`，校验路由键合法；**不得**当作模型传给 Firecrawl。
- `token` 可为槽位名（如 `default`）、或 `openai:…` / `claude:…` 等分发器认可的键（见 `LLMDispatcher.resolve`）。

### 返回值

- `Path`：写入后的 Markdown 绝对路径。

### 直接工具函数（可选）

- `scrape_url_to_markdown(url, ...)`：只调 Firecrawl，返回**原始** Markdown 字符串（**不含**来源声明行）。
- `firecrawl_api_key_from_env()` / `firecrawl_base_url_from_env()`：读取环境变量。

### 异常

- `FirecrawlError`：HTTP/网络/JSON/业务 `success=false`/缺 `markdown` 等。
- `ValueError`：非法 URL 或空 `output_filename`。

## 代码示例

```python
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.web_clean import WebCleanAgent, WebCleanPayload
from byboy.llm.dispatcher import LLMDispatcher

dispatcher = LLMDispatcher.from_env()
agent = WebCleanAgent()
out = agent.run(
    AgentInvocation(
        model=ModelRef("default"),
        llm_part=WebCleanPayload(
            url="https://example.com/faculty",
            output_dir=Path("./out_md"),
            output_filename="page.md",
        ),
    ),
    dispatcher,
)
print(out)
```

## 相关模块

- 下游链接分类：`byboy.agents.tutor_inf.link_choose`（读取本模块产出的 `.md`）。
