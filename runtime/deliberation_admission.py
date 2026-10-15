#!/usr/bin/env python3
"""Evidence-first admission for material Novel-domain decisions and problem root scope.

This module realizes the UAOS cognition floor owner-natively. It does not claim that
every host response is physically intercepted and it does not create a second controller.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class DeliberationAdmissionError(RuntimeError):
    pass


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(v.strip() for v in (values or ()) if isinstance(v, str) and v.strip())


@dataclass(frozen=True)
class MaterialDecisionReceipt:
    question: str
    authority_refs: tuple[str, ...]
    internal_evidence_refs: tuple[str, ...]
    external_evidence_refs: tuple[str, ...]
    alternatives: tuple[str, ...]
    counterexamples: tuple[str, ...]
    challenged_assumptions: tuple[str, ...]
    selected_option: str
    rejection_reasons: tuple[str, ...]
    risks: tuple[str, ...]
    rollback_or_recovery: tuple[str, ...]
    external_research_not_material_reason: str = ""

    @property
    def has_external_grounding(self) -> bool:
        return bool(self.external_evidence_refs or self.external_research_not_material_reason.strip())


def build_material_decision_receipt(
    *,
    question: str,
    authority_refs: Iterable[str],
    internal_evidence_refs: Iterable[str],
    external_evidence_refs: Iterable[str] | None,
    alternatives: Iterable[str],
    counterexamples: Iterable[str],
    challenged_assumptions: Iterable[str],
    selected_option: str,
    rejection_reasons: Iterable[str],
    risks: Iterable[str],
    rollback_or_recovery: Iterable[str],
    external_research_not_material_reason: str = "",
) -> MaterialDecisionReceipt:
    receipt = MaterialDecisionReceipt(
        question=question.strip(),
        authority_refs=_clean(authority_refs),
        internal_evidence_refs=_clean(internal_evidence_refs),
        external_evidence_refs=_clean(external_evidence_refs),
        alternatives=_clean(alternatives),
        counterexamples=_clean(counterexamples),
        challenged_assumptions=_clean(challenged_assumptions),
        selected_option=selected_option.strip(),
        rejection_reasons=_clean(rejection_reasons),
        risks=_clean(risks),
        rollback_or_recovery=_clean(rollback_or_recovery),
        external_research_not_material_reason=external_research_not_material_reason.strip(),
    )
    if not receipt.question:
        raise DeliberationAdmissionError("material decision requires an explicit question")
    if not receipt.authority_refs or not receipt.internal_evidence_refs:
        raise DeliberationAdmissionError("material decision requires current authority and internal evidence")
    if not receipt.has_external_grounding:
        raise DeliberationAdmissionError(
            "material decision requires external evidence or an explicit reason external research is not material"
        )
    if len(receipt.alternatives) < 2:
        raise DeliberationAdmissionError("material decision requires at least two alternatives")
    if not receipt.counterexamples or not receipt.challenged_assumptions:
        raise DeliberationAdmissionError("material decision requires counterexample and assumption challenge")
    if not receipt.selected_option or not receipt.rejection_reasons:
        raise DeliberationAdmissionError("material decision requires selection and rejected-option reasoning")
    if not receipt.risks or not receipt.rollback_or_recovery:
        raise DeliberationAdmissionError("material decision requires risks and rollback/recovery")
    return receipt


def admit_material_mutation(receipt: MaterialDecisionReceipt | None) -> str:
    if receipt is None:
        raise DeliberationAdmissionError("material mutation denied: no deliberation receipt")
    if len(receipt.alternatives) < 2 or not receipt.counterexamples or not receipt.challenged_assumptions:
        raise DeliberationAdmissionError("material mutation denied: deliberation floor incomplete")
    if not receipt.has_external_grounding:
        raise DeliberationAdmissionError("material mutation denied: external-grounding decision missing")
    if not receipt.authority_refs or not receipt.internal_evidence_refs:
        raise DeliberationAdmissionError("material mutation denied: evidence grounding incomplete")
    return "MATERIAL_MUTATION_ADMITTED__EVIDENCE_COMPARE_CHALLENGE_COMPLETE"


class ProblemLayer(str, Enum):
    LOCAL_IMPLEMENTATION = "LOCAL_IMPLEMENTATION"
    DOMAIN_WORKFLOW = "DOMAIN_WORKFLOW"
    DOMAIN_ARCHITECTURE = "DOMAIN_ARCHITECTURE"
    COMMON_CAPABILITY = "COMMON_CAPABILITY"
    CONTROL_PLANE = "CONTROL_PLANE"
    HOST = "HOST"
    REQUIREMENT_OR_GOAL = "REQUIREMENT_OR_GOAL"


class HypothesisDisposition(str, Enum):
    PLAUSIBLE = "PLAUSIBLE"
    SELECTED = "SELECTED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class RootScopeHypothesis:
    hypothesis_id: str
    layer: ProblemLayer
    statement: str
    disposition: HypothesisDisposition
    supporting_evidence_refs: tuple[str, ...]
    falsification_or_rejection_refs: tuple[str, ...]


@dataclass(frozen=True)
class RootScopeReceipt:
    selected_hypothesis_id: str
    selected_layer: ProblemLayer
    compared_layers: tuple[ProblemLayer, ...]
    rejected_hypothesis_ids: tuple[str, ...]
    architecture_reassessment_refs: tuple[str, ...]
    evidence_refs: tuple[str, ...]


def build_root_scope_receipt(
    *,
    hypotheses: Iterable[RootScopeHypothesis],
    selected_hypothesis_id: str,
    systemic_signal: bool = False,
    architecture_reassessment_refs: Iterable[str] | None = None,
    direct_user_or_external_claim_promoted_without_test: bool = False,
) -> RootScopeReceipt:
    """Admit a Novel problem layer before repair/no-change.

    `systemic_signal` applies to repeated/cross-subsystem/architecture-gap/complexity-
    growth/scope-expansion problems and forces an explicit upstream hypothesis test.
    """
    items = tuple(hypotheses)
    architecture_refs = _clean(architecture_reassessment_refs)
    if direct_user_or_external_claim_promoted_without_test:
        raise DeliberationAdmissionError(
            "root-scope admission denied: user/external framing was promoted without falsification"
        )
    if not items:
        raise DeliberationAdmissionError("root-scope admission requires hypotheses")
    ids = [item.hypothesis_id.strip() for item in items]
    if any(not value for value in ids) or len(ids) != len(set(ids)):
        raise DeliberationAdmissionError("root-scope hypothesis ids must be non-empty and unique")
    for item in items:
        if not item.statement.strip() or not item.supporting_evidence_refs or not item.falsification_or_rejection_refs:
            raise DeliberationAdmissionError(
                "every root-scope hypothesis requires statement, supporting evidence and falsification/rejection evidence"
            )
    selected = [item for item in items if item.hypothesis_id == selected_hypothesis_id]
    if len(selected) != 1 or selected[0].disposition is not HypothesisDisposition.SELECTED:
        raise DeliberationAdmissionError("selected_hypothesis_id must identify the one SELECTED hypothesis")
    if sum(item.disposition is HypothesisDisposition.SELECTED for item in items) != 1:
        raise DeliberationAdmissionError("exactly one root-scope hypothesis may be SELECTED")

    layers = tuple(sorted({item.layer for item in items}, key=lambda item: item.value))
    rejected = tuple(sorted(item.hypothesis_id for item in items if item.disposition is HypothesisDisposition.REJECTED))
    if systemic_signal:
        if len(items) < 2 or len(layers) < 2:
            raise DeliberationAdmissionError("systemic problem requires competing hypotheses across at least two layers")
        if not rejected:
            raise DeliberationAdmissionError("systemic problem requires an evidence-rejected alternative")
        upstream = {
            ProblemLayer.DOMAIN_ARCHITECTURE,
            ProblemLayer.COMMON_CAPABILITY,
            ProblemLayer.CONTROL_PLANE,
            ProblemLayer.HOST,
            ProblemLayer.REQUIREMENT_OR_GOAL,
        }
        if not any(item.layer in upstream for item in items):
            raise DeliberationAdmissionError("systemic problem must test an architecture/upstream hypothesis")
        if not architecture_refs:
            raise DeliberationAdmissionError("systemic problem requires architecture reassessment evidence")

    chosen = selected[0]
    evidence = tuple(sorted({
        *chosen.supporting_evidence_refs,
        *chosen.falsification_or_rejection_refs,
        *architecture_refs,
    }))
    return RootScopeReceipt(
        selected_hypothesis_id=chosen.hypothesis_id,
        selected_layer=chosen.layer,
        compared_layers=layers,
        rejected_hypothesis_ids=rejected,
        architecture_reassessment_refs=architecture_refs,
        evidence_refs=evidence,
    )
