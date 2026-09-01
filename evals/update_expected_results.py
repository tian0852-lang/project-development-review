#!/usr/bin/env python3
"""Refresh generated validator evidence; never writes review or business-project files."""
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
OUTPUT = HERE / 'expected-results'
sys.path.insert(0, str(PACKAGE / 'scripts'))

from validate_package import validate as validate_package
from validate_review import validate as validate_review


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    write_json(OUTPUT / 'package-validation.json', validate_package(PACKAGE))
    fixture_results = {}
    for name in ('new-ready', 'change-ready', 'mixed-ready', 'conditional-ready',
                 'intake-valid', 'plan-proposal-valid'):
        result = validate_review(HERE / 'fixtures' / name, fixture=True)
        fixture_results[name] = {key: result[key] for key in ('readiness', 'phase_passed', 'errors')}
    write_json(OUTPUT / 'fixture-results.json', fixture_results)
    result = subprocess.run(
        [sys.executable, '-B', str(HERE / 'run_tests.py')],
        cwd=PACKAGE,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    (OUTPUT / 'validator-tests.txt').write_text(result.stdout, encoding='utf-8')
    if result.returncode:
        raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
