# LinkChoose Agent（Markdown 链接分类）

## 模块作用

- 输入为 `web_clean` 产出的 Markdown 页面（或任意同格式 Markdown）。
- 提取页面中的可点击链接，并输出统一分类结果：
  - `category`: `tutor_profile` / `tutor_expansion` / `irrelevant`
  - `category_confidence`: `high` / `medium` / `low`
  - `scope`: `internal` / `external` / `unknown`
- 将结果写入单个 `.json` 文件，供 `get_tutor_pages` 后续迭代使用。

## 依赖与环境变量

该 Agent 会调用 LLM 路由，需与项目其它 LLM 模块共享配置：

| 变量 | 说明 |
|------|------|
| `PACKY_API_KEY`、`PACKY_BASE_URL`、`PACKY_ANTHROPIC_BASE_URL` | 网关与通道配置 |
| `BYBOY_OPENAI_MODEL`、`BYBOY_CLAUDE_MODEL` | 默认模型 |
| `BYBOY_LLM_DEFAULT_ROUTE`、`BYBOY_SLOT_*` | 路由/槽位映射 |

建议输入 Markdown 首行包含 `> 抓取来源：<url>`（由 `web_clean` 默认写入），便于内外链判断。

## 入参 / 出参

### `LinkChoosePayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `markdown_path` | `str \| Path` | 输入 Markdown 文件路径 |
| `output_dir` | `str \| Path` | 输出目录 |
| `output_filename` | `str` | 输出 JSON 文件名，必须 `.json` 结尾 |

### `run` / `arun` 参数

- `max_tokens`：默认 `8192`
- `repair_max_tokens`：默认 `32768`（JSON 修复阶段）

### 返回值

- `Path`：输出 JSON 的绝对路径。

### 输出 JSON 关键字段

| 键 | 类型 | 说明 |
|----|------|------|
| `meta` | `object` | 输入与来源信息（如 `declared_source_url`、`page_host`） |
| `clickable_links` | `array` | 每项含 `url`、`anchor_text`、`scope`、`category`、`category_confidence`、`category_reason`、`guessed_target_content` |

## 命令行

```bash
python -m byboy.agents.tutor_inf.link_choose path/to/page.md ./out links.json --route BYBOY_SLOT_DEFAULT --max-tokens 8192
```

位置参数：`markdown_path`、`output_dir`、`output_filename`  
可选参数：`--route`、`--max-tokens`

## 调用示例

```python
from pathlib import Path
from byboy.agent.invoke import AgentInvocation, ModelRef
from byboy.agents.tutor_inf.link_choose import LinkChooseAgent, LinkChoosePayload
from byboy.llm.dispatcher import LLMDispatcher

dispatcher = LLMDispatcher.from_env()
out = LinkChooseAgent().run(
    AgentInvocation(
        model=ModelRef("BYBOY_SLOT_DEFAULT"),
        llm_part=LinkChoosePayload(
            markdown_path=Path("./cache/cleaned/page.md"),
            output_dir=Path("./cache/choice"),
            output_filename="page.choice.json",
        ),
    ),
    dispatcher,
)
print(out)
```

## 相关模块

- 上游：`byboy.agents.tutor_inf.web_clean`
- 下游：`byboy.agents.tutor_inf.get_tutor_pages`
