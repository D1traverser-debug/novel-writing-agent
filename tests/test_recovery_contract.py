from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parents[1]
TASK=ROOT/"projects/FQ001_MINGRI_ORDER"


def test_recovery_truth():
    m=json.loads((TASK/"TASK_MANIFEST.json").read_text())
    cp=json.loads((TASK/"checkpoints/CURRENT_CHECKPOINT.json").read_text())
    assert m["task_id"]=="FQ001_MINGRI_ORDER"
    assert m["status"]=="ACTIVE"
    assert cp["status"]=="ACTIVE"
    assert m["last_final_chapter"]==8
    assert m["next_serial_chapter"]==9
    assert m["next_serial_status"]=="HELD_DURING_FULL_FRONT_ARC_REBASE"
    assert cp["production_mode"]=="FULL_FRONT_ARC_REBASE"
    assert m["current_stage"]=="FULL_FRONT_ARC_REBASE_ACTIVE__SIGNING_PACKET_REARCHITECTURE"
    assert m["current_stage"]==cp["current_stage"]
    assert m["next_action"]==cp["next_action"]
    assert m["external_publication"]["confirmed_published_through"]==7


def test_historical_final_hashes_are_preserved_during_rebase():
    m=json.loads((TASK/"TASK_MANIFEST.json").read_text())
    assert hashlib.sha256((TASK/"manuscript/CH0008_FINAL.md").read_bytes()).hexdigest()==m["last_final_hash"]
    expected={1:"79f1a1778c4023fe185606f0493d2019938b61f6cc8e5697408453302e0d0043",2:"2b77d75aabebda658023a9ad570d56337d9391ed8d39fd85bbdcfd89a7d382bb",3:"b586faa1643fa92f9c4b528b1f94e11f7d80fbad4a133d02ea1feb8006911b58",4:"636b88301bbfdd2d9a7b150afef69192879cc26109da5c95c898e271188bc853",5:"d18a02c0bbc51e5585179ae096e3f2452e1f48085b4d188ed37b6ada8fc2e507",6:"9207c149ec8a8acb50dff22dc53cf9e0c4f6b53f63f4bcef6b4f8487332c0810",7:"e7d1ef881b042a70fd699817763cb07c055b06fd7cf9412cc98209739fd539f8"}
    for n,h in expected.items():
        assert hashlib.sha256((TASK/f"manuscript/CH{n:04d}_FINAL.md").read_bytes()).hexdigest()==h


