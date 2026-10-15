#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "projects/FQ001_MINGRI_ORDER"
sys.path.insert(0, str(ROOT / "runtime"))
from release_evidence_guard import validate_repository as validate_release_evidence

problems: list[str] = []


def need(rel: str) -> Path:
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
    return p


def load(rel: str) -> dict:
    p = need(rel)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


CURRENT_REQUIRED = [
    "UAOS_SKILL.md",
    ".uaos/MANIFEST.json",
    ".uaos/ADAPTER.json",
    ".uaos/CAPABILITIES.json",
    "config/ARTIFACT_CONTEXT_GOVERNANCE.json",
    "protocols/ACTIVE_RULEBOOK.md",
    "protocols/NOVEL_PRODUCT_ARCHITECTURE.md",
    "protocols/NOVEL_MASTERY_MODEL.md",
    "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md",
    "research/masterworks/STUDY_STATE.json",
    "research/masterworks/CORPUS_MAP.json",
    "research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json",
    "research/masterworks/CROSS_WORK_LEARNING_STATE.json",
    "research/masterworks/MECHANISM_REGISTRY.json",
    "runtime/owner_behavior_admission.py",
    "runtime/deliberation_admission.py",
    "runtime/learning_transfer_admission.py",
    "runtime/story_reselection_admission.py",
    "runtime/dynamic_outline.py",
    "runtime/story_dependency_graph.py",
    "runtime/narrative_evaluation.py",
    "runtime/release_evidence_guard.py",
    "runtime/masterwork_distillation_guard.py",
    "projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json",
    "projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md",
    "projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json",
    "projects/FQ001_MINGRI_ORDER/NEXT_CHAPTER_CONTRACT.md",
    "projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md",
    "projects/FQ001_MINGRI_ORDER/PLATFORM_PUBLICATION_LOG.md",
    "projects/FQ001_MINGRI_ORDER/manuscript/CH0008_FINAL.md",
    "projects/FQ001_MINGRI_ORDER/reviews/CH0008_ACCEPTANCE.md",
]
for rel in CURRENT_REQUIRED:
    need(rel)

RETIRED_ACTIVE_PATHS = [
    "ENTRYPOINT.md", "PROTOCOL.md", "SKILL.md", "TASK_INDEX.json", "CONTINUITY_ADAPTER.json",
    "AUTHORITY_STATUS.json", "continuity", "migration", "research/masterworks/INDEX.json",
]
for rel in RETIRED_ACTIVE_PATHS:
    if (ROOT / rel).exists():
        problems.append(f"retired-active-path-returned:{rel}")

