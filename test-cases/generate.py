"""Render documentation from CSV; never modify definitions or execution records."""
import argparse
import csv
import html
from pathlib import Path
import re
import sys
BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR.parent
FIELDS = ['ID', 'Title', 'Requirement', 'Behaviour IDs', 'Priority', 'Design status', 'Open question', 'Preconditions', 'Test data', 'Steps', 'Expected result', 'Actual result', 'Status', 'Data used', 'Environment / date', 'Notes / evidence', 'Bug ID']
MAP_FIELDS = ['Behaviour ID', 'Requirement', 'Behaviour', 'Test cases']
STATUSES = {'NOT EXECUTED', 'PASS', 'FAIL', 'BLOCKED'}

def read_csv(path, fields):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != fields:
            raise ValueError(f'{path.name}: unexpected columns')
        rows = list(reader)
    if not rows or any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError(f'{path.name}: empty or malformed rows')
    return rows

def parts(value):
    return [item.strip() for item in value.split(';') if item.strip()]

def load(root):
    cases = read_csv(root / 'test-cases/test-cases.csv', FIELDS)
    mapping = read_csv(root / 'docs/behaviour-map.csv', MAP_FIELDS)
    req_list = re.findall(r'^\| (REQ-[\w-]+) \|', (root / 'docs/02-requirements.md').read_text(encoding='utf-8'), re.M)
    reqs = set(req_list)
    questions = set(re.findall(r'^\| (Q-\d+) \|', (root / 'docs/open-questions.md').read_text(encoding='utf-8'), re.M))
    ids = [c['ID'] for c in cases]
    bids = [b['Behaviour ID'] for b in mapping]
    if len(ids) != len(set(ids)) or len(bids) != len(set(bids)) or len(reqs) != len(req_list):
        raise ValueError('Duplicate test, behaviour or requirement ID')
    by_id = {c['ID']: c for c in cases}
    for c in cases:
        if not re.fullmatch(r'TC-\d{3}', c['ID']) or c['Requirement'] not in reqs:
            raise ValueError(f'{c["ID"]}: invalid ID or requirement')
        required = [f for f in FIELDS if f not in {'Open question', 'Bug ID'}]
        if any(not c[f].strip() for f in required):
            raise ValueError(f'{c["ID"]}: missing required field')
        if c['Priority'] not in {'High', 'Medium', 'Low'} or c['Status'] not in STATUSES:
            raise ValueError(f'{c["ID"]}: invalid priority/status')
        if c['Open question'] and c['Open question'] not in questions:
            raise ValueError(f'{c["ID"]}: unknown question')
        if c['Design status'].startswith('BLOCKED') and not c['Open question']:
            raise ValueError(f'{c["ID"]}: design blocker needs question')
        if c['Status'] == 'NOT EXECUTED':
            if c['Actual result'] != 'NOT EXECUTED' or c['Bug ID']:
                raise ValueError(f'{c["ID"]}: unexecuted case contains result/bug')
        else:
            for field in ['Actual result', 'Environment / date', 'Data used', 'Notes / evidence']:
                if c[field].startswith(('NOT EXECUTED', 'TBD')):
                    raise ValueError(f'{c["ID"]}: executed state missing {field}')
            if c['Status'] in {'PASS', 'FAIL'} and not c['Design status'].startswith('READY'):
                raise ValueError(f'{c["ID"]}: verdict requires reviewed requirement')
    for b in mapping:
        linked = parts(b['Test cases'])
        if not re.fullmatch(r'B-\d{2}', b['Behaviour ID']) or b['Requirement'] not in reqs or not linked:
            raise ValueError('Invalid behaviour mapping')
        if len(linked) != len(set(linked)):
            raise ValueError('Duplicate case within behaviour')
        for tid in linked:
            if tid not in by_id or by_id[tid]['Requirement'] != b['Requirement']:
                raise ValueError(f'{b["Behaviour ID"]}: invalid case mapping {tid}')
    for c in cases:
        expected = {b['Behaviour ID'] for b in mapping if c['ID'] in parts(b['Test cases'])}
        if not expected or set(parts(c['Behaviour IDs'])) != expected:
            raise ValueError(f'{c["ID"]}: inconsistent behaviour references')
    if {b['Requirement'] for b in mapping} != reqs:
        raise ValueError('Requirements missing from behaviour map')
    return cases, mapping, reqs

def cell(value):
    value = html.escape(value, quote=False)
    for char in ['\\', '`', '*', '_', '[', ']']:
        value = value.replace(char, '\\' + char)
    return value.replace('|', '&#124;').replace('\r\n', '\n').replace('\n', '<br>')

def render(root):
    cases, mapping, reqs = load(root)
    md = ['# Manual test cases', '', 'Generated from `test-cases.csv`; edit that file, not this view. See [execution instructions](README.md).', '', 'Expected results are proposed oracles until reviewed. Design blockers are separate from execution status.', '', f'Total: {len(cases)} cases', '']
    for c in cases:
        md += [f'## {c["ID"]} — {cell(c["Title"])}', '', '| Field | Value |', '|---|---|']
        md += [f'| {field} | {cell(c[field])} |' for field in FIELDS[2:]]
        md.append('')
    counts = {s: sum(c['Status'] == s for c in cases) for s in sorted(STATUSES)}
    blocked = sum(c['Design status'].startswith('BLOCKED') for c in cases)
    rtm = ['# Behaviour-level traceability', '', 'Generated from the CSV definitions and behaviour map. Links show design coverage, not confirmed requirements or successful execution.', '', f'{len(reqs)}/{len(reqs)} proposed requirements and {len(mapping)}/{len(mapping)} listed behaviours have mapped cases. This is not exhaustive application coverage.', '', f'Cases: {len(cases)}; design-blocked: {blocked}. Latest case statuses: ' + ', '.join(f'{k}={v}' for k, v in counts.items()) + '.', '', '| Behaviour | Requirement | Proposed behaviour | Cases | Latest execution status | Bug IDs |', '|---|---|---|---|---|---|']
    by_id = {c['ID']: c for c in cases}
    for b in mapping:
        linked = [by_id[tid] for tid in parts(b['Test cases'])]
        statuses = '; '.join(c['ID'] + ': ' + c['Status'] for c in linked)
        bugs = '; '.join(sorted({c['Bug ID'] for c in linked if c['Bug ID']})) or 'None recorded'
        rtm.append('| ' + ' | '.join(cell(x) for x in [b['Behaviour ID'], b['Requirement'], b['Behaviour'], b['Test cases'], statuses, bugs]) + ' |')
    rtm += ['', 'Run-level history: [execution log](../test-cases/execution-log.csv). Details: [test cases](../test-cases/test-cases.md). Defects: [verified findings](../bug-reports/verified-findings.md).', '']
    return {root / 'test-cases/test-cases.md': '\n'.join(md), root / 'docs/04-traceability.md': '\n'.join(rtm)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate without writing; reject stale views')
    args = parser.parse_args()
    try:
        outputs = render(ROOT)
        if args.check:
            stale = [str(p.relative_to(ROOT)) for p, text in outputs.items() if not p.exists() or p.read_text(encoding='utf-8') != text]
            if stale:
                raise ValueError('Stale generated views: ' + ', '.join(stale))
        else:
            for path, text in outputs.items():
                path.write_text(text, encoding='utf-8')
        print('Documentation validation OK' if args.check else 'Rendered two Markdown views; source/results untouched')
        return 0
    except (ValueError, OSError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
