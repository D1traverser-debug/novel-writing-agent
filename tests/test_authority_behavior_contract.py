from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_active_rulebook_uses_caos_external_governance_and_quarantines_retired_controller_semantics():
    rulebook = (ROOT / "protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
    assert "governance_authority: CAOS_CHAT_GOVERNED_EXTERNAL" in rulebook
    assert "CAOS governs cross-project cognition" in rulebook
    assert "D1traverser-debug/universal-agent-os@main" not in rulebook
    assert "Global discovery/routing/single-writer lease: `D1traverser-debug/universal-continuity-agent@main`" not in rulebook
    assert "verify this chat owns `active_lease + resume_epoch`" not in rulebook
    assert "`universal-continuity-agent`, local leases and resume epochs are retired" in rulebook


def test_novel_domain_capabilities_bind_caos_without_copying_or_inheriting_parent_runtime():
    caps = load_json("config/DOMAIN_CAPABILITIES.json")
    governance = load_json("config/CAOS_GOVERNANCE.json")
    assert caps["schema_version"] == "3.0"
    assert caps["profile_version"] == 8
    assert caps["domain_id"] == "novel"
    assert caps["caos_governance_ref"] == "config/CAOS_GOVERNANCE.json"
    assert caps["caos_governance_mode"] == "CHAT_GOVERNED_EXTERNAL__NO_RUNTIME_OR_API_DEPENDENCY"
    assert caps["canonical_evolution_evidence_ref"] == "audits/EVOLUTION_INDEX.json"
    assert "ROOT_SCOPE" in caps["common_behavior_adoption"]
    assert not any(key.startswith("uaos_") for key in caps)
    assert "required_uaos_common_capabilities" not in caps
    assert "hosted_cognition_semantics" not in caps
    assert governance["governance"]["system"] == "CAOS"
    assert governance["governance"]["mode"] == "CHAT_GOVERNED_EXTERNAL"
    assert governance["governance"]["runtime_dependency"] is False
    assert governance["governance"]["api_dependency"] is False
    assert governance["governance"]["source_mutation"] == "FORBIDDEN"
    boundary = governance["execution_boundary"]
    assert boundary["parent_task_identity"] is False
    assert boundary["parent_business_state_mirror"] is False
    assert boundary["runtime_upcall"] is False
    assert boundary["caos_permission_grant"] is False
    capabilities = {row["capability_id"]: row for row in caps["capabilities"]}
    for cap_id in ("recover_before_user_escalation", "problem_root_scope_admission", "problem_to_action_closure"):
        assert capabilities[cap_id]["execution_ref"] == "runtime/owner_behavior_admission.py"
    assert capabilities["material_deliberation_admission"]["execution_ref"] == "runtime/deliberation_admission.py"
    assert capabilities["continual_cross_work_learning"]["execution_ref"] == "runtime/learning_transfer_admission.py"
    assert capabilities["zero_based_story_reselection"]["execution_ref"] == "runtime/story_reselection_admission.py"


def test_canonical_evolution_preserves_prior_production_and_tracks_caos_migration_candidate():
    index = load_json("audits/EVOLUTION_INDEX.json")
    assert index["owner"] == "DOMAIN:novel"
    assert index["governance"]["system"] == "CAOS"
    assert index["governance"]["mode"] == "CHAT_GOVERNED_EXTERNAL"
    assert index["current_open_items"] == ["N-20261115-01-CAOS-GOVERNANCE-MIGRATION"]
    assert set(index["current_open_items"]) == set(index["current_problem_refs"])
    receipts = index["recent_resolved_or_promoted"]
    prior = next(item for item in receipts if item["problem_ref"] == "N-20261015-01-UAOS_AUTHORITY_AND_BEHAVIOR_REPAIR")
    assert prior["production_commit"] == "7cc56fbdca5139c2b61d0a16823d963693e9094c"
    assert prior["production_ci_run"] == 38676046948
    assert prior["result"] == "PASS"
    current = next(item for item in receipts if item["problem_ref"] == "N-20261015-02-LEARNING_TO_PLANNING_OS_REDESIGN")
    assert current["status"] == "PROMOTED__PRODUCTION_CI_VERIFIED__LIVE_POST_RESELECTION_LITERARY_OUTCOME_OPEN"
    assert current["pull_request"] == 3
    assert current["production_commit"] == "e0ec355f476830f77033ada08912d6c58f0bafe4"
    assert current["result"] == "PASS"
    migration = next(item for item in receipts if item["problem_ref"] == "N-20261115-01-CAOS-GOVERNANCE-MIGRATION")
    assert migration["status"] == "CANDIDATE__CI_PENDING"
    assert migration["historical_uaos_provenance"] == "PRESERVED_IN_DATED_AUDITS_AND_GIT_HISTORY_ONLY"


def test_rulebook_and_caos_entry_point_bind_executable_novel_domain_admissions():
    rulebook = (ROOT / "protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
    entry = (ROOT / "CAOS_NOVEL_ENTRY.md").read_text(encoding="utf-8")
    for ref in (
        "runtime/owner_behavior_admission.py",
        "runtime/deliberation_admission.py",
        "runtime/learning_transfer_admission.py",
        "runtime/story_reselection_admission.py",
        "runtime/dynamic_outline.py",
        "runtime/story_dependency_graph.py",
        "runtime/narrative_evaluation.py",
    ):
        assert ref in rulebook or ref in entry
    assert "root-scope receipt" in entry
    assert "typed evolution disposition" in entry
    assert "no incumbent privilege" in entry
    assert not (ROOT / "UAOS_SKILL.md").exists()
    assert not (ROOT / ".uaos").exists()


def test_artifact_governance_keeps_one_novel_business_authority_under_caos():
    gov = load_json("config/ARTIFACT_CONTEXT_GOVERNANCE.json")
    assert gov["business_owner"] == "NOVEL_WRITING_AGENT"
    assert gov["governance"]["system"] == "CAOS"
    assert gov["governance"]["mode"] == "CHAT_GOVERNED_EXTERNAL"
    assert gov["governance"]["runtime_dependency"] is False
    assert gov["canonical_artifact_or_file_stores"] == ["D1traverser-debug/novel-writing-agent@main"]
    assert "CAOS session governance metadata (not business state)" in gov["cache_or_reference_only_stores"]
    assert "universal-continuity-agent" not in json.dumps(gov, ensure_ascii=False)
    assert "UAOS discovery/controller metadata" not in json.dumps(gov, ensure_ascii=False)
