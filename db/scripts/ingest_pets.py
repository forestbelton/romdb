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

PET_SKILLS = common.UpsertFile(
    csv_path="csv/pet_skills.csv",
    upsert_sql="""
        INSERT OR REPLACE INTO pet_skills (
            name,
            type,
            range,
            time,
            cooldown,
            description
        ) VALUES (
            TRIM(:name),
            UPPER(TRIM(:type)),
            :range,
            :time,
            :cooldown,
            :description
        );
    """,
)

PET_SKILLS_MISSING1 = common.UpsertFile(
    csv_path="csv/pets.csv",
    upsert_sql="""
        INSERT OR IGNORE INTO
        pet_skills (name, type, description)
        VALUES (:skill1, '', '');
    """,
)

PET_SKILLS_MISSING2 = common.UpsertFile(
    csv_path="csv/pets.csv",
    upsert_sql="""
        INSERT OR IGNORE INTO
        pet_skills (name, type, description)
        VALUES (:skill2, '', '');
    """,
)

PET_SKILLS_MISSING3 = common.UpsertFile(
    csv_path="csv/pets.csv",
    upsert_sql="""
        INSERT OR IGNORE INTO
        pet_skills (name, type, description)
        VALUES (:skill3, '', '');
    """,
)

PET_SKILLS_MISSING4 = common.UpsertFile(
    csv_path="csv/pets.csv",
    upsert_sql="""
        INSERT OR IGNORE INTO
        pet_skills (name, type, description)
        VALUES (:skill4, '', '');
    """,
)

PET_SKILLS_MISSING5 = common.UpsertFile(
    csv_path="csv/pets.csv",
    upsert_sql="""
        INSERT OR IGNORE INTO
        pet_skills (name, type, description)
        VALUES (:skill5, '', '');
    """,
)

PETS = common.UpsertFile(
    csv_path="csv/pets.csv",
    upsert_sql="""
        INSERT OR REPLACE INTO pets (
            name,
            type,
            skill1,
            skill2,
            skill3,
            skill4,
            skill5,
            hatch_exp
        ) VALUES (
            :name,
            :type,
            (SELECT id FROM pet_skills WHERE name = TRIM(:skill1)),
            (SELECT id FROM pet_skills WHERE name = TRIM(:skill2)),
            (SELECT id FROM pet_skills WHERE name = TRIM(:skill3)),
            (SELECT id FROM pet_skills WHERE name = TRIM(:skill4)),
            (SELECT id FROM pet_skills WHERE name = TRIM(:skill5)),
            :hatch_exp
        );
    """,
)

PET_CATCH_ITEMS = common.UpsertFile(
    csv_path="csv/pet_catch_items.csv",
    upsert_sql="""
        INSERT OR REPLACE INTO pet_catch_items (
            pet_id,
            item_name,
            unit_price_shells,
            quantity
        ) VALUES (
            (
                SELECT id
                FROM pets
                WHERE name = TRIM(:name)
            ),
            :item_name,
            :unit_price_shells,
            :quantity
        );
    """,
)


def main() -> None:
    PET_SKILLS.execute()
    PET_SKILLS_MISSING1.execute()
    PET_SKILLS_MISSING2.execute()
    PET_SKILLS_MISSING3.execute()
    PET_SKILLS_MISSING4.execute()
    PET_SKILLS_MISSING5.execute()
    PETS.execute()
    PET_CATCH_ITEMS.execute()
    common.db.commit()


if __name__ == "__main__":
    main()
