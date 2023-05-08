import csv
import dataclasses
import sqlite3
from typing import Generator, Optional

# TODO: Compute path from script directory
db = sqlite3.connect("romdb.sqlite3")
db.row_factory = sqlite3.Row


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


def execute_many(query: str, data: dict) -> list[sqlite3.Row]:
    cursor = db.cursor()
    try:
        cursor.execute(query, data)
        return cursor.fetchall()
    finally:
        cursor.close()


def execute_for_csv(
    filename: str, query: str, many: bool = False
) -> list[Optional[sqlite3.Row]]:
    if not many:
        return [execute_one(query, row) for row in read_csv(filename)]
    results = []
    for row in read_csv(filename):
        results.extend(execute_many(query, row))
    return results
