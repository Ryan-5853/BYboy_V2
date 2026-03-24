# OutputToCsv Agent（分析 JSON 汇总为 CSV）

## 模块作用

- 读取 `analysed/*.json`（结构可能不一致），调用 LLM 抽取固定字段。
- 按统一表头写入/更新 CSV，并通过状态文件实现增量执行与恢复。
- 当模型返回非合法 JSON 时，触发 JSON 修复阶段再解析。

## 固定表头

`学校`、`院系`、`导师姓名`、`性别`、`年龄`、`所属实验室`、`研究方向`、`招生指标`、`招生要求`、`联系方式`、`邮箱`、`地址`、`教育背景`、`职称`、`荣誉`、`在研项目`、`学术成果`

## 入参 / 出参

### `OutputToCsvPayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `analysed_dir` | `str \| Path` | analysed JSON 目录 |
| `csv_path` | `str \| Path` | 目标 CSV 文件路径 |
| `resume_state_path` | `str \| Path \| None` | 恢复状态 JSON 路径 |
| `run_log_path` | `str \| Path \| None` | 运行日志 JSONL 路径 |

### `run` / `arun` 参数

- `max_tokens`：抽取阶段，默认 `2048`
- `repair_max_tokens`：JSON 修复阶段，默认 `4096`

### 返回值 `OutputToCsvResult`

- `analysed_dir`、`csv_path`
- `scanned_count`、`parsed_count`
- `appended_count`、`updated_count`、`skipped_count`

## 命令行

```bash
python -m byboy.agents.tutor_inf.output_to_csv ./byboy/test/get_tutor_pages_kzgc/cache/analysed --csv-path ./byboy/test/get_tutor_pages_kzgc/cache/tutor_summary.csv --route BYBOY_SLOT_DEFAULT --max-tokens 2048 --repair-max-tokens 4096
```

## 相关模块

- 上游：`byboy.agents.tutor_inf.get_tutor_analyse`
- 主流程入口：`byboy.agents.tutor_inf.get_tutor_inf_main`
