#!/usr/bin/env python3
"""Evidence-bound vector evaluation for Novel product/literary decisions.

A single scalar score is insufficient. Candidate comparison uses named dimensions, hard
gates, explicit provenance and conservative uncertainty. Numeric Pareto comparison is
allowed only when a dimension shares the same rubric/calibration scope across candidates;
otherwise the tradeoff must remain qualitative or be re-benchmarked.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping


class NarrativeEvaluationError(RuntimeError):
    pass


DEFAULT_DIMENSIONS = (
    "ACQUISITION",
    "READER_CONTRACT",
    "CHARACTER_ATTACHMENT",
    "RELATIONSHIP_DYNAMICS",
    "SERIAL_SUSTAINABILITY",
    "ENGINE_DIVERSITY",
    "NARRATIVE_ORCHESTRATION",
    "CONTINUITY",
    "DEVELOPMENT_RICHNESS",
    "MYSTERY_REVELATION",
    "EMOTIONAL_RANGE",
    "VOICE_PROSE",
    "COGNITIVE_LOAD",
    "ORIGINALITY",
    "PLATFORM_FIT",
    "PRODUCTION_COMPLEXITY_RISK",
)

VALID_EVIDENCE_CLASSES = {
    "LIVE_PROJECT_OUTCOME",
    "CURRENT_PLATFORM_FIRST_PARTY",
    "MASTERWORK_OR_CRAFT_EVIDENCE",
    "BLIND_READER_EVIDENCE",
    "STRUCTURAL_ANALYSIS",
    "MODEL_SELF_EVALUATION",
}
VALID_CONFIDENCE = {"LOW", "MEDIUM", "HIGH"}


@dataclass(frozen=True)
class DimensionEvidence:
    dimension: str
    value: float
    higher_is_better: bool
    evidence_class: str
    evidence_refs: tuple[str, ...]
    confidence: str
    rationale: str
    rubric_id: str
    calibration_scope: str
    uncertainty: float
    hard_gate: bool = False
    hard_gate_pass: bool = True


@dataclass(frozen=True)
class CandidateEvaluation:
    candidate_id: str
    dimensions: tuple[DimensionEvidence, ...]
    unresolved_blockers: tuple[str, ...] = ()


def validate_candidate_evaluation(
    evaluation: CandidateEvaluation,
    *,
    required_dimensions: Iterable[str] = DEFAULT_DIMENSIONS,
) -> str:
    if not evaluation.candidate_id:
        raise NarrativeEvaluationError("candidate id required")
    by_dim = {d.dimension: d for d in evaluation.dimensions}
    if len(by_dim) != len(evaluation.dimensions):
        raise NarrativeEvaluationError("duplicate narrative dimension")
    missing = set(required_dimensions) - set(by_dim)
    if missing:
        raise NarrativeEvaluationError("missing required dimensions: " + ",".join(sorted(missing)))
    for dimension in evaluation.dimensions:
        if dimension.evidence_class not in VALID_EVIDENCE_CLASSES:
            raise NarrativeEvaluationError(f"unknown evidence class: {dimension.evidence_class}")
        if dimension.confidence not in VALID_CONFIDENCE:
            raise NarrativeEvaluationError(f"unknown confidence: {dimension.dimension}")
        if not dimension.evidence_refs or not dimension.rationale.strip():
            raise NarrativeEvaluationError(f"dimension lacks evidence: {dimension.dimension}")
        if not dimension.rubric_id.strip() or not dimension.calibration_scope.strip():
            raise NarrativeEvaluationError(f"dimension lacks comparison rubric/calibration scope: {dimension.dimension}")
        if not 0.0 <= dimension.value <= 1.0:
            raise NarrativeEvaluationError(f"dimension out of range: {dimension.dimension}")
        if not 0.0 <= dimension.uncertainty <= 0.5:
            raise NarrativeEvaluationError(f"dimension uncertainty out of range: {dimension.dimension}")
        if dimension.evidence_class == "MODEL_SELF_EVALUATION":
            if dimension.hard_gate:
                raise NarrativeEvaluationError("model self-evaluation cannot be a hard promotion gate")
            if dimension.uncertainty < 0.20:
                raise NarrativeEvaluationError("model self-evaluation may not claim artificially precise uncertainty")
    return "NARRATIVE_VECTOR_EVALUATION_VALID"


def promotion_gate(evaluation: CandidateEvaluation) -> str:
    validate_candidate_evaluation(evaluation)
    failed = [d.dimension for d in evaluation.dimensions if d.hard_gate and not d.hard_gate_pass]
    if failed:
        raise NarrativeEvaluationError("candidate blocked by hard gates: " + ",".join(sorted(failed)))
    if evaluation.unresolved_blockers:
        raise NarrativeEvaluationError("candidate has unresolved blockers")
    return "NARRATIVE_PROMOTION_GATE_PASS"


def _oriented_interval(dimension: DimensionEvidence) -> tuple[float, float]:
    low = max(0.0, dimension.value - dimension.uncertainty)
    high = min(1.0, dimension.value + dimension.uncertainty)
    if dimension.higher_is_better:
        return low, high
    # For lower-is-better metrics, orient so larger is still better.
    return 1.0 - high, 1.0 - low


def _require_dimension_comparability(left: DimensionEvidence, right: DimensionEvidence) -> None:
    if left.higher_is_better != right.higher_is_better:
        raise NarrativeEvaluationError(f"direction mismatch for dimension: {left.dimension}")
    if left.rubric_id != right.rubric_id or left.calibration_scope != right.calibration_scope:
        raise NarrativeEvaluationError(
            f"dimension is not numerically comparable across candidates without re-benchmarking: {left.dimension}"
        )


def pareto_dominates(
    left: CandidateEvaluation,
    right: CandidateEvaluation,
    *,
    dimensions: Iterable[str] = DEFAULT_DIMENSIONS,
) -> bool:
    validate_candidate_evaluation(left, required_dimensions=dimensions)
    validate_candidate_evaluation(right, required_dimensions=dimensions)
    left_by = {d.dimension: d for d in left.dimensions}
    right_by = {d.dimension: d for d in right.dimensions}
    selected = tuple(dimensions)
    at_least_one_definitely_better = False
    for name in selected:
        ldim = left_by[name]
        rdim = right_by[name]
        _require_dimension_comparability(ldim, rdim)
        l_low, l_high = _oriented_interval(ldim)
        r_low, r_high = _oriented_interval(rdim)
        # Conservative dominance: if intervals overlap, do not manufacture certainty.
        if l_low < r_high:
            if l_high < r_low:
                return False
            # overlap means neither side is definitely better on this dimension
            continue
        if l_low > r_high:
            at_least_one_definitely_better = True
    return at_least_one_definitely_better


def pareto_front(
    evaluations: Iterable[CandidateEvaluation],
    *,
    dimensions: Iterable[str] = DEFAULT_DIMENSIONS,
) -> tuple[str, ...]:
    items = tuple(evaluations)
    if len(items) < 2:
        raise NarrativeEvaluationError("Pareto comparison requires at least two candidates")
    ids = [e.candidate_id for e in items]
    if len(ids) != len(set(ids)):
        raise NarrativeEvaluationError("candidate ids must be unique")
    front: list[str] = []
    for candidate in items:
        dominated = any(
            other.candidate_id != candidate.candidate_id
            and pareto_dominates(other, candidate, dimensions=dimensions)
            for other in items
        )
        if not dominated:
            front.append(candidate.candidate_id)
    return tuple(sorted(front))


def require_pairwise_reasoning(
    evaluations: Iterable[CandidateEvaluation],
    *,
    pairwise_tradeoff_refs: Mapping[str, Iterable[str]],
) -> str:
    items = tuple(evaluations)
    ids = {item.candidate_id for item in items}
    if len(ids) < 2:
        raise NarrativeEvaluationError("pairwise reasoning requires multiple candidates")
    for candidate_id in ids:
        refs = tuple(r for r in pairwise_tradeoff_refs.get(candidate_id, ()) if isinstance(r, str) and r.strip())
        if not refs:
            raise NarrativeEvaluationError(f"candidate lacks pairwise/tradeoff evidence: {candidate_id}")
    return "PAIRWISE_TRADEOFF_EVIDENCE_COMPLETE"


def reject_scalar_override(*, aggregate_score: float, hard_gate_failed: bool) -> str:
    if hard_gate_failed:
        raise NarrativeEvaluationError(
            f"aggregate score {aggregate_score:.3f} cannot override a failed hard gate"
        )
    return "SCALAR_PRESENTATION_ALLOWED__NOT_DECISION_AUTHORITY"
