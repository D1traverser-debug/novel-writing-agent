#!/usr/bin/env python3
"""Novel-owner executable admission for recovery, root-scope cognition and problem closure.

This module provides Novel-owned recovery, root-scope and problem-closure admission.
CAOS governs cross-domain cognition in the active ChatGPT session; Novel retains its
business authority and executable domain gates without a parent runtime dependency.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from .deliberation_admission import MaterialDecisionReceipt, admit_material_mutation


RECOVERY_OUTCOMES = {"RESOLVED", "PROVISIONAL", "UNRESOLVED"}
CLOSURE_TERMINALS = {"REPAIR_EXECUTED", "BLOCKED_WITH_REASON", "NO_CHANGE_WITH_EVIDENCE"}


class BehaviorAdmissionError(RuntimeError):
    pass


class ProblemLayer(str, Enum):
    PROSE_OR_ARTIFACT = "PROSE_OR_ARTIFACT"
    PROJECT_WORKFLOW = "PROJECT_WORKFLOW"
    LEARNING_OR_PLAN = "LEARNING_OR_PLAN"
    DOMAIN_ARCHITECTURE = "DOMAIN_ARCHITECTURE"
    COMMON_CAPABILITY = "COMMON_CAPABILITY"
    CAOS_GOVERNANCE = "CAOS_GOVERNANCE"
    HOST = "HOST"
    REQUIREMENT_OR_GOAL = "REQUIREMENT_OR_GOAL"


class HypothesisDisposition(str, Enum):
    PLAUSIBLE = "PLAUSIBLE"
    SELECTED = "SELECTED"
    REJECTED = "REJECTED"


class EvolutionDisposition(str, Enum):
    LOCAL_LEARNING_ONLY = "LOCAL_LEARNING_ONLY"
    NO_DURABLE_EVOLUTION_WITH_EVIDENCE = "NO_DURABLE_EVOLUTION_WITH_EVIDENCE"
    DOMAIN_EVOLUTION_CANDIDATE = "DOMAIN_EVOLUTION_CANDIDATE"
    DOMAIN_EVOLUTION_UPDATED = "DOMAIN_EVOLUTION_UPDATED"
    CAOS_GOVERNANCE_REVIEW = "CAOS_GOVERNANCE_REVIEW"


@dataclass(frozen=True)
class RootScopeHypothesis:
    hypothesis_id: str
    layer: ProblemLayer
    statement: str
    disposition: HypothesisDisposition
    supporting_evidence_refs: tuple[str, ...]
    falsification_or_rejection_refs: tuple[str, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.hypothesis_id, str) or not self.hypothesis_id.strip():
            raise ValueError("root-scope hypothesis requires a nonblank identity")
        if not isinstance(self.statement, str) or not self.statement.strip():
            raise ValueError("root-scope hypothesis requires a nonblank statement")
        if not isinstance(self.layer, ProblemLayer) or not isinstance(self.disposition, HypothesisDisposition):
            raise ValueError("root-scope hypothesis requires typed layer and disposition")
        for label, refs in (
            ("supporting", self.supporting_evidence_refs),
            ("falsification/rejection", self.falsification_or_rejection_refs),
        ):
            if not isinstance(refs, tuple) or not refs or any(
                not isinstance(ref, str) or not ref.strip() for ref in refs
            ):
                raise ValueError(f"root-scope hypothesis requires usable {label} evidence references")


@dataclass(frozen=True)
class RootScopeReceipt:
    selected_hypothesis_id: str
    selected_layer: ProblemLayer
    compared_layers: tuple[ProblemLayer, ...]
    hypothesis_count: int
    material_deliberation_bound: bool
    architecture_reassessment_performed: bool
    durable_problem_record_required: bool
    evidence_refs: tuple[str, ...]
    hypotheses: tuple[RootScopeHypothesis, ...]
    architecture_reassessment_refs: tuple[str, ...]
    material_decision_receipt: MaterialDecisionReceipt | None
    systemic: bool

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.selected_hypothesis_id, str) or not self.selected_hypothesis_id.strip():
            raise ValueError("root-scope receipt requires a selected hypothesis identity")
        if not isinstance(self.hypotheses, tuple) or not self.hypotheses:
            raise ValueError("root-scope receipt must retain the compared hypotheses and their evidence")
        if any(not isinstance(item, RootScopeHypothesis) for item in self.hypotheses):
            raise ValueError("root-scope receipt contains an invalid hypothesis")
        ids = [item.hypothesis_id for item in self.hypotheses]
        if len(ids) != len(set(ids)):
            raise ValueError("root-scope receipt hypothesis identifiers must be unique")
        selected = [item for item in self.hypotheses if item.hypothesis_id == self.selected_hypothesis_id]
        if len(selected) != 1 or selected[0].disposition is not HypothesisDisposition.SELECTED:
            raise ValueError("root-scope receipt must retain exactly one selected hypothesis")
        if sum(item.disposition is HypothesisDisposition.SELECTED for item in self.hypotheses) != 1:
            raise ValueError("root-scope receipt must retain exactly one selected hypothesis")
        layers = tuple(sorted({item.layer for item in self.hypotheses}, key=lambda layer: layer.value))
        if self.compared_layers != layers or self.selected_layer is not selected[0].layer:
            raise ValueError("root-scope receipt layer summary does not match its hypotheses")
        if self.hypothesis_count != len(self.hypotheses):
            raise ValueError("root-scope receipt hypothesis count does not match retained evidence")
        architecture_refs = _clean(self.architecture_reassessment_refs)
        if architecture_refs != self.architecture_reassessment_refs:
            raise ValueError("root-scope receipt architecture evidence contains blank or duplicate references")
        expected_refs = tuple(sorted({
            *(
                ref
                for item in self.hypotheses
                for ref in (*item.supporting_evidence_refs, *item.falsification_or_rejection_refs)
            ),
            *architecture_refs,
        }))
        if self.evidence_refs != expected_refs:
            raise ValueError("root-scope receipt evidence must retain all selected and rejected hypothesis references")
        if self.architecture_reassessment_performed != bool(architecture_refs):
            raise ValueError("root-scope receipt architecture-reassessment flag is inconsistent")
        if self.material_deliberation_bound != (self.material_decision_receipt is not None):
            raise ValueError("root-scope receipt material-deliberation binding is inconsistent")
        if self.material_decision_receipt is not None:
            try:
                admit_material_mutation(self.material_decision_receipt)
            except Exception as exc:
                raise ValueError(f"root-scope receipt has invalid material-deliberation evidence: {exc}") from exc
        if self.systemic:
            if not self.durable_problem_record_required:
                raise ValueError("systemic root-scope receipt must require durable problem evidence")
            if len(self.hypotheses) < 2 or len(layers) < 2:
                raise ValueError("systemic root-scope receipt requires competing hypotheses across layers")
            if not any(item.disposition is HypothesisDisposition.REJECTED for item in self.hypotheses):
                raise ValueError("systemic root-scope receipt requires a rejected alternative")
            if not any(layer in _UPSTREAM_LAYERS for layer in layers):
                raise ValueError("systemic root-scope receipt must test an architecture/upstream layer")
            if not architecture_refs or self.material_decision_receipt is None:
                raise ValueError("systemic root-scope receipt requires architecture and material-deliberation evidence")
        elif self.durable_problem_record_required:
            raise ValueError("non-systemic root-scope receipt cannot assert a systemic durable-record requirement")


_UPSTREAM_LAYERS = {
    ProblemLayer.DOMAIN_ARCHITECTURE,
    ProblemLayer.COMMON_CAPABILITY,
    ProblemLayer.CAOS_GOVERNANCE,
    ProblemLayer.HOST,
    ProblemLayer.REQUIREMENT_OR_GOAL,
}


def require_root_scope_admission(
    *,
    hypotheses: tuple[RootScopeHypothesis, ...],
    selected_hypothesis_id: str,
    material_problem: bool = False,
    repeated_failure: bool = False,
    cross_subsystem: bool = False,
    architecture_gap: bool = False,
    complexity_growth: bool = False,
    scope_expansion: bool = False,
    architecture_reassessment_refs: Iterable[str] | None = None,
    material_decision_receipt: MaterialDecisionReceipt | None = None,
    direct_user_or_external_claim_promoted_without_test: bool = False,
) -> RootScopeReceipt:
    """Establish the problem layer before mutation/closure.

    Material/systemic Novel problems reuse ``MaterialDecisionReceipt`` for external
    grounding, alternatives, counterexamples, challenged assumptions and recovery.
    Root-scope admission adds the missing cross-layer causal question: where does the
    defect actually live?
    """

    if direct_user_or_external_claim_promoted_without_test:
        raise BehaviorAdmissionError(
            "root-scope admission denied: user/external framing was promoted without falsification"
        )
    if not hypotheses:
        raise BehaviorAdmissionError("root-scope admission requires hypotheses")
    if len({h.hypothesis_id for h in hypotheses}) != len(hypotheses):
        raise BehaviorAdmissionError("root-scope hypothesis identifiers must be unique")

    selected = [h for h in hypotheses if h.hypothesis_id == selected_hypothesis_id]
    if len(selected) != 1 or selected[0].disposition is not HypothesisDisposition.SELECTED:
        raise BehaviorAdmissionError("exactly one SELECTED hypothesis must match selected_hypothesis_id")
    if sum(h.disposition is HypothesisDisposition.SELECTED for h in hypotheses) != 1:
        raise BehaviorAdmissionError("exactly one root-scope hypothesis may be SELECTED")

    systemic = any(
        (
            material_problem,
            repeated_failure,
            cross_subsystem,
            architecture_gap,
            complexity_growth,
            scope_expansion,
        )
    )
    architecture_refs = _clean(architecture_reassessment_refs)
    compared_layers = tuple(sorted({h.layer for h in hypotheses}, key=lambda layer: layer.value))

    if systemic:
        if material_decision_receipt is None:
            raise BehaviorAdmissionError(
                "systemic/material Novel problem requires the existing material deliberation receipt"
            )
        try:
            admit_material_mutation(material_decision_receipt)
        except Exception as exc:
            raise BehaviorAdmissionError(f"material deliberation admission failed: {exc}") from exc
        if len(hypotheses) < 2 or len(compared_layers) < 2:
            raise BehaviorAdmissionError(
                "systemic/material problem requires competing hypotheses across at least two layers"
            )
        if not any(h.disposition is HypothesisDisposition.REJECTED for h in hypotheses):
            raise BehaviorAdmissionError("systemic/material problem requires an evidence-rejected alternative")
        if not any(h.layer in _UPSTREAM_LAYERS for h in hypotheses):
            raise BehaviorAdmissionError("systemic/material problem must test an architecture/upstream hypothesis")
        if not architecture_refs:
            raise BehaviorAdmissionError("systemic/material problem requires architecture/upstream reassessment evidence")

    chosen = selected[0]
    refs = tuple(
        sorted(
            {
                *(
                    ref
                    for hypothesis in hypotheses
                    for ref in (*hypothesis.supporting_evidence_refs, *hypothesis.falsification_or_rejection_refs)
                ),
                *architecture_refs,
            }
        )
    )
    return RootScopeReceipt(
        selected_hypothesis_id=chosen.hypothesis_id,
        selected_layer=chosen.layer,
        compared_layers=compared_layers,
        hypothesis_count=len(hypotheses),
        material_deliberation_bound=material_decision_receipt is not None,
        architecture_reassessment_performed=bool(architecture_refs),
        durable_problem_record_required=systemic,
        evidence_refs=refs,
        hypotheses=hypotheses,
        architecture_reassessment_refs=architecture_refs,
        material_decision_receipt=material_decision_receipt,
        systemic=systemic,
    )


def _clean(values: Iterable[str] | None) -> tuple[str, ...]:
    return tuple(v.strip() for v in (values or ()) if isinstance(v, str) and v.strip())


@dataclass(frozen=True)
class RecoveryReceipt:
    outcome: str
    authority_refs: tuple[str, ...]
    artifact_refs: tuple[str, ...]
    context_refs: tuple[str, ...]
    external_evidence_refs: tuple[str, ...]
    unknowns: tuple[str, ...]
    confidence: str
    safe_to_continue: bool

    @property
    def attempted(self) -> bool:
        return bool(self.authority_refs or self.artifact_refs or self.context_refs or self.external_evidence_refs)


def record_recovery_attempt(
    *,
    outcome: str,
    authority_refs: Iterable[str] | None = None,
    artifact_refs: Iterable[str] | None = None,
    context_refs: Iterable[str] | None = None,
    external_evidence_refs: Iterable[str] | None = None,
    unknowns: Iterable[str] | None = None,
    confidence: str = "UNSPECIFIED",
    safe_to_continue: bool,
) -> RecoveryReceipt:
    if outcome not in RECOVERY_OUTCOMES:
        raise BehaviorAdmissionError(f"invalid recovery outcome: {outcome}")
    receipt = RecoveryReceipt(
        outcome=outcome,
        authority_refs=_clean(authority_refs),
        artifact_refs=_clean(artifact_refs),
        context_refs=_clean(context_refs),
        external_evidence_refs=_clean(external_evidence_refs),
        unknowns=_clean(unknowns),
        confidence=confidence.strip() if isinstance(confidence, str) else "UNSPECIFIED",
        safe_to_continue=bool(safe_to_continue),
    )
    if not receipt.attempted:
        raise BehaviorAdmissionError("recovery receipt has no inspected evidence source")
    if outcome == "UNRESOLVED" and not receipt.unknowns:
        raise BehaviorAdmissionError("UNRESOLVED recovery requires concrete unknowns/blockers")
    if outcome in {"RESOLVED", "PROVISIONAL"} and not safe_to_continue:
        raise BehaviorAdmissionError(f"{outcome} recovery cannot be marked unsafe to continue")
    return receipt


def require_user_escalation_admission(
    receipt: RecoveryReceipt | None,
    *,
    explicit_user_confirmation: bool = False,
    requires_user_fact_or_authorization: bool = False,
) -> str:
    if explicit_user_confirmation:
        return "ADMITTED_EXPLICIT_USER_CONFIRMATION"
    if receipt is None or not receipt.attempted:
        raise BehaviorAdmissionError("user escalation denied: no recovery attempt receipt")
    if receipt.outcome in {"RESOLVED", "PROVISIONAL"} and receipt.safe_to_continue:
        raise BehaviorAdmissionError("user escalation denied: safe owner path remains available")
    if requires_user_fact_or_authorization and receipt.outcome == "UNRESOLVED" and receipt.unknowns:
        return "ADMITTED_REQUIRED_USER_FACT_OR_AUTHORIZATION"
    if receipt.outcome == "UNRESOLVED" and receipt.unknowns and not receipt.safe_to_continue:
        return "ADMITTED_UNRESOLVED_AFTER_RECOVERY"
    raise BehaviorAdmissionError("user escalation denied: blocker conditions are not satisfied")


def finalize_problem_closure(
    *,
    problem_detected: bool,
    repair_path_available: bool,
    authority_permits_repair: bool,
    explicit_user_choice_required: bool,
    repair_attempted: bool,
    repair_succeeded: bool,
    blocker_reason: str | None = None,
    no_change_evidence: Iterable[str] | None = None,
    root_scope_receipt: RootScopeReceipt | None = None,
    evolution_disposition: EvolutionDisposition | None = None,
    durable_problem_ref: str | None = None,
) -> str:
    """Reject action/closure that skipped root-scope and evolution admission."""
    if not problem_detected:
        return "CLEAN_NO_PROBLEM"

    evidence = _clean(no_change_evidence)
    blocker = blocker_reason.strip() if isinstance(blocker_reason, str) else ""

    # A genuine user-controlled choice can be surfaced without pretending root cause is settled.
    if explicit_user_choice_required and blocker:
        return "BLOCKED_WITH_REASON"

    if not isinstance(root_scope_receipt, RootScopeReceipt):
        raise BehaviorAdmissionError("problem closure denied: a valid root-scope admission receipt is missing")
    try:
        root_scope_receipt.validate()
    except Exception as exc:
        raise BehaviorAdmissionError(f"problem closure denied: invalid root-scope receipt: {exc}") from exc
    if not isinstance(evolution_disposition, EvolutionDisposition):
        raise BehaviorAdmissionError("problem closure denied: typed evolution disposition is missing")

    durable_required = bool(
        root_scope_receipt.durable_problem_record_required
        or evolution_disposition
        in {
            EvolutionDisposition.DOMAIN_EVOLUTION_CANDIDATE,
            EvolutionDisposition.DOMAIN_EVOLUTION_UPDATED,
            EvolutionDisposition.CAOS_GOVERNANCE_REVIEW,
        }
    )
    if durable_required and not (isinstance(durable_problem_ref, str) and durable_problem_ref.strip()):
        raise BehaviorAdmissionError(
            "problem closure denied: material/evolution-relevant problem requires durable causal evidence"
        )

    if repair_path_available and authority_permits_repair:
        if not repair_attempted:
            raise BehaviorAdmissionError(
                "problem closure denied: admitted authorized repair exists but was not attempted"
            )
        if repair_succeeded:
            return "REPAIR_EXECUTED"
        if blocker:
            return "BLOCKED_WITH_REASON"
        raise BehaviorAdmissionError(
            "problem closure denied: failed repair requires a concrete blocker or further repair"
        )

    if (not authority_permits_repair or not repair_path_available) and blocker:
        return "BLOCKED_WITH_REASON"
    if evidence:
        return "NO_CHANGE_WITH_EVIDENCE"

    raise BehaviorAdmissionError(
        "problem closure denied: no valid repair, blocker, or evidence-backed no-change terminal"
    )
