from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "projects/FQ001_MINGRI_ORDER"


def load_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_recovery_truth_points_to_masterwork_study_before_story_reselection():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    assert m["task_id"] == "FQ001_MINGRI_ORDER"
    assert m["status"] == cp["status"] == "ACTIVE"
    assert m["current_stage"] == cp["current_stage"] == "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING"
    assert m["next_action"] == cp["next_action"]
    assert m["next_serial_chapter"] == cp["next_serial_chapter"] == 9
    assert m["next_serial_status"] == cp["next_serial_status"] == "HELD_DURING_MASTERWORK_DISTILLATION_AND_STORY_RESELECTION"
    assert cp["production_mode"] == "FULL_FRONT_ARC_REBASE"
    assert set(m["user_locked_business_constraints"]) == {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}
    assert m["reopenable_design_scope"] == "ALL_OTHER_STORY_DESIGN_MAY_BE_REBUILT_AFTER_MASTERWORK_DISTILLATION"
    assert m["masterwork_learning"]["active_work"] == "GUI_MI_ZHI_ZHU"
    assert m["masterwork_learning"]["completed_work"] == "SHIRI_ZHONGYAN"


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
    assert cp["rebase"] == rebase or all(cp["rebase"].get(k) == rebase.get(k) for k in cp["rebase"])
    assert (ROOT / rebase["series_master_outline_ref"]).exists()
    assert (ROOT / rebase["frozen_architecture_ref"]).exists()


def test_old_ch9_stays_held():
    c = (TASK / "NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
    assert "chapter_no: 9" in c
    assert "status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" in c
    assert "Do not write old CH9 next" in c


def test_study_checkpoint_has_exact_queue_semantics():
    state = load_json("research/masterworks/STUDY_STATE.json")
    assert state["study_policy"]["mode"] == "ONE_BOOK_AT_A_TIME"
    assert state["study_policy"]["rule"] == "COMPLETE_CURRENT_WORK_BEFORE_NEXT"
    assert state["study_policy"]["cross_work_synthesis"] == "DEFER_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE"
    active = state["active_work"]
    assert active["work_id"] == "GUI_MI_ZHI_ZHU"
    assert active["status"] in {"ACTIVE__PENDING_FIRST_SEQUENTIAL_READ", "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS"}
    if active["status"] == "ACTIVE__PENDING_FIRST_SEQUENTIAL_READ":
        assert active["next_pass"] == "SEQUENTIAL_FULLTEXT_FROM_BEGINNING"
    else:
        assert active["next_pass"].startswith("SEQUENTIAL_CONTINUE__")
        assert len(active["source_sha256"]) == 64
        assert active["coverage"]["sequential_completed"]
        assert active["coverage"]["next_location"]
        assert active["rolling_ledger"]
    assert any(w["work_id"] == "SHIRI_ZHONGYAN" and w["status"] == "COMPLETE" for w in state["queue"])
    assert any(w["work_id"] == "GUI_MI_ZHI_ZHU" and w["status"] == "ACTIVE" for w in state["queue"])
    assert any(w["work_id"] == "NORWEGIAN_WOOD" and w["status"] == "EXCLUDED_BY_USER" for w in state["queue"])


def test_mastery_model_and_historical_architecture_evidence_remain_present():
    mastery = (ROOT / "protocols/NOVEL_MASTERY_MODEL.md").read_text(encoding="utf-8")
    for token in [f"C{i:02d}" for i in range(1, 21)]:
        assert token in mastery
    for level in ("L0", "L1", "L2", "L3", "L4"):
        assert level in mastery
    master = (TASK / "outline/SERIES_MASTER_OUTLINE.md").read_text(encoding="utf-8")
    frozen = (TASK / "outline/FRONT_ARC_REBASE_ARCHITECTURE_V1.md").read_text(encoding="utf-8")
    legacy = (TASK / "outline/ARC_001.md").read_text(encoding="utf-8")
    assert "status: ACTIVE_ARCHITECTURE_AUTHORITY_DURING_FULL_REBASE" in master
    assert "FROZEN_FOR_CANDIDATE_DRAFT" in frozen
    assert "SUPERSEDED_BY_SERIES_MASTER_OUTLINE_FOR_ACTIVE_REBASE" in legacy


def test_novel_os_routes_same_project_but_new_execution_stage():
    idx = load_json("continuity/TASK_INDEX.json")
    alias = load_json("TASK_INDEX.json")
    system = idx["system"]
    assert system["system_id"] == "NOVEL_OS"
    assert system["resume_behavior"] == "ROUTE_TO_ACTIVE_PROJECT"
    assert system["active_project_task_id"] == "FQ001_MINGRI_ORDER"
    assert system["masterwork_learning"]["active_study"] == "GUI_MI_ZHI_ZHU"
    assert system["masterwork_learning"]["completed_studies"] == ["SHIRI_ZHONGYAN"]
    assert system["masterwork_learning"]["study_state_ref"] == "research/masterworks/STUDY_STATE.json"
    task = idx["tasks"][0]
    assert task["current_stage"] == "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING"
    assert alias["tasks"][0]["current_stage"] == task["current_stage"]
    assert alias["tasks"][0]["next_action"] == task["next_action"]
    assert alias["system"]["masterwork_learning"]["active_study"] == "GUI_MI_ZHI_ZHU"


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


def test_execution_capabilities_and_release_evidence_stay_bound():
    caps = load_json("continuity/EXECUTION_CAPABILITIES.json")
    assert caps["release_evidence_contract_version"] == "1.0"
    high = next(c for c in caps["capabilities"] if c["capability_id"] == "high_judgment_serialization_pipeline")
    mw = next(c for c in caps["capabilities"] if c["capability_id"] == "masterwork_distillation_and_transfer_learning")
    det = next(c for c in caps["capabilities"] if c["capability_id"] == "deterministic_guards")
    assert "release_evidence_guard.py" in high["release_enforcement"]
    assert mw["assurance_ceiling"] == "SESSION_EXECUTABLE"
    assert "masterwork_distillation_guard.py" in mw["release_enforcement"]
    assert "MASTERWORK_LEARNING_STATE" in det["scope"]


def test_signing_rejection_and_retry_gate_are_not_lost():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    signing = m["platform_signing"]
    assert signing["attempt_1"] == "REJECTED_QUALITY_EVALUATION"
    assert signing["next_application_threshold"] == 50000
    assert signing["third_application_threshold_if_needed"] == 80000
    assert signing["second_application_gate"] == "SECOND_SIGNING_APPLICATION_REQUIRES_SIGNING_READINESS_AUDIT_PASS"
    assert cp["platform_signing"]["attempt_1"] == signing["attempt_1"]
    assert cp["platform_signing"]["second_application_gate"] == signing["second_application_gate"]


def test_current_state_text_explicitly_prevents_old_resume_path():
    text = (TASK / "CURRENT_STATE.md").read_text(encoding="utf-8")
    assert "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING" in text
    assert "不执行旧 CH9" in text
    assert "不再是当前 next_action" in text
    assert "《诡秘之主》" in text
    assert "《挪威的森林》" in text and "EXCLUDED_BY_USER" in text
