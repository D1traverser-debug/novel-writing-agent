#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
problems: list[str] = []
TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"
ACTIVE_STATUSES = {
    "ACTIVE__PENDING_FIRST_SEQUENTIAL_READ",
    "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS",
    "ACTIVE__PAUSED_BY_USER_AT_SAFE_CHECKPOINT",
}
VALID_STATUSES = ACTIVE_STATUSES | {TERMINAL}


def need(rel: str) -> Path:
    p = ROOT / rel
    if not p.exists():
        problems.append(f"missing:{rel}")
    return p


def load(rel: str) -> dict:
    p = need(rel)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


protocol_p = need("protocols/MASTERWORK_DISTILLATION_PROTOCOL.md")
state = load("research/masterworks/STUDY_STATE.json")
corpus = load("research/masterworks/CORPUS_MAP.json")
evidence_schema = load("research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json")
cross = load("research/masterworks/CROSS_WORK_LEARNING_STATE.json")
registry = load("research/masterworks/MECHANISM_REGISTRY.json")
caps = load(".uaos/CAPABILITIES.json")

for rel in [
    "research/masterworks/CROSS_WORK_PROVISIONAL_SYNTHESIS_2026-10-15.md",
    "runtime/deliberation_admission.py",
    "runtime/learning_transfer_admission.py",
    "runtime/story_reselection_admission.py",
    "runtime/dynamic_outline.py",
    "runtime/story_dependency_graph.py",
    "runtime/narrative_evaluation.py",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_02_OPENING_MICROCRAFT.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_03_CHARACTER_ENSEMBLE.md",
    "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_04_MYSTERY_WORLD_RULES.md",
    "research/masterworks/SHIRI_ZHONGYAN/FULLTEXT_CORPUS_INGEST_2026-10-11.md",
]:
    need(rel)

if protocol_p.exists():
    protocol = protocol_p.read_text(encoding="utf-8")
    if "version: 2.1" not in protocol or "status: ACTIVE_SYSTEM_PROTOCOL" not in protocol:
        problems.append("protocol-version-or-status")
    for stage in (
        "D0 RIGHTS_AND_SOURCE",
        "D3 COLD_READ_TRACE",
        "D5 MICROCRAFT_ANNOTATION",
        "D6 POSITIVE_NEGATIVE_DIFF",
        "D7 ABLATION / COUNTERFACTUAL",
        "D8 CLOSED_CONTEXT_RECONSTRUCTION",
        "D9 CLAIM-CONDITIONED CROSS-WORK TRIANGULATION",
        "D10 PROJECT_TRANSFER_EXPERIMENT",
        "D11 ADVERSARIAL_REVIEW",
        "D12 PROMOTION",
        "D13 STOP / DECAY",
        "D14 CAMPAIGN_SYNTHESIS_AND_STORY_RESELECTION",
    ):
        if stage not in protocol:
            problems.append("protocol-stage:" + stage)

if state.get("status") != "ACTIVE":
    problems.append("study-state-not-active")
if state.get("authority_role") != "SYSTEM_LEARNING_CHECKPOINT_NOT_PROSE_OR_CANON_AUTHORITY":
    problems.append("study-state-authority-role")
policy = state.get("study_policy", {})
expected_policy = {
    "mode": "ONE_BOOK_AT_A_TIME",
    "rule": "COMPLETE_CURRENT_WORK_BEFORE_NEXT",
    "interbook_comparison": "AFTER_EACH_COMPLETED_WORK__NON_PROMOTIONAL",
    "formal_cross_work_synthesis": "DEFER_ACTIVE_RULE_PROMOTION_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE",
    "closed_context_reconstruction": "REQUIRED_AFTER_EACH_COMPLETED_WORK_BEFORE_LEDGER_REOPEN",
    "transfer_probe": "REQUIRED_AFTER_EACH_COMPLETED_WORK_BEFORE_QUEUE_ADVANCE",
    "source_scope": "USER_PROVIDED_STANDARDIZED_TEXT_ONLY_UNLESS_USER_EXPLICITLY_EXPANDS_SCOPE",
}
for key, value in expected_policy.items():
    if policy.get(key) != value:
        problems.append("study-policy:" + key)
if set(state.get("user_locked_business_constraints", [])) != {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}:
    problems.append("user-locked-constraints")

active_work = state.get("active_work") or {}
work_id = active_work.get("work_id")
active_status = active_work.get("status")
next_pass = active_work.get("next_pass")
if not work_id:
    problems.append("study-state-active-work-missing")
if active_status not in VALID_STATUSES:
    problems.append("study-state-active-status")
if active_status == "ACTIVE__PENDING_FIRST_SEQUENTIAL_READ" and next_pass != "SEQUENTIAL_FULLTEXT_FROM_BEGINNING":
    problems.append("study-state-initial-next-pass")
