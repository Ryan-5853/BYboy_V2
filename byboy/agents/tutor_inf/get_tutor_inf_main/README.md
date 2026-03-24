# GetTutorInfMain Agent（导师信息主流程）

## 模块作用

- 统一编排完整链路：
  1. `get_tutor_pages`：抓页面并迭代发现导师主页
  2. `get_tutor_analyse`：批量结构化导师页
  3. `output_to_csv`：抽取固定字段并汇总 CSV
- 面向“一次命令跑全流程”的入口。

## 入参 / 出参

### `GetTutorInfMainPayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `academy_url` | `str` | 学院入口 URL |
| `workdir` | `str \| Path` | 工作目录 |
| `max_depth` | `int` | 抓取最大轮数，默认 `2` |
| `pages_resume_state_path` | `str \| Path \| None` | `get_tutor_pages` 恢复点 |
| `analysed_subdir` | `str` | 分析输出子目录，默认 `cache/analysed` |
| `csv_path` | `str \| Path \| None` | 汇总 CSV 路径 |
| `csv_resume_state_path` | `str \| Path \| None` | CSV 阶段恢复状态 |
| `csv_run_log_path` | `str \| Path \| None` | CSV 运行日志 JSONL |

### `run` / `arun` 参数

- `pages_max_tokens`（默认 `8192`）
- `analyse_max_tokens`（默认 `16384`）
- `csv_max_tokens`（默认 `2048`）
- `csv_repair_max_tokens`（默认 `4096`）

### 返回值 `GetTutorInfMainResult`

- `workdir`
- `pages_result`
- `analyse_result`
- `csv_result`

## 命令行

```bash
python -m byboy.agents.tutor_inf.get_tutor_inf_main "https://example.edu/college" --workdir ./byboy/test/get_tutor_pages_kzgc --slot BYBOY_SLOT_DEFAULT --depth 2 --pages-max-tokens 8192 --analyse-max-tokens 16384 --csv-max-tokens 2048 --csv-repair-max-tokens 4096
```

## 相关模块

- `byboy.agents.tutor_inf.get_tutor_pages`
- `byboy.agents.tutor_inf.get_tutor_analyse`
- `byboy.agents.tutor_inf.output_to_csv`
