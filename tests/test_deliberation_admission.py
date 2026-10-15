import pytest

from runtime.deliberation_admission import (
    DeliberationAdmissionError,
    HypothesisDisposition,
    ProblemLayer,
    RootScopeHypothesis,
    admit_material_mutation,
    build_material_decision_receipt,
    build_root_scope_receipt,
)


def valid_receipt():
    return build_material_decision_receipt(
        question="Should the learning campaign defer all comparison until the final book?",
        authority_refs=["protocols/MASTERWORK_DISTILLATION_PROTOCOL.md", "research/masterworks/STUDY_STATE.json"],
        internal_evidence_refs=["three completed ledgers", "FQ001 signing rejection audit"],
        external_evidence_refs=["learning-transfer research", "long-form generation research"],
        alternatives=["defer all comparison", "compare after every completed work without promotion"],
        counterexamples=["same-series multiple files can falsely inflate corroboration"],
        challenged_assumptions=["more books read automatically means more transferable skill"],
        selected_option="continual non-promotional comparison",
        rejection_reasons=["end-only comparison delays correction of a biased observation frame"],
        risks=["comparison can prematurely overfit current completed works"],
        rollback_or_recovery=["keep interim comparison non-promotional and revise observation axes"],
    )


def hypothesis(hid: str, layer: ProblemLayer, disposition: HypothesisDisposition) -> RootScopeHypothesis:
    return RootScopeHypothesis(
        hypothesis_id=hid,
        layer=layer,
        statement=f"candidate cause {hid}",
        disposition=disposition,
        supporting_evidence_refs=(f"support:{hid}",),
        falsification_or_rejection_refs=(f"probe:{hid}",),
    )


def valid_root(*, systemic: bool = False):
    items = [hypothesis("local", ProblemLayer.DOMAIN_WORKFLOW, HypothesisDisposition.SELECTED)]
    refs = []
    if systemic:
        items.append(hypothesis("upstream", ProblemLayer.DOMAIN_ARCHITECTURE, HypothesisDisposition.REJECTED))
        refs = ["audit:architecture-reassessment"]
    return build_root_scope_receipt(
        hypotheses=items,
        selected_hypothesis_id="local",
        systemic_signal=systemic,
        architecture_reassessment_refs=refs,
    )


def test_material_decision_receipt_admits_complete_deliberation():
    assert admit_material_mutation(valid_receipt()).startswith("MATERIAL_MUTATION_ADMITTED")


def test_material_mutation_rejects_recommendation_without_evidence_floor():
    with pytest.raises(DeliberationAdmissionError):
        build_material_decision_receipt(
            question="rewrite system",
            authority_refs=["a"],
            internal_evidence_refs=["b"],
            external_evidence_refs=[],
            alternatives=["only one"],
            counterexamples=[],
            challenged_assumptions=[],
            selected_option="x",
            rejection_reasons=[],
            risks=[],
            rollback_or_recovery=[],
        )


def test_external_research_may_be_declared_not_material_but_not_silently_skipped():
    receipt = build_material_decision_receipt(
        question="rename an internal evidence id without semantic change",
        authority_refs=["authority"],
        internal_evidence_refs=["current schema"],
        external_evidence_refs=[],
        alternatives=["rename", "leave stale name"],
        counterexamples=["renaming a public contract would be semantic"],
        challenged_assumptions=["all renames are harmless"],
        selected_option="rename internal id",
        rejection_reasons=["stale name creates maintenance ambiguity"],
        risks=["consumer drift"],
        rollback_or_recovery=["revert rename and consumer updates"],
        external_research_not_material_reason="pure internal metadata consistency; no external fact changes the decision",
    )
    assert admit_material_mutation(receipt).startswith("MATERIAL_MUTATION_ADMITTED")


def test_root_scope_rejects_user_or_external_claim_promoted_without_test():
    with pytest.raises(DeliberationAdmissionError, match="promoted without falsification"):
        build_root_scope_receipt(
            hypotheses=[hypothesis("architecture", ProblemLayer.DOMAIN_ARCHITECTURE, HypothesisDisposition.SELECTED)],
            selected_hypothesis_id="architecture",
            direct_user_or_external_claim_promoted_without_test=True,
        )


def test_systemic_root_scope_requires_cross_layer_upstream_hypothesis_and_rejection():
    with pytest.raises(DeliberationAdmissionError, match="at least two layers"):
        build_root_scope_receipt(
            hypotheses=[
                hypothesis("a", ProblemLayer.DOMAIN_WORKFLOW, HypothesisDisposition.SELECTED),
                hypothesis("b", ProblemLayer.DOMAIN_WORKFLOW, HypothesisDisposition.REJECTED),
            ],
            selected_hypothesis_id="a",
            systemic_signal=True,
            architecture_reassessment_refs=["audit:architecture"],
        )

    receipt = valid_root(systemic=True)
    assert receipt.selected_layer == ProblemLayer.DOMAIN_WORKFLOW
    assert ProblemLayer.DOMAIN_ARCHITECTURE in receipt.compared_layers
    assert receipt.rejected_hypothesis_ids == ("upstream",)
