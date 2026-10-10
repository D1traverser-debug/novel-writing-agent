#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

FALLBACK_BASELINE = [2550, 2394, 2630, 2840]

def fanqie_chars(text: str) -> int:
    lines = text.splitlines()
    if lines and lines[0].lstrip().startswith('#'):
        text = '\n'.join(lines[1:])
    return len(re.sub(r'\s+', '', text))

def usable_count(row):
    actual = row.get('actual_fanqie_chars')
    pred = row.get('predicted_fanqie_chars')
    if isinstance(actual, int) and actual > 0:
        return actual, 'actual'
    if isinstance(pred, int) and pred > 0:
        return pred, 'predicted'
    return None, None

def main():
    ap = argparse.ArgumentParser(description='Dynamic FQ001 chapter length gate')
    ap.add_argument('file')
    ap.add_argument('--history')
    ap.add_argument('--chapter', type=int)
    a = ap.parse_args()

    text = Path(a.file).read_text(encoding='utf-8')
    count = fanqie_chars(text)
    baseline = []
    baseline_meta = []

    if a.history and Path(a.history).exists():
        hist = json.loads(Path(a.history).read_text(encoding='utf-8'))
        rows = hist.get('chapters', hist if isinstance(hist, list) else [])
        if a.chapter is not None:
            rows = [r for r in rows if int(r.get('chapter', 10**9)) < a.chapter]
        rows = sorted(rows, key=lambda r: int(r.get('chapter', 0)))
        for r in rows[-4:]:
            c, source = usable_count(r)
            if c is not None:
                baseline.append(c)
                baseline_meta.append({'chapter': r.get('chapter'), 'count': c, 'source': source})

    if len(baseline) < 2:
        baseline = FALLBACK_BASELINE[-4:]
        baseline_meta = [{'chapter': i+1, 'count': c, 'source': 'fallback_actual'} for i,c in enumerate(baseline)]

    avg = sum(baseline) / len(baseline)
    dev = (count / avg - 1) * 100
    hard_block = abs(dev) > 45
    review = abs(dev) > 30
    result = {
        'file': str(a.file),
        'chapter': a.chapter,
        'predicted_fanqie_chars': count,
        'trailing_baseline': baseline_meta,
        'trailing_avg': round(avg, 1),
        'deviation_pct': round(dev, 1),
        'length_deviation_review': review,
        'default_release_blocked': hard_block,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
