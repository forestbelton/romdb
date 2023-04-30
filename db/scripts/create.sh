#!/bin/bash
set -euo pipefail

VIRTUAL_ENV=${VIRTUAL_ENV:-}
SCRIPTDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ENVDIR="${SCRIPTDIR}/../.env"

if [[ "$VIRTUAL_ENV" = "" ]]; then
    if [[ ! -d "$ENVDIR" ]]; then
        python -m venv "$ENVDIR"
    fi
    source "$ENVDIR/bin/activate"
    pip install --quiet --requirement requirements.txt
fi

yoyo apply --batch
python scripts/ingest_pets.py
python scripts/ingest_singra.py
python scripts/ingest_cooking.py