uaos_manifest = load(".uaos/MANIFEST.json")
uaos_adapter = load(".uaos/ADAPTER.json")
caps = load(".uaos/CAPABILITIES.json")
gov = load("config/ARTIFACT_CONTEXT_GOVERNANCE.json")
m = load("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
cp = load("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
study = load("research/masterworks/STUDY_STATE.json")
cross = load("research/masterworks/CROSS_WORK_LEARNING_STATE.json")
corpus = load("research/masterworks/CORPUS_MAP.json")

if uaos_manifest.get("controller") != "D1traverser-debug/universal-agent-os@main" or uaos_manifest.get("status") != "UAOS_CONTROL_PLANE_ACTIVE":
    problems.append("uaos-manifest-controller-or-status")
if uaos_manifest.get("skill", {}).get("entrypoint") != "UAOS_SKILL.md":
    problems.append("uaos-skill-entry")
if uaos_adapter.get("task_identity_authority") != "UAOS" or uaos_adapter.get("cross_chat_continuity_authority") != "UAOS":
    problems.append("uaos-adapter-authority")
if uaos_adapter.get("legacy_controller_compatibility") != "NONE":
    problems.append("uaos-legacy-compatibility")
if gov.get("controller") != "D1traverser-debug/universal-agent-os@main":
    problems.append("artifact-governance-controller")
if caps.get("profile_version") != 6:
    problems.append("profile-version")
if caps.get("common_behavior_assurance_min") != "1.3.0":
    problems.append("common-behavior-min")

cap_ids = {c.get("capability_id") for c in caps.get("capabilities", [])}
for required_cap in {
    "project_recovery", "recover_before_user_escalation", "problem_root_scope_admission", "problem_to_action_closure",
    "material_deliberation_admission", "large_corpus_distillation", "continual_cross_work_learning",
    "zero_based_story_reselection", "draft_and_revision", "review_fanout", "release_and_canon_commit",
    "learning_promotion",
}:
    if required_cap not in cap_ids:
        problems.append("missing-capability:" + required_cap)

for f in ("task_id", "current_stage", "next_action", "canon_version", "last_final_chapter", "last_final_hash", "next_serial_chapter", "next_serial_status"):
    if m.get(f) != cp.get(f):
        problems.append("checkpoint-drift:" + f)
if m.get("task_id") != "FQ001_MINGRI_ORDER" or m.get("status") != "ACTIVE" or cp.get("status") != "ACTIVE":
    problems.append("task-identity-or-status")
if m.get("controller_authority") != "D1traverser-debug/universal-agent-os@main" or cp.get("controller_authority") != "D1traverser-debug/universal-agent-os@main":
    problems.append("controller-authority")
if m.get("controller_task_ref") != "state/tasks/FQ001_MINGRI_ORDER.json" or cp.get("controller_task_ref") != "state/tasks/FQ001_MINGRI_ORDER.json":
    problems.append("controller-task-ref")
for payload, label in ((m, "manifest"), (cp, "checkpoint")):
    if "continuity_protocol_version" in payload or "universal_lease_authority" in payload:
        problems.append(label + "-legacy-control-field")

expected_stage = "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__CLAIM_CONDITIONED_LEARNING__ZERO_BASED_STORY_RESELECTION_PENDING"
expected_serial_status = "HELD_DURING_MASTERWORK_DISTILLATION_AND_ZERO_BASED_STORY_RESELECTION"
if m.get("current_stage") != expected_stage or m.get("next_serial_status") != expected_serial_status:
    problems.append("learning-stage-or-serial-status")
if cp.get("production_mode") != "LEARNING_CAMPAIGN__HISTORICAL_PROJECT_FROZEN":
    problems.append("production-mode")

locks = {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}
if set(m.get("user_locked_business_constraints", [])) != locks or set(cp.get("user_locked_business_constraints", [])) != locks:
    problems.append("user-lock-scope")
if m.get("historical_project_identity", {}).get("role") != "HISTORICAL_CANDIDATE_AND_FAILURE_EVIDENCE__NO_INCUMBENT_PRIVILEGE":
    problems.append("historical-project-incumbent-drift")
if cp.get("story_reselection", {}).get("historical_fq001_role") != "MAY_COMPETE_AS_ONE_CANDIDATE__NO_INCUMBENT_PRIVILEGE":
    problems.append("checkpoint-incumbent-drift")

expected_hashes = {
    1: "79f1a1778c4023fe185606f0493d2019938b61f6cc8e5697408453302e0d0043",
    2: "2b77d75aabebda658023a9ad570d56337d9391ed8d39fd85bbdcfd89a7d382bb",
    3: "b586faa1643fa92f9c4b528b1f94e11f7d80fbad4a133d02ea1feb8006911b58",
    4: "636b88301bbfdd2d9a7b150afef69192879cc26109da5c95c898e271188bc853",
    5: "d18a02c0bbc51e5585179ae096e3f2452e1f48085b4d188ed37b6ada8fc2e507",
    6: "9207c149ec8a8acb50dff22dc53cf9e0c4f6b53f63f4bcef6b4f8487332c0810",
    7: "e7d1ef881b042a70fd699817763cb07c055b06fd7cf9412cc98209739fd539f8",
}
for n, expected in expected_hashes.items():
    p = TASK / f"manuscript/CH{n:04d}_FINAL.md"
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
        problems.append(f"historical-final-hash:{n}")
if hashlib.sha256((TASK / "manuscript/CH0008_FINAL.md").read_bytes()).hexdigest() != m.get("last_final_hash"):
    problems.append("ch8-hash")

current = study.get("active_work", {})
if current.get("work_id") != "GUI_CHUI_DENG" or current.get("status") != "ACTIVE__PAUSED_BY_USER_AT_SAFE_CHECKPOINT":
    problems.append("active-masterwork")
if current.get("coverage", {}).get("next_location") != "源第3914行；继续第二十六章《天砖秘道》玉石王座场景":
    problems.append("active-masterwork-next-location")
if current.get("next_pass") != "SEQUENTIAL_CONTINUE__JINGJUE_GUCHENG_CH26_FROM_SOURCE_LINE_3914":
    problems.append("active-masterwork-next-pass")
if current.get("completion_gate_after_fulltext") != "RUN_D8_D11_CLAIM_CONDITIONED_INTERBOOK_LEARNING_CYCLE_BEFORE_QING_YU_NIAN":
    problems.append("active-masterwork-completion-gate")
for payload, label in ((m, "manifest"), (cp, "checkpoint")):
    ml = payload.get("masterwork_learning", {})
    if ml.get("active_work") != current.get("work_id") or ml.get("active_work_status") != current.get("status"):
        problems.append(label + "-masterwork-binding-drift")
    if ml.get("completion_gate") != "RUN_D8_D11_CLAIM_CONDITIONED_INTERBOOK_LEARNING_CYCLE_BEFORE_QING_YU_NIAN":
        problems.append(label + "-interbook-cycle-gate")

queue = study.get("queue", [])
active_rows = [w for w in queue if w.get("status") == "ACTIVE"]
if len(active_rows) != 1 or active_rows[0].get("work_id") != "GUI_CHUI_DENG":
    problems.append("queue-active-binding")
if not any(w.get("work_id") == "QING_YU_NIAN" and w.get("status") == "PENDING" for w in queue):
    problems.append("qing-yu-nian-not-pending")
if not any(w.get("work_id") == "NORWEGIAN_WOOD" and w.get("status") == "EXCLUDED_BY_USER" for w in queue):
    problems.append("norwegian-not-excluded")

if cross.get("story_reselection", {}).get("status") != "BLOCKED_PENDING_FORMAL_CAMPAIGN_SYNTHESIS":
    problems.append("story-reselection-not-blocked")
if cross.get("learning_loop", {}).get("dependence_policy") != "NO_FIXED_FAMILY_WEIGHT__DEPENDENCE_IS_CLAIM_CONDITIONED_AND_DIMENSION_SPECIFIC":
    problems.append("dependency-model-drift")
if corpus.get("policy", {}).get("evidence_dependence_rule") != "CLAIM_CONDITIONED_AND_DIMENSION_SPECIFIC__NEVER_FIXED_BY_AUTHOR_OR_SERIES_ALONE":
    problems.append("corpus-dependence-drift")

contract = (TASK / "NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
if "chapter_no: 9" not in contract or "status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" not in contract or "Do not write old CH9 next" not in contract:
    problems.append("ch9-hold")

rebase = m.get("rebase", {})
for key, expected in {
    "authorized_by_user": True,
    "mode": "SUSPENDED_HISTORICAL_REBASE_CANDIDATE",
    "execution_status": "SUSPENDED_PENDING_POST_DISTILLATION_ZERO_BASED_STORY_RESELECTION",
    "old_finals_role": "IMMUTABLE_HISTORICAL_BASELINE",
    "candidate_promotion": "BLOCKED_UNTIL_POST_DISTILLATION_ZERO_BASED_STORY_RESELECTION",
}.items():
    if rebase.get(key) != expected:
        problems.append("rebase:" + key)
for key in cp.get("rebase", {}):
    if cp.get("rebase", {}).get(key) != rebase.get(key):
        problems.append("rebase-checkpoint-drift:" + key)

rulebook = (ROOT / "protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
if "version: 2.5-github" not in rulebook or "old FQ001" not in rulebook and "historical FQ001" not in rulebook:
    problems.append("rulebook-version-or-historical-boundary")
mastery = (ROOT / "protocols/NOVEL_MASTERY_MODEL.md").read_text(encoding="utf-8")
for token in [f"C{i:02d}" for i in range(1, 22)]:
    if token not in mastery:
        problems.append("mastery-competency-missing:" + token)
for level in ("L0", "L1", "L2", "L3", "L4"):
    if level not in mastery:
        problems.append("mastery-level-missing:" + level)

for failure in validate_release_evidence(ROOT):
    problems.append("release-evidence:" + failure)

result = {
    "status": "PASS" if not problems else "FAIL",
    "task_id": m.get("task_id"),
    "controller": uaos_manifest.get("controller"),
    "profile_version": caps.get("profile_version"),
    "stage": m.get("current_stage"),
    "active_masterwork": current.get("work_id"),
    "next_source_line": 3914,
    "story_reselection": cross.get("story_reselection", {}).get("status"),
    "historical_project_role": m.get("historical_project_identity", {}).get("role"),
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)