if active_status in {"ACTIVE__SEQUENTIAL_READ_IN_PROGRESS", "ACTIVE__PAUSED_BY_USER_AT_SAFE_CHECKPOINT"}:
    if not isinstance(next_pass, str) or not next_pass.startswith("SEQUENTIAL_CONTINUE__"):
        problems.append("study-state-progress-next-pass")
    coverage = active_work.get("coverage", {})
    if not re.fullmatch(r"[0-9a-f]{64}", active_work.get("source_sha256", "")):
        problems.append("study-state-source-sha256")
    if not re.fullmatch(r"[0-9a-f]{64}", active_work.get("rolling_ledger_sha256", "")):
        problems.append("study-state-ledger-sha256")
    if not coverage.get("sequential_completed") or not coverage.get("next_location"):
        problems.append("study-state-coverage")
    if not active_work.get("rolling_ledger_file_id"):
        problems.append("study-state-rolling-ledger-id")
if work_id == "GUI_CHUI_DENG":
    if active_work.get("coverage", {}).get("next_location") != "源第3914行；继续第二十六章《天砖秘道》玉石王座场景":
        problems.append("gui-chui-deng-cursor-drift")
    if active_work.get("completion_gate_after_fulltext") != "RUN_D8_D11_CLAIM_CONDITIONED_INTERBOOK_LEARNING_CYCLE_BEFORE_QING_YU_NIAN":
        problems.append("gui-chui-deng-post-completion-gate")

queue = state.get("queue", [])
queue_by_id = {w.get("work_id"): w for w in queue}
if work_id not in queue_by_id:
    problems.append("active-work-not-in-queue")
active_queue = [w for w in queue if w.get("status") == "ACTIVE"]
if active_status in ACTIVE_STATUSES and (len(active_queue) != 1 or active_queue[0].get("work_id") != work_id):
    problems.append("queue-active-binding")
if active_status == TERMINAL and (queue_by_id.get(work_id, {}).get("status") != "COMPLETE" or active_queue):
    problems.append("queue-terminal-binding")
if not any(w.get("work_id") == "NORWEGIAN_WOOD" and w.get("status") == "EXCLUDED_BY_USER" for w in queue):
    problems.append("queue-norwegian-excluded")

queue_complete_ids = {w.get("work_id") for w in queue if w.get("status") == "COMPLETE"}
state_complete_ids = {w.get("work_id") for w in state.get("completed_works", [])}
if queue_complete_ids != state_complete_ids:
    problems.append("completed-work-summary-drift")
if active_status in ACTIVE_STATUSES and work_id in state_complete_ids:
    problems.append("active-work-also-completed")
if active_status == TERMINAL and work_id not in state_complete_ids:
    problems.append("terminal-work-not-completed")

corpus_rows = corpus.get("works", [])
corpus_by_id = {w.get("work_id"): w for w in corpus_rows}
if set(queue_by_id) != set(corpus_by_id):
    problems.append("corpus-map-queue-coverage-drift")
for qid, qrow in queue_by_id.items():
    crow = corpus_by_id.get(qid, {})
    if qrow.get("no") != crow.get("queue_no") or qrow.get("title") != crow.get("title"):
        problems.append("corpus-map-identity-drift:" + str(qid))
    if crow.get("queue_status") != qrow.get("status"):
        problems.append("corpus-map-status-drift:" + str(qid))
    forbidden = {"evidence_family_id", "independence_weight", "independent_vote"}
    if forbidden.intersection(crow):
        problems.append("corpus-map-fixed-independence-key:" + str(qid))
if corpus.get("policy", {}).get("evidence_dependence_rule") != "CLAIM_CONDITIONED_AND_DIMENSION_SPECIFIC__NEVER_FIXED_BY_AUTHOR_OR_SERIES_ALONE":
    problems.append("corpus-map-dependence-policy")

if evidence_schema.get("principle") != "EVIDENCE_DEPENDENCE_IS_CLAIM_CONDITIONED_AND_DIMENSION_SPECIFIC__NOT_A_FIXED_PROPERTY_OF_AUTHOR_WORK_OR_SERIES":
    problems.append("narrative-evidence-schema-principle")
dimension_ids = {row.get("id") for row in evidence_schema.get("narrative_dimensions", [])}
required_dimensions = {
    "N01_STORY_FABULA_CAUSAL_ENGINE", "N02_DISCOURSE_TEMPORAL_ORDER", "N03_NARRATOR_POV_FOCALIZATION",
    "N04_CHARACTER_CONSTRUCTION_AGENCY", "N05_RELATIONSHIP_NETWORK_ARCS", "N06_WORLD_SETTING_INSTITUTIONS",
    "N07_INFORMATION_MYSTERY_REVELATION", "N08_EMOTION_TENSION_READER_AFFECT", "N09_PACING_RHYTHM_PAGE_COST",
    "N10_DIALOGUE_VOICE_SUBTEXT", "N11_PROSE_STYLOMETRY_SURFACE", "N12_SERIAL_ENGINE_ESCALATION_PAYOFF",
    "N13_ACQUISITION_PRODUCT_PLATFORM", "N14_THEME_VALUE_CONFLICT", "N15_SPACE_ENVIRONMENT_ACTION",
    "N16_READER_MEMORY_COGNITIVE_LOAD",
}
if not required_dimensions.issubset(dimension_ids):
    problems.append("narrative-evidence-schema-dimensions")
