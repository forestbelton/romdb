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
