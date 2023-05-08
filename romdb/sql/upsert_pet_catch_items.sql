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
