INSERT OR IGNORE INTO singra_story_rewards (
    story_id,
    item_name
) VALUES (
    (
        SELECT id
        FROM singra_stories
        WHERE story_name = TRIM(:story_name)
    ),
    TRIM(:item_name)
);
