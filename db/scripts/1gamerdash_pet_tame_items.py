import csv
import sqlite3

from common import DBFILE

conn = sqlite3.connect(DBFILE)
conn.executescript(
    """
    CREATE TABLE IF NOT EXISTS pet_tame_items(
        id INTEGER PRIMARY KEY,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        monster_id INTEGER NOT NULL REFERENCES monsters(id),
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    );
    """
)

with open("pet_tame_items.csv", "r") as f:
    for row in csv.DictReader(f):
        print(row)
        try:
            conn.execute(
                """
                INSERT INTO pet_tame_items (monster_id, item_name, quantity)
                VALUES (
                    (SELECT id FROM monsters WHERE name = :name),
                    :item_name,
                    :quantity
                );
                """,
                row,
            )
        except sqlite3.IntegrityError as exc:
            print(exc)
        conn.commit()
