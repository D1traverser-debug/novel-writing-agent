#!/usr/bin/env python3
import argparse, json, re, pathlib

def main():
    ap = argparse.ArgumentParser(description='NOVEL_OS final proofread guard v1.0')
    ap.add_argument('file', type=pathlib.Path)
    args = ap.parse_args()
    text = args.file.read_text(encoding='utf-8')
    warnings = []

    pairs = [('“','”'),('‘','’'),('（','）'),('【','】'),('《','》')]
    for a, b in pairs:
        if text.count(a) != text.count(b):
            warnings.append(f'unbalanced:{a}{b}:{text.count(a)}!={text.count(b)}')

    patterns = [
        (r'[，。！？；：、]{2,}', 'repeated_punctuation'),
        (r'\t', 'tab_character'),
        (r' {2,}', 'multiple_ascii_spaces'),
        (r'([一二三四五六七八九十两\d]+)个月多', 'quantity_order_months'),
        (r'([一二三四五六七八九十两\d]+)个星期多', 'quantity_order_weeks'),
        (r'([一二三四五六七八九十两\d]+)天多', 'quantity_order_days'),
        (r'(?<!\d)\d{1}:\d{2}(?!\d)', 'time_single_digit_hour'),
    ]
    for pat, label in patterns:
        for m in re.finditer(pat, text):
            line = text.count('\n', 0, m.start()) + 1
            warnings.append(f'{label}:line={line}:text={m.group(0)}')

    for token in ['的的','了了','着着','吗吗','呢呢','吧吧','是是']:
        pos = text.find(token)
        while pos != -1:
            line = text.count('\n', 0, pos) + 1
            warnings.append(f'suspected_duplicate_char:line={line}:text={token}')
            pos = text.find(token, pos + 1)

    result = {'status': 'PASS' if not warnings else 'REVIEW_REQUIRED', 'warnings': warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not warnings else 1

if __name__ == '__main__':
    raise SystemExit(main())
