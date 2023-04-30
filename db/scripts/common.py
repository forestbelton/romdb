import csv
import dataclasses
import sqlite3
from typing import Generator, Optional, TypedDict

# TODO: Compute path from script directory
db = sqlite3.connect("romdb.sqlite3")
db.row_factory = sqlite3.Row


class Entity(TypedDict):
    id: int


@dataclasses.dataclass
class Upsert:
    fetch_existing_sql: str
    insert_new_sql: str

    def execute(self, data: dict) -> Optional[sqlite3.Row]:
        upsert(self.fetch_existing_sql, self.insert_new_sql, data)


def read_csv(filename: str) -> Generator[dict, None, None]:
    with open(filename, "r") as f:
        r = csv.DictReader(f)
        for row in r:
            yield row


def execute_one(query: str, data: dict) -> Optional[sqlite3.Row]:
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        return cursor.fetchone()
    finally:
        cursor.close()


def execute_for_csv(filename: str, query: str) -> list[Optional[sqlite3.Row]]:
    return [execute_one(query, row) for row in read_csv(filename)]


@dataclasses.dataclass
class UpsertFile:
    csv_path: str
    upsert_sql: str

    def execute(self) -> list[sqlite3.Row]:
        return execute_for_csv(self.csv_path, self.upsert_sql)


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
