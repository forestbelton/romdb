import csv
import sqlite3

db = sqlite3.connect("singra.sqlite3")
db.executescript("""
CREATE TABLE IF NOT EXISTS singra_story_quests(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    map_name TEXT NOT NULL,
    story_name TEXT NOT NULL,
    quest_number INTEGER NOT NULL,
    quest_name TEXT NOT NULL,
    UNIQUE (story_name, quest_number)
);

CREATE INDEX IF NOT EXISTS singra_story_quests_story_name
    ON singra_story_quests (story_name);

CREATE TABLE IF NOT EXISTS singra_story_rewards(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    story_name TEXT UNIQUE NOT NULL REFERENCES singra_story_quests (story_name),
    item_name TEXT NOT NULL
);
""")
db.commit()


def insert_story_quest(row):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM singra_story_quests WHERE story_name = ? AND quest_number = ?", (row["story_name"], row["quest_number"],))
    existing = cursor.fetchone()
    if existing is not None:
        cursor.close()
        return
    cursor.execute("INSERT INTO singra_story_quests (map_name, story_name, quest_number, quest_name) VALUES (?, ?, ?, ?)",
        (row["map_name"], row["story_name"], row["quest_number"], row["quest_name"],))
    cursor.close()


def insert_story_reward(row):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM singra_story_rewards WHERE story_name = ?", (row["story_name"],))
    existing = cursor.fetchone()
    if existing is not None:
        cursor.close()
        return
    cursor.execute("INSERT INTO singra_story_rewards (story_name, item_name) VALUES (?, ?)", (row["story_name"], row["item_name"],))
    cursor.close()


def main() -> None:
    with open("singra_story_quests.csv", "r") as f:
        r = csv.DictReader(f)
        for row in r:
            insert_story_quest(row)
            db.commit()
    with open("singra_story_rewards.csv", "r") as f:
        r = csv.DictReader(f)
        for row in r:
            insert_story_reward(row)
            db.commit()

if __name__ == "__main__":
    main()

