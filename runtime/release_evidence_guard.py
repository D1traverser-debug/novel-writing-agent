#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "projects/FQ001_MINGRI_ORDER"
STRICT_FROM_CHAPTER = 9

REQUIRED_REVIEW_ROLES = {
    "CONTINUITY_AUDITOR",
    "FRESH_READER",
    "RETENTION_AUDITOR",
    "EDITORIAL",
    "ADVERSARIAL_RELEASE",
    "QUALITY_DISCOVERY",
}
REQUIRED_PIPELINE_ROLES = {
    "ARCHITECT",
    "CANON_LIBRARIAN",
    "WRITER",
    "COPYEDITOR_PROOFREADER",
    "ARTIFACT_RELEASE_ENGINEER",
    "CANON_COMMITTER",
}
FINAL_BODY_BOUND_PIPELINE_ROLES = {
    "COPYEDITOR_PROOFREADER",
    "ARTIFACT_RELEASE_ENGINEER",
    "CANON_COMMITTER",
}
ALLOWED_EXECUTOR_MODES = {"CHAT_BRIDGED", "ISOLATED_EXTERNAL"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def acceptance_metadata(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.+?)\s*$", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def _chapter_no(path: Path) -> int | None:
    m = re.match(r"CH(\d{4})_ACCEPTANCE\.md$", path.name)
    return int(m.group(1)) if m else None


def _resolve(root: Path, ref: str) -> Path:
    p = Path(ref)
    return p if p.is_absolute() else root / p


def _receipt_by_role(receipts: list[dict[str, Any]], role: str) -> list[dict[str, Any]]:
    return [r for r in receipts if r.get("role_id") == role]


def _valid_sha256(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _verify_ref_hash(
    root: Path,
    *,
    ref: Any,
    expected_sha: Any,
    label: str,
    problems: list[str],
) -> None:
    if not isinstance(ref, str) or not ref.strip():
        problems.append(f"{label}:ref-missing")
        return
    if not _valid_sha256(expected_sha):
        problems.append(f"{label}:sha256-invalid")
        return
    path = _resolve(root, ref)
    if not path.exists() or not path.is_file():
        problems.append(f"{label}:ref-missing")
        return
    if sha256_file(path) != expected_sha:
        problems.append(f"{label}:hash-mismatch")


def _verify_ref_list(
    root: Path,
    *,
    items: Any,
    label: str,
    min_items: int,
    max_items: int | None,
    problems: list[str],
) -> None:
    if not isinstance(items, list) or len(items) < min_items or (max_items is not None and len(items) > max_items):
        problems.append(f"{label}:invalid-list")
        return
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            problems.append(f"{label}:{index}:invalid-entry")
            continue
        _verify_ref_hash(
            root,
            ref=item.get("ref"),
            expected_sha=item.get("sha256"),
            label=f"{label}:{index}",
            problems=problems,
        )


def validate_chapter(root: Path, task: Path, chapter_no: int) -> list[str]:
    problems: list[str] = []
    cid = f"CH{chapter_no:04d}"
    final_path = task / "manuscript" / f"{cid}_FINAL.md"
    acceptance_path = task / "reviews" / f"{cid}_ACCEPTANCE.md"

    if not acceptance_path.exists():
        return problems
    if not final_path.exists():
        return [f"{cid}:acceptance-without-final"]

    final_hash = sha256_file(final_path)
    acceptance_text = acceptance_path.read_text(encoding="utf-8")
    meta = acceptance_metadata(acceptance_text)

    if meta.get("source_hash") != final_hash:
        problems.append(f"{cid}:acceptance-source-hash-mismatch")

    if chapter_no < STRICT_FROM_CHAPTER:
        if meta.get("evidence_assurance") != "LEGACY_AGGREGATE_MIGRATED":
            problems.append(f"{cid}:legacy-evidence-assurance-marker-missing")
        if meta.get("role_receipts") != "NOT_AVAILABLE":
            problems.append(f"{cid}:legacy-role-receipts-marker-missing")
        if meta.get("isolated_reviewer_attestation") != "NOT_CLAIMED":
            problems.append(f"{cid}:legacy-isolation-marker-missing")
        return problems

    if meta.get("evidence_contract_version") != "1.0":
        problems.append(f"{cid}:evidence-contract-version")

    evidence_ref = meta.get("execution_evidence_ref")
    evidence_sha = meta.get("execution_evidence_sha256")
    context_ref = meta.get("context_pack_ref")
    context_sha = meta.get("context_pack_sha256")
    if not all((evidence_ref, evidence_sha, context_ref, context_sha)):
        problems.append(f"{cid}:acceptance-evidence-pointers-incomplete")
        return problems

    evidence_path = _resolve(root, evidence_ref)
    context_path = _resolve(root, context_ref)
    if not evidence_path.exists():
        problems.append(f"{cid}:execution-evidence-missing")
        return problems
    if not context_path.exists():
        problems.append(f"{cid}:context-pack-missing")
        return problems
    if sha256_file(evidence_path) != evidence_sha:
        problems.append(f"{cid}:execution-evidence-hash-mismatch")
    if sha256_file(context_path) != context_sha:
        problems.append(f"{cid}:context-pack-hash-mismatch")

    try:
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        context = json.loads(context_path.read_text(encoding="utf-8"))
    except Exception as exc:
        problems.append(f"{cid}:invalid-json:{type(exc).__name__}")
        return problems

    if context.get("schema_version") != "1.0":
        problems.append(f"{cid}:context-schema-version")
    if context.get("chapter_id") != cid or context.get("status") != "FROZEN":
        problems.append(f"{cid}:context-identity-or-status")
    authority_commit = str(context.get("authority_commit", ""))
    if not re.fullmatch(r"[0-9a-f]{40}", authority_commit):
        problems.append(f"{cid}:context-authority-commit")

    contract_ref = context.get("contract_snapshot_ref")
    contract_sha = context.get("contract_snapshot_sha256")
    _verify_ref_hash(
        root,
        ref=contract_ref,
        expected_sha=contract_sha,
        label=f"{cid}:contract-snapshot",
        problems=problems,
    )
    _verify_ref_hash(
        root,
        ref=context.get("project_profile_ref"),
        expected_sha=context.get("project_profile_sha256"),
        label=f"{cid}:project-profile",
        problems=problems,
    )
    _verify_ref_list(
        root,
        items=context.get("canon_refs"),
        label=f"{cid}:canon-ref",
        min_items=1,
        max_items=None,
        problems=problems,
    )
    _verify_ref_list(
        root,
        items=context.get("recent_final_refs"),
        label=f"{cid}:recent-final-ref",
        min_items=1,
        max_items=3,
        problems=problems,
    )
    rule_slices = context.get("rule_slices")
    if not isinstance(rule_slices, list) or len(rule_slices) > 4 or any(not isinstance(item, str) or not item.strip() for item in rule_slices):
        problems.append(f"{cid}:context-rule-slices")

    if evidence.get("schema_version") != "1.0":
        problems.append(f"{cid}:evidence-schema-version")
    if evidence.get("chapter_id") != cid:
        problems.append(f"{cid}:evidence-chapter-id")
    if evidence.get("source_hash") != final_hash:
        problems.append(f"{cid}:evidence-source-hash")
    if evidence.get("context_pack_ref") != context_ref or evidence.get("context_pack_sha256") != context_sha:
        problems.append(f"{cid}:evidence-context-binding")
    if evidence.get("assurance") != "ROLE_SEPARATED_NOT_ATTESTED_ISOLATED":
        problems.append(f"{cid}:evidence-assurance")

    receipts = evidence.get("role_receipts")
    if not isinstance(receipts, list):
        problems.append(f"{cid}:role-receipts-not-list")
        return problems

    seen_receipt_ids: set[str] = set()
    for receipt in receipts:
        receipt_id = receipt.get("receipt_id")
        role_id = receipt.get("role_id")
        if not isinstance(receipt_id, str) or not receipt_id.strip():
            problems.append(f"{cid}:receipt-id-missing:{role_id}")
        elif receipt_id in seen_receipt_ids:
            problems.append(f"{cid}:duplicate-receipt-id:{receipt_id}")
        else:
            seen_receipt_ids.add(receipt_id)

        if not isinstance(receipt.get("result_summary"), str) or not receipt.get("result_summary", "").strip():
            problems.append(f"{cid}:receipt-result-summary-missing:{role_id}")

        mode = receipt.get("executor_mode")
        if mode not in ALLOWED_EXECUTOR_MODES:
            problems.append(f"{cid}:invalid-executor-mode:{role_id}")
        if mode == "ISOLATED_EXTERNAL" and not (receipt.get("execution_identity") and receipt.get("trace_ref")):
            problems.append(f"{cid}:isolated-receipt-without-attestation:{role_id}")
        if str(receipt.get("assurance", "")).upper() == "ATTESTED_ISOLATED" and mode != "ISOLATED_EXTERNAL":
            problems.append(f"{cid}:false-isolated-claim:{role_id}")
        if mode == "CHAT_BRIDGED" and receipt.get("input_hash") != context_sha:
            problems.append(f"{cid}:chat-bridged-context-binding:{role_id}")

        if role_id in FINAL_BODY_BOUND_PIPELINE_ROLES and receipt.get("source_hash") != final_hash:
            problems.append(f"{cid}:pipeline-final-source-binding:{role_id}")

    for role in REQUIRED_PIPELINE_ROLES:
        rows = _receipt_by_role(receipts, role)
        if not any(r.get("status") in {"PASS", "COMPLETED"} for r in rows):
            problems.append(f"{cid}:missing-pipeline-receipt:{role}")

    for role in REQUIRED_REVIEW_ROLES:
        rows = _receipt_by_role(receipts, role)
        final_rows = [
            r for r in rows
            if r.get("source_hash") == final_hash
            and r.get("input_hash") == context_sha
            and r.get("status") in {"PASS", "RELEASE"}
        ]
        if not final_rows:
            problems.append(f"{cid}:missing-final-review-receipt:{role}")
        blinded_rows = [
            r for r in rows
            if r.get("peer_review_visibility") == "BLINDED_FROM_PEER_CONCLUSIONS"
            and _valid_sha256(r.get("source_hash"))
            and r.get("input_hash") == context_sha
        ]
        if not blinded_rows:
            problems.append(f"{cid}:review-blinding-receipt-missing:{role}")

    issue_ledger = evidence.get("issue_ledger")
    if not isinstance(issue_ledger, dict):
        problems.append(f"{cid}:issue-ledger-missing")
    else:
        if issue_ledger.get("unresolved_blocker") != 0:
            problems.append(f"{cid}:unresolved-blocker")
        if issue_ledger.get("unresolved_high") != 0:
            problems.append(f"{cid}:unresolved-high")
        revision_rounds = issue_ledger.get("revision_rounds")
        if not isinstance(revision_rounds, int) or revision_rounds < 0 or revision_rounds > 2:
            problems.append(f"{cid}:revision-rounds")
        elif revision_rounds > 0:
            refiner = _receipt_by_role(receipts, "REFINER")
            if not any(r.get("status") in {"PASS", "COMPLETED"} for r in refiner):
                problems.append(f"{cid}:missing-refiner-receipt")

    return problems


def validate_repository(root: Path = ROOT) -> list[str]:
    task = root / "projects/FQ001_MINGRI_ORDER"
    reviews = task / "reviews"
    if not reviews.exists():
        return ["reviews-directory-missing"]
    problems: list[str] = []
    for acceptance in sorted(reviews.glob("CH????_ACCEPTANCE.md")):
        chapter_no = _chapter_no(acceptance)
        if chapter_no is not None:
            problems.extend(validate_chapter(root, task, chapter_no))
    return problems


def main() -> int:
    problems = validate_repository(ROOT)
    result = {
        "status": "PASS" if not problems else "FAIL",
        "strict_from_chapter": STRICT_FROM_CHAPTER,
        "assurance": "ROLE_SEPARATED_NOT_ATTESTED_ISOLATED",
        "evidence_strength": "STRUCTURED_SELF_ATTESTED_CHAT_BRIDGED_UNLESS_EXTERNAL_TRACE_PRESENT",
        "failures": problems,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
