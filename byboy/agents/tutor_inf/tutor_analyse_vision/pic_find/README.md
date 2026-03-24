# PicFind Agent（导师页图片发现与下载）

## 模块作用

- 抓取目标导师页 HTML，收集可能相关的图片 URL（`img/srcset/og:image/background-image` 等）。
- 下载图片到指定目录并按序号命名。
- 生成 `manifest.json`，记录来源 URL、过滤结果与本地文件映射。

## 入参 / 出参

### `PicFindPayload`

| 字段 | 类型 | 说明 |
|------|------|------|
| `url` | `str` | 导师页 URL |
| `output_dir` | `str \| Path` | 图片输出目录 |

### 返回值 `PicFindResult`

- `image_paths`：本地图片路径元组（按序）
- `manifest_path`：清单 JSON 路径

## 特性

- 自动处理相对链接、`//host/path`、`base href`。
- 根据 MIME / 文件头推断后缀。
- 对无效 URL、重复 URL、非图片响应做过滤。

## 相关模块

- 调用方：`byboy.agents.tutor_inf.tutor_analyse_vision`
- 下游识别：`byboy.agents.tutor_inf.tutor_analyse_vision.pic_recog`
