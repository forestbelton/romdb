INSERT OR REPLACE INTO singra_stories (
    map_name,
    story_name
) VALUES (
    TRIM(:map_name),
    TRIM(:story_name)
);
