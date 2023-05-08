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
