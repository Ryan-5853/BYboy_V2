# PicRecog Agent（单图多模态结构化）

## 模块作用

- 输入单张图片与导师中文名，调用视觉模型抽取图中可见信息。
- 输出单个 JSON 对象（`extracted`），并写同名侧车 `.json` 文件。
- 该结果用于 `tutor_analyse_vision` 的多图合并阶段。

## 入参 / 出参

### `PicRecogPayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `image_path` | `str \| Path` | 图片路径 |
| `tutor_name_cn` | `str` | 导师中文名 |

### `run` / `arun` 参数

- `max_tokens`：默认 `16384`

### 返回值 `PicRecogResult`

- `json_path`：侧车 JSON 路径（默认写到图片同目录、同文件名不同后缀）

## 输出侧车格式

侧车 JSON 主要字段：

- `source_image`
- `source_image_path`
- `tutor_name_cn`
- `extracted`（模型输出结构化对象）

## 相关模块

- 上游：`byboy.agents.tutor_inf.tutor_analyse_vision.pic_find`
- 编排方：`byboy.agents.tutor_inf.tutor_analyse_vision`
