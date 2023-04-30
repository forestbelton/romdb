import csv

import common


def upsert_recipe(row):
    return common.upsert(
        "SELECT * FROM cooking_recipes WHERE name = :recipe_name",
        "INSERT INTO cooking_recipes (name, num_stars) VALUES (:recipe_name, :num_stars)",
        row,
    )


def upsert_recipe_ingredient(row):
    return common.upsert(
        "SELECT * FROM cooking_recipe_ingredients WHERE recipe_id = (SELECT id FROM cooking_recipes WHERE name = :recipe_name) AND ingredient_name = :ingredient_name",
        "INSERT INTO cooking_recipe_ingredients (recipe_id, ingredient_name) VALUES ((SELECT id FROM cooking_recipes WHERE name = :recipe_name), :ingredient_name)",
        row,
    )


def main() -> None:
    for row in common.read_csv("csv/cooking_recipes.csv"):
        upsert_recipe(row)
    for row in common.read_csv("csv/cooking_recipe_ingredients.csv"):
        upsert_recipe_ingredient(row)


if __name__ == "__main__":
    main()
