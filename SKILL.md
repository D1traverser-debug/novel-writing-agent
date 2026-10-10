---
name: novel-writing-agent
version: 2.0.0-github
scope: 独立长篇网络小说生产、连载、审计、恢复
primary_platform: 番茄小说
source_system_version: NOVEL_OS 1.9.0
---

# Novel Writing Agent Skill

GitHub business authority: `D1traverser-debug/novel-writing-agent@main`.
Global cross-chat routing / single-writer lease authority: `D1traverser-debug/universal-continuity-agent@main`.

## 0. Non-negotiable boundaries
1. 不允许仅根据聊天上下文续写；先按 `ENTRYPOINT.md` 恢复。
2. 未通过质量硬门的草稿不能更新 Canon 或进入发布候选。
3. 正文 hash 改变，所有依赖正文的旧审计立即 STALE。
4. 不得为赶更新牺牲连续性、逻辑、原创性、人物生命感与读者体验。
5. 小说内部可逆、可记录、可审计的工作由 ORCHESTRATOR 主动决定；用户不承担 QA/流程经理职责。
6. 平台最终发布/删除/替换、签约、付费、法律/合规声明等外部高后果动作仍由用户确认或执行。
7. 已发布 Canon 不得静默覆盖；事实变化必须走 Retcon。
8. `REBASE/REPAIR/RECOVERY_AUDIT` 等维护模式下禁止仅按章节号误开新章。

## 1. Authority and recovery
冲突时：用户最新明确外部事实 > GitHub `main` 当前任务/Canon/FINAL/审计 > Library 派生交付物/备份 > 历史镜像 > 聊天记忆。

写入任何 material checkpoint 前，必须重读 Universal task manifest，确认当前 `active_lease.lease_id + resume_epoch`；旧聊天失去 lease 后必须 fail closed。

恢复入口与读取顺序见 `ENTRYPOINT.md`。

## 2. Production organization
采用最小足够复杂度的编辑部式编排：
- `EXECUTIVE_ORCHESTRATOR`：恢复、调度、冲突裁决、最终放行；不得自写自批。
- `CANON_LIBRARIAN`：Context Pack / Canon / 线程 / 伏笔 / 承诺。
- `ARCHITECT`：章节功能、合同、scene engine、risk map。
- `WRITER`：只依据冻结 Context Pack + Contract 写正文。
- 独立审稿：Continuity / Fresh Reader / Retention / Editorial / Adversarial / Quality Discovery。
- `REFINER`：只根据 issue ledger 修稿；默认最多2轮完整 evaluator-optimizer。
- `COPYEDITOR_PROOFREADER`：文学修改结束后独立终校。
- `ARTIFACT_RELEASE_ENGINEER`：Word同源、渲染、hash、Guard、恢复产物。
- `CANON_COMMITTER`：全部同一 hash 签字后才提交 Canon。

Reviewer 首轮相互隔离；禁止用多数票覆盖 BLOCKER/HIGH。专项专家只按实际风险触发。

## 3. Standard serialization pipeline
`RECOVER -> VERIFY_LEASE -> CHECK_MODE -> FREEZE_CONTEXT -> ARCHITECT+CANON -> DRAFT -> INDEPENDENT_REVIEW_FANOUT -> ISSUE_MERGE -> REVISE -> RE-AUDIT -> FINAL_PROOFREAD -> ARTIFACT_QA -> DETERMINISTIC_GUARD -> CANON_COMMIT -> RELEASE -> CHECKPOINT`

## 4. Minimum sufficient Context Pack
Writer 默认只接收：
- `projects/<task>/PROJECT_PROFILE.md` 中 Active Writing Profile；
- 当前 `NEXT_CHAPTER_CONTRACT.md`；
- 最近3章必要正文/摘要；
- 本章相关人物/物件/地点/规则 Canon；
- active THREADS / FORESHADOW / READER_PROMISES 相关子集；
- 最多2—4个本章真正相关的专项规则；
- 最近跨章风险。

研究日志、全部历史审计、完整规则仓库默认不得整包灌给 Writer。Context Pack 冻结后，除 Canon/现实事实/合规 BLOCKER 外，不临时注入新技巧。

## 5. Project identity
每章发布前必须确认作品仍是：现代城市真实运行质感 + 狭窄未来订单异常 + 第三人称限知陈渡 + 有限信息下的选择与后果。不得漂成万能系统、纯刑侦、纯规则怪谈或全知天才推理。

项目具体身份、声纹、世界规则与冻结基线见 `PROJECT_PROFILE.md`；当前 Canon 见 `CANON_SNAPSHOT.json`。

## 6. Release hard gates
只有以下全部对同一正文 hash 明确 PASS，ORCHESTRATOR 才能说“可以传/可以发布”：
- Canon / timeline / spatial / knowledge / capability / contract contradictions = 0；
- Fresh Reader / Retention / Editorial BLOCKER/HIGH = 0；
- Adversarial Release = RELEASE；
- Quality Discovery / project identity regression PASS；
- 适用的 Domain Reality / Beta Reader / Length Gate PASS；
- Final Proofread 三遍：mechanical + semantic + read-aloud；
- deterministic guards PASS；
- FINAL 与 Word 同源；Word逐页渲染检查通过；
- Acceptance / Release Gate / checkpoint / recovery pointers 与 source hash 一致。

用户指出本应自动发现的问题时，立即撤销旧 Release，按 reminder-dependency incident 修复、重审并升级通用防线。

## 7. Craft / QA rulebook
所有当前激活的场景、声纹、对白、人物关系、悬疑、公平信息、长期架构、主题、伏笔、情绪、Reader Memory、Opposition、空间调度、Transition、Domain Reality、平台、字数、终校、Agent组织与防漂移规则，统一蒸馏在：

`protocols/ACTIVE_RULEBOOK.md`

历史完整协议和研究证据仍保留在迁移前 Library 备份中，但不自动进入 Writer 主上下文，也不能覆盖当前 GitHub active rulebook。

## 8. Canon / prose rules
- Canon facts 与 prose surface 分离。
- 纯措辞/节奏/场景呈现优化且事实不变可走 `PROSE_REBASE`。
- 改变人物已知事实、事件结果、系统规则、时间线必须正式 Retcon + 影响分析 + 新 Canon version + 重审。
- CH1–CH4 FROZEN_BASELINE 不因后续审美/技巧学习反复返工。

## 9. Length and data
章节长度以真实番茄后台数据优先；无实际值时使用 FINAL 预测值。常规约2400–3000，重大章约2600–3300仅作当前基线，不是机械目标。相对最近4章均值偏离 >30% 强制专审，>45% 默认阻塞，除非结构上明确必要。

平台读完率、跟读率、评论聚类等真实数据高于模型自评分。不得为更新量或字数目标水文。

## 10. Periodic regression
- 每5章：长度 × 纹理 × 钩子 × 情绪颜色 × 角色出场 × 讨论性检查。
- 每10章/单元：Long-form + World Rule + Foreshadow + Identity Regression。
- 每50章/卷级节点：全局 Canon reconciliation。
- 重大结构修改前后：checkpoint/snapshot。

## 11. Stop rule
当前身份回归 PASS、硬门全过、没有重复数据证据要求改规则时，停止系统改造并继续正文。系统进化服务于作品，不以规则/Agent数量为成果。
