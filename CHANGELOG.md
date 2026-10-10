# NOVEL_OS Changelog

## 2026-10-10 — v2.1 execution-evidence hardening / evidence-before-claim
- 按 Universal Continuity `operational_hygiene@1.0 + evolution@1.0` 对小说系统执行挑刺、候选反证、最小修复与回归，不把用户建议或 assistant 第一方案直接当架构权威；完整决策证据见 `audits/NOVEL_SYSTEM_EVOLUTION_AUDIT_2026-10-10.md`。
- 根因确认：GitHub cutover 已完整迁移业务真值和流程规则，但“角色执行证据”压缩过度；此前 `CH0008_ACCEPTANCE.md` 可汇总多个 reviewer PASS，却没有 per-role invocation receipt / frozen Context Pack receipt / immutable chapter-contract snapshot 的机械强制。
- 拒绝“新增更多永久 Reviewer Agent”“强制伪造 ATTESTED_ISOLATED”“重做 CH8 补历史收据”“新建平行 CANON_SNAPSHOT/policy”等方案；采用最小可验证方案：release execution-evidence contract v1。
- 从 CH9 起新增硬门：不可变 `contracts/CHxxxx_CONTRACT.md`、冻结 `execution/CHxxxx_CONTEXT_PACK.json`、角色级 `reviews/CHxxxx_EXECUTION_EVIDENCE.json`、issue ledger、FINAL hash 与 Acceptance 双向绑定；`runtime/release_evidence_guard.py` fail closed。
- 正常 reviewer 继续允许 `CHAT_BRIDGED` 角色分离，但必须记录 blind-first-pass 可见性并明确 `ROLE_SEPARATED_NOT_ATTESTED_ISOLATED`；只有独立 execution identity + trace 才能声称 `ATTESTED_ISOLATED`。
- CH8 不重放、不补造历史证据；保留原 `FINAL_ACCEPTED / PUBLISH_READY` 业务状态，同时标记 `LEGACY_AGGREGATE_MIGRATED / role_receipts=NOT_AVAILABLE / isolated_reviewer_attestation=NOT_CLAIMED`。
- 修复 `SKILL.md` 对不存在 `CANON_SNAPSHOT.json` 的悬空权威引用；当前 Canon 继续由项目 `canon/` ledgers 共同定义，不新增重复 Canon authority。
- 修复 Active Rulebook 仍指向 Library backup evidence 的 post-cutover 漂移；旧 Notion/Library/legacy Drive 继续保持非权威历史线索身份。
- owner CI 现在运行 `recovery_guard.py + release_evidence_guard.py + 全量 pytest`；synthetic negative tests 覆盖“CH9 无执行证据”“CHAT_BRIDGED 假称 ATTESTED_ISOLATED”等失败场景。
- owner 元数据收敛到 `domain_contract=2.1-github / Skill=2.1.0-github / runtime=github-owner-2.2 / release_evidence_contract=1.0`；不改变 CH8/CH9 业务 stage、Canon v12、外部发布事实、Universal `resume_epoch=2` 或 active lease。

## 2026-10-10 — Post-cutover source cleanup and artifact-vault hardening
- 完成 GitHub primary 切换后的旧源审计与清理：GitHub `main` 保持唯一小说业务/系统权威，Universal Continuity 仅负责路由与 single-writer lease。
- 将当前 CH1–CH8 DOCX、封面/平台证据和迁移前 recovery ZIP 快照迁入 Google Drive `/ChatGPT/NOVEL_OS_小说系统_交付归档`；Google Drive 明确为非权威 artifact vault，不参与 Canon/checkpoint/Skill/恢复真值判定。
- 在验证 Google Drive 归档可读后删除 ChatGPT Library `/NOVEL_OS_小说系统` 完整旧执行树，避免旧 `00_SYSTEM / 01_PROJECTS / 99_RECOVERY` 与 GitHub 形成竞争权威。
- 审计当前可访问 Notion 与 Google Drive：未发现仍可与 GitHub 竞争的 live 小说执行入口；历史 Notion / legacy Google Drive 材料即使未来重新出现，也只能作为非权威历史线索。
- 修正 `AUTHORITY_STATUS.json`、`ARTIFACT_CONTEXT_GOVERNANCE.json`、`ENTRYPOINT.md`、`SKILL.md`、`PROTOCOL.md`、`README.md`、迁移 manifest/acceptance、Continuity adapter 与当前 checkpoint 的 post-cutover 存储语义。
- CH8 派生 DOCX 引用改为 Google Drive artifact vault；Universal task manifest 同步该引用但不改变业务 `current_stage / next_action`、active lease 或 `resume_epoch`。
- `runtime/recovery_guard.py` 与 `tests/test_recovery_contract.py` 新增存储治理回归：Library 重新成为执行/交付权威、Drive 被误标为业务权威、checkpoint 派生引用退回 Library 等情况均 fail closed。

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
