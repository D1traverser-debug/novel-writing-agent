#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
problems: list[str] = []


def load(rel: str):
    path = ROOT / rel
    if not path.exists():
        problems.append("missing:" + rel)
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def text(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        problems.append("missing:" + rel)
        return ""
    return path.read_text(encoding="utf-8")


manifest = load(".uaos/MANIFEST.json")
caps = load(".uaos/CAPABILITIES.json")
study = load("research/masterworks/STUDY_STATE.json")
corpus = load("research/masterworks/CORPUS_MAP.json")
evidence_schema = load("research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json")
cross = load("research/masterworks/CROSS_WORK_LEARNING_STATE.json")
registry = load("research/masterworks/MECHANISM_REGISTRY.json")
task = load("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
checkpoint = load("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
rulebook = text("protocols/ACTIVE_RULEBOOK.md")
mastery = text("protocols/NOVEL_MASTERY_MODEL.md")
learning_protocol = text("protocols/MASTERWORK_DISTILLATION_PROTOCOL.md")
architecture = text("protocols/NOVEL_PRODUCT_ARCHITECTURE.md")

# Authority/version alignment.
if caps.get("profile_version") != 5:
    problems.append("profile-not-5")
if "version: 2.5-github" not in rulebook:
    problems.append("rulebook-not-2.5")
if "version: 2.0" not in mastery:
    problems.append("mastery-not-2.0")
if "version: 2.1" not in learning_protocol:
    problems.append("masterwork-protocol-not-2.1")
if "version: 1.0" not in architecture:
    problems.append("product-architecture-not-1.0")

required_refs = {
    "product_architecture_ref": "protocols/NOVEL_PRODUCT_ARCHITECTURE.md",
    "narrative_evidence_schema_ref": "research/masterworks/NARRATIVE_EVIDENCE_SCHEMA.json",
    "material_deliberation_admission_ref": "runtime/deliberation_admission.py",
    "learning_transfer_admission_ref": "runtime/learning_transfer_admission.py",
    "story_reselection_admission_ref": "runtime/story_reselection_admission.py",
    "dynamic_outline_ref": "runtime/dynamic_outline.py",
    "story_dependency_graph_ref": "runtime/story_dependency_graph.py",
    "narrative_evaluation_ref": "runtime/narrative_evaluation.py",
}
for key, expected in required_refs.items():
    if manifest.get("domain_authority", {}).get(key) != expected:
        problems.append("manifest-ref:" + key)
    if not (ROOT / expected).is_file():
        problems.append("manifest-ref-missing:" + key)

# Exact study cursor and queue transition.
current = study.get("active_work", {})
if current.get("work_id") != "GUI_CHUI_DENG":
    problems.append("active-work")
if current.get("coverage", {}).get("next_location") != "源第3914行；继续第二十六章《天砖秘道》玉石王座场景":
    problems.append("cursor")
if current.get("completion_gate_after_fulltext") != "RUN_D8_D11_CLAIM_CONDITIONED_INTERBOOK_LEARNING_CYCLE_BEFORE_QING_YU_NIAN":
    problems.append("post-work-cycle-gate")
if not any(x.get("work_id") == "QING_YU_NIAN" and x.get("status") == "PENDING" for x in study.get("queue", [])):
    problems.append("next-work-not-pending")

# Claim-conditioned evidence, never fixed author/series family weighting.
if corpus.get("policy", {}).get("evidence_dependence_rule") != "CLAIM_CONDITIONED_AND_DIMENSION_SPECIFIC__NEVER_FIXED_BY_AUTHOR_OR_SERIES_ALONE":
    problems.append("dependency-policy")
for work in corpus.get("works", []):
    if any(key in work for key in ("evidence_family_id", "independent_vote", "independence_weight")):
        problems.append("fixed-independence-key:" + str(work.get("work_id")))
if evidence_schema.get("principle") != "EVIDENCE_DEPENDENCE_IS_CLAIM_CONDITIONED_AND_DIMENSION_SPECIFIC__NOT_A_FIXED_PROPERTY_OF_AUTHOR_WORK_OR_SERIES":
    problems.append("evidence-schema-principle")
if cross.get("learning_loop", {}).get("dependence_policy") != "NO_FIXED_FAMILY_WEIGHT__DEPENDENCE_IS_CLAIM_CONDITIONED_AND_DIMENSION_SPECIFIC":
    problems.append("cross-work-dependence-policy")
if registry.get("current_campaign_max_level") != "REFERENCE":
    problems.append("bootstrap-mechanisms-not-reference")
for row in registry.get("mechanisms", []):
    if "support_evidence_family_ids" in row:
        problems.append("fixed-family-returned:" + str(row.get("mechanism_id")))
    if row.get("active_rule"):
        problems.append("premature-active-rule:" + str(row.get("mechanism_id")))

# Historical FQ001 must remain evidence, not incumbent active identity.
if task.get("historical_project_identity", {}).get("role") != "HISTORICAL_CANDIDATE_AND_FAILURE_EVIDENCE__NO_INCUMBENT_PRIVILEGE":
    problems.append("task-incumbent-bias")
if checkpoint.get("story_reselection", {}).get("historical_fq001_role") != "MAY_COMPETE_AS_ONE_CANDIDATE__NO_INCUMBENT_PRIVILEGE":
    problems.append("checkpoint-incumbent-bias")
if cross.get("story_reselection", {}).get("status") != "BLOCKED_PENDING_FORMAL_CAMPAIGN_SYNTHESIS":
    problems.append("reselection-not-blocked")
if checkpoint.get("next_serial_status") != "HELD_DURING_MASTERWORK_DISTILLATION_AND_ZERO_BASED_STORY_RESELECTION":
    problems.append("prose-not-held")

# Architectural layer separation must remain explicit.
for invariant in (
    "LEARNING_EVIDENCE != ACTIVE_RULE",
    "STORY_CANDIDATE != ACTIVE_PROJECT_IDENTITY",
    "PLAN != CANON",
    "MODEL_SELF_EVALUATION != LIVE_READER_OR_PLATFORM_OUTCOME",
):
    if invariant not in text("UAOS_SKILL.md") and invariant not in architecture:
        problems.append("missing-invariant:" + invariant)

result = {
    "status": "PASS" if not problems else "FAIL",
    "profile": caps.get("profile_version"),
    "active_work": current.get("work_id"),
    "next_source_line": 3914,
    "evidence_model": "CLAIM_CONDITIONED_MULTIDIMENSIONAL",
    "story_reselection": cross.get("story_reselection", {}).get("status"),
    "failures": problems,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
