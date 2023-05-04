import common

RECIPES = common.UpsertFile(
    csv_path="csv/cooking_recipes.csv",
    upsert_sql="""
        INSERT OR REPLACE INTO cooking_recipes (
            name,
            num_stars,
            method,
            cook_mastery_effect,
            cook_mastery_value,
            taste_mastery_effect,
            taste_mastery_value
        ) VALUES (
            TRIM(:recipe_name),
            :num_stars,
            TRIM(:method),
            TRIM(:cook_mastery_effect),
            TRIM(:cook_mastery_value),
            TRIM(:taste_mastery_effect),
            TRIM(:taste_mastery_value)
        );
    """,
)

RECIPE_INGREDIENTS = common.UpsertFile(
    csv_path="csv/cooking_recipe_ingredients.csv",
    upsert_sql="""
        INSERT OR REPLACE INTO cooking_recipe_ingredients (
            recipe_id,
            ingredient_name
        ) VALUES (
            (
                SELECT id
                FROM cooking_recipes
                WHERE name = TRIM(:recipe_name)
            ),
            TRIM(:ingredient_name)
        );
    """,
)


def main() -> None:
    RECIPES.execute()
    RECIPE_INGREDIENTS.execute()
    common.db.commit()


if __name__ == "__main__":
    main()
