import common


SINGRA_STORIES = common.UpsertFile(
    csv_path="csv/singra_story_quests.csv",
    upsert_sql="""
        INSERT OR REPLACE INTO singra_stories (
            map_name,
            story_name
        ) VALUES (
            TRIM(:map_name),
            TRIM(:story_name)
        );
    """,
)

SINGRA_STORY_QUESTS = common.UpsertFile(
    csv_path="csv/singra_story_quests.csv",
    upsert_sql="""
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
    """,
)

SINGRA_STORY_REWARDS = common.UpsertFile(
    csv_path="csv/singra_story_rewards.csv",
    upsert_sql="""
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
    """,
)


def main() -> None:
    SINGRA_STORIES.execute()
    SINGRA_STORY_QUESTS.execute()
    SINGRA_STORY_REWARDS.execute()
    common.db.commit()


if __name__ == "__main__":
    main()
