#!/usr/bin/env python3
"""Check the published reference data; optionally compare the exact local FZ.

This does not test hardware, measure resistance or analyse a BIOS binary.
Python standard library only. The commercial BoardView is never copied out.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import sys
from urllib.parse import unquote
import zlib

ROOT = Path(__file__).resolve().parents[1]

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

def read_json(name: str) -> dict:
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))

def read_fz(path: Path, expected_hash: str) -> dict:
    data = path.read_bytes()
    require(hashlib.sha256(data).hexdigest() == expected_hash,
            'FZ SHA-256 differs from the documented source; do not silently reuse its map.')
    require(len(data) > 8, 'FZ is too short')
    tail_length = struct.unpack('<I', data[-4:])[0]
    offset = len(data) - tail_length + 4
    require(4 < offset < len(data) - 4, 'Invalid FZ description offset')
    lines = zlib.decompress(data[4:offset]).decode('latin1').splitlines()
    parts = {}
    section = ''
    for line in lines:
        f = line.split('!')
        if f[0] == 'A' and len(f) > 1:
            section = f[1]
        elif f[0] == 'S' and section == 'REFDES':
            require(f[4] in ('YES', 'NO'), 'Unknown mirror field')
            parts[f[1]] = {'side': 'BOTTOM' if f[4] == 'YES' else 'TOP', 'pins': []}
        elif f[0] == 'S' and section == 'NET_NAME':
            parts[f[2]]['pins'].append([f[3], float(f[5]), float(f[6]), f[1]])
    for line in zlib.decompress(data[offset:]).decode('latin1').splitlines():
        f = line.split('\t')
        if len(f) > 3 and f[3] in parts:
            parts[f[3]]['description'] = f[1]
    return parts

def check_links() -> int:
    count = 0
    for doc in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
            if target.startswith(('https://', 'http://', 'mailto:', '#')):
                continue
            rel = unquote(target.split('#', 1)[0])
            require((doc.parent / rel).exists(), f'Broken link: {doc.relative_to(ROOT)} -> {target}')
            count += 1
    return count

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--boardview', type=Path, help='Privately held, exact documented .fz file')
    parser.add_argument('--photo', type=Path, help='Original full-resolution 1000075612.jpg')
    args = parser.parse_args()
    extract = read_json('boardview-extract.json')
    configs = read_json('configurations.json')['configurations']
    probes = read_json('probe-checks.json')
    parts = extract['parts']
    pinmap = {f'{name}.{p[0]}': p for name, part in parts.items() for p in part['pins']}
    for bit, pair in extract['pairs'].items():
        for state, rail in [('zero', 'GND'), ('one', '+1.8VS')]:
            part = parts[pair[state]]
            require(part['side'] == pair['side'], f'Wrong side: {pair[state]}')
            require({p[3] for p in part['pins']} == {f'DIMM_SEL{bit}', rail},
                    f'Unexpected nets: {pair[state]}')
    require(len(configs) == 9, 'Expected nine recovered profiles')
    require(len({c['sel3_to_0'] for c in configs}) == 9, 'Duplicate selector code')
    for c in configs:
        bits = c['sel3_to_0']
        require(len(bits) == 4 and set(bits) <= {'0', '1'}, 'Bad selector string')
        expected = [extract['pairs'][str(i)]['one' if b == '1' else 'zero']
                    for i, b in zip((3, 2, 1, 0), bits)]
        require(c['populated'] == expected, f'Population mismatch: {c["part_number"]}')
        require(c['packages'] == 8 and c['per_package_gb'] * 8 == c['total_gb'], 'Capacity mismatch')
        require(int(c['boardmask'], 16) == 1 << c['apcb_instance'], 'BoardMask mismatch')
    for key, point in probes['points'].items():
        require(key in pinmap, f'Unknown probe pad {key}')
        p = pinmap[key]
        require(p[1:3] == point['xy_mils'] and p[3] == point['net'], f'Probe mismatch: {key}')
    for test in probes['tests']:
        require(pinmap[test['red']][3] == pinmap[test['black']][3] == test['net'],
                f'Test {test["test"]} does not connect the same net')
    if args.boardview:
        raw = read_fz(args.boardview, extract['source_sha256'])
        for name, expected in parts.items():
            actual = raw[name]
            require(actual['side'] == expected['side'], f'FZ side mismatch: {name}')
            expected_pins = {str(p[0]): p[1:] for p in expected['pins']}
            actual_pins = {str(p[0]): p[1:] for p in actual['pins']}
            require(actual_pins == expected_pins, f'FZ pad/net mismatch: {name}')
            require(('Nobom' not in actual.get('description', '')) == expected['populated'],
                    f'FZ BOM mismatch: {name}')
        print('Exact local FZ hash, selected nets, pad coordinates, sides and BOM matched.')
    if args.photo:
        require(hashlib.sha256(args.photo.read_bytes()).hexdigest() == probes['photo_sha256'],
                'Source photo hash differs; do not reuse pixel coordinates.')
        print('Original source photograph hash matched.')
    links = check_links()
    print(f'PASS: 9 profiles, 4 strap pairs, 3 same-net probe tests, {links} local links.')
    print('Scope: documentation consistency only. Hardware measurements and BIOS validation remain separate.')
    return 0

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, IndexError, zlib.error) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
