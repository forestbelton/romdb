import common

# NB: Some pets, such as Mechanical Hound, actually offer two bonus stats on
#     hatch rather than one. This eventually should be accounted for in the
#     database as right now this data is ignored.
#
#     Known affected pets: Mechanical Hound, Roween, Small Siroma, Orc Lady,
#                          Sky Petite, Highland Parasite, Orc Baby, Moonlight
#                          Flower, Lightning Gentleman
#
# NB: Some pets have no bonus stats at all! This further justifies a separate
#     M:1 table for hatch unlock stats.
#
#     Known affected pets: Mini Gryphon

SQL_INGESTIONS = [
    ("csv/cooking_recipes.csv", "sql/upsert_cooking_recipes.sql"),
    ("csv/cooking_recipe_ingredients.csv", "sql/upsert_cooking_recipe_ingredients.sql"),
    ("csv/pet_skills.csv", "sql/upsert_pet_skills.sql"),
    # TODO: Remove missing pet skill SQL when pet skill CSV becomes complete
    ("csv/pets.csv", "sql/upsert_missing_pet_skill1.sql"),
    ("csv/pets.csv", "sql/upsert_missing_pet_skill2.sql"),
    ("csv/pets.csv", "sql/upsert_missing_pet_skill3.sql"),
    ("csv/pets.csv", "sql/upsert_missing_pet_skill4.sql"),
    ("csv/pets.csv", "sql/upsert_missing_pet_skill5.sql"),
    ("csv/pets.csv", "sql/upsert_pets.sql"),
    ("csv/pet_catch_items.csv", "sql/upsert_pet_catch_items.sql"),
    ("csv/singra_story_quests.csv", "sql/upsert_singra_stories.sql"),
    ("csv/singra_story_quests.csv", "sql/upsert_singra_story_quests.sql"),
    ("csv/singra_story_rewards.csv", "sql/upsert_singra_story_rewards.sql"),
]


def ingest() -> None:
    for csv_path, upsert_sql_path in SQL_INGESTIONS:
        upsert_csv_file(csv_path, upsert_sql_path)


def upsert_csv_file(csv_path: str, upsert_sql_path: str) -> None:
    print(f"Ingesting {csv_path} with {upsert_sql_path}...")
    with open(upsert_sql_path, "r") as f:
        upsert_sql = f.read()
    common.execute_for_csv(csv_path, upsert_sql)
    common.db.commit()
