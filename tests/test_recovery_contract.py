from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
TASK=ROOT/"projects/FQ001_MINGRI_ORDER"
def test_recovery_truth():
    m=json.loads((TASK/"TASK_MANIFEST.json").read_text())
    cp=json.loads((TASK/"checkpoints/CURRENT_CHECKPOINT.json").read_text())
    assert m["task_id"]=="FQ001_MINGRI_ORDER"
    assert m["status"]=="WAITING"
    assert m["last_final_chapter"]==8
    assert m["next_serial_chapter"]==9
    assert m["current_stage"]==cp["current_stage"]
    assert m["next_action"]==cp["next_action"]
    assert m["external_publication"]["confirmed_published_through"]==7
def test_ch8_hash():
    m=json.loads((TASK/"TASK_MANIFEST.json").read_text())
    assert hashlib.sha256((TASK/"manuscript/CH0008_FINAL.md").read_bytes()).hexdigest()==m["last_final_hash"]
def test_ch9_ready():
    c=(TASK/"NEXT_CHAPTER_CONTRACT.md").read_text()
    assert "chapter_no: 9" in c and "status: READY" in c

def test_novel_os_routes_to_active_project_without_duplicate_task():
    idx=json.loads((ROOT/"continuity/TASK_INDEX.json").read_text())
    system=idx["system"]
    assert system["system_id"]=="NOVEL_OS"
    assert system["display_name_zh"]=="小说系统"
    assert system["resume_behavior"]=="ROUTE_TO_ACTIVE_PROJECT"
    assert system["active_project_task_id"]=="FQ001_MINGRI_ORDER"
    assert "小说系统" in system["resume_aliases"]
    assert "NOVEL_OS" in system["resume_aliases"]
    tasks=[t for t in idx["tasks"] if t["task_id"]=="FQ001_MINGRI_ORDER"]
    assert len(tasks)==1
    assert tasks[0]["is_active_project"] is True
    assert tasks[0]["system_id"]=="NOVEL_OS"
    assert tasks[0]["candidate_label_zh"]=="小说系统｜《凌晨零点，我接到明天的订单》"

def test_continuity_adapter_system_project_semantics():
    adapter=json.loads((ROOT/"CONTINUITY_ADAPTER.json").read_text())
    topology=adapter["system_project_topology"]
    assert topology["system_id"]=="NOVEL_OS"
    assert topology["routing_rule"]=="SYSTEM_ALIAS_RESOLVES_OWNER_THEN_ACTIVE_PROJECT"
    assert topology["single_active_project_behavior"]=="AUTO_BIND_WITHOUT_SECOND_USER_SELECTION"
    assert topology["duplicate_task_for_system_and_same_project"] is False
    assert adapter["capabilities"]["resolve_system_resume_alias"]["source"]=="continuity/TASK_INDEX.json#system"

def test_compatibility_task_index_mirrors_system_route():
    canonical=json.loads((ROOT/"continuity/TASK_INDEX.json").read_text())
    alias=json.loads((ROOT/"TASK_INDEX.json").read_text())
    assert alias["canonical_ref"]=="continuity/TASK_INDEX.json"
    assert alias["system"]["system_id"]==canonical["system"]["system_id"]
    assert alias["system"]["active_project_task_id"]==canonical["system"]["active_project_task_id"]
