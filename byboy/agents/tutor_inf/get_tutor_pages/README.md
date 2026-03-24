# GetTutorPages Agent（导师页面抓取编排）

## 模块作用

- 以学院入口页为起点，维护 3 个 URL 列表并迭代抓取：
  - `list1_possible_pages`：待处理页面
  - `list2_tutor_profiles`：识别出的导师主页
  - `list3_processed_pages`：已处理页面
- 每轮将页面交给 `web_clean` 生成 Markdown，再交给 `link_choose` 分类链接。
- 将过程状态持久化到 `cache/state.json`，支持断点恢复。

## 目录与状态文件

默认以 `output_dir` 为根，生成：

- `cache/cleaned/`：网页清洗后的 Markdown
- `cache/choice/`：每页链接分类 JSON
- `cache/state.json`：迭代状态（核心恢复点）

## 入参 / 出参

### `GetTutorPagesPayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `academy_url` | `str` | 学院入口 URL |
| `output_dir` | `str \| Path` | 工作目录 |
| `max_depth` | `int` | 最大迭代轮数，默认 `2` |
| `resume_state_path` | `str \| Path \| None` | 可选，已有 `state.json` 路径 |

### `run` / `arun` 参数

- `max_tokens`：传给 `link_choose` 的 token 上限，默认 `8192`。

### 返回值 `GetTutorPagesResult`

- `output_dir`、`cache_dir`、`cleaned_dir`、`choice_dir`、`state_path`
- `round_count`
- `list1_pending_count`、`list2_tutor_profile_count`、`list3_processed_count`

## 命令行

```bash
python -m byboy.agents.tutor_inf.get_tutor_pages "https://example.edu/college" --workdir ./byboy/test/get_tutor_pages_kzgc --depth 2 --route BYBOY_SLOT_DEFAULT --max-tokens 8192
```

常用参数：`--workdir`、`--depth`、`--route`、`--max-tokens`、`--resume-state`

## 相关模块

- 上游调用：`byboy.agents.tutor_inf.get_tutor_inf_main`
- 子步骤：`byboy.agents.tutor_inf.web_clean`、`byboy.agents.tutor_inf.link_choose`
