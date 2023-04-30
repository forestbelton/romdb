#!/bin/bash
set -euo pipefail

VIRTUAL_ENV=${VIRTUAL_ENV:-}

if [[ "$VIRTUAL_ENV" = "" ]]; then
    if [[ ! -d "$(pwd)/.env" ]]; then
        python -m venv $(pwd)/.env
    fi
    source $(pwd)/.env/bin/activate
    pip install --quiet --requirement requirements.txt
fi

yoyo apply --batch
python scripts/ingest_pets.py
python scripts/ingest_singra.py
python scripts/ingest_cooking.py
