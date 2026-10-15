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


def test_canonical_evolution_entrypoint_preserves_prior_receipt_and_current_candidate():
    index = load_json("audits/EVOLUTION_INDEX.json")
    assert index["owner"] == "DOMAIN:novel"
    assert index["common_behavior_assurance_min"] == "1.2.0"
    assert index["current_open_items"] == ["N-20261015-02-LEARNING_TO_PLANNING_OS_REDESIGN"]
    assert index["current_problem_refs"]["N-20261015-02-LEARNING_TO_PLANNING_OS_REDESIGN"]["status"] == "CANDIDATE_EVALUATION"
    receipts = index["recent_resolved_or_promoted"]
    row = next(item for item in receipts if item["problem_ref"] == "N-20261015-01-UAOS_AUTHORITY_AND_BEHAVIOR_REPAIR")
    assert row["production_commit"] == "7cc56fbdca5139c2b61d0a16823d963693e9094c"
    assert row["production_ci_run"] == 38676046948
    assert row["result"] == "PASS"
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
