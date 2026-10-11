#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "projects/FQ001_MINGRI_ORDER"
sys.path.insert(0, str(ROOT / "runtime"))
from release_evidence_guard import validate_repository as validate_release_evidence

problems = []


def need(rel):
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
    return p

required = [
    "ENTRYPOINT.md","PROTOCOL.md","SKILL.md","AUTHORITY_STATUS.json","CONTINUITY_ADAPTER.json","TASK_INDEX.json",
    "continuity/TASK_INDEX.json","continuity/EXECUTION_CAPABILITIES.json","continuity/ARTIFACT_CONTEXT_GOVERNANCE.json",
    "continuity/UNIVERSAL_PROTOCOL_ADAPTER.json","protocols/ACTIVE_RULEBOOK.md","protocols/NOVEL_MASTERY_MODEL.md",
    "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md","research/masterworks/INDEX.json","research/masterworks/STUDY_STATE.json",
    "runtime/release_evidence_guard.py","runtime/masterwork_distillation_guard.py",
    "projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json","projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md",
    "projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json","projects/FQ001_MINGRI_ORDER/NEXT_CHAPTER_CONTRACT.md",
    "projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md","projects/FQ001_MINGRI_ORDER/PLATFORM_PUBLICATION_LOG.md",
    "projects/FQ001_MINGRI_ORDER/outline/SERIES_MASTER_OUTLINE.md","projects/FQ001_MINGRI_ORDER/outline/FRONT_ARC_REBASE_ARCHITECTURE_V1.md",
    "projects/FQ001_MINGRI_ORDER/outline/ARC_001.md",
    "projects/FQ001_MINGRI_ORDER/canon/CHARACTERS.json","projects/FQ001_MINGRI_ORDER/canon/CHARACTER_DRIVES.json",
    "projects/FQ001_MINGRI_ORDER/canon/THREADS.json","projects/FQ001_MINGRI_ORDER/canon/FORESHADOW.jsonl",
    "projects/FQ001_MINGRI_ORDER/canon/TIMELINE.jsonl","projects/FQ001_MINGRI_ORDER/canon/READER_PROMISES.json",
    "projects/FQ001_MINGRI_ORDER/manuscript/CH0008_FINAL.md","projects/FQ001_MINGRI_ORDER/reviews/CH0008_ACCEPTANCE.md",
    "audits/PLATFORM_SIGNING_SIGNAL_2026-10-11.md","audits/FRONT_ARC_SIGNING_REPAIR_MATRIX_2026-10-11.md",
    "audits/FULL_REBASE_LEARNING_EVIDENCE_2026-10-11.md","audits/FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md",
    "audits/NOVEL_MASTERY_EVOLUTION_2026-10-11.md","audits/FQ001_ARCHITECTURE_MASTERY_BENCHMARK_2026-10-11.md",
]
for rel in required:
    need(rel)

m = json.loads((TASK / "TASK_MANIFEST.json").read_text(encoding="utf-8"))
cp = json.loads((TASK / "checkpoints/CURRENT_CHECKPOINT.json").read_text(encoding="utf-8"))
expected_stage = "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING"
expected_next_serial_status = "HELD_DURING_MASTERWORK_DISTILLATION_AND_STORY_RESELECTION"

for f in ("task_id","current_stage","next_action","canon_version","last_final_chapter","last_final_hash","next_serial_chapter","next_serial_status"):
    if m.get(f) != cp.get(f):
        problems.append("checkpoint-drift:" + f)
if m.get("task_id") != "FQ001_MINGRI_ORDER":
    problems.append("task-id")
if m.get("status") != "ACTIVE" or cp.get("status") != "ACTIVE":
    problems.append("task-not-active")
if m.get("current_stage") != expected_stage:
    problems.append("study-stage")
if m.get("next_serial_status") != expected_next_serial_status:
    problems.append("study-next-serial-status")
if cp.get("production_mode") != "FULL_FRONT_ARC_REBASE":
    problems.append("historical-rebase-production-mode")

expected_hashes = {
    1:"79f1a1778c4023fe185606f0493d2019938b61f6cc8e5697408453302e0d0043",
    2:"2b77d75aabebda658023a9ad570d56337d9391ed8d39fd85bbdcfd89a7d382bb",
    3:"b586faa1643fa92f9c4b528b1f94e11f7d80fbad4a133d02ea1feb8006911b58",
    4:"636b88301bbfdd2d9a7b150afef69192879cc26109da5c95c898e271188bc853",
    5:"d18a02c0bbc51e5585179ae096e3f2452e1f48085b4d188ed37b6ada8fc2e507",
    6:"9207c149ec8a8acb50dff22dc53cf9e0c4f6b53f63f4bcef6b4f8487332c0810",
    7:"e7d1ef881b042a70fd699817763cb07c055b06fd7cf9412cc98209739fd539f8",
}
for n, h in expected_hashes.items():
    p = TASK / f"manuscript/CH{n:04d}_FINAL.md"
    if not p.exists():
        problems.append(f"missing-published:{n}")
    elif hashlib.sha256(p.read_bytes()).hexdigest() != h:
        problems.append(f"historical-final-hash:{n}")
