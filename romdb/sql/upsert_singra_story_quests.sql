INSERT OR REPLACE INTO singra_story_quests (
    story_id,
    quest_number,
    quest_name
) VALUES (
    (
        SELECT id
        FROM singra_stories
        WHERE map_name = TRIM(:map_name)
        AND story_name = TRIM(:story_name)
    ),
    :quest_number,
    TRIM(:quest_name)
);
