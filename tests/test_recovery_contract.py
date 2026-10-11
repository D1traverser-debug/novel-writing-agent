from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "projects/FQ001_MINGRI_ORDER"
TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"


def load_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_recovery_truth_points_to_exact_current_masterwork():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    state = load_json("research/masterworks/STUDY_STATE.json")
    assert m["task_id"] == "FQ001_MINGRI_ORDER"
    assert m["status"] == cp["status"] == "ACTIVE"
    assert m["current_stage"] == cp["current_stage"] == "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING"
    assert m["next_action"] == cp["next_action"]
    assert m["next_serial_chapter"] == cp["next_serial_chapter"] == 9
    assert m["next_serial_status"] == cp["next_serial_status"] == "HELD_DURING_MASTERWORK_DISTILLATION_AND_STORY_RESELECTION"
    assert cp["production_mode"] == "FULL_FRONT_ARC_REBASE"
    assert set(m["user_locked_business_constraints"]) == {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}
    current = state["active_work"]
    assert m["masterwork_learning"]["active_work"] == cp["masterwork_learning"]["active_work"] == current["work_id"]
    assert m["masterwork_learning"]["active_work_status"] == cp["masterwork_learning"]["active_work_status"] == current["status"]
    assert m["masterwork_learning"]["active_work_next_location"] == cp["masterwork_learning"]["active_work_next_location"] == current["coverage"]["next_location"]


def test_historical_final_hashes_are_preserved():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    assert hashlib.sha256((TASK / "manuscript/CH0008_FINAL.md").read_bytes()).hexdigest() == m["last_final_hash"]
    expected = {
        1:"79f1a1778c4023fe185606f0493d2019938b61f6cc8e5697408453302e0d0043",
        2:"2b77d75aabebda658023a9ad570d56337d9391ed8d39fd85bbdcfd89a7d382bb",
        3:"b586faa1643fa92f9c4b528b1f94e11f7d80fbad4a133d02ea1feb8006911b58",
        4:"636b88301bbfdd2d9a7b150afef69192879cc26109da5c95c898e271188bc853",
        5:"d18a02c0bbc51e5585179ae096e3f2452e1f48085b4d188ed37b6ada8fc2e507",
        6:"9207c149ec8a8acb50dff22dc53cf9e0c4f6b53f63f4bcef6b4f8487332c0810",
        7:"e7d1ef881b042a70fd699817763cb07c055b06fd7cf9412cc98209739fd539f8",
    }
    for n, h in expected.items():
        assert hashlib.sha256((TASK / f"manuscript/CH{n:04d}_FINAL.md").read_bytes()).hexdigest() == h


def test_existing_rebase_is_suspended_historical_candidate_not_next_action():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    rebase = m["rebase"]
    assert rebase["authorized_by_user"] is True
    assert rebase["mode"] == "CONTROLLED_FULL_FRONT_ARC_REBASE"
    assert rebase["execution_status"] == "SUSPENDED_PENDING_POST_DISTILLATION_STORY_RESELECTION"
    assert rebase["old_finals_role"] == "IMMUTABLE_HISTORICAL_BASELINE"
    assert rebase["frozen_architecture_role"] == "HISTORICAL_CANDIDATE_NOT_NEXT_ACTION"
    assert rebase["candidate_promotion"] == "BLOCKED_UNTIL_POST_DISTILLATION_STORY_RESELECTION"
    assert all(cp["rebase"].get(k) == rebase.get(k) for k in cp["rebase"])