comparison_ids = {row.get("id") for row in evidence_schema.get("comparison_designs", [])}
for needed in {"WITHIN_AUTHOR_CROSS_WORK", "WITHIN_SERIES_CROSS_STAGE", "CROSS_AUTHOR_SAME_OR_ADJACENT_GENRE", "CROSS_GENRE_SAME_FUNCTION"}:
    if needed not in comparison_ids:
        problems.append("narrative-evidence-schema-comparison:" + needed)

if cross.get("status") != "ACTIVE_CAMPAIGN":
    problems.append("cross-work-state-not-active")
if cross.get("current_gate", {}).get("active_work") != work_id:
    problems.append("cross-work-active-binding")
if cross.get("learning_loop", {}).get("interim_promotion_policy") != "NON_PROMOTIONAL__REFERENCE_ONLY_UNTIL_DEPENDENCY_REVIEW__THEN_EXPERIMENTAL":
    problems.append("cross-work-interim-promotion-policy")
if cross.get("formal_campaign_synthesis", {}).get("status") != "BLOCKED_UNTIL_ALL_NON_EXCLUDED_QUEUE_WORKS_COMPLETE":
    problems.append("cross-work-formal-synthesis-gate")
if cross.get("story_reselection", {}).get("status") != "BLOCKED_PENDING_FORMAL_CAMPAIGN_SYNTHESIS":
    problems.append("story-reselection-premature")
if cross.get("story_reselection", {}).get("historical_fq001_role") != "ONE_CANDIDATE_OR_EVIDENCE_SOURCE_ONLY__NO_INCUMBENT_PRIVILEGE":
    problems.append("historical-fq001-incumbent-privilege")

if registry.get("current_campaign_max_level") != "REFERENCE":
    problems.append("mechanism-registry-campaign-ceiling")
for mechanism in registry.get("mechanisms", []):
    if not mechanism.get("target_dimensions"):
        problems.append("mechanism-target-dimensions-missing:" + str(mechanism.get("mechanism_id")))
    if any(dim not in dimension_ids for dim in mechanism.get("target_dimensions", [])):
        problems.append("mechanism-unknown-dimension:" + str(mechanism.get("mechanism_id")))
    if "support_evidence_family_ids" in mechanism:
        problems.append("mechanism-fixed-family-model-returned:" + str(mechanism.get("mechanism_id")))
    if mechanism.get("active_rule"):
        problems.append("premature-active-rule:" + str(mechanism.get("mechanism_id")))
    if mechanism.get("status") != "REFERENCE":
        problems.append("premature-mechanism-promotion:" + str(mechanism.get("mechanism_id")))

required_caps = {"large_corpus_distillation", "continual_cross_work_learning", "material_deliberation_admission", "zero_based_story_reselection"}
cap_by_id = {c.get("capability_id"): c for c in caps.get("capabilities", [])}
missing_caps = required_caps - set(cap_by_id)
if missing_caps:
    problems.append("uaos-learning-capabilities-missing:" + ",".join(sorted(missing_caps)))
large = cap_by_id.get("large_corpus_distillation", {})
if not {"source_identity", "coverage_cursor", "rolling_ledger", "single_work_context_isolation"}.issubset(set(large.get("required", []))):
    problems.append("uaos-large-corpus-capability-contract")
continual = cap_by_id.get("continual_cross_work_learning", {})
if not {
    "multidimensional_evidence_schema", "claim_conditioned_dependency_assessment", "comparison_design",
    "shared_factor_assessment", "closed_context_reconstruction", "non_promotional_interbook_comparison",
    "alternative_explanations", "negative_or_boundary_evidence", "transfer_probe", "mechanism_registry",
}.issubset(set(continual.get("required", []))):
    problems.append("uaos-continual-learning-capability-contract")

if (ROOT / "continuity").exists() or (ROOT / "TASK_INDEX.json").exists() or (ROOT / "research/masterworks/INDEX.json").exists():
    problems.append("retired-learning-index-returned")

result = {
    "status": "PASS" if not problems else "FAIL",
    "protocol": "MASTERWORK_DISTILLATION_PROTOCOL@2.1",
    "evidence_model": "CLAIM_CONDITIONED_MULTIDIMENSIONAL_DEPENDENCY_GRAPH",
    "active_study_binding": work_id,
    "active_status": active_status,
    "completed_studies": sorted(queue_complete_ids),
    "next_pass": next_pass,
    "cross_work_learning": cross.get("status"),
    "story_reselection": cross.get("story_reselection", {}).get("status"),
    "assurance": "SEQUENTIAL_SOURCE_COVERAGE__MULTIDIMENSIONAL_COMPARISON__DEPENDENCY_CHALLENGE__TRANSFER_GATED__STORY_RESELECTION_BLOCKED_UNTIL_CAMPAIGN_COMPLETE",
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
