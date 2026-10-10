# Current State

project_id: FQ001_MINGRI_ORDER
canon_version: 12
last_final_chapter: 8
last_final_hash: fbdc1d4b2b37c905225f9abf2feb38bc8706732a8a1eb43b4fb12fa42015ba14
story_time: 10月8日 01:47
current_volume: 1
current_arc: 不能送错的人
production_mode: FULL_FRONT_ARC_REBASE
production_status: FULL_FRONT_ARC_REBASE_ACTIVE__SIGNING_PACKET_REARCHITECTURE
next_serial_chapter: 9
next_serial_status: HELD_DURING_FULL_FRONT_ARC_REBASE

## 当前权威判断

2026-10-11，用户明确允许当前小说前段整体退回重改。该授权改变了此前“尽量减少已发布正文迁移成本”的优化约束。

在重新执行 Universal Continuity 完整学习/维护方法（用户信号分类、M0–M11、证据分层、候选竞争、反证、复杂度预算、二阶挑战、supersession、回归计划）后，旧的逐章签约修复矩阵不再是 active 最优方案。

当前采用：`CONTROLLED_FULL_FRONT_ARC_REBASE`。

- active plan: `audits/FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md`
- learning evidence: `audits/FULL_REBASE_LEARNING_EVIDENCE_2026-10-11.md`
- old targeted matrix: `audits/FRONT_ARC_SIGNING_REPAIR_MATRIX_2026-10-11.md`，仅历史证据，已 superseded。

## 历史正文 / Canon 边界

- CH1–CH7：历史外部发布事实仍保留，系统**不会因为内部重构就推断平台已经撤回或替换**。
- CH8《药盒上的名字》：历史 FINAL_ACCEPTED / PUBLISH_READY，Canon v12；外部是否发布仍未确认。
- CH1–CH8 旧 FINAL 与旧 hash：保留为 `IMMUTABLE_HISTORICAL_BASELINE`，不删除、不改写历史证据。
- 当前 Canon v12：仍是事实起点。新架构可改变场景顺序/章节边界；若要改变人物已知事实、事件结果、系统规则或时间线，必须走正式 Retcon/Canon reconciliation。
- 旧CH9合同已改为 `SUPERSEDED_BY_FULL_FRONT_ARC_REBASE`，不可直接执行；其“陈渡/许知微建立前瞻验证关系”设计作为高价值素材迁入新前段目标CH7附近。

## 当前前段重构目标

把旧CH1–CH8约2万字视作一个完整的“签约/读者获取阅读包”重新架构，不再逐章局部打补丁。

当前八章目标架构：
1. CH1：更快进入明日达、自我订单、死亡时间；保留最少但足够的未来真实性证明。
2. CH2：168普通订单与死亡窗口相撞；压缩机构验证；匿名“不要提前送达”干预前移。
3. CH3：完成第一单23:46重大 payoff，陈渡活下来，有真实余波；结算6.8%/未来信用并开启第二单。
4. CH4：钥匙/B2/车辆错位 + 秦朗拒收，人物冲突为主。
5. CH5：当前驾驶人/备用钥匙责任冲突 + 药盒钩子。
6. CH6：药盒秦朗标签 + 许知微正式进入持续主线；确认陈渡提前知道姓名；患者发作早于第二单。
7. CH7：迁入旧CH9的强设计——建立可前置、可证伪的事实验证关系；陈渡作出是否让另一个人进入验证链的关系选择。
8. CH8：第二单/验证关系产生新的后果或 reframe，形成完整单元 payoff + 下一单元强承诺，而不是只停在另一个调查起点。

章数/边界是当前项目 prototype，不是不可改的公式；Architecture/Reader review 可以在证据支持下调整。

## 作品身份不变

- 都市脑洞 × 悬疑单元剧 × 城市群像。
- 第三人称限知陈渡。
- 现代城市真实运行质感；超常只开一扇小口。
- 陈渡靠城市/路线/临场判断而非全知推理。
- 未来信息有用但不完整；修改未来会迁移风险。
- 核心人物轴改用“小人物选择与后果”，不再把“小人物逆袭”当必须兑现的财富/地位承诺。

## 主要人物历史状态（作为重构素材/Canon参考）
- 陈渡：10月8日01:47，在二院急诊观察区外；第二单逾期，疑似备用钥匙仍封存在B2值班点。他确认患者在订单出现前已经发作，正在面对许知微对“为何提前知道秦朗”的追问。
- 许知微：二院急诊医生；不相信超自然，只承认可验证事实。历史CH8确认陈渡在药盒标签可见前说出秦朗。
- 秦朗：四个月前已交回6Q73，拒收原因未知；其姓名出现在6Q73储物格的一盒旧药上。
- 董哥：6Q73当前驾驶/使用人之一，持工作钥匙，不认识秦朗。

这些事实是当前 Canon 起点；新前段可以调整揭示顺序，但不能无记录地改变事实本身。

## 平台签约状态 / 战略硬门

- 首次签约评估：`NOT_APPROVED / REJECTED_QUALITY_EVALUATION`。
- 可见原因：泛化“签约质量要求未达到”；无更细粒度编辑原因。
- 不得推断为AI检测、安全审核、抄袭、侵权或其他隐藏原因。
- 第二次标准机会：当前规则约5万字。
- 若第二次仍拒绝，当前规则约8万字还有第三次机会。
- 二签硬门：`SECOND_SIGNING_APPLICATION_REQUIRES_SIGNING_READINESS_AUDIT_PASS`。
- 禁止：不修 acquisition/front arc，只靠字数继续冲5万。
- 实际番茄撤回/替换/发布属于用户控制的外部动作；内部候选通过不等于平台已替换。

## 当前执行边界

- CH9 execution：HOLD。
- 旧CH1–CH8：历史基线，不直接覆盖。
- 下一阶段先完成新 front-arc architecture 的 packet-level validation，然后再开始 coherent candidate rewrite。
- 新候选正文必须在 whole-packet gates 通过前保持 candidate；不允许“改完第一章就把它单独变成新FINAL”。
- future CH9+/replacement release 仍执行 execution-evidence contract v1；CHAT_BRIDGED receipts 不得被描述为独立执行 attestation。

## 下一步

冻结并引用旧CH1–CH8作为历史基线；以 `FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md` 为当前结构计划，先完成新签约阅读包架构的挑战/验证，然后按统一架构重写候选CH1–CH8。完成 whole-packet Continuity / Fresh Reader / Retention / Editorial / Adversarial / Signing Readiness 审核前，不晋升替换正文，不执行旧CH9，不消耗5万字二签机会。