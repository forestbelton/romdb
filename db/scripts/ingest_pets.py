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
            TRIM(:description)
        );
    """,
)


def PET_SKILLS_MISSING(n: int) -> common.UpsertFile:
    return common.UpsertFile(
        csv_path="csv/pets.csv",
        upsert_sql=f"""
            INSERT OR IGNORE INTO
            pet_skills (name, type, description)
            VALUES (:skill{n}, '', '');
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
            TRIM(:name),
            TRIM(UPPER(:type)),
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
            TRIM(:item_name),
            :unit_price_shells,
            :quantity
        );
    """,
)


def main() -> None:
    PET_SKILLS.execute()
    for skill_id in range(1, 6):
        PET_SKILLS_MISSING(skill_id).execute()
    PETS.execute()
    PET_CATCH_ITEMS.execute()
    common.db.commit()


if __name__ == "__main__":
    main()
