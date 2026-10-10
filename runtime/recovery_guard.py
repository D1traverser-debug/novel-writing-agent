#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys

ROOT=Path(__file__).resolve().parents[1]
TASK=ROOT/"projects/FQ001_MINGRI_ORDER"
sys.path.insert(0, str(ROOT/"runtime"))
from release_evidence_guard import validate_repository as validate_release_evidence

problems=[]
def need(rel):
    p=ROOT/rel
    if not p.exists(): problems.append(f"missing:{rel}")
    return p

for rel in [
 "ENTRYPOINT.md","PROTOCOL.md","SKILL.md","AUTHORITY_STATUS.json","CONTINUITY_ADAPTER.json","TASK_INDEX.json",
 "continuity/TASK_INDEX.json","continuity/EXECUTION_CAPABILITIES.json","continuity/ARTIFACT_CONTEXT_GOVERNANCE.json",
 "continuity/UNIVERSAL_PROTOCOL_ADAPTER.json","protocols/ACTIVE_RULEBOOK.md","runtime/release_evidence_guard.py",
 "projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json","projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md",
 "projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json","projects/FQ001_MINGRI_ORDER/NEXT_CHAPTER_CONTRACT.md",
 "projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md","projects/FQ001_MINGRI_ORDER/PLATFORM_PUBLICATION_LOG.md",
 "projects/FQ001_MINGRI_ORDER/canon/CHARACTERS.json","projects/FQ001_MINGRI_ORDER/canon/CHARACTER_DRIVES.json",
 "projects/FQ001_MINGRI_ORDER/canon/THREADS.json","projects/FQ001_MINGRI_ORDER/canon/FORESHADOW.jsonl",
 "projects/FQ001_MINGRI_ORDER/canon/TIMELINE.jsonl","projects/FQ001_MINGRI_ORDER/canon/READER_PROMISES.json",
 "projects/FQ001_MINGRI_ORDER/manuscript/CH0008_FINAL.md","projects/FQ001_MINGRI_ORDER/reviews/CH0008_ACCEPTANCE.md",
 "audits/PLATFORM_SIGNING_SIGNAL_2026-10-11.md","audits/FRONT_ARC_SIGNING_REPAIR_MATRIX_2026-10-11.md",
 "audits/FULL_REBASE_LEARNING_EVIDENCE_2026-10-11.md","audits/FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md"]: need(rel)

m=json.loads((TASK/"TASK_MANIFEST.json").read_text(encoding="utf-8"))
cp=json.loads((TASK/"checkpoints/CURRENT_CHECKPOINT.json").read_text(encoding="utf-8"))
for f in ("task_id","current_stage","next_action","canon_version","last_final_chapter","last_final_hash","next_serial_chapter","next_serial_status"):
    if m.get(f)!=cp.get(f): problems.append("checkpoint-drift:"+f)
if m.get("task_id")!="FQ001_MINGRI_ORDER": problems.append("task-id")
if m.get("status")!="ACTIVE" or cp.get("status")!="ACTIVE": problems.append("task-not-active")
if m.get("current_stage")!="FULL_FRONT_ARC_REBASE_ACTIVE__SIGNING_PACKET_REARCHITECTURE": problems.append("rebase-stage")
if m.get("next_serial_status")!="HELD_DURING_FULL_FRONT_ARC_REBASE": problems.append("rebase-next-serial-status")
if cp.get("production_mode")!="FULL_FRONT_ARC_REBASE": problems.append("rebase-production-mode")
if hashlib.sha256((TASK/"manuscript/CH0008_FINAL.md").read_bytes()).hexdigest()!=m.get("last_final_hash"): problems.append("ch8-hash")

# Historical FINALs remain immutable evidence during the rebase.
expected={1:"79f1a1778c4023fe185606f0493d2019938b61f6cc8e5697408453302e0d0043",2:"2b77d75aabebda658023a9ad570d56337d9391ed8d39fd85bbdcfd89a7d382bb",3:"b586faa1643fa92f9c4b528b1f94e11f7d80fbad4a133d02ea1feb8006911b58",4:"636b88301bbfdd2d9a7b150afef69192879cc26109da5c95c898e271188bc853",5:"d18a02c0bbc51e5585179ae096e3f2452e1f48085b4d188ed37b6ada8fc2e507",6:"9207c149ec8a8acb50dff22dc53cf9e0c4f6b53f63f4bcef6b4f8487332c0810",7:"e7d1ef881b042a70fd699817763cb07c055b06fd7cf9412cc98209739fd539f8"}
for n,h in expected.items():
    p=TASK/f"manuscript/CH{n:04d}_FINAL.md"
    if not p.exists(): problems.append(f"missing-published:{n}")
    elif hashlib.sha256(p.read_bytes()).hexdigest()!=h: problems.append(f"historical-final-hash:{n}")

