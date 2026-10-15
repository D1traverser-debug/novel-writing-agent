from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TERMINAL = "SINGLE_BOOK_DISTILLATION_COMPLETE__REFERENCE_EXTRACTED__CROSS_WORK_PENDING"


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_protocol_covers_full_learning_to_reselection_pipeline():
    text = (ROOT / "protocols/MASTERWORK_DISTILLATION_PROTOCOL.md").read_text(encoding="utf-8")
    assert "version: 2.0" in text
    for stage in (
        "D0 RIGHTS_AND_SOURCE",
        "D3 COLD_READ_TRACE",
        "D5 MICROCRAFT_ANNOTATION",
        "D6 POSITIVE_NEGATIVE_DIFF",
        "D7 ABLATION / COUNTERFACTUAL",
        "D8 CLOSED_CONTEXT_RECONSTRUCTION",
        "D9 CROSS-WORK_TRIANGULATION",
        "D10 PROJECT_TRANSFER_EXPERIMENT",
        "D11 ADVERSARIAL_REVIEW",
        "D12 PROMOTION",
        "D13 STOP / DECAY",
        "D14 CAMPAIGN_SYNTHESIS_AND_STORY_RESELECTION",
    ):
        assert stage in text


def test_study_state_binds_exactly_one_current_work_and_safe_pause():
    state = load_json("research/masterworks/STUDY_STATE.json")
    assert state["status"] == "ACTIVE"
    assert state["authority_role"] == "SYSTEM_LEARNING_CHECKPOINT_NOT_PROSE_OR_CANON_AUTHORITY"
    assert state["study_policy"]["mode"] == "ONE_BOOK_AT_A_TIME"
    assert state["study_policy"]["rule"] == "COMPLETE_CURRENT_WORK_BEFORE_NEXT"
    assert state["study_policy"]["interbook_comparison"] == "AFTER_EACH_COMPLETED_WORK__NON_PROMOTIONAL"
    assert state["study_policy"]["formal_cross_work_synthesis"] == "DEFER_ACTIVE_RULE_PROMOTION_UNTIL_SINGLE_BOOK_QUEUE_COMPLETE"
    assert state["study_policy"]["closed_context_reconstruction"] == "REQUIRED_AFTER_EACH_COMPLETED_WORK_BEFORE_LEDGER_REOPEN"
    assert state["study_policy"]["transfer_probe"] == "REQUIRED_AFTER_EACH_COMPLETED_WORK_BEFORE_QUEUE_ADVANCE"
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
    assert current["completion_gate_after_fulltext"] == "RUN_D8_D11_INTERBOOK_LEARNING_CYCLE_BEFORE_QING_YU_NIAN"


def test_completed_summary_and_queue_are_one_source_of_truth():
    state = load_json("research/masterworks/STUDY_STATE.json")
    queue = state["queue"]
    current = state["active_work"]
    assert current["work_id"] in {row["work_id"] for row in queue}
    active = [row for row in queue if row["status"] == "ACTIVE"]
    assert len(active) == 1 and active[0]["work_id"] == current["work_id"]
    complete_ids = {row["work_id"] for row in queue if row["status"] == "COMPLETE"}
    assert complete_ids == {row["work_id"] for row in state["completed_works"]}
    assert not (ROOT / "research/masterworks/INDEX.json").exists()
    assert not (ROOT / "TASK_INDEX.json").exists()
    assert not (ROOT / "continuity").exists()


def test_completed_baseline_metadata_remains_in_study_state_and_work_files():
    state = load_json("research/masterworks/STUDY_STATE.json")
    completed = {row["work_id"]: row for row in state["completed_works"]}
    assert completed["SHIRI_ZHONGYAN"]["status"] == TERMINAL
    assert completed["GUI_MI_ZHI_ZHU"]["status"] == TERMINAL
    assert completed["DAO_MU_BI_JI"]["status"] == TERMINAL
    assert (ROOT / "research/masterworks/SHIRI_ZHONGYAN/DISTILLATION_PASS_01.md").is_file()
    assert (ROOT / "research/masterworks/GUI_MI_ZHI_ZHU").is_dir()
    assert (ROOT / "research/masterworks/DAO_MU_BI_JI").is_dir()


