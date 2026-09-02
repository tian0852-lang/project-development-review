# project-development-review

[English](README.md) | 简体中文

## Skill 简介

`project-development-review` 是一套面向设计师、产品经理和 AI 开发协作者的开发前评审 Skill。

它帮助用户在正式 Vibe Coding 前，将设计稿、产品目标、页面范围、交互规则、页面资源、数据边界和验收要求，整理成有证据、有版本、有确认记录的规格文档、技术实施计划与开发交接资料。

当前版本：`2.2.1`

## 快速开始

安装对应平台适配层后，发送以下提示词开始评审。

```text
请通过 Figma MCP 或 MasterGo MCP 链接设计文档并开始项目评审。

项目名称：……
项目目标：……
设计源：Figma 或 MasterGo（二选一）
设计链接：……
当前截图：……
目标平台：……
项目仓库：……
```

每次评审只能选择一个设计源；开始评审前，请在设计工具中选中需要评审的画板，直至评审结束；Skill 会先核对设计源、盘点页面与资源，并请我确认范围后再生成规格草稿。

## 支持平台

ChatGPT、Codex、TraeWork、TraeCode、Cursor、Claude Code。

各平台采用“核心规范 + 平台适配层 + 持续规则 + 降级提示”。不同平台的安装入口和原生 Skill 能力并不完全相同，应按对应适配说明安装和验证。

## 核心能力

- 支持新项目、已有项目局部变更和混合项目评审；
- 每次评审只能选择 Figma 或 MasterGo 作为唯一设计源；
- 先盘点并确认页面数量、名称、节点、尺寸和本期范围；
- 同步盘点图标、图片、字体、尺寸、格式、倍数和使用位置；
- 已评审项目会识别资源的新增、修改、移除、移动和未知变化；
- 用户授权后，将已确认资源保存到 `review_root/assets/<resource-id>/<scale>/`；
- 评审页面跳转、导航参数、返回方式、状态保留、弹窗和异常恢复；
- 直接在对话中展示页面范围、做与不做的界定及全部待确认项；
- 区分设计证据、用户说明、技术建议和用户批准；
- 规格确认后生成只读技术评估和技术计划；
- 计划确认后生成实施任务卡与开发交接资料。

## 资源管理

资源清单重点记录：

- Resource ID；
- 使用页面和设计节点；
- 图标或图片用途；
- 原始、设计、导出和运行时尺寸；
- 1x、2x、3x 等导出倍数；
- 格式、裁切和适配方式；
- 来源、访问权限和使用授权；
- 确认状态、保存状态、路径与 SHA-256。

资源只允许保存到评审目录，不写入业务工程。Skill 会阻止路径穿越、未授权保存、摘要不一致和静默覆盖。

## 评审产物

评审资料默认保存在独立的 `review_root`，主要包括：

- 项目与工程基线；
- 设计源记录；
- 页面清单；
- 页面资源清单；
- 决定与待确认项；
- 七份产品和设计规格；
- 技术评估任务卡；
- 技术实施计划；
- 实施任务卡；
- 批准记录；
- 开发交接说明；
- 最终验证报告；
- 变更项目的影响与资源差异报告。

## 能力边界

本 Skill 只负责开发前评审、规格确认、技术计划和开发交接。

即使用户已经确认计划，它也不会：

- 编写或修改业务代码；
- 安装或升级依赖；
- 修改原生工程配置；
- 执行 Git 提交或推送；
- 替用户决定产品规则；
- 猜测设计 Token、跳转参数、返回规则或弹窗结果；
- 把设计原型连线直接转换成代码；
- 将未核验的历史确认作为当前开发授权。

最终目标是将“根据截图猜测开发”转化为“根据证据、规格、资源、版本和用户确认进行可信交接”。

## 平台安装

[SKILL.md](SKILL.md) 是执行入口。安装说明：[ChatGPT](adapters/chatgpt/INSTALL.md)、[Codex](adapters/codex/INSTALL.md)、[TraeWork](adapters/trae-work/INSTALL.md)、[TraeCode](adapters/trae-code/INSTALL.md)、[Cursor](adapters/cursor/INSTALL.md)、[Claude Code](adapters/claude-code/INSTALL.md)。能力证据和限制见[兼容性表](references/platform-compatibility.md)。

安装时保留完整包，并合并持续规则，不覆盖原规则。本轮没有安装、发布或对六客户端进行实际运行认证。建议后续经单独授权，在独立测试工作区验收。无法加载原生 Skill 时使用适配层降级提示；缺少阶段必读资料只能收集输入和整理页面草稿。无文件能力时必须标记仅文本交付，不能声称已经落盘或完成文件校验。

## 校验

Python 3.9 以上，纯标准库；无需安装 PyYAML。在 Skill 包目录执行：

```sh
python3 -B scripts/validate_package.py
python3 -B scripts/validate_review.py /评审包绝对路径 --stage specification_preflight
python3 -B scripts/validate_review.py /评审包绝对路径 --stage handoff_validation
python3 -B evals/run_tests.py
```

校验工具只读，不生成批准、不改写摘要。前期校验通过不等于可开发。合成样例必须加 --fixture，不能作为真实用户批准。工具只实现声明的 JSON Schema 子集，不能证明用户意图、设计真实性或自然语言无矛盾。

[测试说明](evals/README.md)与[验证报告](evals/expected-results/verification-report.md)区分自动检查、人工证据审查、智能体行为场景和真实客户端运行。

## 后续升级

维护资料已移出运行包，放在上级 `项目评审skill v2.0/maintenance/`：`v1-to-v2.md`、`PROJECT_HANDOFF.zh-CN.md` 和 `root-cause-analysis.zh-CN.md`。禁止把 v1 的 Confirmed 批量转为 Approved；旧包、已安装副本和原始样本保持不动。

机器执行资料保持英文；回复跟随当前消息语言，项目文档沿用首次需求的主要语言。README 的中英切换不改变项目语言。
