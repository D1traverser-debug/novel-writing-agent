import pytest

from runtime.deliberation_admission import build_material_decision_receipt
from runtime.owner_behavior_admission import (
    BehaviorAdmissionError,
    EvolutionDisposition,
    HypothesisDisposition,
    ProblemLayer,
    RootScopeHypothesis,
    finalize_problem_closure,
    record_recovery_attempt,
    require_root_scope_admission,
    require_user_escalation_admission,
)


def hypothesis(hypothesis_id, layer, disposition):
    return RootScopeHypothesis(
        hypothesis_id=hypothesis_id,
        layer=layer,
        statement=f"candidate root at {layer.value}",
        disposition=disposition,
        supporting_evidence_refs=(f"evidence:support:{hypothesis_id}",),
        falsification_or_rejection_refs=(f"evidence:probe:{hypothesis_id}",),
    )


def material_receipt():
    return build_material_decision_receipt(
        question="Which layer owns the repeated Novel failure?",
        authority_refs=["protocols/NOVEL_PRODUCT_ARCHITECTURE.md"],
        internal_evidence_refs=["audits/EVOLUTION_INDEX.json"],
        external_evidence_refs=["method:root-cause-falsification"],
        alternatives=["local workflow defect", "domain architecture defect"],
        counterexamples=["same symptom can occur with correct architecture"],
        challenged_assumptions=["first repairable symptom is root cause"],
        selected_option="local workflow defect",
        rejection_reasons=["architecture hypothesis contradicted by trajectory evidence"],
        risks=["premature repair"],
        rollback_or_recovery=["revert candidate and preserve checkpoint"],
    )


def local_root():
    return require_root_scope_admission(
        hypotheses=(hypothesis("local", ProblemLayer.PROJECT_WORKFLOW, HypothesisDisposition.SELECTED),),
        selected_hypothesis_id="local",
    )


def systemic_root():
    return require_root_scope_admission(
        hypotheses=(
            hypothesis("workflow", ProblemLayer.PROJECT_WORKFLOW, HypothesisDisposition.SELECTED),
            hypothesis("architecture", ProblemLayer.DOMAIN_ARCHITECTURE, HypothesisDisposition.REJECTED),
        ),
        selected_hypothesis_id="workflow",
        material_problem=True,
        architecture_reassessment_refs=["evidence:architecture:reassessed"],
        material_decision_receipt=material_receipt(),
    )


def test_recoverable_missing_context_continues_with_provisional_candidate_instead_of_user_escalation():
    receipt = record_recovery_attempt(
        outcome="PROVISIONAL",
        authority_refs=["projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json"],
        artifact_refs=["projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md"],
        context_refs=["current selected Novel task context"],
        unknowns=["live reader outcome is not yet observed"],
        confidence="MEDIUM",
        safe_to_continue=True,
    )
    with pytest.raises(BehaviorAdmissionError, match="safe owner path"):
        require_user_escalation_admission(receipt)


def test_user_escalation_is_denied_without_recovery_receipt():
    with pytest.raises(BehaviorAdmissionError, match="no recovery attempt receipt"):
        require_user_escalation_admission(None)


def test_unresolved_required_user_fact_can_be_escalated_after_recovery():
    receipt = record_recovery_attempt(
        outcome="UNRESOLVED",
        authority_refs=["projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json"],
        artifact_refs=["projects/FQ001_MINGRI_ORDER/PLATFORM_PUBLICATION_LOG.md"],
        unknowns=["whether the user actually published/replaced the external platform chapter"],
        confidence="HIGH_ABOUT_INTERNAL_STATE__UNKNOWN_EXTERNAL_FACT",
        safe_to_continue=False,
    )
    assert require_user_escalation_admission(
        receipt,
        requires_user_fact_or_authorization=True,
    ) == "ADMITTED_REQUIRED_USER_FACT_OR_AUTHORIZATION"


def test_repairable_problem_cannot_skip_root_scope_even_if_repair_would_succeed():
    with pytest.raises(BehaviorAdmissionError, match="root-scope admission"):
        finalize_problem_closure(
            problem_detected=True,
            repair_path_available=True,
            authority_permits_repair=True,
            explicit_user_choice_required=False,
            repair_attempted=True,
            repair_succeeded=True,
        )