def test_corpus_map_covers_queue_and_does_not_treat_same_series_as_independent_votes():
    state = load_json("research/masterworks/STUDY_STATE.json")
    corpus = load_json("research/masterworks/CORPUS_MAP.json")
    queue = {w["work_id"]: w for w in state["queue"]}
    mapped = {w["work_id"]: w for w in corpus["works"]}
    assert set(mapped) == set(queue)
    assert mapped["DUNE_01"]["evidence_family_id"] == "DUNE_SERIES"
    assert mapped["DUNE_02"]["evidence_family_id"] == "DUNE_SERIES"
    assert mapped["DUNE_03"]["evidence_family_id"] == "DUNE_SERIES"
    assert mapped["DEVOTION_OF_SUSPECT_X"]["evidence_family_id"] == "HIGASHINO_AUTHOR_CLUSTER"
    assert mapped["MALICE"]["evidence_family_id"] == "HIGASHINO_AUTHOR_CLUSTER"
    assert mapped["BYAKUYAKO"]["evidence_family_id"] == "HIGASHINO_AUTHOR_CLUSTER"


def test_cross_work_learning_is_active_but_formal_promotion_and_reselection_are_blocked():
    cross = load_json("research/masterworks/CROSS_WORK_LEARNING_STATE.json")
    assert cross["status"] == "ACTIVE_CAMPAIGN"
    assert cross["bootstrap_comparison"]["status"] == "COMPLETE__NON_PROMOTIONAL"
    assert cross["learning_loop"]["interim_promotion_policy"] == "NON_PROMOTIONAL__REFERENCE_AND_EXPERIMENTAL_ONLY"
    assert cross["formal_campaign_synthesis"]["status"] == "BLOCKED_UNTIL_ALL_NON_EXCLUDED_QUEUE_WORKS_COMPLETE"
    assert cross["story_reselection"]["status"] == "BLOCKED_PENDING_FORMAL_CAMPAIGN_SYNTHESIS"
    assert cross["story_reselection"]["historical_fq001_role"] == "ONE_CANDIDATE_OR_EVIDENCE_SOURCE_ONLY__NO_INCUMBENT_PRIVILEGE"


def test_mechanism_registry_is_compact_learning_evidence_not_active_rulebook():
    registry = load_json("research/masterworks/MECHANISM_REGISTRY.json")
    assert registry["current_campaign_max_level"] == "EXPERIMENTAL"
    assert registry["mechanisms"]
    for row in registry["mechanisms"]:
        assert row["status"] in {"REFERENCE", "EXPERIMENTAL"}
        assert row["active_rule"] is False
        assert len(row["support_work_ids"]) == len(row["support_evidence_family_ids"])


def test_uaos_capability_contract_exposes_learning_to_planning_mechanics():
    caps = load_json(".uaos/CAPABILITIES.json")
    ids = {c["capability_id"] for c in caps["capabilities"]}
    assert {
        "large_corpus_distillation",
        "continual_cross_work_learning",
        "material_deliberation_admission",
        "zero_based_story_reselection",
    }.issubset(ids)
    review = next(c for c in caps["capabilities"] if c["capability_id"] == "review_fanout")
    assert review["assurance_rule"] == "ROLE_SEPARATION_IS_NOT_PROVIDER_INDEPENDENCE"


def test_queue_sequence_and_exclusions_remain_intact():
    state = load_json("research/masterworks/STUDY_STATE.json")
    queue = state["queue"]
    active = [w for w in queue if w["status"] == "ACTIVE"]
    assert len(active) == 1 and active[0]["work_id"] == "GUI_CHUI_DENG"
    assert any(w["work_id"] == "QING_YU_NIAN" and w["status"] == "PENDING" for w in queue)
    assert any(w["work_id"] == "NORWEGIAN_WOOD" and w["status"] == "EXCLUDED_BY_USER" for w in queue)