def test_ch9_is_held_and_its_strong_design_is_migration_source():
    c=(TASK/"NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
    assert "chapter_no: 9" in c
    assert "status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" in c
    assert "production_mode: FULL_FRONT_ARC_REBASE" in c
    assert "Do not write old CH9 next" in c
    assert "许知微" in c
    assert "precommit" in c.lower()


def test_full_front_arc_rebase_is_durable_and_old_patch_plan_is_superseded():
    m=json.loads((TASK/"TASK_MANIFEST.json").read_text())
    cp=json.loads((TASK/"checkpoints/CURRENT_CHECKPOINT.json").read_text())
    rebase=m["rebase"]
    assert rebase["authorized_by_user"] is True
    assert rebase["scope"]=="CH1-CH8_FRONT_ARC"
    assert rebase["mode"]=="CONTROLLED_FULL_FRONT_ARC_REBASE"
    assert rebase["old_finals_role"]=="IMMUTABLE_HISTORICAL_BASELINE"
    assert rebase["old_chapter_boundaries_binding"] is False
    assert rebase["old_ch9_contract_status"]=="SUPERSEDED_BY_FULL_FRONT_ARC_REBASE"
    assert rebase["candidate_promotion"]=="WHOLE_PACKET_GATES_BEFORE_AUTHORITATIVE_REPLACEMENT"
    assert cp["rebase"]["mode"]==rebase["mode"]
    assert (ROOT/rebase["plan_ref"]).exists()
    assert (ROOT/rebase["learning_evidence_ref"]).exists()
    old=(ROOT/"audits/FRONT_ARC_SIGNING_REPAIR_MATRIX_2026-10-11.md").read_text(encoding="utf-8")
    plan=(ROOT/rebase["plan_ref"]).read_text(encoding="utf-8")
    learning=(ROOT/rebase["learning_evidence_ref"]).read_text(encoding="utf-8")
    assert "SUPERSEDED_FOR_ACTIVE_EXECUTION" in old
    assert "M0 — Intake" in plan and "M11 — Durable learning" in plan
    assert "CONTROLLED_FULL_FRONT_ARC_REBASE" in learning


def test_project_profile_exposes_rebase_not_old_frozen_baseline_as_active_architecture():
    p=(TASK/"PROJECT_PROFILE.md").read_text(encoding="utf-8")
    assert "production_mode: FULL_FRONT_ARC_REBASE" in p
    assert "baseline: HISTORICAL_FINAL_CH01_CH08__REBASE_AUTHORIZED" in p
    assert "next_serial_status: HELD_DURING_FULL_FRONT_ARC_REBASE" in p
    assert "Full front-arc rebase objective" in p
    assert "HISTORICAL_SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" in p


def test_novel_os_routes_to_active_project_without_duplicate_task():
    idx=json.loads((ROOT/"continuity/TASK_INDEX.json").read_text())
    system=idx["system"]
    assert system["system_id"]=="NOVEL_OS"
    assert system["display_name_zh"]=="小说系统"
    assert system["resume_behavior"]=="ROUTE_TO_ACTIVE_PROJECT"
    assert system["active_project_task_id"]=="FQ001_MINGRI_ORDER"
    assert "小说系统" in system["resume_aliases"]
    assert "NOVEL_OS" in system["resume_aliases"]
    tasks=[t for t in idx["tasks"] if t["task_id"]=="FQ001_MINGRI_ORDER"]
    assert len(tasks)==1
    assert tasks[0]["is_active_project"] is True
    assert tasks[0]["system_id"]=="NOVEL_OS"
    assert tasks[0]["candidate_label_zh"]=="小说系统｜《凌晨零点，我接到明天的订单》"
    assert tasks[0]["current_stage"]=="FULL_FRONT_ARC_REBASE_ACTIVE__SIGNING_PACKET_REARCHITECTURE"


def test_continuity_adapter_system_project_semantics():
    adapter=json.loads((ROOT/"CONTINUITY_ADAPTER.json").read_text())
    topology=adapter["system_project_topology"]
    assert topology["system_id"]=="NOVEL_OS"
    assert topology["routing_rule"]=="SYSTEM_ALIAS_RESOLVES_OWNER_THEN_ACTIVE_PROJECT"
    assert topology["single_active_project_behavior"]=="AUTO_BIND_WITHOUT_SECOND_USER_SELECTION"
    assert topology["duplicate_task_for_system_and_same_project"] is False
    assert adapter["capabilities"]["resolve_system_resume_alias"]["source"]=="continuity/TASK_INDEX.json#system"


def test_compatibility_task_index_mirrors_system_route_and_stage():
    canonical=json.loads((ROOT/"continuity/TASK_INDEX.json").read_text())
    alias=json.loads((ROOT/"TASK_INDEX.json").read_text())
    assert alias["canonical_ref"]=="continuity/TASK_INDEX.json"
    assert alias["system"]["system_id"]==canonical["system"]["system_id"]
    assert alias["system"]["active_project_task_id"]==canonical["system"]["active_project_task_id"]
    assert alias["tasks"][0]["current_stage"]==canonical["tasks"][0]["current_stage"]


def test_post_cutover_storage_governance():
    auth=json.loads((ROOT/"AUTHORITY_STATUS.json").read_text())
    gov=json.loads((ROOT/"continuity/ARTIFACT_CONTEXT_GOVERNANCE.json").read_text())
    cp=json.loads((TASK/"checkpoints/CURRENT_CHECKPOINT.json").read_text())
    adapter=json.loads((ROOT/"CONTINUITY_ADAPTER.json").read_text())
    assert auth["status"]=="GITHUB_PRIMARY"
    assert auth["business_authority"] is True
    assert auth["library_post_cutover_role"]=="REMOVED_NO_NOVEL_EXECUTION_TREE"
    assert auth["artifact_vault"]["provider"]=="Google Drive"
    assert auth["artifact_vault"]["business_authority"] is False
    assert auth["artifact_vault"]["path"]=="/Google Drive/ChatGPT/NOVEL_OS_小说系统_交付归档"
    assert "Google Drive" in gov["external_artifact_vault_if_any"]
    assert "ChatGPT Library" not in gov["external_artifact_vault_if_any"]
    assert any("Google Drive" in r for r in cp["derived_artifact_refs"])
    assert not any("ChatGPT Library" in r for r in cp["derived_artifact_refs"])
    assert adapter["external_artifact_vault"]["business_authority"] is False
    assert adapter["external_artifact_vault"]["recovery_state_source"] is False


def test_release_evidence_and_rebase_capabilities_are_bound_not_just_prose():
    caps=json.loads((ROOT/"continuity/EXECUTION_CAPABILITIES.json").read_text())
    assert caps["release_evidence_contract_version"]=="1.0"
    high=next(c for c in caps["capabilities"] if c["capability_id"]=="high_judgment_serialization_pipeline")
    det=next(c for c in caps["capabilities"] if c["capability_id"]=="deterministic_guards")
    assert "REBASE_ARCHITECTURE" in high["scope"]
    assert "SIGNING_READINESS" in high["scope"]
    assert "release_evidence_guard.py" in high["release_enforcement"]
    assert any("role-specific structured self-attested execution/review receipts" in item for item in high["evidence_contract"])
    assert any("whole-packet continuity/pacing/attachment/signing-readiness" in item for item in high["evidence_contract"])
    assert any("CI/regression can verify recovery" in item for item in caps["owner_notes"])
    assert "FULL_FRONT_ARC_REBASE_STATE" in det["scope"]
    assert "SUPERSESSION" in det["scope"]
    assert "release_evidence_guard.py" in det["invocation_path"]
    assert (ROOT/"runtime/release_evidence_guard.py").exists()


def test_active_authority_has_no_dangling_canon_snapshot_or_legacy_library_source():
    skill=(ROOT/"SKILL.md").read_text(encoding="utf-8")
    rulebook=(ROOT/"protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
    assert "不存在另一个可覆盖这些 ledgers 的 `CANON_SNAPSHOT.json` 权威" in skill
    assert "historical protocol files/research remain Library backup evidence" not in rulebook
    assert "Google Drive artifact vault" in rulebook
    assert "Full front-arc rebase / learning-to-authority promotion" in skill
    assert "Full-unit rebase / owner evolution" in rulebook


def test_ch8_legacy_acceptance_does_not_fake_role_or_isolation_receipts():
    text=(TASK/"reviews/CH0008_ACCEPTANCE.md").read_text(encoding="utf-8")
    assert "evidence_assurance: LEGACY_AGGREGATE_MIGRATED" in text
    assert "role_receipts: NOT_AVAILABLE" in text
    assert "isolated_reviewer_attestation: NOT_CLAIMED" in text
    assert "must not replay CH8" in text


def test_signing_rejection_is_durable_and_second_attempt_is_gated():
    m=json.loads((TASK/"TASK_MANIFEST.json").read_text())
    cp=json.loads((TASK/"checkpoints/CURRENT_CHECKPOINT.json").read_text())
    signing=m["platform_signing"]
    assert signing["attempt_1"]=="REJECTED_QUALITY_EVALUATION"
    assert signing["next_application_threshold"]==50000
    assert signing["third_application_threshold_if_needed"]==80000
    assert signing["second_application_gate"]=="SECOND_SIGNING_APPLICATION_REQUIRES_SIGNING_READINESS_AUDIT_PASS"
    assert cp["platform_signing"]["attempt_1"]==signing["attempt_1"]
    assert cp["platform_signing"]["second_application_gate"]==signing["second_application_gate"]
    assert (ROOT/signing["quality_diagnosis_ref"]).exists()
    assert (ROOT/signing["active_rebase_plan_ref"]).exists()
    assert (ROOT/signing["learning_evidence_ref"]).exists()
    assert "DO_NOT_BLINDLY_CONTINUE_TO_50K_WITHOUT_FRONT_ARC_REBASE" in m["strategic_constraints"]
    assert "SECOND_SIGNING_APPLICATION_REQUIRES_SIGNING_READINESS_AUDIT_PASS" in m["strategic_constraints"]
    assert "平台签约拒绝" in (ROOT/"SKILL.md").read_text(encoding="utf-8")


def test_universal_methodology_adapter_records_regression_without_overclaiming_outcome():
    a=json.loads((ROOT/"continuity/UNIVERSAL_PROTOCOL_ADAPTER.json").read_text())
    assert a["skill_version"]=="Novel Writing Agent 2.3.0-github"
    assert a["runtime_version"]=="github-owner-2.4"
    assert a["full_front_arc_rebase"]["mode"]=="CONTROLLED_FULL_FRONT_ARC_REBASE"
    assert a["methodology"]["profile_applicability"]["evolution"]["status"]=="APPLIES"
    assert "FULL_REBASE_LEARNING_EVIDENCE" in a["methodology"]["hook_bindings"]["learning_evidence_location"]
    assurance=a["methodology_assurance"]
    assert assurance["owner_regression_status"]=="PASS"
    assert assurance["owner_regression_evidence"]["validated_behavioral_head"]=="779de49898b4450b21ec2e62a737b1f91ec4c05d"
    assert assurance["owner_regression_evidence"]["github_actions_run_id"]==38083956011
    assert assurance["owner_regression_evidence"]["job_id"]==114306430298
    assert "does not prove" in assurance["boundary"]
