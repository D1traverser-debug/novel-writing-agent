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
 "protocols/ACTIVE_RULEBOOK.md","runtime/release_evidence_guard.py",
 "projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json","projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md",
 "projects/FQ001_MINGRI_ORDER/checkpoints/CURRENT_CHECKPOINT.json","projects/FQ001_MINGRI_ORDER/NEXT_CHAPTER_CONTRACT.md",
 "projects/FQ001_MINGRI_ORDER/PROJECT_PROFILE.md","projects/FQ001_MINGRI_ORDER/canon/CHARACTERS.json",
 "projects/FQ001_MINGRI_ORDER/canon/CHARACTER_DRIVES.json","projects/FQ001_MINGRI_ORDER/canon/THREADS.json",
 "projects/FQ001_MINGRI_ORDER/canon/FORESHADOW.jsonl","projects/FQ001_MINGRI_ORDER/canon/TIMELINE.jsonl",
 "projects/FQ001_MINGRI_ORDER/canon/READER_PROMISES.json","projects/FQ001_MINGRI_ORDER/manuscript/CH0008_FINAL.md",
 "projects/FQ001_MINGRI_ORDER/reviews/CH0008_ACCEPTANCE.md"]: need(rel)

m=json.loads((TASK/"TASK_MANIFEST.json").read_text(encoding="utf-8"))
cp=json.loads((TASK/"checkpoints/CURRENT_CHECKPOINT.json").read_text(encoding="utf-8"))
for f in ("task_id","current_stage","next_action","canon_version","last_final_chapter","last_final_hash","next_serial_chapter","next_serial_status"):
    if m.get(f)!=cp.get(f): problems.append("checkpoint-drift:"+f)
if m["task_id"]!="FQ001_MINGRI_ORDER": problems.append("task-id")
if hashlib.sha256((TASK/"manuscript/CH0008_FINAL.md").read_bytes()).hexdigest()!=m["last_final_hash"]: problems.append("ch8-hash")

expected={1:"79f1a1778c4023fe185606f0493d2019938b61f6cc8e5697408453302e0d0043",2:"2b77d75aabebda658023a9ad570d56337d9391ed8d39fd85bbdcfd89a7d382bb",3:"b586faa1643fa92f9c4b528b1f94e11f7d80fbad4a133d02ea1feb8006911b58",4:"636b88301bbfdd2d9a7b150afef69192879cc26109da5c95c898e271188bc853",5:"d18a02c0bbc51e5585179ae096e3f2452e1f48085b4d188ed37b6ada8fc2e507",6:"9207c149ec8a8acb50dff22dc53cf9e0c4f6b53f63f4bcef6b4f8487332c0810",7:"e7d1ef881b042a70fd699817763cb07c055b06fd7cf9412cc98209739fd539f8"}
for n,h in expected.items():
    p=TASK/f"manuscript/CH{n:04d}_FINAL.md"
    if not p.exists(): problems.append(f"missing-published:{n}")
    elif hashlib.sha256(p.read_bytes()).hexdigest()!=h: problems.append(f"published-hash:{n}")

state=(TASK/"CURRENT_STATE.md").read_text(encoding="utf-8")
if "canon_version: 12" not in state or "last_final_chapter: 8" not in state or "next_serial_chapter: 9" not in state: problems.append("current-state")
if "尚未确认外部发布" not in state: problems.append("publication-state")
contract=(TASK/"NEXT_CHAPTER_CONTRACT.md").read_text(encoding="utf-8")
if "chapter_no: 9" not in contract or "status: READY" not in contract: problems.append("ch9-contract")

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
if alias.get("canonical_ref")!="continuity/TASK_INDEX.json": problems.append("task-index-alias-canonical")
if alias.get("system",{}).get("active_project_task_id")!="FQ001_MINGRI_ORDER": problems.append("task-index-alias-active-project")
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

# Release-evidence contract must be enforceable, not merely declared.
for failure in validate_release_evidence(ROOT):
    problems.append("release-evidence:"+failure)
cap=json.loads((ROOT/"continuity/EXECUTION_CAPABILITIES.json").read_text(encoding="utf-8"))
if cap.get("release_evidence_contract_version")!="1.0": problems.append("release-evidence-contract-version")
if not any(c.get("capability_id")=="deterministic_guards" and "release_evidence_guard.py" in c.get("invocation_path","") for c in cap.get("capabilities",[])):
    problems.append("release-evidence-guard-not-bound")

result={"status":"PASS" if not problems else "FAIL","task_id":m["task_id"],"system_id":system.get("system_id"),"active_project_task_id":system.get("active_project_task_id"),"stage":m["current_stage"],"next_action":m["next_action"],"artifact_vault":vault.get("path"),"release_evidence_contract":cap.get("release_evidence_contract_version"),"failures":problems}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if problems else 0)
