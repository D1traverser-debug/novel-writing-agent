from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"
ACTIVE_STATUSES = {"ACTIVE__PENDING_FIRST_SEQUENTIAL_READ", "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS"}


def load_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_protocol_still_covers_full_distillation_pipeline():
    text = (ROOT / "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md").read_text(encoding="utf-8")
    for stage in (
        "D0 RIGHTS_AND_SOURCE","D3 COLD_READ_TRACE","D5 MICROCRAFT_ANNOTATION","D6 POSITIVE_NEGATIVE_DIFF",
        "D7 ABLATION / COUNTERFACTUAL","D8 CROSS-WORK_TRIANGULATION","D9 PROJECT_TRANSFER_EXPERIMENT",
        "D10 ADVERSARIAL_REVIEW","D11 PROMOTION","D12 STOP / DECAY",
    ):
        assert stage in text


def test_study_state_binds_exactly_one_current_work_without_title_hardcoding():
    state = load_json("research/masterworks/STUDY_STATE.json")
    assert state["status"] == "ACTIVE"
    assert state["authority_role"] == "SYSTEM_LEARNING_CHECKPOINT_NOT_PROSE_OR_CANON_AUTHORITY"
    assert state["study_policy"]["mode"] == "ONE_BOOK_AT_A_TIME"
    assert state["study_policy"]["rule"] == "COMPLETE_CURRENT_WORK_BEFORE_NEXT"
    assert state["study_policy"]["cross_work_synthesis"] == "DEFER_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE"
    assert set(state["user_locked_business_constraints"]) == {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}

    current = state["active_work"]
    queue = state["queue"]
    assert current["work_id"] in {w["work_id"] for w in queue}
    assert current["status"] in ACTIVE_STATUSES | {TERMINAL}
    if current["status"] in ACTIVE_STATUSES:
        actives = [w for w in queue if w["status"] == "ACTIVE"]
        assert len(actives) == 1
        assert actives[0]["work_id"] == current["work_id"]
    if current["status"] == "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS":
        assert current["next_pass"].startswith("SEQUENTIAL_CONTINUE__")
        assert len(current["source_sha256"]) == 64
        assert len(current["rolling_ledger_sha256"]) == 64
        assert current["coverage"]["sequential_completed"]
        assert current["coverage"]["next_location"]
    assert any(w["work_id"] == "NORWEGIAN_WOOD" and w["status"] == "EXCLUDED_BY_USER" for w in queue)


def test_registry_and_indexes_follow_current_state_dynamically():
    state = load_json("research/masterworks/STUDY_STATE.json")
    registry = load_json("research/masterworks/INDEX.json")
    canonical = load_json("continuity/TASK_INDEX.json")
    alias = load_json("TASK_INDEX.json")
    current = state["active_work"]
    complete_ids = {w["work_id"] for w in state["queue"] if w["status"] == "COMPLETE"}

    assert registry["status"] == "ACTIVE"
    assert registry["study_state_ref"] == "research/masterworks/STUDY_STATE.json"
    assert registry["authority_role"] == "LEARNING_EVIDENCE_REGISTRY_NOT_EXECUTION_AUTHORITY"
    active = registry["active_studies"]
    assert len(active) == 1
    assert active[0]["work_id"] == current["work_id"]
    assert active[0]["current_status"] == current["status"]
    assert active[0]["next_pass"] == current["next_pass"]
    assert active[0]["execution_authority"] is False
    for field in ("source_file_id", "source_sha256", "rolling_ledger_file_id", "rolling_ledger_sha256"):
        assert active[0][field] == current[field]

    completed = {s["work_id"] for s in registry["completed_studies"]}
    assert complete_ids <= completed
    for idx in (canonical, alias):
        learning = idx["system"]["masterwork_learning"]
        assert learning["active_study"] == current["work_id"]
        assert set(learning["completed_studies"]) == complete_ids
        assert learning["study_state_ref"] == "research/masterworks/STUDY_STATE.json"


def test_completed_baselines_remain_preserved():
    registry = load_json("research/masterworks/INDEX.json")
    completed = {s["work_id"]: s for s in registry["completed_studies"]}
    shiri = completed["SHIRI_ZHONGYAN"]
    guimi = completed["GUI_MI_ZHI_ZHU"]
    assert shiri["current_status"] == TERMINAL
    assert guimi["current_status"] == TERMINAL
    assert shiri["fulltext_coverage"]["sequential_study_completed"] == "SOURCE_ORDER_1-1360"
    assert guimi["fulltext_coverage"]["sequential_study_completed"] == "ALL_8_VOLUMES__THROUGH_FULL_BOOK_END"
    assert guimi["fulltext_coverage"]["full_book_end_verified"] is True
    assert "MORE_COMPLEXITY_IS_ALWAYS_BETTER" in shiri["explicitly_not_promoted"]
    assert "COPY_ANY_PLOT_RULE_CHARACTER_REVEAL_PHRASE_OR_ICONIC_STRUCTURE" in guimi["explicitly_not_promoted"]


def test_current_dao_second_volume_checkpoint_is_source_bound():
    state = load_json("research/masterworks/STUDY_STATE.json")
    current = state["active_work"]
    assert current["work_id"] == "DAO_MU_BI_JI"
    assert current["status"] == "ACTIVE__SEQUENTIAL_READ_IN_PROGRESS"
    assert current["source_file_id"] == "1j22-7Q5H3rsBY0fsCa3K3TmpQ3qhLBRG"
    assert current["source_sha256"] == "7ee1015d5a384e0acaf85a05367e95c3eb5ed3cb3c7b95fcb5333ffe81bb6768"
    assert current["rolling_ledger_file_id"] == "17r1Q49KNT858dJLvrEWQeRlnt7-tb5f4"
    assert current["rolling_ledger_sha256"] == "133dfb0de4decc2ab21aeb1042aadc340cec21870b96a23c99c11448dceae7bc"
    assert current["coverage"]["sequential_completed"] == "QIXING_LUWANGGONG__CH1-CH29__VOLUME_01_COMPLETE__NUHAI_QIANSHA__CH1-CH46__VOLUME_02_COMPLETE"
    assert current["coverage"]["next_location"] == "《秦岭神树》第一章《老痒出狱》"


def test_execution_capability_keeps_learning_claim_ceiling():
    caps = load_json("continuity/EXECUTION_CAPABILITIES.json")
    mw = next(c for c in caps["capabilities"] if c["capability_id"] == "masterwork_distillation_and_transfer_learning")
    det = next(c for c in caps["capabilities"] if c["capability_id"] == "deterministic_guards")
    assert mw["assurance_ceiling"] == "SESSION_EXECUTABLE"
    assert "PROJECT_TRANSFER" in mw["scope"]
    assert "CROSS_WORK_TRIANGULATION" in mw["scope"]
    assert "masterwork_distillation_guard.py" in mw["release_enforcement"]
    assert "MASTERWORK_LEARNING_STATE" in det["scope"]
    assert any("learning capability, not a prose or Canon authority" in note for note in caps["owner_notes"])
