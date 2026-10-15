import pytest

from runtime.narrative_evaluation import (
    CandidateEvaluation,
    DEFAULT_DIMENSIONS,
    DimensionEvidence,
    NarrativeEvaluationError,
    pareto_front,
    promotion_gate,
    reject_scalar_override,
    require_pairwise_reasoning,
    validate_candidate_evaluation,
)


def candidate(candidate_id: str, *, acquisition: float, attachment: float, complexity: float, fail_gate=False):
    rows = []
    for dim in DEFAULT_DIMENSIONS:
        value = 0.65
        higher = dim != "PRODUCTION_COMPLEXITY_RISK"
        if dim == "ACQUISITION":
            value = acquisition
        if dim == "CHARACTER_ATTACHMENT":
            value = attachment
        if dim == "PRODUCTION_COMPLEXITY_RISK":
            value = complexity
        rows.append(
            DimensionEvidence(
                dimension=dim,
                value=value,
                higher_is_better=higher,
                evidence_class="STRUCTURAL_ANALYSIS",
                evidence_refs=(f"evidence:{candidate_id}:{dim}",),
                confidence="MEDIUM",
                rationale=f"bounded candidate evidence for {dim}",
                hard_gate=(dim == "READER_CONTRACT"),
                hard_gate_pass=not fail_gate,
            )
        )
    return CandidateEvaluation(candidate_id=candidate_id, dimensions=tuple(rows))


def test_full_vector_required():
    assert validate_candidate_evaluation(candidate("A", acquisition=.8, attachment=.6, complexity=.4)).startswith("NARRATIVE_VECTOR")
    partial = CandidateEvaluation(
        candidate_id="P",
        dimensions=(
            DimensionEvidence("ACQUISITION", .8, True, "STRUCTURAL_ANALYSIS", ("e",), "LOW", "r"),
        ),
    )
    with pytest.raises(NarrativeEvaluationError):
        validate_candidate_evaluation(partial)


def test_hard_gate_cannot_be_overridden_by_high_average():
    bad = candidate("BAD", acquisition=.99, attachment=.99, complexity=.1, fail_gate=True)
    with pytest.raises(NarrativeEvaluationError):
        promotion_gate(bad)
    with pytest.raises(NarrativeEvaluationError):
        reject_scalar_override(aggregate_score=.97, hard_gate_failed=True)


def test_pareto_front_preserves_tradeoffs_instead_of_forcing_single_winner():
    a = candidate("A", acquisition=.9, attachment=.55, complexity=.3)
    b = candidate("B", acquisition=.72, attachment=.86, complexity=.35)
    c = candidate("C", acquisition=.6, attachment=.5, complexity=.6)
    front = set(pareto_front((a, b, c)))
    assert front == {"A", "B"}


def test_pairwise_reasoning_required_for_all_candidates():
    a = candidate("A", acquisition=.9, attachment=.55, complexity=.3)
    b = candidate("B", acquisition=.72, attachment=.86, complexity=.35)
    assert require_pairwise_reasoning(
        (a, b),
        pairwise_tradeoff_refs={"A": ("A-v-B",), "B": ("B-v-A",)},
    ) == "PAIRWISE_TRADEOFF_EVIDENCE_COMPLETE"
    with pytest.raises(NarrativeEvaluationError):
        require_pairwise_reasoning((a, b), pairwise_tradeoff_refs={"A": ("A-v-B",)})
