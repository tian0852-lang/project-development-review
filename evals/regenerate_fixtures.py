#!/usr/bin/env python3
"""Regenerate only the package's named synthetic fixtures from fixture_factory."""
from pathlib import Path

from fixture_factory import build_fixture


HERE = Path(__file__).resolve().parent
FIXTURES = {
    'new-ready': {'mode': 'new'},
    'change-ready': {'mode': 'change'},
    'mixed-ready': {'mode': 'mixed'},
    'conditional-ready': {'mode': 'new', 'conditional': True},
    'intake-valid': {'mode': 'new', 'stage': 'intake'},
    'plan-proposal-valid': {'mode': 'new', 'stage': 'technical_plan'},
}


def main():
    for name, options in FIXTURES.items():
        root = HERE / 'fixtures' / name
        files = build_fixture(name=name, **options)
        for relative, text in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')
        print(f'{name}: {len(files)} generated files')


if __name__ == '__main__':
    main()
