---
name: novel-writing-agent
version: 2.3.0-github
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
9. 聚合式“某角色 PASS”文字本身不是角色已执行的充分证据；从 CH9 起必须满足 execution-evidence contract v1。
10. `CHAT_BRIDGED` 角色 receipt 是结构化自证记录，不是独立执行 attestation；不得把可校验的文件/hash 绑定描述成对模型认知过程或执行时序的独立证明。
11. 平台签约拒绝、真实读者数据显著恶化、事实/合规硬缺陷属于可重新打开既有“冻结基线”的硬证据；不得把这类外部失败降格成普通审美建议，也不得在未诊断前盲目冲下一次平台机会。
12. 用户允许大改/全退回时，授权只改变可接受的迁移成本与外部操作边界；“全部重写”本身仍是候选机制，必须与局部修复、结构重排、保留/删除旧机制等方案竞争后再采用。

## 1. Authority and recovery
冲突时：用户最新明确外部事实 > GitHub `main` 当前任务/Canon/FINAL/审计 > Google Drive `/ChatGPT/NOVEL_OS_小说系统_交付归档` 中明确需要的派生交付物/历史迁移证据 > 已退役的 Notion / Library / 旧 Google Drive 材料（仅历史线索，不得恢复执行状态） > 聊天记忆。

写入任何 material checkpoint 前，必须重读 Universal task manifest，确认当前 `active_lease.lease_id + resume_epoch`；旧聊天失去 lease 后必须 fail closed。

恢复入口与读取顺序见 `ENTRYPOINT.md`。

### 1.1 NOVEL_OS system/project topology
`NOVEL_OS` 是小说生产系统；`NOVEL_WRITING_AGENT` 是其 GitHub domain owner；具体作品是该系统管理的 project task。

当前 active project：`FQ001_MINGRI_ORDER` / 《凌晨零点，我接到明天的订单》。

系统和项目必须联动但分层：
- 系统层保存写作方法、质量门、Agent/工作流、学习与进化规则；
- 项目层保存本书 Canon、人物、章节、发布状态、伏笔、合同与 checkpoint；
- 系统规则可以改变后续项目工作的执行方式，但不得覆盖项目事实；
- 项目章节推进不得抹掉系统级学习/治理规则。

`继承小说系统`、`继续小说系统`、`恢复小说系统`、`NOVEL_OS`、`Novel Writing Agent` 必须先路由到本 owner，再读取 `continuity/TASK_INDEX.json#system.active_project_task_id` 自动恢复当前 active project。只有一个 authoritative active project 时，不要求用户再次选择项目；未来存在多个 active project 时，必须按明确项目提示路由或展示项目候选，禁止合并状态。

不得为了让“小说系统”可继承而复制出一个与同一 active project 平行、重复承载相同业务进度的 durable task。

## 2. Production organization
采用最小足够复杂度的编辑部式编排：
- `EXECUTIVE_ORCHESTRATOR`：恢复、调度、冲突裁决、最终放行；不得自写自批。
- `CANON_LIBRARIAN`：Context Pack / Canon / 线程 / 伏笔 / 承诺。
- `ARCHITECT`：章节功能、合同、scene engine、risk map。
- `WRITER`：只依据冻结 Context Pack + Contract 写正文。
- 独立首轮判断：Continuity / Fresh Reader / Retention / Editorial / Adversarial / Quality Discovery。
- `REFINER`：只根据 issue ledger 修稿；默认最多2轮完整 evaluator-optimizer。
- `COPYEDITOR_PROOFREADER`：文学修改结束后独立终校。
- `ARTIFACT_RELEASE_ENGINEER`：Word同源、渲染、hash、Guard、恢复产物。
- `CANON_COMMITTER`：全部同一 hash 签字后才提交 Canon。

Reviewer 首轮必须在输入层隔离彼此结论；禁止用多数票覆盖 BLOCKER/HIGH。专项专家只按实际风险触发。当前正常 reviewer 属于 `CHAT_BRIDGED` 角色分离，不得声称 `ATTESTED_ISOLATED`；只有存在独立 execution identity + trace 时才允许该更高保证等级。

