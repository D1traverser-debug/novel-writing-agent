#!/usr/bin/env python3
"""Executable learning-transfer contracts for the Novel domain.

Evidence dependence is claim-conditioned and dimension-specific. Author, series, genre,
POV, market and period are possible dependency factors, not automatic merge keys or
fixed weights. The system therefore validates comparison design, unresolved confounds,
negative evidence and transfer—not book counts.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class LearningTransferAdmissionError(RuntimeError):
    pass


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(v.strip() for v in (values or ()) if isinstance(v, str) and v.strip())


VALID_STANCES = {"SUPPORT", "CONTRADICT", "BOUNDARY", "MIXED"}
VALID_FACTOR_RELEVANCE = {"LOW", "MEDIUM", "HIGH", "UNKNOWN"}
VALID_COMPARISON_DESIGNS = {
    "WITHIN_AUTHOR_CROSS_WORK",
    "WITHIN_SERIES_CROSS_STAGE",
    "CROSS_AUTHOR_SAME_OR_ADJACENT_GENRE",
    "CROSS_GENRE_SAME_FUNCTION",
    "CROSS_FORMAT_OR_MARKET",
    "WITHIN_WORK_CROSS_ARC",
    "MATCHED_SURFACE_DIFFERENT_FUNCTION",
    "MATCHED_FUNCTION_DIFFERENT_SURFACE",
}


@dataclass(frozen=True)
class ClosedContextReconstruction:
    work_id: str
    compact_index_ref: str
    recalled_mechanisms: tuple[str, ...]
    recalled_boundaries: tuple[str, ...]
    missed_or_distorted: tuple[str, ...]
    correction_refs: tuple[str, ...]


@dataclass(frozen=True)
class ObservationRef:
    work_id: str
    evidence_ref: str
    stance: str
    observation_scale: str


@dataclass(frozen=True)
class SharedFactorAssessment:
    factor_id: str
    affected_work_ids: tuple[str, ...]
    relevance_to_claim: str
    rationale: str
    mitigation_or_contrast: str


@dataclass(frozen=True)
class CrossWorkComparisonReceipt:
    claim_id: str
    target_dimensions: tuple[str, ...]
    observations: tuple[ObservationRef, ...]
    comparison_designs: tuple[str, ...]
    shared_factor_assessments: tuple[SharedFactorAssessment, ...]
    common_or_candidate_mechanisms: tuple[str, ...]
    conflicts_or_boundary_conditions: tuple[str, ...]
    negative_evidence_refs: tuple[str, ...]
    alternative_explanations: tuple[str, ...]
    updated_observation_axes: tuple[str, ...]
    unresolved_confounds: tuple[str, ...]
    promotion_requested: bool = False


@dataclass(frozen=True)
class TransferProbeReceipt:
    capability_id: str
    target_case_id: str
    target_dimensions: tuple[str, ...]
    source_mechanism_ids: tuple[str, ...]
    alternatives: tuple[str, ...]
    predicted_gain: tuple[str, ...]
    predicted_side_effects: tuple[str, ...]
    adversarial_findings: tuple[str, ...]
    outcome: str
    evidence_refs: tuple[str, ...]


@dataclass(frozen=True)
class PromotionEvidenceBundle:
    mechanism_id: str
    target_dimensions: tuple[str, ...]
    comparison_receipt_refs: tuple[str, ...]
    comparison_designs: tuple[str, ...]
    supporting_work_ids: tuple[str, ...]
    boundary_or_contradiction_refs: tuple[str, ...]
    resolved_high_relevance_factor_refs: tuple[str, ...]
    unresolved_high_relevance_factors: tuple[str, ...]
    transfer_probe_refs: tuple[str, ...]
    external_or_live_outcome_refs: tuple[str, ...]


def admit_closed_context_reconstruction(receipt: ClosedContextReconstruction) -> str:
    if not receipt.work_id or not receipt.compact_index_ref:
        raise LearningTransferAdmissionError("closed-context reconstruction requires work and compact index")
    if not receipt.recalled_mechanisms or not receipt.recalled_boundaries:
        raise LearningTransferAdmissionError("reconstruction requires mechanisms and boundaries, not summary alone")
    if receipt.missed_or_distorted and not receipt.correction_refs:
        raise LearningTransferAdmissionError("reconstruction errors require correction evidence")
    return "CLOSED_CONTEXT_RECONSTRUCTION_ADMITTED"


def admit_interbook_comparison(
    receipt: CrossWorkComparisonReceipt,
    *,
    completed_work_ids: Iterable[str],
) -> str:
    completed = set(_clean(completed_work_ids))
    if not receipt.claim_id or not receipt.target_dimensions:
        raise LearningTransferAdmissionError("comparison requires a claim and target narrative dimensions")
    if len(receipt.observations) < 2:
        raise LearningTransferAdmissionError("comparison requires at least two observations")
    work_ids = [obs.work_id for obs in receipt.observations]
    if any(work_id not in completed for work_id in work_ids):
        raise LearningTransferAdmissionError("comparison may only use completed works as completed evidence")
    if len(set(work_ids)) < 2:
        raise LearningTransferAdmissionError("interbook comparison requires at least two works")
    for obs in receipt.observations:
        if obs.stance not in VALID_STANCES:
            raise LearningTransferAdmissionError(f"invalid observation stance: {obs.stance}")
        if not obs.evidence_ref or not obs.observation_scale:
            raise LearningTransferAdmissionError("every observation requires evidence ref and observation scale")
    if not receipt.comparison_designs:
        raise LearningTransferAdmissionError("comparison requires an explicit comparison design")
    if any(d not in VALID_COMPARISON_DESIGNS for d in receipt.comparison_designs):
        raise LearningTransferAdmissionError("comparison uses unknown comparison design")
    if not receipt.shared_factor_assessments:
        raise LearningTransferAdmissionError("comparison requires shared-factor assessment; independence may not be assumed")
    for factor in receipt.shared_factor_assessments:
        if factor.relevance_to_claim not in VALID_FACTOR_RELEVANCE:
            raise LearningTransferAdmissionError("invalid shared-factor relevance")
        if not factor.factor_id or not factor.affected_work_ids or not factor.rationale:
            raise LearningTransferAdmissionError("shared-factor assessment is incomplete")
        if factor.relevance_to_claim in {"MEDIUM", "HIGH", "UNKNOWN"} and not factor.mitigation_or_contrast:
            raise LearningTransferAdmissionError(
                "material/unknown shared factor requires mitigation, contrast, or explicit unresolved-confound handling"
            )
    if not receipt.common_or_candidate_mechanisms:
        raise LearningTransferAdmissionError("comparison requires candidate mechanism structure")
    if not receipt.conflicts_or_boundary_conditions or not receipt.negative_evidence_refs:
        raise LearningTransferAdmissionError("comparison requires conflict/boundary and negative evidence")
    if not receipt.alternative_explanations:
        raise LearningTransferAdmissionError("comparison requires alternative explanations")
    if not receipt.updated_observation_axes:
        raise LearningTransferAdmissionError("comparison must update future observation axes")
    if receipt.promotion_requested:
        raise LearningTransferAdmissionError("interbook comparison is non-promotional during active corpus study")
    return "INTERBOOK_COMPARISON_ADMITTED__CLAIM_CONDITIONED__NON_PROMOTIONAL"


def admit_transfer_probe(receipt: TransferProbeReceipt) -> str:
    if not receipt.capability_id or not receipt.target_case_id or not receipt.target_dimensions:
        raise LearningTransferAdmissionError("transfer probe requires capability, target case and target dimensions")
    if not receipt.source_mechanism_ids:
        raise LearningTransferAdmissionError("transfer probe requires source mechanisms")
    if len(receipt.alternatives) < 2:
        raise LearningTransferAdmissionError("transfer probe requires at least two candidate applications")
    if not receipt.predicted_gain or not receipt.predicted_side_effects:
        raise LearningTransferAdmissionError("transfer probe requires gain and side-effect predictions")
    if not receipt.adversarial_findings:
        raise LearningTransferAdmissionError("transfer probe requires adversarial review")
    if receipt.outcome not in {"SUPPORTED", "REJECTED", "INCONCLUSIVE"}:
        raise LearningTransferAdmissionError("invalid transfer probe outcome")
    if not receipt.evidence_refs:
        raise LearningTransferAdmissionError("transfer probe requires evidence refs")
    return "TRANSFER_PROBE_ADMITTED"


def admit_active_rule_promotion(
    bundle: PromotionEvidenceBundle,
    *,
    corpus_campaign_complete: bool,
) -> str:
    if not bundle.mechanism_id or not bundle.target_dimensions:
        raise LearningTransferAdmissionError("promotion requires mechanism id and target dimensions")
    if not corpus_campaign_complete:
        raise LearningTransferAdmissionError("ACTIVE_RULE promotion is blocked while the current corpus campaign is incomplete")
    if len(bundle.supporting_work_ids) < 3:
        raise LearningTransferAdmissionError("promotion requires repeated support across at least three works; this is not an independence claim")
    if len(bundle.comparison_receipt_refs) < 2 or len(set(bundle.comparison_designs)) < 2:
        raise LearningTransferAdmissionError("promotion requires at least two distinct comparison designs")
    if not set(bundle.comparison_designs).issubset(VALID_COMPARISON_DESIGNS):
        raise LearningTransferAdmissionError("promotion references unknown comparison design")
    if not bundle.boundary_or_contradiction_refs:
        raise LearningTransferAdmissionError("promotion requires boundary or contradiction evidence")
    if bundle.unresolved_high_relevance_factors:
        raise LearningTransferAdmissionError(
            "promotion denied: high-relevance dependency/confound factors remain unresolved"
        )
    if not bundle.resolved_high_relevance_factor_refs:
        raise LearningTransferAdmissionError("promotion requires evidence showing material shared factors were challenged")
    if not bundle.transfer_probe_refs:
        raise LearningTransferAdmissionError("promotion requires transfer probes")
    if not bundle.external_or_live_outcome_refs:
        raise LearningTransferAdmissionError("promotion requires project/platform/live outcome evidence or equivalent benchmark evidence")
    return "ACTIVE_RULE_PROMOTION_ADMITTED__DEPENDENCY_CHALLENGED__TRANSFER_VERIFIED"
