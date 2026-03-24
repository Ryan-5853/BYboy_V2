# BYboy_V2

一个面向考研/保研信息收集场景的 Agent 工程。  
项目目标：帮助同学在收集院校与导师公开信息时，减少“逐页浏览主页、手动查找和整理”的重复劳动，把流程从“人工逐条复制”升级为“可复用、可恢复、可追踪”的自动化链路。

---

## 1. 项目定位与目标

在院校/导师信息搜集过程中，常见痛点包括：

- 页面分散：学院页、师资页、导师个人主页、分页列表来回跳转
- 信息碎片化：研究方向、联系方式、项目成果分布在不同模块甚至图片中
- 手工整理耗时：最终还要落到统一表格中用于对比

本工程当前优先实现 `tutor_inf`（导师信息链路）模块，目标是：

1. 从学院入口页自动迭代发现导师相关页面  
2. 对导师页做结构化抽取（文本链路 + 视觉链路）  
3. 汇总到统一 CSV，便于筛选和比对  
4. 过程可断点恢复，支持持续补抓与增量更新

未来会继续扩展其它业务模块（不仅限于 `tutor_inf`），沿用统一的 Agent 调用契约和路由配置方式。

---

## 2. 当前工程结构（核心）

```text
BYboy_V2/
├─ byboy/
│  ├─ agents/
│  │  └─ tutor_inf/                 # 当前主业务模块
│  │     ├─ get_tutor_inf_main/     # 一键主流程编排
│  │     ├─ get_tutor_pages/        # 入口页迭代抓取与链接分类编排
│  │     ├─ get_tutor_analyse/      # 批量导师页分析编排
│  │     ├─ tutor_analyse/          # 单导师页文本结构化
│  │     ├─ tutor_analyse_vision/   # 单导师页视觉结构化（含子 agent）
│  │     │  ├─ pic_find/
│  │     │  └─ pic_recog/
│  │     ├─ web_clean/              # 网页转 Markdown（Firecrawl）
│  │     ├─ link_choose/            # 链接分类
│  │     └─ output_to_csv/          # analysed JSON -> CSV
│  ├─ llm/                          # 路由、槽位、分发器
│  ├─ packyapi/                     # Packy 网关客户端配置
│  └─ settings.py                   # 从环境变量构造 Dispatcher
├─ .env.example                     # 环境变量模板
└─ requirements.txt                 # 依赖
```

---

## 3. 环境准备与部署

## 3.1 运行环境

- Python 3.10+（建议 3.10/3.11）
- 可访问所配置的 LLM 网关与 Firecrawl 服务
- Windows / Linux / macOS 均可（命令示例默认 PowerShell 风格）

## 3.2 安装依赖

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`requirements.txt` 当前核心依赖：

- `openai>=1.40.0`
- `anthropic>=0.40.0`
- `python-dotenv>=1.0.0`

## 3.3 配置环境变量

1. 复制模板：

```powershell
copy .env.example .env
```

2. 按需填写 `.env`（至少以下几项）：

- LLM 网关：
  - `PACKY_API_KEY`
  - `PACKY_BASE_URL`
  - `PACKY_ANTHROPIC_BASE_URL`
- 模型与默认路由：
  - `BYBOY_OPENAI_MODEL`
  - `BYBOY_CLAUDE_MODEL`
  - `BYBOY_LLM_DEFAULT_ROUTE`
- Firecrawl：
  - `FIRECRAWL_API_KEY`
  - `FIRECRAWL_BASE_URL`（可选，默认 `https://api.firecrawl.dev`）

3. 推荐配置语义槽位（便于 CLI 统一传参）：

- `BYBOY_SLOT_DEFAULT_MODEL=claude:...`
- `BYBOY_SLOT_DEFAULT_API_KEY=...`
- `BYBOY_SLOT_VISION_MODEL=openai_vision:...` 或 `claude_vision:...`
- `BYBOY_SLOT_VISION_API_KEY=...`

