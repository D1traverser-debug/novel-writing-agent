# Next Chapter Contract — Historical CH9 Design Source

chapter_no: 9
status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE
production_mode: FULL_FRONT_ARC_REBASE
previous_final_hash: fbdc1d4b2b37c905225f9abf2feb38bc8706732a8a1eb43b4fb12fa42015ba14
created_after_ch8: 2026-10-09
superseded_for_execution: 2026-10-11
superseded_by: audits/FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md

## Current execution meaning

This file is **not an executable READY next chapter contract while FULL_FRONT_ARC_REBASE is active**.

The strongest design payload below remains valuable source material, especially the Chen Du / Xu Zhiwei precommit-verification relationship. The full-rebase plan targets migration of that engine into the new front arc around the target CH7 region so the durable character/mainline engine arrives earlier.

Do not write old CH9 next. Do not discard this design. Re-architect the CH1–CH8 signing packet first; a new executable next-chapter contract is generated only after the replacement front arc is promoted.

---

## Historical Purpose
把陈渡/许知微从“第一次碰撞”推进到可持续的事实验证关系，同时继续第二单而不是切换新单元。核心问题不是让许知微相信明日达，而是：一个人声称提前知道信息时，怎样把事后解释变成可验证的时间证据。

## Historical Start state
- 10月8日01:47，二院急诊观察区外。
- 患者继续观察；当前只确认其可能从6Q73储物格取用了与自己常用包装/规格不完全一致的格列美脲，不能把药盒等同于最终诊断。
- 药盒旧标签姓名秦朗、日期约四个月前。患者称半个月前曾把自己的药落在同一储物格。
- 第二单01:30已逾期、明日达暂无即时反馈；疑似备用钥匙仍封存在B2值班点。
- 许知微已经确认：陈渡在看见药盒标签前说出了“秦朗”。

## Historical Must happen
- 陈渡回答“什么时候知道秦朗”：如实交代自己此前因一把车钥匙去找过秦朗、秦朗拒收，并交代可验证的现实时间链；不能用一句“我知道未来”替代事实。
- 许知微把“信息来源”与“事实真假”分开处理：即使不接受明日达，她也承认陈渡确实在标签揭示前掌握了秦朗姓名。
- 两人建立一个前瞻验证原则：如果陈渡以后再次声称提前知道某个具体事实，必须在验证前留下不可事后修改的时间记录/消息，而不是事后讲故事。
- 陈渡必须做一个人物选择：是否允许另一个人进入自己的验证链。选择应体现他对失控的厌恶与刚经历的现实后果，而不是轻易把秘密全盘托出。
- 继续推进T005/RP008/RP009：明确“患者已在订单出现前发作”这一事实，把第二单目标进一步从“阻止误服”剥离；但不能直接得出钥匙真实用途。
- 对“患者半个月前自称落过自己的药，而当前盒却是秦朗四个月前的旧盒”只形成可检验分支，不把记忆陈述当作已证实交换/投放。
- 许知微必须保留医生现实边界：病人优先，不能为了陈渡的谜题离岗调查停车场。

## Historical Must not happen
- 不让许知微在旧CH9就相信超自然、时间穿越或系统。
- 不把旧手机异常界面当成能被她直接验证的证据。
- 不开放医院数据库/监控/药房后台给陈渡。
- 不突然让秦朗赶到医院，不让顾行舟/幕后组织解释。
- 不新增明日达能力，不在10月9日00:11来源时点前强行结算第二单。
- 不把药盒事实直接定性为投毒、犯罪或故意换药。
- 不把许知微写成只会说金句的理性机器；她首先是正在值急诊的医生。

## Historical Scene engine
方法论审讯 + 现实时间线核对 + “是否允许别人验证自己”这一关系选择。强度低于事故章，但必须有关系和规则上的不可逆增量。

## Historical Hook
在许知微要求“下次先留下时间证据”之后，第二单的现实链出现一个新的可验证接口：不是系统提示，而是钥匙/药盒/当前车辆使用关系中某个现实人物或物件迫使陈渡继续行动。具体实现由ARCHITECT在新前段重构时重新竞争，不得机械照搬成旧CH9。