## 3. Standard serialization pipeline
`RECOVER -> VERIFY_LEASE -> CHECK_MODE -> FREEZE_CONTEXT -> ARCHITECT+CANON -> DRAFT -> INDEPENDENT_REVIEW_FANOUT -> ISSUE_MERGE -> REVISE -> RE-AUDIT -> FINAL_PROOFREAD -> ARTIFACT_QA -> DETERMINISTIC_GUARD -> CANON_COMMIT -> RELEASE -> CHECKPOINT`

### 3.1 Execution-evidence contract v1（CH9+ / promoted replacement prose）
任何进入 `FINAL_ACCEPTED / PUBLISH_READY` 的新正文必须按适用的 execution-evidence contract 留下证据；正常连续写作从 CH9 起强制，FULL_FRONT_ARC_REBASE 产生的替换候选在准备晋升时同样不得绕过证据/重审义务。

1. `projects/<task>/contracts/CHxxxx_CONTRACT.md`：执行前形成的不可变章节合同快照；
2. `projects/<task>/execution/CHxxxx_CONTEXT_PACK.json`：冻结输入收据，至少记录 owner commit、合同快照 hash、Project Profile hash、相关 Canon refs、最近必要 FINAL refs、最多2—4个 rule slices；所有本地 Project Profile / Canon / recent FINAL ref 都必须存在且与记录 hash 一致；
3. `projects/<task>/reviews/CHxxxx_EXECUTION_EVIDENCE.json`：角色级执行收据、正文 source hash、Context Pack hash、issue ledger、reviewer 首轮 peer-visibility；每个 receipt 必须有唯一 id、Context Pack 绑定与非空结果摘要，最终终校/制品/Canon 提交类角色必须绑定 FINAL source hash；
4. Acceptance 必须 hash-bind 上述 Context Pack 与 execution evidence。

聚合 Acceptance 只能汇总已存在的证据，不能替代证据。正文 hash 改变后，所有 body-dependent review receipts 失效并必须重新绑定/重审。

`CHAT_BRIDGED` receipt 的保证等级只能是 `ROLE_SEPARATED_NOT_ATTESTED_ISOLATED`。确定性 guard 能验证文件存在、hash、输入绑定、角色字段和内部一致性，但不能独立证明同一模型的认知过程，也不能证明所有 receipt 不是在同一 session 事后补写；真正的 execution attestation / chronological provenance 只能由不同 execution identity、provider trace 或其他独立可验证执行面提供。禁止通过增加角色名、文件数量或自填 timestamp 来伪装更高 assurance。

历史 CH8 acceptance 属于迁移前 `LEGACY_AGGREGATE_MIGRATED`。在本次 full rebase 中，它只证明旧正文的历史验收状态，不能被重放为替换候选的当前质量证据。

## 4. Minimum sufficient Context Pack
Writer 默认只接收：
- `projects/<task>/PROJECT_PROFILE.md` 中 Active Writing Profile；
- 当前章节/重构单元的冻结 Contract/Architecture slice；
- 必要的最近正文或当前 rebase packet 相关候选；
- 本章相关人物/物件/地点/规则 Canon；
- active THREADS / FORESHADOW / READER_PROMISES 相关子集；
- 最多2—4个本章真正相关的专项规则；
- 最近跨章风险。

研究日志、全部历史审计、完整规则仓库默认不得整包灌给 Writer。Context Pack 冻结后，除 Canon/现实事实/合规 BLOCKER 外，不临时注入新技巧。冻结内容必须留下 durable receipt，不能只存在聊天里。

FULL_FRONT_ARC_REBASE 期间，旧 CH1–CH8 FINAL 作为历史业务证据/素材库存在；Writer 不得因为它们存在就机械沿用旧章节边界。只加载当前 Architecture 明确选中的旧场景/事实。

