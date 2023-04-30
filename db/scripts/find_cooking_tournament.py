import common

FIND_BEST_RECIPES_QUERY = """
WITH recipe_ingredient_counts AS (
  SELECT
    recipe_id,
    ingredient_name,
    (ingredient_name IN ({0})) AS has_ingredient
  FROM cooking_recipe_ingredients
  WHERE recipe_id IN (
    SELECT DISTINCT recipe_id
    FROM cooking_recipe_ingredients
    WHERE ingredient_name IN ({0})
  )
),
candidate_recipe_ids AS (
  SELECT DISTINCT recipe_id
  FROM recipe_ingredient_counts ric
  WHERE NOT EXISTS (
    SELECT 1 FROM recipe_ingredient_counts
    WHERE recipe_id = ric.recipe_id AND has_ingredient = 0
  )
)
SELECT id, name, num_stars
FROM cooking_recipes cr
JOIN candidate_recipe_ids cri ON cr.id = cri.recipe_id
ORDER BY num_stars DESC;
"""


def find_best_recipes(ingredients: list[str]):
    cursor = common.db.cursor()
    param_list = ",".join(["?" for ingredient in ingredients])
    query = FIND_BEST_RECIPES_QUERY.format(param_list)
    cursor.execute(query, ingredients + ingredients)
    return [dict(row) for row in cursor.fetchall()]


def main() -> None:
    while True:
        line = input("Ingredients (comma separated): ")
        ings = [word.strip() for word in line.split(",")]
        recipes = find_best_recipes(ings)
        print(recipes)


if __name__ == "__main__":
    main()
