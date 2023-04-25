-- 
-- depends: 20230425_01_gDK3c-create-tables-for-pet-data
CREATE TABLE singra_stories(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    map_name TEXT NOT NULL,
    story_name TEXT NOT NULL,
    reward_item_name TEXT NOT NULL
);

CREATE TABLE singra_story_quests(
    id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMETSTAMP,
    story_id INTEGER NOT NULL REFERENCES singra_stories(id),
    quest_number INTEGER NOT NULL,
    quest_name TEXT NOT NULL,
    UNIQUE (story_id, quest_number),
    CHECK (quest_number > 0)
);