## 5. Project identity
每章发布前必须确认作品仍是：现代城市真实运行质感 + 狭窄未来订单异常 + 第三人称限知陈渡 + 有限信息下的选择与后果。不得漂成万能系统、纯刑侦、纯规则怪谈或全知天才推理。

项目具体身份、声纹、世界规则与历史基线见 `PROJECT_PROFILE.md`。当前 Canon 由 `projects/<task>/canon/` 下的 `CHARACTERS.json`、`CHARACTER_DRIVES.json`、`THREADS.json`、`FORESHADOW.jsonl`、`TIMELINE.jsonl`、`READER_PROMISES.json` 等权威 ledgers 共同定义；不存在另一个可覆盖这些 ledgers 的 `CANON_SNAPSHOT.json` 权威。

## 6. Release hard gates
只有以下全部对同一正文 hash 明确 PASS，ORCHESTRATOR 才能说“可以传/可以发布”：
- Canon / timeline / spatial / knowledge / capability / contract contradictions = 0；
- Fresh Reader / Retention / Editorial BLOCKER/HIGH = 0；
- Adversarial Release = RELEASE；
- Quality Discovery / project identity regression PASS；
- 适用的 Domain Reality / Beta Reader / Length Gate PASS；
- Final Proofread 三遍：mechanical + semantic + read-aloud；
- deterministic guards PASS；
- 适用的 release evidence gate PASS；
- FINAL 与 Word 同源；Word逐页渲染检查通过；
- Acceptance / execution evidence / Release Gate / checkpoint / recovery pointers 与 source hash 一致。

对于 `FULL_FRONT_ARC_REBASE`，单章 PASS 不能单独晋升替换；还必须完成 whole-packet Continuity / pacing-engine diversity / character attachment / signing-readiness 复审，确认整包可晋升后再执行显式 replacement transaction。

用户指出本应自动发现的问题时，立即撤销旧 Release，按 reminder-dependency incident 修复、重审并升级通用防线。

## 7. Craft / QA rulebook
所有当前激活的场景、声纹、对白、人物关系、悬疑、公平信息、长期架构、主题、伏笔、情绪、Reader Memory、Opposition、空间调度、Transition、Domain Reality、平台、字数、终校、Agent组织、防漂移与 full-rebase 规则，统一蒸馏在：

`protocols/ACTIVE_RULEBOOK.md`

迁移前的历史完整协议/研究证据仅作为历史迁移快照保存在 Google Drive artifact vault 中，不自动进入 Writer 主上下文，也不能覆盖当前 GitHub active rulebook。旧 Notion、Library 或旧 Google Drive 执行材料即使未来被重新发现，也只能作为非权威历史线索。

## 8. Canon / prose rules
- Canon facts 与 prose surface 分离。
- 纯措辞/节奏/场景呈现优化且事实不变可走 `PROSE_REBASE`。
- 改变人物已知事实、事件结果、系统规则、时间线必须正式 Retcon + 影响分析 + 新 Canon version + 重审。
- 历史 `FROZEN_BASELINE` 默认不因普通审美/技巧学习反复返工；但平台签约拒绝、真实读者数据显著恶化、事实/合规硬缺陷等外部硬失败可触发受控解冻。受控解冻必须留下失败证据、影响分析、候选比较、active plan，并保持旧 FINAL 可追溯，不得静默覆盖。

### 8.1 Platform signing-feedback loop
番茄签约申请属于高价值外部评估事件。每次申请前后执行：