if hashlib.sha256((TASK / "manuscript/CH0008_FINAL.md").read_bytes()).hexdigest() != m.get("last_final_hash"):
    problems.append("ch8-hash")

state_text = (TASK / "CURRENT_STATE.md").read_text(encoding="utf-8")
for token in (
    "canon_version: 12","last_final_chapter: 8","next_serial_chapter: 9",expected_stage,
    "SIGNING_MODE_IMMUTABLE","SERIALIZATION_MODE_IMMUTABLE","GUI_MI_ZHI_ZHU","EXCLUDED_BY_USER",
):
    if token not in state_text:
        problems.append("current-state:" + token)
if "CH8" not in state_text or "仍未确认" not in state_text:
    problems.append("publication-state")

study = json.loads((ROOT / "research/masterworks/STUDY_STATE.json").read_text(encoding="utf-8"))
registry = json.loads((ROOT / "research/masterworks/INDEX.json").read_text(encoding="utf-8"))
if study.get("study_policy", {}).get("mode") != "ONE_BOOK_AT_A_TIME":
    problems.append("study-policy")
if set(study.get("user_locked_business_constraints", [])) != {"SIGNING_MODE_IMMUTABLE","SERIALIZATION_MODE_IMMUTABLE"}:
    problems.append("locked-business-constraints")
if study.get("active_work", {}).get("work_id") != "GUI_MI_ZHI_ZHU":
    problems.append("active-masterwork")
if not any(w.get("work_id") == "SHIRI_ZHONGYAN" and w.get("status") == "COMPLETE" for w in study.get("queue", [])):
    problems.append("shiri-not-complete")
if not any(w.get("work_id") == "NORWEGIAN_WOOD" and w.get("status") == "EXCLUDED_BY_USER" for w in study.get("queue", [])):
    problems.append("norwegian-not-excluded")
if registry.get("active_studies", [{}])[0].get("work_id") != "GUI_MI_ZHI_ZHU":
    problems.append("registry-active-masterwork")
completed = {s.get("work_id"): s for s in registry.get("completed_studies", [])}
if completed.get("SHIRI_ZHONGYAN", {}).get("current_status") != "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING":
    problems.append("registry-shiri-completion")

