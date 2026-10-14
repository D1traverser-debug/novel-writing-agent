from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_protocol_still_covers_full_distillation_pipeline():
    text = (ROOT / "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md").read_text(encoding="utf-8")
    for stage in (
        "D0 RIGHTS_AND_SOURCE",
        "D3 COLD_READ_TRACE",
        "D5 MICROCRAFT_ANNOTATION",
        "D6 POSITIVE_NEGATIVE_DIFF",
        "D7 ABLATION / COUNTERFACTUAL",
        "D8 CROSS-WORK_TRIANGULATION",
        "D9 PROJECT_TRANSFER_EXPERIMENT",
        "D10 ADVERSARIAL_REVIEW",
        "D11 PROMOTION",
        "D12 STOP / DECAY",
    ):
        assert stage in text


def test_study_state_binds_exactly_one_current_work_and_safe_pause():
    state = load_json("research/masterworks/STUDY_STATE.json")
    assert state["status"] == "ACTIVE"
    assert state["authority_role"] == "SYSTEM_LEARNING_CHECKPOINT_NOT_PROSE_OR_CANON_AUTHORITY"
    assert state["study_policy"]["mode"] == "ONE_BOOK_AT_A_TIME"
    assert state["study_policy"]["rule"] == "COMPLETE_CURRENT_WORK_BEFORE_NEXT"
    assert state["study_policy"]["cross_work_synthesis"] == "DEFER_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE"
    assert set(state["user_locked_business_constraints"]) == {"SIGNING_MODE_IMMUTABLE", "SERIALIZATION_MODE_IMMUTABLE"}

    current = state["active_work"]
    assert current["work_id"] == "GUI_CHUI_DENG"
    assert current["status"] == "ACTIVE__PAUSED_BY_USER_AT_SAFE_CHECKPOINT"
    assert current["source_file_id"] == "1sNSSvaHcGTxqtAC4kXMR8c7VYdTbJMOL"
    assert current["source_sha256"] == "c02631f309cb6e30981a56566b5194c5e7c8661c4c71f66a7888d6970116bc3a"
    assert current["rolling_ledger_file_id"] == "1j9Lx98jpx-pmNMma8EW8DEYTiqjKurtF"
    assert current["rolling_ledger_sha256"] == "3cec0a78067c7d1acbc6605b4af859d1860f13d46e1770141b979b7f3143c02f"
    assert current["coverage"]["sequential_completed"] == "SOURCE_LINE_77_THROUGH_3913__JINGJUE_GUCHENG_CH26_PARTIAL"
    assert current["coverage"]["next_location"] == "源第3914行；继续第二十六章《天砖秘道》玉石王座场景"
    assert current["next_pass"] == "SEQUENTIAL_CONTINUE__JINGJUE_GUCHENG_CH26_FROM_SOURCE_LINE_3914"


def test_registry_follows_current_state_without_controller_indexes():
    state = load_json("research/masterworks/STUDY_STATE.json")
    registry = load_json("research/masterworks/INDEX.json")
    current = state["active_work"]
    complete_ids = {w["work_id"] for w in state["queue"] if w["status"] == "COMPLETE"}

    assert registry["status"] == "ACTIVE"
    assert registry["study_state_ref"] == "research/masterworks/STUDY_STATE.json"
    assert registry["authority_role"] == "LEARNING_EVIDENCE_REGISTRY_NOT_EXECUTION_AUTHORITY"
    assert len(registry["active_studies"]) == 1
    active = registry["active_studies"][0]
    assert active["work_id"] == current["work_id"]
    assert active["current_status"] == current["status"]
    assert active["next_pass"] == current["next_pass"]
    assert active["execution_authority"] is False
    for field in ("source_file_id", "source_sha256", "rolling_ledger_file_id", "rolling_ledger_sha256"):
        assert active[field] == current[field]
    assert complete_ids <= {s["work_id"] for s in registry["completed_studies"]}
    assert not (ROOT / "TASK_INDEX.json").exists()
    assert not (ROOT / "continuity").exists()


def test_completed_baselines_remain_preserved():
    registry = load_json("research/masterworks/INDEX.json")
    completed = {s["work_id"]: s for s in registry["completed_studies"]}
    assert completed["SHIRI_ZHONGYAN"]["current_status"] == TERMINAL
    assert completed["GUI_MI_ZHI_ZHU"]["current_status"] == TERMINAL
    assert completed["DAO_MU_BI_JI"]["current_status"] == TERMINAL
    assert "MORE_COMPLEXITY_IS_ALWAYS_BETTER" in completed["SHIRI_ZHONGYAN"]["explicitly_not_promoted"]
    assert "COPY_ANY_PLOT_RULE_CHARACTER_REVEAL_PHRASE_OR_ICONIC_STRUCTURE" in completed["GUI_MI_ZHI_ZHU"]["explicitly_not_promoted"]


def test_uaos_capability_contract_keeps_distillation_bounded():
    caps = load_json(".uaos/CAPABILITIES.json")
    cap = next(c for c in caps["capabilities"] if c["capability_id"] == "large_corpus_distillation")
    assert set(cap["required"]) == {"source_identity", "coverage_cursor", "rolling_ledger"}
    assert cap["side_channel_allowed"] is False
    review = next(c for c in caps["capabilities"] if c["capability_id"] == "review_fanout")
    assert review["assurance_rule"] == "ROLE_SEPARATION_IS_NOT_PROVIDER_INDEPENDENCE"


def test_queue_sequence_and_exclusions_remain_intact():
    state = load_json("research/masterworks/STUDY_STATE.json")
    queue = state["queue"]
    active = [w for w in queue if w["status"] == "ACTIVE"]
    assert len(active) == 1 and active[0]["work_id"] == "GUI_CHUI_DENG"
    assert any(w["work_id"] == "QING_YU_NIAN" and w["status"] == "PENDING" for w in queue)
    assert any(w["work_id"] == "NORWEGIAN_WOOD" and w["status"] == "EXCLUDED_BY_USER" for w in queue)
