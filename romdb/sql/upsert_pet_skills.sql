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
