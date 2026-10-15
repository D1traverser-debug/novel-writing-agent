from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_active_rulebook_uses_uaos_and_quarantines_retired_controller_semantics():
    rulebook = (ROOT / "protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
    assert "parent_authority: D1traverser-debug/universal-agent-os@main" in rulebook
    assert "Global discovery/routing/single-writer lease: `D1traverser-debug/universal-continuity-agent@main`" not in rulebook
    assert "verify this chat owns `active_lease + resume_epoch`" not in rulebook
    assert "`universal-continuity-agent`, local leases and resume epochs are retired" in rulebook


def test_novel_adopts_common_behavior_1_2_and_profile_5_learning_to_planning_execution():
    caps = load_json(".uaos/CAPABILITIES.json")
    assert caps["schema_version"] == "2.4"
    assert caps["profile_version"] == 5
    assert caps["common_behavior_assurance_min"] == "1.2.0"
    assert caps["common_behavior_adoption"] == "OWNER_NATIVE_EXECUTABLE_ADMISSION_AND_TRAJECTORY_EVIDENCE"
    assert caps["canonical_evolution_evidence_ref"] == "audits/EVOLUTION_INDEX.json"
    capabilities = {row["capability_id"]: row for row in caps["capabilities"]}
    for cap_id in ("recover_before_user_escalation", "problem_to_action_closure"):
        assert capabilities[cap_id]["execution_ref"] == "runtime/owner_behavior_admission.py"
    assert capabilities["material_deliberation_admission"]["execution_ref"] == "runtime/deliberation_admission.py"
    assert capabilities["continual_cross_work_learning"]["execution_ref"] == "runtime/learning_transfer_admission.py"
    assert capabilities["zero_based_story_reselection"]["execution_ref"] == "runtime/story_reselection_admission.py"


def test_canonical_evolution_entrypoint_supports_resolved_production_receipt():
    index = load_json("audits/EVOLUTION_INDEX.json")
    assert index["owner"] == "DOMAIN:novel"
    assert index["common_behavior_assurance_min"] == "1.2.0"
    assert index["current_open_items"] == []
    assert index["current_problem_refs"] == {}

    receipts = index["recent_resolved_or_promoted"]
    prior = next(item for item in receipts if item["problem_ref"] == "N-20261015-01-UAOS_AUTHORITY_AND_BEHAVIOR_REPAIR")
    assert prior["production_commit"] == "7cc56fbdca5139c2b61d0a16823d963693e9094c"
    assert prior["production_ci_run"] == 38676046948
    assert prior["result"] == "PASS"

    current = next(item for item in receipts if item["problem_ref"] == "N-20261015-02-LEARNING_TO_PLANNING_OS_REDESIGN")
    assert current["status"] == "PROMOTED__PRODUCTION_CI_VERIFIED__LIVE_POST_RESELECTION_LITERARY_OUTCOME_OPEN"
    assert current["pull_request"] == 3
    assert current["candidate_final_head"] == "4d53781e5cdf0d2fe1e6ebe244b66dba35c4958e"
    assert current["candidate_ci_run"] == 38706239260
    assert current["candidate_ci_number"] == 305
    assert current["production_commit"] == "e0ec355f476830f77033ada08912d6c58f0bafe4"
    assert current["production_ci_run"] == 38706383327
    assert current["production_ci_number"] == 306
    assert current["result"] == "PASS"
    assert current["self_corrections"]
    assert "runtime/deliberation_admission.py" in index["execution_refs"]
    assert "runtime/story_reselection_admission.py" in index["execution_refs"]


def test_rulebook_and_skill_point_to_executable_learning_to_planning_admissions():
    rulebook = (ROOT / "protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
    skill = (ROOT / "UAOS_SKILL.md").read_text(encoding="utf-8")
    for ref in (
        "runtime/owner_behavior_admission.py",
        "runtime/deliberation_admission.py",
        "runtime/learning_transfer_admission.py",
        "runtime/story_reselection_admission.py",
        "runtime/dynamic_outline.py",
        "runtime/story_dependency_graph.py",
        "runtime/narrative_evaluation.py",
    ):
        assert ref in rulebook or ref in skill
    assert "recommendation-only" in rulebook
    assert "no incumbent privilege" in rulebook
