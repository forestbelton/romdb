import common

RECIPES = common.UpsertFile(
    csv_path="csv/cooking_recipes.csv",
    upsert_sql="""
        INSERT OR IGNORE INTO cooking_recipes (
            name,
            num_stars
        ) VALUES (
            :recipe_name,
            :num_stars
        );
    """,
)

RECIPE_INGREDIENTS = common.UpsertFile(
    csv_path="csv/cooking_recipe_ingredients.csv",
    upsert_sql="""
        INSERT OR IGNORE INTO cooking_recipe_ingredients (
            recipe_id,
            ingredient_name
        ) VALUES (
            (
                SELECT id
                FROM cooking_recipes
                WHERE name = :recipe_name
            ),
            :ingredient_name
        );
    """,
)


def main() -> None:
    RECIPES.execute()
    RECIPE_INGREDIENTS.execute()
    common.db.commit()


if __name__ == "__main__":
    main()