def test_old_ch9_stays_held():
    c = (TASK / "NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
    assert "chapter_no: 9" in c
    assert "status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" in c
    assert "Do not write old CH9 next" in c


def test_study_queue_and_registry_are_dynamic_not_title_hardcoded():
    state = load_json("research/masterworks/STUDY_STATE.json")
    registry = load_json("research/masterworks/INDEX.json")
    current = state["active_work"]
    queue = state["queue"]
    active_rows = [w for w in queue if w["status"] == "ACTIVE"]
    assert len(active_rows) == 1
    assert active_rows[0]["work_id"] == current["work_id"]
    assert current["status"] == "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS"
    assert current["next_pass"].startswith("SEQUENTIAL_CONTINUE__")
    assert len(current["source_sha256"]) == 64
    assert len(current["rolling_ledger_sha256"]) == 64
    assert current["coverage"]["sequential_completed"]
    assert current["coverage"]["next_location"]
    active_registry = registry["active_studies"]
    assert len(active_registry) == 1
    assert active_registry[0]["work_id"] == current["work_id"]
    complete_ids = {w["work_id"] for w in queue if w["status"] == "COMPLETE"}
    registry_complete = {w["work_id"] for w in registry["completed_studies"]}
    assert complete_ids <= registry_complete
    assert any(w["work_id"] == "NORWEGIAN_WOOD" and w["status"] == "EXCLUDED_BY_USER" for w in queue)


def test_current_dao_resume_point_is_exact():
    state = load_json("research/masterworks/STUDY_STATE.json")
    current = state["active_work"]
    assert current["work_id"] == "DAO_MU_BI_JI"
    assert current["coverage"]["sequential_completed"] == "QIXING_LUWANGGONG__CH1-CH29__VOLUME_01_COMPLETE__NUHAI_QIANSHA__CH1-CH46__VOLUME_02_COMPLETE"
    assert current["coverage"]["next_location"] == "《秦岭神树》第一章《老痒出狱》"
    assert current["source_sha256"] == "7ee1015d5a384e0acaf85a05367e95c3eb5ed3cb3c7b95fcb5333ffe81bb6768"
    assert current["rolling_ledger_sha256"] == "133dfb0de4decc2ab21aeb1042aadc340cec21870b96a23c99c11448dceae7bc"


def test_mastery_model_and_historical_architecture_evidence_remain_present():
    mastery = (ROOT / "protocols/NOVEL_MASTERY_MODEL.md").read_text(encoding="utf-8")
    for token in [f"C{i:02d}" for i in range(1, 21)]:
        assert token in mastery
    for level in ("L0", "L1", "L2", "L3", "L4"):
        assert level in mastery
    assert "status: ACTIVE_ARCHITECTURE_AUTHORITY_DURING_FULL_REBASE" in (TASK / "outline/SERIES_MASTER_OUTLINE.md").read_text(encoding="utf-8")
    assert "FROZEN_FOR_CANDIDATE_DRAFT" in (TASK / "outline/FRONT_ARC_REBASE_ARCHITECTURE_V1.md").read_text(encoding="utf-8")
    assert "SUPERSEDED_BY_SERIES_MASTER_OUTLINE_FOR_ACTIVE_REBASE" in (TASK / "outline/ARC_001.md").read_text(encoding="utf-8")


def test_novel_os_routes_same_project_and_current_masterwork_binding():
    state = load_json("research/masterworks/STUDY_STATE.json")
    idx = load_json("continuity/TASK_INDEX.json")
    alias = load_json("TASK_INDEX.json")
    current_id = state["active_work"]["work_id"]
    complete_ids = {w["work_id"] for w in state["queue"] if w["status"] == "COMPLETE"}
    assert idx["system"]["system_id"] == "NOVEL_OS"
    assert idx["system"]["resume_behavior"] == "ROUTE_TO_ACTIVE_PROJECT"
    assert idx["system"]["active_project_task_id"] == "FQ001_MINGRI_ORDER"
    assert idx["system"]["masterwork_learning"]["active_study"] == current_id
    assert alias["system"]["masterwork_learning"]["active_study"] == current_id
    assert set(idx["system"]["masterwork_learning"]["completed_studies"]) == complete_ids
    assert set(alias["system"]["masterwork_learning"]["completed_studies"]) == complete_ids
    assert alias["tasks"][0]["next_action"] == idx["tasks"][0]["next_action"]


def test_post_cutover_storage_governance_remains_intact():
    auth = load_json("AUTHORITY_STATUS.json")
    gov = load_json("continuity/ARTIFACT_CONTEXT_GOVERNANCE.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    assert auth["status"] == "GITHUB_PRIMARY"
    assert auth["business_authority"] is True
    assert auth["library_post_cutover_role"] == "REMOVED_NO_NOVEL_EXECUTION_TREE"
    assert auth["artifact_vault"]["provider"] == "Google Drive"
    assert auth["artifact_vault"]["business_authority"] is False
    assert "Google Drive" in gov["external_artifact_vault_if_any"]
    assert any("Google Drive" in r for r in cp["derived_artifact_refs"])


def test_execution_capabilities_and_signing_state_stay_bound():
    caps = load_json("continuity/EXECUTION_CAPABILITIES.json")
    assert caps["release_evidence_contract_version"] == "1.0"
    mw = next(c for c in caps["capabilities"] if c["capability_id"] == "masterwork_distillation_and_transfer_learning")
    assert mw["assurance_ceiling"] == "SESSION_EXECUTABLE"
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    assert m["platform_signing"]["attempt_1"] == cp["platform_signing"]["attempt_1"] == "REJECTED_QUALITY_EVALUATION"
    assert m["platform_signing"]["second_application_gate"] == cp["platform_signing"]["second_application_gate"] == "SECOND_SIGNING_APPLICATION_REQUIRES_SIGNING_READINESS_AUDIT_PASS"


def test_current_state_text_explicitly_points_to_dao_not_old_resume_path():
    text = (TASK / "CURRENT_STATE.md").read_text(encoding="utf-8")
    assert "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING" in text
    assert "不执行旧 CH9" in text
    assert "active_masterwork_id: DAO_MU_BI_JI" in text
    assert "《秦岭神树》第一章《老痒出狱》" in text
    assert "《挪威的森林》" in text and "EXCLUDED_BY_USER" in text