contract = (TASK / "NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
if "chapter_no: 9" not in contract or "status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" not in contract or "Do not write old CH9 next" not in contract:
    problems.append("ch9-hold")

rebase = m.get("rebase", {})
cp_rebase = cp.get("rebase", {})
if rebase.get("authorized_by_user") is not True:
    problems.append("rebase-user-authorization")
if rebase.get("mode") != "CONTROLLED_FULL_FRONT_ARC_REBASE":
    problems.append("rebase-mode")
if rebase.get("execution_status") != "SUSPENDED_PENDING_POST_DISTILLATION_STORY_RESELECTION":
    problems.append("rebase-suspension")
if rebase.get("old_finals_role") != "IMMUTABLE_HISTORICAL_BASELINE":
    problems.append("rebase-old-finals-role")
if rebase.get("frozen_architecture_role") != "HISTORICAL_CANDIDATE_NOT_NEXT_ACTION":
    problems.append("rebase-architecture-role")
if rebase.get("candidate_promotion") != "BLOCKED_UNTIL_POST_DISTILLATION_STORY_RESELECTION":
    problems.append("rebase-promotion-block")
for f in ("authorized_by_user","scope","mode","execution_status","old_finals_role","old_chapter_boundaries_binding","old_ch9_contract_status","candidate_promotion","series_master_outline_ref","frozen_architecture_ref","frozen_architecture_role"):
    if cp_rebase.get(f) != rebase.get(f):
        problems.append("rebase-checkpoint-drift:" + f)

mastery = (ROOT / "protocols/NOVEL_MASTERY_MODEL.md").read_text(encoding="utf-8")
for token in [f"C{i:02d}" for i in range(1,21)]:
    if token not in mastery:
        problems.append("mastery-competency-missing:" + token)
for level in ("L0","L1","L2","L3","L4"):
    if level not in mastery:
        problems.append("mastery-level-missing:" + level)
mastery_state = m.get("mastery", {})
cp_mastery = cp.get("mastery", {})
for f in ("system_model_ref","series_master_outline_ref","front_arc_frozen_architecture_ref","project_benchmark_ref","architecture_gate","maximum_current_claim"):
    if cp_mastery.get(f) != mastery_state.get(f):
        problems.append("mastery-checkpoint-drift:" + f)

chars = json.loads((TASK / "canon/CHARACTERS.json").read_text(encoding="utf-8"))
threads = json.loads((TASK / "canon/THREADS.json").read_text(encoding="utf-8"))
prom = json.loads((TASK / "canon/READER_PROMISES.json").read_text(encoding="utf-8"))
if not any(c.get("name") == "许知微" and c.get("last_updated_chapter") == 8 for c in chars):
    problems.append("canon-characters")
if threads.get("T005", {}).get("last_progress_chapter") != 8:
    problems.append("canon-thread-T005")
if prom.get("version") != 6:
    problems.append("canon-promises")

idx = json.loads((ROOT / "continuity/TASK_INDEX.json").read_text(encoding="utf-8"))
alias = json.loads((ROOT / "TASK_INDEX.json").read_text(encoding="utf-8"))
adapter = json.loads((ROOT / "CONTINUITY_ADAPTER.json").read_text(encoding="utf-8"))
system = idx.get("system", {})
if system.get("system_id") != "NOVEL_OS" or system.get("active_project_task_id") != "FQ001_MINGRI_ORDER":
    problems.append("system-route")
if system.get("resume_behavior") != "ROUTE_TO_ACTIVE_PROJECT":
    problems.append("system-resume-behavior")
learning = system.get("masterwork_learning", {})
if learning.get("active_study") != "GUI_MI_ZHI_ZHU" or learning.get("study_state_ref") != "research/masterworks/STUDY_STATE.json":
    problems.append("system-learning-route")
active = {t.get("task_id"): t for t in idx.get("tasks", [])}.get("FQ001_MINGRI_ORDER", {})
if active.get("current_stage") != m.get("current_stage") or active.get("next_action") != m.get("next_action"):
    problems.append("task-index-state-drift")
if alias.get("tasks", [{}])[0].get("current_stage") != m.get("current_stage") or alias.get("tasks", [{}])[0].get("next_action") != m.get("next_action"):
    problems.append("compat-index-state-drift")
if alias.get("system", {}).get("masterwork_learning", {}).get("active_study") != "GUI_MI_ZHI_ZHU":
    problems.append("compat-learning-route")
topology = adapter.get("system_project_topology", {})
if topology.get("system_id") != "NOVEL_OS" or topology.get("routing_rule") != "SYSTEM_ALIAS_RESOLVES_OWNER_THEN_ACTIVE_PROJECT":
    problems.append("adapter-system-routing")

for failure in validate_release_evidence(ROOT):
    problems.append("release-evidence:" + failure)
cap = json.loads((ROOT / "continuity/EXECUTION_CAPABILITIES.json").read_text(encoding="utf-8"))
if cap.get("release_evidence_contract_version") != "1.0":
    problems.append("release-evidence-contract-version")
if not any(c.get("capability_id") == "masterwork_distillation_and_transfer_learning" for c in cap.get("capabilities", [])):
    problems.append("masterwork-capability-missing")

signing = m.get("platform_signing", {})
cp_signing = cp.get("platform_signing", {})
if signing.get("attempt_1") != "REJECTED_QUALITY_EVALUATION":
    problems.append("signing-attempt1-state")
if signing.get("next_application_threshold") != 50000 or signing.get("third_application_threshold_if_needed") != 80000:
    problems.append("signing-thresholds")
if signing.get("second_application_gate") != "SECOND_SIGNING_APPLICATION_REQUIRES_SIGNING_READINESS_AUDIT_PASS":
    problems.append("signing-second-gate")
for f in ("attempt_1","next_application_threshold","third_application_threshold_if_needed","second_application_gate"):
    if cp_signing.get(f) != signing.get(f):
        problems.append("signing-checkpoint-drift:" + f)

result = {
    "status": "PASS" if not problems else "FAIL",
    "task_id": m.get("task_id"),
    "system_id": system.get("system_id"),
    "stage": m.get("current_stage"),
    "next_action": m.get("next_action"),
    "active_masterwork": study.get("active_work", {}).get("work_id"),
    "completed_masterworks": [w.get("work_id") for w in study.get("completed_works", [])],
    "rebase_execution_status": rebase.get("execution_status"),
    "signing_attempt_1": signing.get("attempt_1"),
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
