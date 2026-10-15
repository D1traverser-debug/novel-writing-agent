import pytest

from runtime.learning_transfer_admission import (
    ClosedContextReconstruction,
    CrossWorkComparisonReceipt,
    LearningTransferAdmissionError,
    TransferProbeReceipt,
    admit_active_rule_promotion,
    admit_closed_context_reconstruction,
    admit_interbook_comparison,
    admit_transfer_probe,
)


def test_closed_context_reconstruction_requires_correction_when_distorted():
    receipt = ClosedContextReconstruction(
        work_id="GUI_MI_ZHI_ZHU",
        compact_index_ref="research/masterworks/MECHANISM_REGISTRY.json",
        recalled_mechanisms=("M001", "M002"),
        missed_or_distorted=("relationship engine underweighted",),
        correction_refs=("GUI_MI_ZHI_ZHU ledger",),
    )
    assert admit_closed_context_reconstruction(receipt) == "CLOSED_CONTEXT_RECONSTRUCTION_ADMITTED"


def test_interbook_comparison_is_non_promotional_and_family_aware():
    receipt = CrossWorkComparisonReceipt(
        current_work_id="DAO_MU_BI_JI",
        compared_work_ids=("SHIRI_ZHONGYAN", "GUI_MI_ZHI_ZHU"),
        evidence_family_ids=("DAO_MU_BI_JI_SERIES", "SHIRI_ZHONGYAN_INDEPENDENT", "GUI_MI_ZHI_ZHU_INDEPENDENT"),
        common_mechanisms=("bounded epistemic competence",),
        conflicts_or_boundary_conditions=("first-person uncertainty differs from omniscient planning",),
        negative_evidence=("mystery debt can accumulate",),
        updated_observation_axes=("payoff density",),
        promotion_requested=False,
    )
    completed = {"SHIRI_ZHONGYAN", "GUI_MI_ZHI_ZHU", "DAO_MU_BI_JI"}
    assert admit_interbook_comparison(receipt, completed_work_ids=completed) == "INTERBOOK_COMPARISON_ADMITTED__NON_PROMOTIONAL"


def test_same_series_three_files_do_not_count_as_three_independent_votes():
    receipt = CrossWorkComparisonReceipt(
        current_work_id="DUNE_03",
        compared_work_ids=("DUNE_01", "DUNE_02"),
        evidence_family_ids=("DUNE_SERIES", "DUNE_SERIES", "DUNE_SERIES"),
        common_mechanisms=("power has cost",),
        conflicts_or_boundary_conditions=("volume role changes",),
        negative_evidence=("series context is shared",),
        updated_observation_axes=("cross-author contrast",),
    )
    with pytest.raises(LearningTransferAdmissionError):
        admit_interbook_comparison(receipt, completed_work_ids={"DUNE_01", "DUNE_02", "DUNE_03"})


def test_interbook_comparison_cannot_promote_during_active_campaign():
    receipt = CrossWorkComparisonReceipt(
        current_work_id="DAO_MU_BI_JI",
        compared_work_ids=("SHIRI_ZHONGYAN",),
        evidence_family_ids=("DAO_MU_BI_JI_SERIES", "SHIRI_ZHONGYAN_INDEPENDENT"),
        common_mechanisms=("relationship cost",),
        conflicts_or_boundary_conditions=("different POV",),
        negative_evidence=("genre surface differs",),
        updated_observation_axes=("relationship entry timing",),
        promotion_requested=True,
    )
    with pytest.raises(LearningTransferAdmissionError):
        admit_interbook_comparison(receipt, completed_work_ids={"DAO_MU_BI_JI", "SHIRI_ZHONGYAN"})


def test_transfer_probe_requires_alternatives_side_effects_and_adversarial_review():
    receipt = TransferProbeReceipt(
        capability_id="C05_RELATIONSHIP",
        target_case_id="synthetic-urban-suspense-01",
        source_mechanism_ids=("M005_RELATIONSHIP_ADHESION_REQUIRES_COST",),
        alternatives=("shared operational risk", "conflicting obligation"),
        predicted_gain=("earlier attachment",),
        predicted_side_effects=("may slow mystery exposition",),
        adversarial_findings=("do not copy tomb-adventure rescue surface",),
        outcome="SUPPORTED",
        evidence_refs=("benchmark:synthetic-urban-suspense-01",),
    )
    assert admit_transfer_probe(receipt) == "TRANSFER_PROBE_ADMITTED"


def test_active_rule_promotion_blocked_before_campaign_complete():
    with pytest.raises(LearningTransferAdmissionError):
        admit_active_rule_promotion(
            mechanism_id="M001",
            corpus_campaign_complete=False,
            supporting_work_ids=("A", "B", "C"),
            supporting_evidence_family_ids=("FA", "FB", "FC"),
            genre_clusters=("G1", "G2", "G3"),
            negative_or_boundary_evidence=("boundary",),
            transfer_probe_refs=("probe",),
            external_or_live_outcome_refs=("outcome",),
        )


def test_active_rule_promotion_requires_independent_families_and_genre_diversity():
    with pytest.raises(LearningTransferAdmissionError):
        admit_active_rule_promotion(
            mechanism_id="M001",
            corpus_campaign_complete=True,
            supporting_work_ids=("DUNE_01", "DUNE_02", "DUNE_03"),
            supporting_evidence_family_ids=("DUNE_SERIES", "DUNE_SERIES", "DUNE_SERIES"),
            genre_clusters=("SCI_FI", "SCI_FI", "SCI_FI"),
            negative_or_boundary_evidence=("boundary",),
            transfer_probe_refs=("probe",),
            external_or_live_outcome_refs=("outcome",),
        )
