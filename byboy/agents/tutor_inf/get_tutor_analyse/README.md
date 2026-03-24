# GetTutorAnalyse Agent（批量导师页分析）

## 模块作用

- 读取 `get_tutor_pages` 产出的工作区：
  - `cache/state.json`
  - `cache/cleaned/*.md`
- 对 `list2_tutor_profiles` 中尚未分析的导师页逐个调用 `tutor_analyse`。
- 输出到 `cache/analysed/*.json`（可配置子目录），并写 `manifest.json` 汇总结果。
- 每成功一页会即时回写 `state.json` 的 `list4_analysed_profiles`，支持中断恢复。

## 入参 / 出参

### `GetTutorAnalysePayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `workspace_dir` | `str \| Path` | `get_tutor_pages` 工作目录 |
| `analysed_subdir` | `str` | 输出子目录，默认 `cache/analysed` |

### `run` / `arun` 参数

- `max_tokens`：传给 `tutor_analyse` 的 token 上限，默认 `16384`。

### 返回值 `GetTutorAnalyseResult`

- `workspace_dir`
- `analysed_dir`
- `manifest_path`
- `success_count`
- `skipped_count`

## 命令行

```bash
python -m byboy.agents.tutor_inf.get_tutor_analyse ./byboy/test/get_tutor_pages_kzgc --route BYBOY_SLOT_DEFAULT --max-tokens 16384 --analysed-subdir cache/analysed
```

## 依赖

- 依赖 `state.json` 中的 `list2_tutor_profiles` 与 `records[*].cleaned_file`。
- 依赖 `tutor_analyse` 进行单页结构化抽取。

## 相关模块

- 上游：`byboy.agents.tutor_inf.get_tutor_pages`
- 下游：`byboy.agents.tutor_inf.output_to_csv`