state=(TASK/"CURRENT_STATE.md").read_text(encoding="utf-8")
if "canon_version: 12" not in state or "last_final_chapter: 8" not in state or "next_serial_chapter: 9" not in state: problems.append("current-state")
if "production_mode: FULL_FRONT_ARC_REBASE" not in state or "FULL_FRONT_ARC_REBASE_ACTIVE__SIGNING_PACKET_REARCHITECTURE" not in state: problems.append("current-state-rebase")
if "CH8" not in state or "仍未确认" not in state: problems.append("publication-state")

# Old CH9 is deliberately held/superseded, while its relationship-engine design remains available as source material.
contract=(TASK/"NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
if "chapter_no: 9" not in contract: problems.append("ch9-contract-number")
if "status: SUPERSEDED_BY_FULL_FRONT_ARC_REBASE" not in contract: problems.append("ch9-contract-not-held")
if "Do not write old CH9 next" not in contract: problems.append("ch9-contract-execution-escape")
if "许知微" not in contract or "precommit" not in contract.lower(): problems.append("ch9-design-migration-source")

# Full-rebase evidence/plan and supersession must be durable.
rebase=m.get("rebase",{})
cp_rebase=cp.get("rebase",{})
if rebase.get("authorized_by_user") is not True: problems.append("rebase-user-authorization")
if rebase.get("scope")!="CH1-CH8_FRONT_ARC": problems.append("rebase-scope")
if rebase.get("mode")!="CONTROLLED_FULL_FRONT_ARC_REBASE": problems.append("rebase-mode")
if rebase.get("old_finals_role")!="IMMUTABLE_HISTORICAL_BASELINE": problems.append("rebase-old-finals-role")
if rebase.get("old_chapter_boundaries_binding") is not False: problems.append("rebase-old-boundary-binding")
if rebase.get("old_ch9_contract_status")!="SUPERSEDED_BY_FULL_FRONT_ARC_REBASE": problems.append("rebase-ch9-status")
if rebase.get("candidate_promotion")!="WHOLE_PACKET_GATES_BEFORE_AUTHORITATIVE_REPLACEMENT": problems.append("rebase-promotion-gate")
for f in ("authorized_by_user","scope","mode","old_finals_role","old_chapter_boundaries_binding","old_ch9_contract_status","candidate_promotion"):
    if cp_rebase.get(f)!=rebase.get(f): problems.append("rebase-checkpoint-drift:"+f)
for ref_key in ("plan_ref","learning_evidence_ref"):
    ref=rebase.get(ref_key)
    if not ref or not (ROOT/ref).exists(): problems.append("rebase-ref:"+ref_key)
old_matrix=(ROOT/"audits/FRONT_ARC_SIGNING_REPAIR_MATRIX_2026-10-11.md").read_text(encoding="utf-8")
if "SUPERSEDED_FOR_ACTIVE_EXECUTION" not in old_matrix: problems.append("old-repair-matrix-still-active")
plan=(ROOT/"audits/FULL_FRONT_ARC_REBASE_PLAN_2026-10-11.md").read_text(encoding="utf-8")
learn=(ROOT/"audits/FULL_REBASE_LEARNING_EVIDENCE_2026-10-11.md").read_text(encoding="utf-8")
if "M0 — Intake" not in plan or "M11 — Durable learning" not in plan: problems.append("rebase-plan-m0-m11")
if "LEARNING_EVIDENCE" not in learn or "CONTROLLED_FULL_FRONT_ARC_REBASE" not in learn: problems.append("rebase-learning-evidence")
profile=(TASK/"PROJECT_PROFILE.md").read_text(encoding="utf-8")
if "production_mode: FULL_FRONT_ARC_REBASE" not in profile: problems.append("profile-rebase-mode")
if "next_serial_status: HELD_DURING_FULL_FRONT_ARC_REBASE" not in profile: problems.append("profile-ch9-hold")
if "Full front-arc rebase objective" not in profile: problems.append("profile-rebase-objective")

chars=json.loads((TASK/"canon/CHARACTERS.json").read_text(encoding="utf-8"))
threads=json.loads((TASK/"canon/THREADS.json").read_text(encoding="utf-8"))
prom=json.loads((TASK/"canon/READER_PROMISES.json").read_text(encoding="utf-8"))
if not any(c.get("name")=="许知微" and c.get("last_updated_chapter")==8 for c in chars): problems.append("canon-characters")
if threads.get("T005",{}).get("last_progress_chapter")!=8: problems.append("canon-thread-T005")
if prom.get("version")!=6: problems.append("canon-promises")

# System/project continuity topology guard.
idx=json.loads((ROOT/"continuity/TASK_INDEX.json").read_text(encoding="utf-8"))
alias=json.loads((ROOT/"TASK_INDEX.json").read_text(encoding="utf-8"))
adapter=json.loads((ROOT/"CONTINUITY_ADAPTER.json").read_text(encoding="utf-8"))
system=idx.get("system",{})
if system.get("system_id")!="NOVEL_OS": problems.append("system-id")
if system.get("active_project_task_id")!="FQ001_MINGRI_ORDER": problems.append("system-active-project")
if system.get("resume_behavior")!="ROUTE_TO_ACTIVE_PROJECT": problems.append("system-resume-behavior")
aliases=set(system.get("resume_aliases",[]))
if not {"小说系统","NOVEL_OS"}.issubset(aliases): problems.append("system-resume-aliases")
idx_tasks={t.get("task_id"):t for t in idx.get("tasks",[])}
active=idx_tasks.get("FQ001_MINGRI_ORDER",{})
if active.get("system_id")!="NOVEL_OS" or active.get("is_active_project") is not True: problems.append("system-project-binding")
if active.get("candidate_label_zh")!="小说系统｜《凌晨零点，我接到明天的订单》": problems.append("system-candidate-label")
if active.get("current_stage")!=m.get("current_stage") or active.get("next_action")!=m.get("next_action"): problems.append("task-index-state-drift")
if alias.get("canonical_ref")!="continuity/TASK_INDEX.json": problems.append("task-index-alias-canonical")
if alias.get("system",{}).get("active_project_task_id")!="FQ001_MINGRI_ORDER": problems.append("task-index-alias-active-project")
if alias.get("tasks",[{}])[0].get("current_stage")!=m.get("current_stage"): problems.append("compat-index-stage-drift")
topology=adapter.get("system_project_topology",{})
if topology.get("system_id")!="NOVEL_OS": problems.append("adapter-system-id")
if topology.get("routing_rule")!="SYSTEM_ALIAS_RESOLVES_OWNER_THEN_ACTIVE_PROJECT": problems.append("adapter-system-routing")
if topology.get("single_active_project_behavior")!="AUTO_BIND_WITHOUT_SECOND_USER_SELECTION": problems.append("adapter-single-project-autobind")

# Post-cutover storage governance guard.
auth=json.loads((ROOT/"AUTHORITY_STATUS.json").read_text(encoding="utf-8"))
gov=json.loads((ROOT/"continuity/ARTIFACT_CONTEXT_GOVERNANCE.json").read_text(encoding="utf-8"))
if auth.get("status")!="GITHUB_PRIMARY" or auth.get("business_authority") is not True: problems.append("authority-not-github-primary")
if auth.get("library_post_cutover_role")!="REMOVED_NO_NOVEL_EXECUTION_TREE": problems.append("library-role-regression")
vault=auth.get("artifact_vault",{})
if vault.get("provider")!="Google Drive" or vault.get("business_authority") is not False: problems.append("artifact-vault-authority")
if vault.get("path")!="/Google Drive/ChatGPT/NOVEL_OS_小说系统_交付归档": problems.append("artifact-vault-path")
if "ChatGPT Library" in gov.get("external_artifact_vault_if_any",""): problems.append("governance-library-vault-regression")
refs=cp.get("derived_artifact_refs",[])
if any("ChatGPT Library" in r for r in refs): problems.append("checkpoint-library-derived-ref")
if not any("Google Drive" in r for r in refs): problems.append("checkpoint-missing-drive-derived-ref")

entry=(ROOT/"ENTRYPOINT.md").read_text(encoding="utf-8")
skill=(ROOT/"SKILL.md").read_text(encoding="utf-8")
protocol=(ROOT/"PROTOCOL.md").read_text(encoding="utf-8")
rulebook=(ROOT/"protocols/ACTIVE_RULEBOOK.md").read_text(encoding="utf-8")
for label,text in (("entrypoint",entry),("skill",skill),("protocol",protocol),("rulebook",rulebook)):
    if "ChatGPT Library is a backup / derived-artifact store" in text or "Library 派生交付物/备份" in text or "Derived/binary artifacts in ChatGPT Library" in text or "historical protocol files/research remain Library backup evidence" in text:
        problems.append(f"legacy-storage-wording:{label}")
if "CANON_SNAPSHOT.json" in skill and "不存在另一个可覆盖这些 ledgers 的 `CANON_SNAPSHOT.json` 权威" not in skill:
    problems.append("dangling-canon-snapshot-authority")
if "Full front-arc rebase / learning-to-authority promotion" not in skill: problems.append("skill-full-rebase")
if "Full-unit rebase / owner evolution" not in rulebook: problems.append("rulebook-full-rebase")

# Release-evidence contract must remain enforceable, not merely declared.
for failure in validate_release_evidence(ROOT):
    problems.append("release-evidence:"+failure)
cap=json.loads((ROOT/"continuity/EXECUTION_CAPABILITIES.json").read_text(encoding="utf-8"))
if cap.get("release_evidence_contract_version")!="1.0": problems.append("release-evidence-contract-version")
if not any(c.get("capability_id")=="deterministic_guards" and "release_evidence_guard.py" in c.get("invocation_path","") for c in cap.get("capabilities",[])):
    problems.append("release-evidence-guard-not-bound")
high=next((c for c in cap.get("capabilities",[]) if c.get("capability_id")=="high_judgment_serialization_pipeline"),{})
if "REBASE_ARCHITECTURE" not in high.get("scope","") or "SIGNING_READINESS" not in high.get("scope",""): problems.append("rebase-capability-not-bound")

# Fanqie signing rejection is durable platform evidence and must not be forgotten on resume.
signing=m.get("platform_signing",{})
cp_signing=cp.get("platform_signing",{})
if signing.get("attempt_1")!="REJECTED_QUALITY_EVALUATION": problems.append("signing-attempt1-state")
if signing.get("next_application_threshold")!=50000: problems.append("signing-next-threshold")
if signing.get("third_application_threshold_if_needed")!=80000: problems.append("signing-third-threshold")
if signing.get("second_application_gate")!="SECOND_SIGNING_APPLICATION_REQUIRES_SIGNING_READINESS_AUDIT_PASS": problems.append("signing-second-gate")
for f in ("attempt_1","next_application_threshold","third_application_threshold_if_needed","second_application_gate"):
    if cp_signing.get(f)!=signing.get(f): problems.append("signing-checkpoint-drift:"+f)
for ref_key in ("quality_diagnosis_ref","active_rebase_plan_ref","learning_evidence_ref"):
    ref=signing.get(ref_key)
    if not ref or not (ROOT/ref).exists(): problems.append("signing-evidence-ref:"+ref_key)
if "DO_NOT_BLINDLY_CONTINUE_TO_50K_WITHOUT_FRONT_ARC_REBASE" not in m.get("strategic_constraints",[]): problems.append("signing-blind-retry-guard")
if "平台签约拒绝" not in skill or "Platform signing-feedback loop" not in skill: problems.append("skill-signing-feedback-loop")
platform_log=(TASK/"PLATFORM_PUBLICATION_LOG.md").read_text(encoding="utf-8")
if "首次签约申请：`NOT_APPROVED / 签约评估未通过`" not in platform_log: problems.append("platform-log-signing-result")

result={
 "status":"PASS" if not problems else "FAIL",
 "task_id":m.get("task_id"),
 "system_id":system.get("system_id"),
 "active_project_task_id":system.get("active_project_task_id"),
 "stage":m.get("current_stage"),
 "next_action":m.get("next_action"),
 "rebase_mode":rebase.get("mode"),
 "old_ch9_status":rebase.get("old_ch9_contract_status"),
 "artifact_vault":vault.get("path"),
 "release_evidence_contract":cap.get("release_evidence_contract_version"),
 "signing_attempt_1":signing.get("attempt_1"),
 "signing_next_threshold":signing.get("next_application_threshold"),
 "failures":problems
}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if problems else 0)
