#!/usr/bin/env bash
# MagicSquare_XX — 로컬 가상환경(.venv) 생성 및 dev 설치
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ ! -x .venv/bin/python ]]; then
  echo "Creating .venv ..."
  python3 -m venv .venv
fi

echo "Upgrading pip ..."
.venv/bin/python -m pip install -U pip

echo "Installing project (editable) with dev extras ..."
.venv/bin/python -m pip install -e ".[dev]"

echo ""
echo "Done. Activate and run tests:"
echo "  source .venv/bin/activate"
echo "  python -m pytest tests/entity/test_d_loc_01.py -v"
