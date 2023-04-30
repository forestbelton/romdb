-- Create cooking recipe tables
-- depends: 20230425_02_yKFlP-create-singra-master-box-tables
CREATE TABLE IF NOT EXISTS cooking_recipes(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT UNIQUE NOT NULL,
    num_stars INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS cooking_recipe_ingredients(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    recipe_id INTEGER NOT NULL REFERENCES cooking_recipes(id),
    ingredient_name TEXT NOT NULL,
    UNIQUE (recipe_id, ingredient_name)
);
