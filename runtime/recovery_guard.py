#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys
ROOT=Path(__file__).resolve().parents[1]
TASK=ROOT/"projects/FQ001_MINGRI_ORDER"
problems=[]
def need(rel):
    p=ROOT/rel
    if not p.exists(): problems.append(f"missing:{rel}")
    return p
for rel in [
 "ENTRYPOINT.md","PROTOCOL.md","SKILL.md","AUTHORITY_STATUS.json","CONTINUITY_ADAPTER.json","TASK_INDEX.json",
 "protocols/ACTIVE_RULEBOOK.md","projects/FQ001_MINGRI_ORDER/TASK_MANIFEST.json","projects/FQ001_MINGRI_ORDER/CURRENT_STATE.md",
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
result={"status":"PASS" if not problems else "FAIL","task_id":m["task_id"],"stage":m["current_stage"],"next_action":m["next_action"],"failures":problems}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if problems else 0)