说明：CLI 里常见 `--route BYBOY_SLOT_DEFAULT` / `--route BYBOY_SLOT_VISION`，会经 `LLMDispatcher` 解析为对应后端与模型。

---

## 4. 快速开始（推荐主流程）

使用一条命令跑通导师信息链路：

```powershell
python -m byboy.agents.tutor_inf.get_tutor_inf_main `
  "https://example.edu/college" `
  --workdir ./byboy/test/get_tutor_pages_kzgc `
  --slot BYBOY_SLOT_DEFAULT
```

常用参数：

- `--depth`：页面迭代轮数（默认 2）
- `--pages-max-tokens`：链接分类阶段 token
- `--analyse-max-tokens`：导师结构化阶段 token
- `--csv-max-tokens`：CSV 抽取阶段 token
- `--csv-repair-max-tokens`：CSV JSON 修复阶段 token
- `--pages-resume-state`：页面抓取恢复点 `state.json`
- `--csv-resume-state` / `--csv-run-log`：CSV 阶段恢复与日志

执行后可重点查看：

- `workdir/cache/state.json`（抓取状态）
- `workdir/cache/analysed/*.json`（导师结构化结果）
- `workdir/cache/tutor_summary.csv`（汇总结果）

---

## 5. tutor_inf 模块调用逻辑与流程

## 5.1 总体流程图（当前实现）

```text
academy_url
   |
   v
get_tutor_pages
   |- web_clean    : URL -> Markdown
   |- link_choose  : Markdown -> 链接分类 JSON
   `- 迭代更新 state.json
   |
   v
get_tutor_analyse
   `- tutor_analyse : 导师页 -> 结构化 JSON（analysed）
   |
   v
output_to_csv
   `- analysed/*.json -> 固定列 CSV（增量更新）
```

`get_tutor_inf_main` 是上述三步的一键编排入口。

## 5.2 各 Agent 职责（简述）

- `web_clean`  
  调 Firecrawl 抓网页并转 Markdown，首行写入 `> 抓取来源：URL`。

- `link_choose`  
  对 Markdown 里的链接做分类，核心分类：
  - `tutor_profile`
  - `tutor_expansion`
  - `irrelevant`

- `get_tutor_pages`  
  管理三类 URL 列表并迭代抓取，落地 `cache/cleaned`、`cache/choice`、`cache/state.json`。

- `tutor_analyse`  
  单导师页文本结构化，产出 `meta + extracted` JSON。

- `tutor_analyse_vision`（视觉兜底链路）  
  `pic_find` 找图并下载，`pic_recog` 逐图识别，再合并多图结果。

- `get_tutor_analyse`  
  批量读取 `list2_tutor_profiles`，调用 `tutor_analyse` 并维护分析清单。

- `output_to_csv`  
  将结构化 JSON 抽取为固定字段表头，支持增量合并、断点恢复、运行日志。

- `get_tutor_inf_main`  
  将 pages -> analyse -> csv 串成完整主流程。

每个 agent 的详细字段与示例，请直接查看各目录下 `README.md`。

---

## 6. 分步运行（调试/排障常用）

## 6.1 仅抓取导师相关页面

```powershell
python -m byboy.agents.tutor_inf.get_tutor_pages `
  "https://example.edu/college" `
  --workdir ./byboy/test/get_tutor_pages_kzgc `
  --depth 2 `
  --route BYBOY_SLOT_DEFAULT
```

## 6.2 批量分析导师页

```powershell
python -m byboy.agents.tutor_inf.get_tutor_analyse `
  --workdir ./byboy/test/get_tutor_pages_kzgc `
  --route BYBOY_SLOT_DEFAULT `
  --max-tokens 16384
```

## 6.3 汇总 CSV

```powershell
python -m byboy.agents.tutor_inf.output_to_csv `
  ./byboy/test/get_tutor_pages_kzgc/cache/analysed `
  --route BYBOY_SLOT_DEFAULT `
  --max-tokens 2048 `
  --repair-max-tokens 4096
```

---

## 7. 如何修改与扩展

## 7.1 调整模型与路由

- 在 `.env` 中修改 `BYBOY_SLOT_*` 与通道默认模型
- `LLMDispatcher.from_env()` 会读取并构造路由
- 推荐业务代码统一传 `ModelRef("BYBOY_SLOT_XXX")`，避免硬编码模型名

## 7.2 调整提取策略

- `link_choose/agent.py`：链接分类规则与输出结构
- `tutor_analyse/agent.py`：文本结构化提示词与 JSON 修复策略
- `tutor_analyse_vision/*`：视觉识别与合并逻辑
- `output_to_csv/agent.py`：固定字段映射、合并策略、增量状态

## 7.3 新增业务模块（未来模块建议）

建议复用当前范式：

1. 定义 `Payload` / `Result` 数据结构  
2. 实现 `run` / `arun`  
3. 提供 `__main__.py` 命令行入口  
4. 提供该模块的 `README.md`（输入、输出、流程、示例）  
5. 如需编排，新增 `*_main` 入口统一串联

这样可保持“模块独立可运行 + 主流程可编排”的一致工程风格。

---

## 8. 常见问题（FAQ）

- **Q: 为什么要写 `state.json`？**  
  A: 用于断点恢复、避免重复处理、支持长链路分批执行。

- **Q: 为什么有文本链路和视觉链路？**  
  A: 部分页面文字信息很少、关键信息在图片里，视觉链路用于补全信息覆盖。

- **Q: 是否一定要一键主流程？**  
  A: 不一定。调试时建议分步运行，定位更清晰。

---

## 9. 版权声明（重要）

本工程中所有“用户代码”均由作者独立编写，发布目的仅用于学习、交流与讨论。  
**严禁任何形式的商业化使用**，包括但不限于：售卖、二次打包收费、商业 SaaS 集成、商业咨询交付等。

若你基于本项目进行学习或改进，欢迎在非商业场景下参与贡献与讨论。  
本项目将持续更新，欢迎 issue / PR / 交流建议。

---

## 10. 使用限制与合规声明（重要）

使用本工程即表示你承诺遵守以下约束：

1. **遵守 LLM 与第三方服务条款**  
   必须遵循各模型厂商、网关服务、抓取服务的地区限制、账号政策、API 使用协议与服务条款。

2. **禁止违法违规用途**  
   不得使用本工程生成、传播、协助生成违法违规信息，不得从事任何违反法律法规的活动。

3. **仅用于公开信息收集**  
   仅可处理公开可访问的信息页面；不得用于抓取、归档或推断个人隐私、敏感身份信息等。

4. **禁止生成不实内容**  
   不得利用本工程伪造、篡改或批量生成虚假导师/院校信息，不得用于误导性传播。

5. **遵守网站规则与反爬策略**  
   对存在明确反爬机制、访问限制、robots 协议限制或明确禁止自动化访问的网站，不得进行自动化抓取。  
   不得绕过验证码、鉴权、频控、风控或其他技术保护措施。

6. **控制访问频率与影响范围**  
   应合理限速，避免对目标站点造成异常负载、服务干扰或安全风险。

7. **数据安全与最小化原则**  
   对产生的中间文件与结果文件应妥善保存，避免泄露；仅保留必要数据，尽量减少冗余复制。

8. **结果需人工复核**  
   LLM 输出可能存在幻觉或抽取偏差，任何用于决策、公开传播或提交材料的内容必须人工核验。

如因不当使用导致的法律风险、账号风险或第三方纠纷，由使用者自行承担责任。

---

## 11. 贡献与后续计划

- 欢迎提交 issue：错误反馈、配置疑问、适配建议
- 欢迎提交 PR：bugfix、新 agent、提示词优化、文档改进
- 后续将继续扩展除 `tutor_inf` 之外的其它信息收集与整理模块，保持统一的调用契约和可恢复流水线能力

如果你愿意一起维护，欢迎参与。

