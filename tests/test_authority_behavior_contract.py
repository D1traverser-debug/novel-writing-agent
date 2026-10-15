from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_active_rulebook_uses_uaos_and_quarantines_retired_controller_semantics():
    rulebook = (ROOT / "protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
    assert "Parent control-plane authority: `D1traverser-debug/universal-agent-os@main`" in rulebook
    assert "Global discovery/routing/single-writer lease: `D1traverser-debug/universal-continuity-agent@main`" not in rulebook
    assert "verify this chat owns `active_lease + resume_epoch`" not in rulebook
    assert "No Novel-local lease, resume epoch or parallel controller is active" in rulebook
    assert "historical only and must never be required by current execution" in rulebook


def test_novel_adopts_common_behavior_1_2_with_owner_native_execution():
    caps = load_json(".uaos/CAPABILITIES.json")
    assert caps["schema_version"] == "2.2"
    assert caps["profile_version"] == 4
    assert caps["common_behavior_assurance_min"] == "1.2.0"
    assert caps["common_behavior_adoption"] == "OWNER_NATIVE_EXECUTABLE_ADMISSION_AND_TRAJECTORY_EVIDENCE"
    assert caps["canonical_evolution_evidence_ref"] == "audits/EVOLUTION_INDEX.json"
    capabilities = {row["capability_id"]: row for row in caps["capabilities"]}
    for cap_id in ("recover_before_user_escalation", "problem_to_action_closure"):
        assert capabilities[cap_id]["execution_ref"] == "runtime/owner_behavior_admission.py"


def test_canonical_evolution_entrypoint_is_novel_owned_and_event_scoped():
    index = load_json("audits/EVOLUTION_INDEX.json")
    assert index["owner"] == "DOMAIN:novel"
    assert index["common_behavior_assurance_min"] == "1.2.0"
    assert index["current_open_items"] == []
    assert index["current_problem_refs"] == {}
    receipts = index["recent_resolved_or_promoted"]
    row = next(item for item in receipts if item["problem_ref"] == "N-20261015-01-UAOS_AUTHORITY_AND_BEHAVIOR_REPAIR")
    assert row["status"] == "PROMOTED__PRODUCTION_CI_VERIFIED__LIVE_BEHAVIOR_OBSERVATION_OPEN"
    assert row["production_commit"] == "7cc56fbdca5139c2b61d0a16823d963693e9094c"
    assert row["production_ci_run"] == 38676046948
    assert row["production_ci_number"] == 289
    assert row["result"] == "PASS"
    assert "runtime/owner_behavior_admission.py" in index["execution_refs"]


def test_rulebook_points_to_executable_admission_and_evolution_entrypoint():
    rulebook = (ROOT / "protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
    assert "runtime/owner_behavior_admission.py" in rulebook
    assert "audits/EVOLUTION_INDEX.json" in rulebook
    assert "a detected repairable problem cannot end as recommendation-only" in rulebook
    assert "before externalizing a plausibly recoverable dependency to the user" in rulebook
