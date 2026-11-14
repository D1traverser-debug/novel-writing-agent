# CAOS Governance Entry — Novel Writing Agent

Status: CANDIDATE__NOT_MERGED
Effective date: 2026-11-15
Domain: NOVEL
Authority Context: DOMAIN:novel
Repository: D1traverser-debug/novel-writing-agent

## 1. Governance boundary

CAOS is the cross-project cognition and governance system for Novel work in the active ChatGPT session. Its source repository is `D1traverser-debug/cognition-agent-os`. Use the installed `cognition-parent-chatgpt-intake` Skill when available.

This entry is a Novel-owned integration contract. It does not copy the CAOS implementation, create a second controller, start a daemon, or add a CAOS runtime/API dependency.

**CAOS source is read-only.** Do not create, edit, delete, rename, merge, or otherwise mutate CAOS repository code, documentation, branches, pull requests, configuration, releases, or installed Skill assets.

Governance mode is `CHAT_GOVERNED_EXTERNAL`: CAOS governs complete-goal recovery, cross-layer root-cause investigation, research and comparison, decision rechallenge, execution discipline, independent acceptance and cross-domain learning in the active ChatGPT session. It does not create Novel task identities, own Novel business state, grant Novel permissions, or make automatic runtime calls.

## 2. Authority ownership

| Concern | Authority |
| --- | --- |
| Complete user-goal recovery, cross-layer root-cause investigation, external method research, competing alternatives, counterexample testing, decision rechallenge, execution governance, independent acceptance and cross-domain learning | CAOS governance in the active ChatGPT session |
| Novel task identity, exact project/checkpoint state, learning corpus/cursor, narrative evidence, story reselection, Plan, Canon, prose, release evidence, Rulebook and domain evolution | Novel Writing Agent |
| External publication, signing, deletion, payment, compliance and user-controlled platform facts | User / explicitly authorized external provider |

Novel remains the sole owner of `task_id`, `TASK_MANIFEST.json`, `CURRENT_CHECKPOINT.json`, learning cursor, Canon and prose. CAOS governance context is not a Novel business identity. No parent task ledger, lease, runtime proxy, business-state mirror or duplicate continuation system is introduced.

## 3. Startup protocol

For a new Novel task or continuation:

1. Activate CAOS governance in the current ChatGPT session for every material Novel task and every cross-project decision. If CAOS governance is unavailable, do not claim a CAOS-governed acceptance.
2. Read this file, `README.md`, `config/CAOS_GOVERNANCE.json`, `config/DOMAIN_CAPABILITIES.json`, `protocols/ACTIVE_RULEBOOK.md` and `protocols/NOVEL_PRODUCT_ARCHITECTURE.md`.
3. Resolve the exact Novel task from the Novel-owned task manifest and checkpoint; do not reconstruct business state from CAOS memory or historical controller records.
4. Read the exact `STUDY_STATE.json`, corpus, Canon, Plan and artifact slices needed for the requested action.
5. Apply Novel's learning, story-selection, Plan/Canon, prose, release and external-publication boundaries.
6. For material/systemic changes, use CAOS governance to challenge the complete goal, causal layers, methods, alternatives, counterexamples and verification plan before changing Novel-owned code or rules.
7. Verify actual Novel artifacts and user-visible outcomes independently. CI is engineering evidence, not proof of literary or commercial success.

## 4. Domain execution gates remain active

Novel's owner-native `runtime/owner_behavior_admission.py` and `runtime/deliberation_admission.py` remain narrow domain execution gates. They enforce Novel-specific recovery, material decision evidence, root-scope admission and its evidence-bearing receipt, typed evolution disposition and repair/no-change/block closure. They are not a second CAOS cognition controller and do not invoke a parent runtime.

Keep these separations:
- `LEARNING_EVIDENCE != ACTIVE_RULE`
- `STORY_CANDIDATE != ACTIVE_PROJECT_IDENTITY`
- `PLAN != CANON`
- `CANON != PROSE_SURFACE`
- `MODEL_SELF_EVALUATION != LIVE_READER_OR_PLATFORM_OUTCOME`
- `ROLE_SEPARATION != PROVIDER_ATTESTED_INDEPENDENCE`

## 5. Current business-state preservation

The governance migration does not change the Novel business cursor or project canon. The active masterwork remains `GUI_CHUI_DENG`, paused at the user-approved safe checkpoint after source line 3913; the next sequential location is source line 3914 in 《鬼吹灯I-1之精绝古城》第二十六章《天砖秘道》. After full-text completion, the D8–D11 claim-conditioned interbook learning cycle remains mandatory before `QING_YU_NIAN` can activate.

No replacement prose is authorized during the current masterwork study. Historical FQ001 remains a candidate/failure-evidence source with no incumbent privilege. The user-locked signing and serialization constraints remain unchanged.

## 6. Historical cleanup

The active UAOS manifest, adapter, capability profile and Skill are retired from the current Novel execution surface. Historical audits, migration records, prior CI evidence and Git history remain provenance only; they are not current startup instructions, business-state authorities or runtime dependencies.
