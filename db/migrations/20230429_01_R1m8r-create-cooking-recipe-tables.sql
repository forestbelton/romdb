-- Create cooking recipe tables
-- depends: 20230425_02_yKFlP-create-singra-master-box-tables
CREATE TABLE IF NOT EXISTS cooking_recipes(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    num_stars INTEGER NOT NULL,
    cook_mastery_effect TEXT NOT NULL,
    cook_mastery_value REAL NOT NULL,
    taste_mastery_effect TEXT NOT NULL,
    taste_mastery_value REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS cooking_recipe_ingredients(
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES cooking_recipes(id),
    ingredient_name TEXT NOT NULL,
    UNIQUE (recipe_id, ingredient_name)
);

CREATE TABLE IF NOT EXISTS cooking_recipe_effects(
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES cooking_recipes(id),
    effect TEXT NOT NULL,
    value TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS cooking_recipe_effects_recipe_id_idx
ON cooking_recipe_effects (recipe_id);
