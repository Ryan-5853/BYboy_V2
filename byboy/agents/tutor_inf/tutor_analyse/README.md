# TutorAnalyse Agent（单导师页全文结构化）

## 模块作用

- 处理单个导师主页：
  1. 若未提供 `markdown_path`，先调用 `web_clean` 抓取页面为 Markdown
  2. 调用 LLM 将 Markdown 全文结构化为 JSON
  3. 输出结果 JSON，同时在本包 `cache/` 保留 Markdown 缓存
- 支持信息质量判定（`suspect_no_text_info`），供视觉兜底链路判断是否需要切换策略。

## 入参 / 出参

### `TutorAnalysePayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `url` | `str` | 导师页 URL |
| `tutor_name_cn` | `str` | 导师中文名（上下文对齐） |
| `output_dir` | `str \| Path` | 结果 JSON 输出目录 |
| `output_filename` | `str` | 输出文件名 |
| `markdown_path` | `str \| Path \| None` | 可选，已抓取 Markdown 路径（提供后跳过抓取） |

### `run` / `arun` 参数

- `max_tokens`：结构化抽取，默认 `16384`
- `repair_max_tokens`：JSON 修复，默认 `32768`

### 返回值 `TutorAnalyseResult`

- `json_path`：输出 JSON 路径
- `markdown_cache_path`：本包缓存 Markdown 路径
- `suspect_no_text_info`：文本信息疑似不足标记（可为 `None`）

## 命令行

```bash
python -m byboy.agents.tutor_inf.tutor_analyse "https://example.edu/faculty/zhang" 张三 ./out zhang.json --route BYBOY_SLOT_DEFAULT --max-tokens 16384
```

可选：`--markdown-path`（使用已有 Markdown）

## 相关模块

- 上游编排：`byboy.agents.tutor_inf.get_tutor_analyse`
- 文本抓取：`byboy.agents.tutor_inf.web_clean`
- 视觉替代链路：`byboy.agents.tutor_inf.tutor_analyse_vision`
