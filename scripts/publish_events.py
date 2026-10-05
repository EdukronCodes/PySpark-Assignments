"""Publish immutable JSON files using atomic rename on the local filesystem."""
from pathlib import Path
import argparse
import os
import shutil
import time

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--source', default='data/events_archive')
p.add_argument('--target', default='data/stream_input')
p.add_argument('--batch', type=int, help='Publish one batch; omit to publish all in order')
p.add_argument('--interval', type=float, default=5)
a = p.parse_args()
source, target = ROOT / a.source, ROOT / a.target
target.mkdir(parents=True, exist_ok=True)
files = [source / f'batch_{a.batch:03d}.json'] if a.batch else sorted(source.glob('batch_*.json'))
if not files: raise SystemExit('No source batches; run generate_data.py first.')
for i, f in enumerate(files):
    if not f.is_file(): raise SystemExit(f'Missing source: {f}')
    dest = target / f.name
    if dest.exists():
        print(f'Skip already published: {dest.name}')
        continue
    temp = target / ('.'+f.name+'.tmp')
    shutil.copyfile(f, temp)
    os.replace(temp, dest)
    print(f'Published {dest.name}', flush=True)
    if i < len(files)-1: time.sleep(max(0, a.interval))
