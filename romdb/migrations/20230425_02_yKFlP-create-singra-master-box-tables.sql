-- Create Singra Master Box tables
-- depends: 20230425_01_gDK3c-create-pet-tables
CREATE TABLE IF NOT EXISTS singra_stories(
    id INTEGER PRIMARY KEY,
    map_name TEXT NOT NULL,
    story_name TEXT NOT NULL,
    UNIQUE (map_name, story_name)
);

CREATE IF NOT EXISTS TABLE singra_story_quests(
    id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL REFERENCES singra_stories(id),
    quest_number INTEGER NOT NULL,
    quest_name TEXT NOT NULL,
    UNIQUE (story_id, quest_number),
    CHECK (quest_number > 0)
);

CREATE IF NOT EXISTS TABLE singra_story_rewards(
    id INTEGER PRIMARY KEY,
    story_id INTEGER NOT NULL REFERENCES singra_stories(id),
    item_name TEXT NOT NULL,
    UNIQUE (story_id, item_name)
);
