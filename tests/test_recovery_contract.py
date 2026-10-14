from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "projects/FQ001_MINGRI_ORDER"


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_uaos_is_the_only_current_controller_surface():
    manifest = load_json(".uaos/MANIFEST.json")
    adapter = load_json(".uaos/ADAPTER.json")
    assert manifest["controller"] == "D1traverser-debug/universal-agent-os@main"
    assert manifest["status"] == "UAOS_CONTROL_PLANE_ACTIVE"
    assert manifest["skill"]["entrypoint"] == "UAOS_SKILL.md"
    assert adapter["task_identity_authority"] == "UAOS"
    assert adapter["cross_chat_continuity_authority"] == "UAOS"
    assert adapter["legacy_controller_compatibility"] == "NONE"
    for retired in (
        "ENTRYPOINT.md",
        "PROTOCOL.md",
        "SKILL.md",
        "TASK_INDEX.json",
        "CONTINUITY_ADAPTER.json",
        "AUTHORITY_STATUS.json",
        "continuity",
        "migration",
        "research/masterworks/INDEX.json",
    ):
        assert not (ROOT / retired).exists(), retired


def test_project_checkpoint_is_uaos_native_without_v37_control_fields():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    assert m["schema_version"] == cp["schema_version"] == "3.0-uaos"
    assert m["controller_authority"] == cp["controller_authority"] == "D1traverser-debug/universal-agent-os@main"
    assert m["controller_task_ref"] == cp["controller_task_ref"] == "state/tasks/FQ001_MINGRI_ORDER.json"
    assert m["domain_binding_ref"] == cp["domain_binding_ref"] == ".uaos/MANIFEST.json"
    for payload in (m, cp):
        assert "continuity_protocol_version" not in payload
        assert "universal_lease_authority" not in payload
        assert payload["controller_contract_version"] == "UAOS_TASK_BINDING_1.0"
        assert "registry_ref" not in payload["masterwork_learning"]


def test_recovery_truth_points_to_exact_current_masterwork_pause():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    state = load_json("research/masterworks/STUDY_STATE.json")
    current = state["active_work"]
    assert m["task_id"] == cp["task_id"] == "FQ001_MINGRI_ORDER"
    assert m["status"] == cp["status"] == "ACTIVE"
    assert m["current_stage"] == cp["current_stage"] == "MASTERWORK_SINGLE_BOOK_DISTILLATION_ACTIVE__STORY_RESELECTION_PENDING"
    assert m["next_action"] == cp["next_action"]
    assert m["next_serial_chapter"] == cp["next_serial_chapter"] == 9
    assert m["next_serial_status"] == cp["next_serial_status"] == "HELD_DURING_MASTERWORK_DISTILLATION_AND_STORY_RESELECTION"
    assert current["work_id"] == "GUI_CHUI_DENG"
    assert current["status"] == "ACTIVE__PAUSED_BY_USER_AT_SAFE_CHECKPOINT"
    assert current["coverage"]["sequential_completed"] == "SOURCE_LINE_77_THROUGH_3913__JINGJUE_GUCHENG_CH26_PARTIAL"
    assert current["coverage"]["next_location"] == "源第3914行；继续第二十六章《天砖秘道》玉石王座场景"
    assert current["next_pass"] == "SEQUENTIAL_CONTINUE__JINGJUE_GUCHENG_CH26_FROM_SOURCE_LINE_3914"
    assert m["masterwork_learning"]["active_work"] == cp["masterwork_learning"]["active_work"] == "GUI_CHUI_DENG"
    assert m["masterwork_learning"]["active_work_status"] == cp["masterwork_learning"]["active_work_status"] == current["status"]
    assert cp["masterwork_learning"]["active_work_next_location"] == "SOURCE_LINE_3914__JINGJUE_GUCHENG_CH26_CONTINUE"


def test_study_state_has_one_active_work_and_consistent_completed_summary():
    state = load_json("research/masterworks/STUDY_STATE.json")
    queue = state["queue"]
    active_rows = [row for row in queue if row["status"] == "ACTIVE"]
    assert active_rows == [{"no": 4, "work_id": "GUI_CHUI_DENG", "title": "鬼吹灯全集", "status": "ACTIVE"}]
    assert any(row["work_id"] == "QING_YU_NIAN" and row["status"] == "PENDING" for row in queue)
    assert any(row["work_id"] == "NORWEGIAN_WOOD" and row["status"] == "EXCLUDED_BY_USER" for row in queue)
    complete_ids = {row["work_id"] for row in queue if row["status"] == "COMPLETE"}
    assert complete_ids == {row["work_id"] for row in state["completed_works"]}


def test_historical_final_hashes_are_preserved():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    assert hashlib.sha256((TASK / "manuscript/CH0008_FINAL.md").read_bytes()).hexdigest() == m["last_final_hash"]
    expected = {
        1: "79f1a1778c4023fe185606f0493d2019938b61f6cc8e5697408453302e0d0043",
        2: "2b77d75aabebda658023a9ad570d56337d9391ed8d39fd85bbdcfd89a7d382bb",
        3: "b586faa1643fa92f9c4b528b1f94e11f7d80fbad4a133d02ea1feb8006911b58",
        4: "636b88301bbfdd2d9a7b150afef69192879cc26109da5c95c898e271188bc853",
        5: "d18a02c0bbc51e5585179ae096e3f2452e1f48085b4d188ed37b6ada8fc2e507",
        6: "9207c149ec8a8acb50dff22dc53cf9e0c4f6b53f63f4bcef6b4f8487332c0810",
        7: "e7d1ef881b042a70fd699817763cb07c055b06fd7cf9412cc98209739fd539f8",
    }
    for n, expected_hash in expected.items():
        assert hashlib.sha256((TASK / f"manuscript/CH{n:04d}_FINAL.md").read_bytes()).hexdigest() == expected_hash


def test_rebase_and_old_ch9_remain_suspended_not_executable():
    m = load_json("projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json")
    cp = load_json("projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json")
    rebase = m["rebase"]
    assert rebase["authorized_by_user"] is True
    assert rebase["execution_status"] == "SUSPENDED_PENDING_POST_DISTILLATION_STORY_RESELECTION"
    assert rebase["old_finals_role"] == "IMMUTABLE_HISTORICAL_BASELINE"
    assert rebase["candidate_promotion"] == "BLOCKED_UNTIL_POST_DISTILLATION_STORY_RESELECTION"
    assert all(cp["rebase"].get(k) == v for k, v in cp["rebase"].items())
    contract = (TASK / "NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
    assert "chapter_no: 9" in contract
    assert "status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" in contract
    assert "Do not write old CH9 next" in contract


def test_artifact_governance_is_current_uaos_model():
    gov = load_json("config/ARTIFACT_CONTEXT_GOVERNANCE.json")
    assert gov["controller"] == "D1traverser-debug/universal-agent-os@main"
    assert gov["canonical_artifact_or_file_stores"] == ["D1traverser-debug/novel-writing-agent@main"]
    assert "UAOS discovery/controller metadata" in gov["cache_or_reference_only_stores"]
    assert "universal-continuity-agent" not in json.dumps(gov, ensure_ascii=False)
