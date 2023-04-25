import csv
import sqlite3
from typing import Generator, TypedDict

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

