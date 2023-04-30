import csv
import sqlite3
from typing import Generator, Optional, TypedDict

# TODO: Compute path from script directory
db = sqlite3.connect("romdb.sqlite3")
db.row_factory = sqlite3.Row


class Entity(TypedDict):
    id: int
    created_at: str


def read_csv(filename: str) -> Generator[dict, None, None]:
    with open(filename, "r") as f:
        r = csv.DictReader(f)
        for row in r:
            yield row


def upsert(
    fetch_existing_query: str, insert_new_query: str, data: dict
) -> Optional[sqlite3.Row]:
    cursor = db.cursor()
    existing = None
    try:
        cursor.execute(fetch_existing_query, data)
        existing = cursor.fetchone()
        if existing is None:
            cursor.execute(insert_new_query, data)
            existing = cursor.fetchone()
            db.commit()
    finally:
        cursor.close()
    return existing
