#!/bin/bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
python3 "$HERE/solve.py"
