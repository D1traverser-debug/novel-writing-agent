# NOVEL_OS Changelog

## 2026-10-10 — System/project continuity routing hardening
- 修复“小说系统”与具体小说项目在 Continuity 发现/恢复语义中被误当作平行任务或只暴露项目、丢失系统语境的问题。
- 明确 `NOVEL_OS` 为小说生产系统、`NOVEL_WRITING_AGENT` 为 domain owner，`FQ001_MINGRI_ORDER` 为当前 authoritative active project；系统与项目逻辑联动、状态分层。
- `继承小说系统 / 继续小说系统 / 恢复小说系统 / NOVEL_OS / Novel Writing Agent` 现在由 owner 语义解析到 `active_project_task_id`；单一 active project 时自动绑定，不再要求用户二次选择。
- 保留具体项目唯一 USER durable task，不复制一个承载相同章节进度的“系统任务”；裸继承仍按 Universal USER 候选规则工作，但 owner 提供 `小说系统｜《凌晨零点，我接到明天的订单》` 的系统语境候选标签。
- 将 owner `ENTRYPOINT.md` 的 Continuity 标记从旧 v3.3 收敛到当前 v3.7，并把 system/project route 放进恢复顺序。
- `runtime/recovery_guard.py` 与 `tests/test_recovery_contract.py` 新增 system/project topology、alias、active-project binding 与 compatibility-index 同步回归；不修改 CH8/CH9 业务 checkpoint、Canon 或发布事实。

## 1.3.0｜2026-10-08
- 用户将“随时中断/新会话/删除旧聊天后无损继承”提升为小说系统最高硬要求。
- 建立永久稳定恢复入口 `99_RECOVERY/START_HERE.md` 与机器可读 `HANDOFF_MANIFEST.json`；恢复不再依赖带日期的入口或聊天记忆。
- 新增 production mode / transaction 概念：正常连载、FRONT_ARC_REBASE、RELEASE_REPAIR、RECOVERY_AUDIT；维护模式下禁止按 `last_final+1` 误开新章。
- 对 CH1-CH4 进行局外人首次阅读复盘，确认 CH2-CH4 存在跨章“验证/查询/记录/总结”同构、机械短段与人物情绪不足；决定执行一次性前四章终局重基线，CH5暂停。
- 升级写作学习体系：番茄官方课程/治理 + 真实平台数据 + 叙事研究 + Fresh Reader + 社区模式报警 + agent/skill工程实践。
- QA从三审扩展为 Continuity / Fresh Reader / Reader Retention / Editorial / Adversarial Release；发布审查默认拒稿而非默认PASS。
- 新增人物认同/情绪投入、场景生命、语言体验、跨章纹理监控；“信息量高/逻辑正确/风格一致”不再能证明好看。
- 新增 Character Drives 与 Reader Promise Ledger。
- 前四章重基线通过后进入 FROZEN_BASELINE；未来学习不得触发无限返工。

## 1.2.2｜2026-10-08
- CH4 提交前自检发现 `PROJECT.yaml` 与 `CURRENT_POINTER.json` 状态漂移并修复。
- 将项目/系统入口同步纳入每章 Canon Commit。
- 强化 deterministic Guard 的章节号、Canon 版本、FINAL/Acceptance hash 与 pointer 检查。

## 1.2.1｜2026-10-07
- 新增 `AUTONOMY_CHARTER.md`，固化内部可逆工作的全权执行授权。
- 强化职责分离、hash绑定审计、改稿重审。
- 新增旧版系统恢复入口并记录 CH1-CH3 已发布。

## 1.2.0｜2026-10-07
- 新增平台 PRELAUNCH GATE、元数据/封面/黄金三章/结构/恢复/合规前置审计。

## 1.0.1｜2026-10-07
- 增加 deterministic `novel_guard.py` 与 seeded-error benchmark。

## 1.0.0｜2026-10-07
- 建立独立 NOVEL_OS、Canon/Draft 隔离、职责分离与跨会话恢复。

## 2026-10-09 — v1.8.0 Agent architecture reassessment
- 将“每个工种都做常驻Agent”的直觉方案改为最小足够复杂度的混合编排。
- Reviewer首轮独立parallel fan-out/fan-in；默认禁用开放式group debate。
- Writer/Refiner采用有界evaluator-optimizer，最多2轮完整修订后升级结构诊断。
- Library保持单一权威状态；handoff最小化；manager保留最终放行责任。
- 新增Agent必须通过anti-overengineering条件。

## 2026-10-09 — v1.9.0 Drift control / context compaction
- 新增 `DRIFT_CONTROL_PROTOCOL.md`：学习隔离、作品身份回归、上下文预算、生产期冻结。
- 新增项目级 `ACTIVE_WRITING_PROFILE.md`：Writer使用短而稳定的身份胶囊，不再加载全部研究/Skill/历史审计。
- 新研究默认REFERENCE/EXPERIMENTAL，先shadow test再决定是否进入Active规则。
- 每章执行identity regression；每10章最多一次Profile结构性升级。
- Context Pack冻结后不在当前章临时注入新技巧；系统通过硬门后停止改造，回到正文。
