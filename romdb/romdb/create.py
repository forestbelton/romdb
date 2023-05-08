import os
import pathlib

import yoyo

import romdb.ingest

TOOL_DIR = pathlib.Path(__file__).parent.parent
YOYO_CONFIG_PATH = "./yoyo.ini"


def create(schema_only: bool = False) -> None:
    os.chdir(TOOL_DIR)
    config = yoyo.config.read_config(TOOL_DIR / YOYO_CONFIG_PATH)
    defaults = config.defaults()
    backend = yoyo.get_backend(defaults["database"])
    migrations = yoyo.read_migrations(defaults["sources"])
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    if not schema_only:
        romdb.ingest.ingest()
