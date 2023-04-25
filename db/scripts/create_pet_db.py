import csv
import sqlite3

db = sqlite3.connect("pets.sqlite3")
db.executescript(
    """
    CREATE TABLE IF NOT EXISTS pet_skills(
        id INTEGER PRIMARY KEY,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        name TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL,
        range REAL,
        time REAL,
        cooldown REAL,
        description TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS pets(
        id INTEGER PRIMARY KEY,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        name TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL,
        skill1 INTEGER NOT NULL REFERENCES pet_skills(id),
        skill2 INTEGER NOT NULL REFERENCES pet_skills(id),
        skill3 INTEGER NOT NULL REFERENCES pet_skills(id),
        skill4 INTEGER NOT NULL REFERENCES pet_skills(id),
        skill5 INTEGER NOT NULL REFERENCES pet_skills(id),
        hatch_exp INTEGER NOT NULL,
        hatch_stat INTEGER,
        hatch_stat_amount INTEGER
    );

    CREATE TABLE IF NOT EXISTS pet_catch_items(
        id INTEGER PRIMARY KEY,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        pet_id INTEGER NOT NULL REFERENCES pets(id),
        item_name TEXT NOT NULL,
        unit_price_shells INTEGER,
        quantity INTEGER NOT NULL
    );
    """
)

def get_skill_id_by_name(name: str) -> int:
    cursor = db.cursor()
    cursor.execute("SELECT id FROM pet_skills WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute("INSERT INTO pet_skills (name, type, description) VALUES (?, '', '')", (name,))
        cursor.execute("SELECT id FROM pet_skills WHERE name = ?", (name,))
        row = cursor.fetchone()
    cursor.close()
    db.commit()
    return row[0]


# NB: Some pets, such as Mechanical Hound, actually offer two bonus stats on
#     hatch rather than one. This eventually should be accounted for in the
#     schema as right now the extra data is ignored.
#
#     Known affected pets: Mechanical Hound, Roween, Small Siroma, Orc Lady,
#                          Sky Petite, Highland Parasite, Orc Baby, Moonlight
#                          Flower, Lightning Gentleman
#
# NB: Some pets have no bonus stats at all! This further justifies a separate
#     M:1 table for hatch unlock stats.
#
#     Known affected pets: Mini Gryphon
def ingest_pets_csv() -> None:
    print("=== pets === ")
    cursor = db.cursor()
    with open("pets.csv", "r") as f:
        r = csv.DictReader(f)
        for row in r:
            print(row)
            for field in ["hatch_exp", "hatch_stat_amount"]:
                if row[field] != "":
                    row[field] = int(row[field])
                else:
                    row[field] = None
            for field in ["skill1", "skill2", "skill3", "skill4", "skill5"]:
                row[field] = get_skill_id_by_name(row[field])
            print(row)
            cursor.execute("INSERT INTO pets (name, type, skill1, skill2, skill3, skill4, skill5, hatch_exp, hatch_stat, hatch_stat_amount) VALUES (:name, :type, :skill1, :skill2, :skill3, :skill4, :skill5, :hatch_exp, :hatch_stat, :hatch_stat_amount)", row)
            db.commit()
    cursor.close()

def ingest_pet_skills_csv() -> None:
    print("=== pet_skills ===")
    cursor = db.cursor()
    with open("pet_skills.csv", "r") as f:
        r = csv.DictReader(f)
        for row in r:
            print(row)
            get_skill_id_by_name(row["name"])
            assert row["type"] in {"ACTIVE", "PASSIVE"}
            if row["type"] == "ACTIVE":
                for field in {"range", "time", "cooldown"}:
                    if field not in row:
                        continue
                    row[field] = float(row[field])
                if "time" not in row:
                    row["time"] = 0.0
            elif row["type"] == "PASSIVE":
                assert row["range"] == ""
                row["range"] = None
                assert row["time"] == ""
                row["time"] = None
                assert row["cooldown"] == ""
                row["cooldown"] = None
            cursor.execute("UPDATE pet_skills SET type = :type, range = :range, time = :time, cooldown = :cooldown, description = :description WHERE name = :name", row)
            db.commit()
    cursor.close()


def ingest_pet_catch_items_csv() -> None:
    print("=== pet_catch_items ===")
    cursor = db.cursor()
    with open("pet_tame_items.csv", "r") as f:
        r = csv.DictReader(f)
        for row in r:
            print(row)
            cursor.execute(
                """
                INSERT INTO pet_catch_items (
                    pet_id,
                    item_name,
                    unit_price_shells,
                    quantity
                ) VALUES (
                    (SELECT id FROM pets WHERE name = :name),
                    :item_name,
                    :unit_price_shells,
                    :quantity
                )
                """,
                row
            )
            db.commit()
    cursor.close()


def main() -> None:
    ingest_pets_csv()
    ingest_pet_skills_csv()
    ingest_pet_catch_items_csv()

if __name__ == "__main__":
    main()

