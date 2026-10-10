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