def test_admitted_authorized_repair_cannot_end_as_recommendation_only():
    with pytest.raises(BehaviorAdmissionError, match="was not attempted"):
        finalize_problem_closure(
            problem_detected=True,
            repair_path_available=True,
            authority_permits_repair=True,
            explicit_user_choice_required=False,
            repair_attempted=False,
            repair_succeeded=False,
            root_scope_receipt=local_root(),
            evolution_disposition=EvolutionDisposition.LOCAL_LEARNING_ONLY,
        )


def test_successful_authorized_repair_closes_after_root_scope_and_evolution():
    assert finalize_problem_closure(
        problem_detected=True,
        repair_path_available=True,
        authority_permits_repair=True,
        explicit_user_choice_required=False,
        repair_attempted=True,
        repair_succeeded=True,
        root_scope_receipt=local_root(),
        evolution_disposition=EvolutionDisposition.LOCAL_LEARNING_ONLY,
    ) == "REPAIR_EXECUTED"


def test_user_controlled_external_publication_can_block_without_fake_root_claim():
    assert finalize_problem_closure(
        problem_detected=True,
        repair_path_available=False,
        authority_permits_repair=False,
        explicit_user_choice_required=True,
        repair_attempted=False,
        repair_succeeded=False,
        blocker_reason="external platform publication/replacement is user-controlled",
    ) == "BLOCKED_WITH_REASON"


def test_user_or_external_claim_cannot_be_promoted_directly():
    with pytest.raises(BehaviorAdmissionError, match="promoted without falsification"):
        require_root_scope_admission(
            hypotheses=(hypothesis("architecture", ProblemLayer.DOMAIN_ARCHITECTURE, HypothesisDisposition.SELECTED),),
            selected_hypothesis_id="architecture",
            direct_user_or_external_claim_promoted_without_test=True,
        )


def test_material_root_scope_reuses_existing_material_deliberation_gate():
    with pytest.raises(BehaviorAdmissionError, match="material deliberation receipt"):
        require_root_scope_admission(
            hypotheses=(
                hypothesis("workflow", ProblemLayer.PROJECT_WORKFLOW, HypothesisDisposition.SELECTED),
                hypothesis("architecture", ProblemLayer.DOMAIN_ARCHITECTURE, HypothesisDisposition.REJECTED),
            ),
            selected_hypothesis_id="workflow",
            material_problem=True,
            architecture_reassessment_refs=["evidence:architecture"],
        )


def test_material_problem_requires_durable_causal_evidence_before_action():
    with pytest.raises(BehaviorAdmissionError, match="durable causal evidence"):
        finalize_problem_closure(
            problem_detected=True,
            repair_path_available=True,
            authority_permits_repair=True,
            explicit_user_choice_required=False,
            repair_attempted=True,
            repair_succeeded=True,
            root_scope_receipt=systemic_root(),
            evolution_disposition=EvolutionDisposition.DOMAIN_EVOLUTION_CANDIDATE,
        )


def test_material_problem_can_close_with_durable_evolution_evidence():
    assert finalize_problem_closure(
        problem_detected=True,
        repair_path_available=True,
        authority_permits_repair=True,
        explicit_user_choice_required=False,
        repair_attempted=True,
        repair_succeeded=True,
        root_scope_receipt=systemic_root(),
        evolution_disposition=EvolutionDisposition.DOMAIN_EVOLUTION_UPDATED,
        durable_problem_ref="audits/EVOLUTION_INDEX.json#EVO-20261016-COMMON-BEHAVIOR-1-3",
    ) == "REPAIR_EXECUTED"


def test_no_change_requires_root_scope_evolution_and_evidence():
    assert finalize_problem_closure(
        problem_detected=True,
        repair_path_available=False,
        authority_permits_repair=True,
        explicit_user_choice_required=False,
        repair_attempted=False,
        repair_succeeded=False,
        no_change_evidence=["checkpoint and Canon already agree; mutation would create drift"],
        root_scope_receipt=local_root(),
        evolution_disposition=EvolutionDisposition.NO_DURABLE_EVOLUTION_WITH_EVIDENCE,
    ) == "NO_CHANGE_WITH_EVIDENCE"
