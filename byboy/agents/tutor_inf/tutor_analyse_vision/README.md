# TutorAnalyseVision Agent（导师页视觉结构化）

## 模块作用

- 面向“页面文本不足但图片信息较多”的导师页场景，执行视觉链路：
  1. `pic_find`：从 HTML 抽取并下载候选图片
  2. `pic_recog`：逐图多模态识别并生成侧车 JSON
  3. 合并阶段：将多图结果去重合并成单个 `extracted` JSON
- 输出结果结构与 `tutor_analyse` 对齐（`meta + extracted`），便于下游复用。

## 输入输出

该 Agent 的 `inv.llm_part` 直接复用 `TutorAnalysePayload`。

### `run` / `arun` 参数

- `max_tokens`：逐图识别阶段 token 上限，默认 `16384`
- `merge_max_tokens`：合并阶段 token 上限，默认跟随 `max_tokens`

### 返回值

- `TutorAnalyseResult`（`json_path` + `markdown_cache_path`）

## 视觉缓存

在本包 `cache/` 下按 URL 哈希建立会话目录，包含：

- `images/`：下载后的图片
- 每图 `.json` 侧车文件
- 图片清单 `manifest.json`

## 命令行

```bash
python -m byboy.agents.tutor_inf.tutor_analyse_vision "https://example.edu/faculty/zhang" 张三 ./out zhang_vision.json --route BYBOY_SLOT_VISION --max-tokens 16384 --merge-max-tokens 16384
```

可选：`--markdown-path`（仅记录提示，不影响视觉抓图来源）

## 相关模块

- 子 agent：`byboy.agents.tutor_inf.tutor_analyse_vision.pic_find`
- 子 agent：`byboy.agents.tutor_inf.tutor_analyse_vision.pic_recog`
- 对照链路：`byboy.agents.tutor_inf.tutor_analyse`
