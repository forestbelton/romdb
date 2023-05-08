#!/bin/bash
set -euo pipefail

VIRTUAL_ENV=${VIRTUAL_ENV:-}
SCRIPTDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
DBDIR="${SCRIPTDIR}/.."
ENVDIR="${DBDIR}/.env"

cd "$DBDIR"
if [[ "$VIRTUAL_ENV" = "" ]]; then
    if [[ ! -d "$ENVDIR" ]]; then
        python -m venv "$ENVDIR"
    fi
    source "$ENVDIR/bin/activate"
    pip install --quiet --requirement requirements.txt
fi

PYTHONPATH=. python romdb/cli.py create