1. 申请前读取当前番茄官方签约规则与评估维度，不把历史阈值/旧攻略当永久规则；
2. 申请结果只记录平台实际可见事实，明确区分 `安全审核失败`、`签约评估拒绝`、`签约通过`；
3. 泛化“质量未达标”不能被擅自解释成 AI、抄袭、违规或某一单点写作缺陷；
4. 签约评估拒绝后，先对当前可见前段做 opening / pacing / character setup / immersion / mainline 诊断，再决定继续写、局部 rebase 或结构修复；
5. 禁止“原文不动，只堆字数到下一阈值再试”；下一次申请必须有 durable signing-readiness gate；
6. 已发布章节可在内部生成候选修订，但平台正文替换仍属于用户控制的外部高影响动作；
7. 任何修订造成正文 hash 变化，旧 body-dependent 审计失效，必须按现有 release/rebase 规则重审；
8. 签约结果是平台/商业状态，不改变故事 Canon，但可以改变生产优先级和质量修复策略。

### 8.2 Full front-arc rebase / learning-to-authority promotion
当真实外部硬失败 + 有效用户影响授权使“低迁移成本”不再是主约束时，owner 可以把修复层级从句子/章节提升到完整 acquisition/front-arc 单元，但必须遵守：

1. `LEARNING_EVIDENCE` 与执行权威分离：课程、研究、社区、模型诊断先记录来源/证据等级，不能直接成为 Active 规则；
2. 对用户提出的“全改”、assistant第一方案、局部修复、blank-slate rewrite、no-change 等候选进行比较与反证；
3. 先冻结旧 FINAL/hashes 作为不可变历史基线，再改 active architecture；
4. old chapter boundary 不是 Canon，允许重排；Canon factual truth 仍需显式 Retcon 才能改变；
5. 先 architecture prototype / whole-packet plan，再写正文；禁止八章各自优化后拼成“新版本”；
6. 强场景/强对白/强伏笔可以复用，但必须服务新 packet，而不是为保旧稿而保；
7. superseded matrix/contract 必须明确退出 hot path，禁止两套 active 方案共存；
8. whole-packet candidate 未过 Continuity / Fresh Reader / Retention / Editorial / Adversarial / identity / signing-readiness 前，不覆盖旧 FINAL；
9. CI/Guard 只能证明 rebase 状态、supersession 和证据机制没有漂移，不能证明作品已经“变好”；真实质量结果需 action-level review + 读者/平台/live signing 证据；
10. 本项目“目标CH3完成第一重大promise payoff、CH6–7建立许知微持续关系”是当前结构 hypothesis/target，不得泛化成所有小说的固定黄金公式。

Current FQ001 active refs:
- `audits/FULL_REBASE_LEARNING_EVIDENCE_2026-10-11.md`
- `audits/FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md`

## 9. Length and data
章节长度以真实番茄后台数据优先；无实际值时使用 FINAL 预测值。常规约2400–3000，重大章约2600–3300仅作当前基线，不是机械目标。相对最近4章均值偏离 >30% 强制专审，>45% 默认阻塞，除非结构上明确必要。

FULL_FRONT_ARC_REBASE 期间先以 packet function / scene engine / reader experience 为主，不为了维持旧章均值强行切章；最终准备平台替换时再按实际新章节边界重建长度基线。

平台读完率、跟读率、评论聚类、签约评估等真实平台信号高于模型自评分。不得为更新量、字数门槛或下一次签约机会水文。

## 10. Periodic regression
- 每5章：长度 × 纹理 × 钩子 × 情绪颜色 × 角色出场 × 讨论性检查。
- 每10章/单元：Long-form + World Rule + Foreshadow + Identity Regression。
- 每50章/卷级节点：全局 Canon reconciliation。
- 重大结构修改前后：checkpoint/snapshot。
- 每次平台签约评估拒绝：立即新增一次 front-arc signing-quality audit，不等待下一个常规周期。
- FULL_FRONT_ARC_REBASE：architecture freeze、candidate packet ready、promotion 前分别做 packet-level regression；不以单章自评分替代整包验证。

## 11. Stop rule
当前 full-rebase architecture 经过挑战并冻结后，停止继续收集无边界写作技巧，进入候选正文生产。只有新的 hard fact、Canon contradiction、platform rule change、reader outcome 或 BLOCKER/HIGH 才重新打开架构；系统进化服务于作品，不以规则/Agent数量为成果。