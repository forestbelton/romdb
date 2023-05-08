INSERT OR REPLACE INTO pets (
    name,
    type,
    skill1,
    skill2,
    skill3,
    skill4,
    skill5,
    hatch_exp
) VALUES (
    TRIM(:name),
    TRIM(UPPER(:type)),
    (SELECT id FROM pet_skills WHERE name = TRIM(:skill1)),
    (SELECT id FROM pet_skills WHERE name = TRIM(:skill2)),
    (SELECT id FROM pet_skills WHERE name = TRIM(:skill3)),
    (SELECT id FROM pet_skills WHERE name = TRIM(:skill4)),
    (SELECT id FROM pet_skills WHERE name = TRIM(:skill5)),
    :hatch_exp
);
