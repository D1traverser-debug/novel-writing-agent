#!/usr/bin/env python3
"""Evidence-bound vector evaluation for Novel product/literary decisions.

A single scalar score is deliberately insufficient. Candidate comparison is performed on
named dimensions with hard gates, missing-evidence handling and Pareto dominance.
This is an evaluation contract, not a replacement for reader/platform outcomes.
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


@dataclass(frozen=True)
class DimensionEvidence:
    dimension: str
    value: float
    higher_is_better: bool
    evidence_class: str
    evidence_refs: tuple[str, ...]
    confidence: str
    rationale: str
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
        if not dimension.evidence_refs or not dimension.rationale.strip():
            raise NarrativeEvaluationError(f"dimension lacks evidence: {dimension.dimension}")
        if not 0.0 <= dimension.value <= 1.0:
            raise NarrativeEvaluationError(f"dimension out of range: {dimension.dimension}")
        if dimension.hard_gate and not dimension.hard_gate_pass:
            # Failure is legal evidence, but this candidate cannot be promoted.
            continue
    return "NARRATIVE_VECTOR_EVALUATION_VALID"


def promotion_gate(evaluation: CandidateEvaluation) -> str:
    validate_candidate_evaluation(evaluation)
    failed = [d.dimension for d in evaluation.dimensions if d.hard_gate and not d.hard_gate_pass]
    if failed:
        raise NarrativeEvaluationError("candidate blocked by hard gates: " + ",".join(sorted(failed)))
    if evaluation.unresolved_blockers:
        raise NarrativeEvaluationError("candidate has unresolved blockers")
    return "NARRATIVE_PROMOTION_GATE_PASS"


def _oriented(dimension: DimensionEvidence) -> float:
    return dimension.value if dimension.higher_is_better else 1.0 - dimension.value


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
    at_least_one_better = False
    for name in selected:
        l = _oriented(left_by[name])
        r = _oriented(right_by[name])
        if l < r:
            return False
        if l > r:
            at_least_one_better = True
    return at_least_one_better


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
    """Regression helper: no average may override a hard gate."""
    if hard_gate_failed:
        raise NarrativeEvaluationError(
            f"aggregate score {aggregate_score:.3f} cannot override a failed hard gate"
        )
    return "SCALAR_PRESENTATION_ALLOWED__NOT_DECISION_AUTHORITY"
