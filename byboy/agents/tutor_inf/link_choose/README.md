# LinkChoose Agent（Markdown 链接分类）

## 模块作用

- 输入为 **WebClean**（或其它工具）产出的 **Markdown 整页正文**（链接以 `[文本](url)` 等形式保留）。
- 调用 **LLM**（经 `LLMDispatcher` → Packy 上 OpenAI 兼容或 Claude），将链接分为两类：
  - **`tutor_homepage_links`**：指向具体导师个人主页/简介的链接；
  - **`iteration_links`**：同校/同院体系内、抓取后**更可能扩展出更多导师或分页**的站内导航类链接。
- 将模型输出的 JSON 与元数据一并写入指定 **JSON 文件**。

系统提示词要求模型**只输出一个 JSON 对象**（无 Markdown 代码块、无前后说明文字）。

## 依赖与环境变量

LinkChoose 依赖 **Packy** 网关与 BYboy 路由配置，与项目其它 LLM 调用相同，例如：

| 变量 | 说明 |
|------|------|
| `PACKY_API_KEY`、`PACKY_BASE_URL`、`PACKY_ANTHROPIC_BASE_URL` | Packy 客户端 |
| `BYBOY_OPENAI_MODEL`、`BYBOY_CLAUDE_MODEL` | 各通道默认模型 |
| `BYBOY_LLM_DEFAULT_ROUTE` | `claude` 或 `openai`，影响 `default` 槽位回退 |
| `BYBOY_SLOT_*` | 语义槽位，如 `BYBOY_SLOT_DEFAULT=claude:…` |

详见仓库根目录 `.env.example` 与 `byboy.settings`。

**建议** Markdown 由 `web_clean` 生成，以便首行存在 `> 抓取来源：URL`，供模型判断站内/站外；若无该行，Agent 仍运行，但 `meta.declared_source_url` 为 `null`。

## 调用流程

1. 构造 `LLMDispatcher.from_env()`（或等价注入 OpenAI/Claude 客户端与路由表）。
2. 构造 `AgentInvocation(model=ModelRef(路由键), llm_part=LinkChoosePayload(...))`。
3. 调用 `LinkChooseAgent().run(inv, dispatcher, max_tokens=8192)` 或 `await ...arun(...)`。
4. 内部：`resolve` → 读入 Markdown → 解析可选来源声明 → 组装 `system` + `user` 消息 → `agent_complete` → 解析 JSON → 校验字段 → 写入 JSON。
5. 返回值为输出文件的 **`Path`**。

### 与 WebClean 的典型流水线

`URL` → **WebClean** → `page.md` → **LinkChoose** → `links.json`。

## 入参 / 出参（接口）

### `LinkChoosePayload`（即 `AgentInvocation.llm_part`）

| 字段 | 类型 | 说明 |
|------|------|------|
| `markdown_path` | `str \| Path` | 已存在的 Markdown 文件路径 |
| `output_dir` | `str \| Path` | JSON 输出目录 |
| `output_filename` | `str` | 输出文件名，如 `result.json` |

### `AgentInvocation.model`（`ModelRef`）

- 用于选择 **LLM 路由**（如 `default`、`reasoning`，或 `openai:模型id` / `claude:模型id`），与 `LLMDispatcher.resolve` 规则一致。

### `run` / `arun` 额外参数

- `max_tokens`：默认 `8192`，传入底层补全调用。

### 输出 JSON 结构（写入磁盘）

根对象字段：

| 键 | 类型 | 说明 |
|----|------|------|
| `meta` | `object` | `markdown_path`、`declared_source_url`（来自首行声明，无则为 `null`）、`page_host`（从声明 URL 解析的 host，无则为 `null`） |
| `tutor_homepage_links` | `array` | 导师主页链接对象列表（字段由模型按系统提示填充，如 `url`、`anchor_text`、`tutor_name` 等） |
| `iteration_links` | `array` | 可迭代扩展链接对象列表 |
| `debug` | `object` | 至少含 `notes`、`suspicions` 字符串数组（由系统提示约束） |

### 辅助 API

- `parse_llm_json_object(text)`：从模型原文中剥离可选 \`\`\`json 围栏后 `json.loads`，根须为对象。

### 异常

- `FileNotFoundError`：Markdown 路径不是文件。
- `LinkChooseError`：非合法 JSON、缺键、类型不符等。
- `KeyError`：路由键无法解析（来自 `dispatcher.resolve`）。

## 命令行

在仓库根目录、已配置 `.env`：

```bash
python -m byboy.agents.tutor_inf.link_choose path/to/page.md ./out links.json --route default
```

参数：`markdown_path`、`output_dir`、`output_filename`；可选 `--route`、`--max-tokens`。

## 代码示例

```python
from pathlib import Path

from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.link_choose import LinkChooseAgent, LinkChoosePayload
from byboy.llm.dispatcher import LLMDispatcher

dispatcher = LLMDispatcher.from_env()
agent = LinkChooseAgent()
out = agent.run(
    AgentInvocation(
        model=ModelRef("default"),
        llm_part=LinkChoosePayload(
            markdown_path=Path("./out_md/page.md"),
            output_dir=Path("./out_json"),
            output_filename="links.json",
        ),
    ),
    dispatcher,
    max_tokens=8192,
)
print(out)
```

## 相关模块

- 上游网页转 Markdown：`byboy.agents.tutor_inf.web_clean`。
- 通用调用契约：`byboy.agent.invoke`（`AgentInvocation`、`ModelRef`、`agent_complete` 等）。
