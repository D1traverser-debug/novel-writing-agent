#!/usr/bin/env python3
"""Executable learning-transfer contracts for the Novel domain.

The goal is not to anthropomorphize model memory. The system verifies that compacted
learning evidence remains usable after the source/ledger is closed, that cross-work
comparisons do not double-count related evidence families, and that transfer is tested
before a craft rule is promoted.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class LearningTransferAdmissionError(RuntimeError):
    pass


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(v.strip() for v in (values or ()) if isinstance(v, str) and v.strip())


@dataclass(frozen=True)
class ClosedContextReconstruction:
    work_id: str
    compact_index_ref: str
    recalled_mechanisms: tuple[str, ...]
    missed_or_distorted: tuple[str, ...]
    correction_refs: tuple[str, ...]


@dataclass(frozen=True)
class CrossWorkComparisonReceipt:
    current_work_id: str
    compared_work_ids: tuple[str, ...]
    evidence_family_ids: tuple[str, ...]
    common_mechanisms: tuple[str, ...]
    conflicts_or_boundary_conditions: tuple[str, ...]
    negative_evidence: tuple[str, ...]
    updated_observation_axes: tuple[str, ...]
    promotion_requested: bool = False


@dataclass(frozen=True)
class TransferProbeReceipt:
    capability_id: str
    target_case_id: str
    source_mechanism_ids: tuple[str, ...]
    alternatives: tuple[str, ...]
    predicted_gain: tuple[str, ...]
    predicted_side_effects: tuple[str, ...]
    adversarial_findings: tuple[str, ...]
    outcome: str
    evidence_refs: tuple[str, ...]


def admit_closed_context_reconstruction(receipt: ClosedContextReconstruction) -> str:
    if not receipt.work_id or not receipt.compact_index_ref:
        raise LearningTransferAdmissionError("closed-context reconstruction requires work and compact index")
    if not receipt.recalled_mechanisms:
        raise LearningTransferAdmissionError("closed-context reconstruction requires recalled mechanism structure")
    if receipt.missed_or_distorted and not receipt.correction_refs:
        raise LearningTransferAdmissionError("reconstruction errors require correction evidence")
    return "CLOSED_CONTEXT_RECONSTRUCTION_ADMITTED"


def admit_interbook_comparison(
    receipt: CrossWorkComparisonReceipt,
    *,
    completed_work_ids: Iterable[str],
) -> str:
    completed = set(_clean(completed_work_ids))
    if receipt.current_work_id not in completed:
        raise LearningTransferAdmissionError("interbook comparison requires a completed current work")
    if any(w not in completed for w in receipt.compared_work_ids):
        raise LearningTransferAdmissionError("comparison may only count completed works as completed evidence")
    if receipt.current_work_id in receipt.compared_work_ids:
        raise LearningTransferAdmissionError("current work must not be duplicated in compared work ids")
    if completed - {receipt.current_work_id} and not receipt.compared_work_ids:
        raise LearningTransferAdmissionError("a completed work must be compared with prior completed evidence")
    all_works = (receipt.current_work_id,) + receipt.compared_work_ids
    if len(receipt.evidence_family_ids) != len(all_works):
        raise LearningTransferAdmissionError("evidence family ids must bind one-to-one to compared works")
    if len(set(receipt.evidence_family_ids)) < min(2, len(all_works)):
        raise LearningTransferAdmissionError("cross-work comparison cannot pretend one evidence family is independent corroboration")
    if not receipt.common_mechanisms or not receipt.conflicts_or_boundary_conditions:
        raise LearningTransferAdmissionError("comparison requires both commonality and conflict/boundary evidence")
    if not receipt.negative_evidence or not receipt.updated_observation_axes:
        raise LearningTransferAdmissionError("comparison requires negative evidence and updated observation axes")
    if receipt.promotion_requested:
        raise LearningTransferAdmissionError("interbook comparison is non-promotional during active corpus study")
    return "INTERBOOK_COMPARISON_ADMITTED__NON_PROMOTIONAL"


def admit_transfer_probe(receipt: TransferProbeReceipt) -> str:
    if not receipt.capability_id or not receipt.target_case_id:
        raise LearningTransferAdmissionError("transfer probe requires capability and target case")
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
    *,
    mechanism_id: str,
    corpus_campaign_complete: bool,
    supporting_work_ids: Iterable[str],
    supporting_evidence_family_ids: Iterable[str],
    genre_clusters: Iterable[str],
    negative_or_boundary_evidence: Iterable[str],
    transfer_probe_refs: Iterable[str],
    external_or_live_outcome_refs: Iterable[str],
) -> str:
    works = _clean(supporting_work_ids)
    families = _clean(supporting_evidence_family_ids)
    genres = _clean(genre_clusters)
    negatives = _clean(negative_or_boundary_evidence)
    probes = _clean(transfer_probe_refs)
    outcomes = _clean(external_or_live_outcome_refs)
    if not mechanism_id.strip():
        raise LearningTransferAdmissionError("promotion requires mechanism id")
    if not corpus_campaign_complete:
        raise LearningTransferAdmissionError("ACTIVE_RULE promotion is blocked while the current corpus campaign is incomplete")
    if len(works) < 3 or len(set(families)) < 3 or len(set(genres)) < 2:
        raise LearningTransferAdmissionError("promotion requires at least three independent evidence families across at least two genre clusters")
    if len(families) != len(works):
        raise LearningTransferAdmissionError("support work/evidence-family cardinality mismatch")
    if not negatives or not probes:
        raise LearningTransferAdmissionError("promotion requires boundary evidence and transfer probes")
    if not outcomes:
        raise LearningTransferAdmissionError("promotion requires external/platform/live outcome evidence or equivalent project benchmark evidence")
    return "ACTIVE_RULE_PROMOTION_ADMITTED__CROSS_FAMILY_TRANSFER_VERIFIED"
