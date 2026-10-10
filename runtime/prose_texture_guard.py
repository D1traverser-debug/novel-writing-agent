#!/usr/bin/env python3
import argparse, json, re, statistics
from pathlib import Path

CJK = re.compile(r'[\u4e00-\u9fff]')
TIME = re.compile(r'^(?:[01]?\d|2[0-3])[:：][0-5]\d[。.]?$|^(?:凌晨|上午|下午|晚上)?[一二三四五六七八九十〇零两\d]+点')
CONTRAST = [re.compile(p) for p in [r'不是.{0,30}[，,。；;]?\s*是', r'没有.{0,30}[，,。；;]?\s*只', r'一个.{0,60}另一个']]
SUMMARY = re.compile(r'(这意味着|也就是说|这至少|因此|由此|结论|真正.{0,10}是|意识到|明白了?|换句话说)')
PROCEDURAL = re.compile(r'(拨(?:了)?电话|挂断|截图|拍照|备忘录|记下|记录|搜索|搜“|查了?|核验|确认|时间表|风险图|路径[AB]|已确认|未知：)')


def cjk_len(s): return len(CJK.findall(s))

def analyze(path):
    text = Path(path).read_text(encoding='utf-8')
    lines = [x.strip() for x in text.splitlines()]
    paras = [x for x in lines if x and not x.startswith('#')]
    lens = [cjk_len(p) for p in paras]
    short12 = sum(1 for n in lens if n <= 12)
    short25 = sum(1 for n in lens if n <= 25)
    timestamps = sum(1 for p in paras if TIME.search(p))
    brackets = sum(1 for p in paras if p.startswith('【') and p.endswith('】'))
    contrast = sum(sum(1 for _ in rx.finditer(text)) for rx in CONTRAST)
    summary = len(SUMMARY.findall(text))
    procedural = len(PROCEDURAL.findall(text))
    dialogue = sum(1 for p in paras if p.startswith('“') or p.startswith('「'))
    return {
        'file': Path(path).name,
        'paragraphs': len(paras),
        'median_cjk_chars_per_paragraph': statistics.median(lens) if lens else 0,
        'short_para_le_12_ratio': round(short12/max(1,len(paras)),3),
        'short_para_le_25_ratio': round(short25/max(1,len(paras)),3),
        'standalone_time_paragraphs': timestamps,
        'bracketed_ui_or_note_paragraphs': brackets,
        'contrast_pattern_hits': contrast,
        'summary_marker_hits': summary,
        'procedural_marker_hits': procedural,
        'dialogue_paragraph_ratio': round(dialogue/max(1,len(paras)),3)
    }


def main():
    ap=argparse.ArgumentParser(description='Heuristic prose texture fingerprint; warning tool, not literary judge')
    ap.add_argument('files', nargs='+')
    ap.add_argument('--json', action='store_true')
    a=ap.parse_args()
    rows=[analyze(f) for f in a.files]
    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))

if __name__=='__main__': main()
