import csv
import sqlite3
from typing import TypedDict

import common
from common import db, Entity


class Story(TypedDict):
    map_name: str
    story_name: str
    reward_item_name: str
    quests: list[str]


class StoryEntity(Entity, Story):
    pass


class StoryQuestEntity(Entity):
    quest_number: int
    quest_name: str


def read_stories() -> list[Story]:
    stories_by_name: dict[str, Story] = {}
    quests_by_story_name: dict[str, list[tuple[int, str]]] = {}
    for row in common.read_csv("csv/singra_story_quests.csv"):
        story_name = row["story_name"]
        if story_name not in stories_by_name:
            stories_by_name[story_name] = {
                "map_name": row["map_name"],
                "quests": [],
                "reward_item_name": "",
                "story_name": story_name,
            }
        if story_name not in quests_by_story_name:
            quests_by_story_name[story_name] = []
        quests_by_story_name[story_name].append(
            (int(row["quest_number"]), row["quest_name"])
        )
    for story_name, quests in quests_by_story_name.items():
        stories_by_name[story_name]["quests"] = [
            quest[1] for quest in sorted(quests, key=lambda quest: quest[0])
        ]
    for row in common.read_csv("csv/singra_story_rewards.csv"):
        story = stories_by_name[row["story_name"]]
        story["reward_item_name"] = row["item_name"]
    return list(stories_by_name.values())


def upsert_story(story: Story) -> StoryEntity:
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM singra_stories WHERE story_name = ?", (story["story_name"],)
    )
    existing_story = cursor.fetchone()
    if existing_story is not None:
        cursor.close()
        return existing_story
    cursor.execute(
        "INSERT INTO singra_stories (map_name, story_name, reward_item_name) VALUES (:map_name, :story_name, :reward_item_name)",
        {
            "map_name": story["map_name"],
            "story_name": story["story_name"],
            "reward_item_name": story["reward_item_name"],
        },
    )
    cursor.execute(
        "SELECT * FROM singra_stories WHERE story_name = ?", (story["story_name"],)
    )
    new_story = cursor.fetchone()
    cursor.close()
    return new_story


def upsert_story_quest(
    story_id: int, quest_number: int, quest_name: str
) -> StoryQuestEntity:
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM singra_story_quests WHERE story_id = :story_id AND quest_number = :quest_number",
        {"story_id": story_id, "quest_number": quest_number},
    )
    existing = cursor.fetchone()
    if existing is not None:
        cursor.close()
        return existing
    cursor.execute(
        "INSERT INTO singra_story_quests (story_id, quest_number, quest_name) VALUES (:story_id, :quest_number, :quest_name)",
        {"story_id": story_id, "quest_number": quest_number, "quest_name": quest_name},
    )
    cursor.execute(
        "SELECT * FROM singra_story_quests WHERE story_id = :story_id AND quest_number = :quest_number",
        {"story_id": story_id, "quest_number": quest_number},
    )
    return cursor.fetchone()


def main() -> None:
    stories = read_stories()
    for story in stories:
        story_row = upsert_story(story)
        for quest_number, quest_name in enumerate(story["quests"]):
            upsert_story_quest(story_row["id"], quest_number + 1, quest_name)
    db.commit()


if __name__ == "__main__":
    main()
