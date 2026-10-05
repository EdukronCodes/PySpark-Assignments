"""Deterministic course fixtures; no third-party dependencies."""
from pathlib import Path
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
import csv
import json
import random

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'

def write_csv(name, rows):
    target = DATA / 'raw' / f'{name}.csv'
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def main():
    rng = random.Random(42)
    customers = [dict(customer_id=f'C{i:03d}', name=f'Synthetic Customer {i}',
        email='' if i % 17 == 0 else f' buyer{i}@example.test ',
        city=[' Delhi ', 'mumbai', 'Bengaluru', 'CHENNAI'][i % 4],
        signup_date='2026-06-01', updated_at='2026-06-01T00:00:00Z') for i in range(1, 81)]
    stores = [dict(store_id=f'S{i:02d}', store_name=f'Store {i}', city=city)
              for i, city in enumerate(['Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Pune'], 1)]
    products = [dict(product_id=f'P{i:03d}', product_name=f'Product {i}',
        category=['Grocery', 'Electronics', 'Clothing', 'Home'][i % 4],
        list_price=str(100 + i * 75), cost_price=str(50 + i * 40)) for i in range(1, 21)]
    orders, lines = [], []
    for i in range(1, 301):
        ts = datetime(2026, 7, 1, 8) + timedelta(days=(i-1) % 90, hours=i % 12)
        orders.append(dict(order_id=f'O{i:04d}', customer_id=f'C{rng.randint(1,80):03d}',
            store_id=f'S{rng.randint(1,5):02d}', order_ts=ts.isoformat()+'Z',
            status='cancelled' if i % 10 == 0 else 'completed', channel='online' if i % 3 == 0 else 'store'))
        for j in range(1, rng.randint(1, 4)+1):
            p = rng.choice(products)
            lines.append(dict(line_id=f'L{i:04d}_{j}', order_id=f'O{i:04d}', product_id=p['product_id'],
                quantity=rng.randint(1, 5), unit_price=p['list_price'], discount_pct=rng.choice(['0.00','0.05','0.10'])))
    original_lines = [r.copy() for r in lines]
    # Exactly 10 invalid additions and 8 identical duplicate additions.
    for i in range(10):
        bad = original_lines[i].copy()
        bad['line_id'] = f'BAD{i:02d}'
        if i < 3: bad['quantity'] = -1
        elif i < 6: bad['discount_pct'] = '1.50'
        elif i < 8: bad['product_id'] = 'P999'
        else: bad['order_id'] = ''
        lines.append(bad)
    lines.extend(r.copy() for r in original_lines[:8])
    completed = {r['order_id'] for r in orders if r['status'] == 'completed'}
    returns = [dict(return_id=f'R{i:03d}', line_id=r['line_id'], return_quantity=1,
        return_ts='2026-09-30T12:00:00Z', reason='damaged' if i % 2 else 'changed_mind')
        for i, r in enumerate([x for x in original_lines if x['order_id'] in completed][:30], 1)]
    tables = dict(customers=customers, stores=stores, products=products, orders=orders, order_items=lines, returns=returns)
    for name, rows in tables.items(): write_csv(name, rows)
    for folder in ['events_archive', 'payments_archive', 'stream_input', 'payments_input']:
        (DATA / folder).mkdir(parents=True, exist_ok=True)
    event_total = 0
    for batch in range(1, 7):
        events, payments = [], []
        for j in range(8):
            num = (batch-1)*8+j+1
            ts = datetime(2026, 9, 30, 10) + timedelta(minutes=(batch-1)*10+j)
            event = dict(event_id=f'E{num:04d}', event_time=ts.isoformat()+'Z',
                customer_id=f'C{num:03d}', order_id=f'O{num:04d}',
                event_type='purchase' if j % 3 else 'view',
                items=[dict(product_id='P001', quantity=2, unit_price='175.00'),
                       dict(product_id='P002', quantity=1, unit_price='250.00')] if j % 3 else [],
                device=dict(os='android', app_version='1.0'), attributes=dict(campaign='autumn'))
            events.append(event)
            if event['event_type'] == 'purchase':
                payments.append(dict(payment_id=f'PAY{num:04d}', order_id=event['order_id'],
                    payment_time=(ts+timedelta(minutes=2)).isoformat()+'Z', amount='600.00'))
        if batch == 2:
            duplicate = dict(event_id='E0001', event_time='2026-09-30T10:01:00Z', customer_id='C001',
                order_id='O0001', event_type='view', items=[], device=dict(os='android', app_version='1.0'), attributes={})
            events.append(duplicate)
        if batch == 3:
            late = events[1].copy()
            late.update(event_id='LATE_WITHIN', event_time='2026-09-30T10:16:00Z')
            events.append(late)
        if batch == 5:
            late = events[1].copy()
            late.update(event_id='LATE_BEYOND', event_time='2026-09-30T10:00:00Z')
            events.append(late)
        if batch == 6:
            bad = events[1].copy()
            bad.update(event_id='BAD_EVENT', event_time='not-a-timestamp', items=[])
            events.append(bad)
        for folder, rows in [('events_archive', events), ('payments_archive', payments)]:
            (DATA / folder / f'batch_{batch:03d}.json').write_text(
                ''.join(json.dumps(row)+'\n' for row in rows), encoding='utf-8')
        event_total += len(events)
    cent = Decimal('0.01')
    def net(r):
        return (Decimal(r['quantity'])*Decimal(r['unit_price'])*(1-Decimal(r['discount_pct']))).quantize(cent, rounding=ROUND_HALF_UP)
    booked = sum((net(r) for r in original_lines if r['order_id'] in completed), Decimal(0))
    line_lookup = {r['line_id']: r for r in original_lines}
    refunds = sum((net(line_lookup[r['line_id']]) / Decimal(line_lookup[r['line_id']]['quantity'])
                   for r in returns), Decimal(0)).quantize(cent)
    manifest = dict(seed=42, raw_counts={k: len(v) for k,v in tables.items()},
        invalid_line_additions=10, identical_duplicate_additions=8, clean_unique_lines=len(original_lines),
        completed_orders=270, booked_revenue=str(booked), accepted_return_units=30,
        return_adjusted_revenue=str(booked-refunds), event_rows=event_total,
        event_unique_ids=event_total-1, event_batches=6)
    (DATA / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(json.dumps(manifest, indent=2))

if __name__ == '__main__': main()
