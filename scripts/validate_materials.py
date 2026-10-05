"""Check course structure, fixtures and local Markdown links without Spark."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import ast
import csv
import json
import re
from question_bank import QUESTIONS

root = Path(__file__).resolve().parents[1]
days = sorted((root / 'days').glob('day-*.md'))
assert len(days) == 30
assert set(QUESTIONS) == set(range(1, 31))
total_questions = 0
for i, path in enumerate(days, 1):
    assert path.name.startswith(f'day-{i:02d}-')
    text = path.read_text(encoding='utf-8')
    for section in ['## Assignments', '## More examples to solve', '## Completion checks', '## Submit today']:
        assert section in text, (path, section)
    section = text.split('## Daily question bank - 30 questions\n', 1)[1].split('## Completion checks', 1)[0]
    questions = re.findall(r'^(\d+)\. (.+)$', section, re.MULTILINE)
    assert [int(num) for num, _ in questions] == list(range(1, 31)), path
    assert [q for _, q in questions] == QUESTIONS[i], path
    assert len(set(QUESTIONS[i])) == 30, path
    assert f'submissions/day-{i:02d}/answers.md' in text, path
    total_questions += len(questions)
assert total_questions == 900
for path in root.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if not target.startswith(('https://', 'http://', '#')):
            assert (path.parent / target.split('#')[0]).exists(), (path, target)
for path in list((root / 'scripts').glob('*.py')) + list((root / 'examples').glob('*.py')):
    ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
manifest = json.loads((root / 'data/manifest.json').read_text())
tables = {}
for name, expected in manifest['raw_counts'].items():
    with (root / 'data/raw' / f'{name}.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == expected
    tables[name] = rows
products = {r['product_id'] for r in tables['products']}
orders = {r['order_id']:r for r in tables['orders']}
accepted, rejected = [], []
for r in tables['order_items']:
    valid = (r['line_id'] and r['order_id'] in orders and r['product_id'] in products
             and int(r['quantity']) > 0 and Decimal(r['unit_price']) >= 0
             and 0 <= Decimal(r['discount_pct']) <= 1)
    (accepted if valid else rejected).append(r)
unique = {r['line_id']: r for r in accepted}
assert len(rejected) == manifest['invalid_line_additions']
assert len(accepted) - len(unique) == manifest['identical_duplicate_additions']
assert len(unique) == manifest['clean_unique_lines']
revenue = Decimal(0)
for r in unique.values():
    if orders[r['order_id']]['status'] == 'completed':
        revenue += (Decimal(r['quantity'])*Decimal(r['unit_price'])*(1-Decimal(r['discount_pct']))).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
assert revenue == Decimal(manifest['booked_revenue'])
events = [json.loads(line) for p in sorted((root / 'data/events_archive').glob('*.json')) for line in p.read_text().splitlines()]
assert len(events) == manifest['event_rows']
assert len({r['event_id'] for r in events}) == manifest['event_unique_ids']
assert sum(r['event_time'] == 'not-a-timestamp' for r in events) == 1
print(f'PASS: {len(days)} daily files, {total_questions} correctly numbered topic-specific questions, all local links and Python syntax, six CSV tables, revenue {revenue}, {len(events)} event rows.')
