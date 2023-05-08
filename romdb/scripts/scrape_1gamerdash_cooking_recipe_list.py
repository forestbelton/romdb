import csv
import re

import bs4
import requests

FLOAT_RE = re.compile(r"^\d+(\.\d+)?%?$")
COOKING_IMG_URL_RE = re.compile(
    r"^https://1gamerdash.com/wp-content/themes/ogd/assets/images/cooking/(.*?)\.(png|jpg)\?x26807$"
)


def get_ing_name(src: str) -> str:
    m = COOKING_IMG_URL_RE.match(src)
    img_name = m.group(1)
    return " ".join([word.title() for word in img_name.split("-")])


def get_ing_names(col: bs4.Tag) -> list[str]:
    if len(col.contents) == 1 and isinstance(col.contents[0], bs4.NavigableString):
        return [str(col.contents[0])]
    return [get_ing_name(node["src"]) for node in col.contents]


EFFECT_NAMES = {
    "ATK": "ATTACK",
    "ATTACK SPD": "ATTACK_SPEED",
    "CAST DELAY": "CAST_DELAY",
    "DEF": "DEFENSE",
    "DMG ON ALL EXCEPT MVP AND MINI MONSTERS": "DMG_MONSTER_NOMVP",
    "DMG ON MVP AND MINI MONSTERS": "DMG_MONSTER_MVP",
    "DMG INCREASE TO PLAYERS": "PLAYER_DMG",
    "IGNORE DEF": "IGNORE_DEFENSE",
    "M.ATK": "MAGIC_ATTACK",
    "M.DEF": "MAGIC_DEFENSE",
    "M.PEN": "MAGIC_PENETRATION",
    "MAX HP": "MAX_HP",
    "MAX SP": "MAX_SP",
    "MOVE SPD": "MOVE_SPEED",
    "PEN": "PENETRATION",
    "PHYSICAL DEFENSE": "DEFENSE",
}


def _parse_effect(raw_effect: str) -> tuple[str, str]:
    if raw_effect.startswith("*"):
        return ("COMPLEX", raw_effect)
    elif "+" in raw_effect or "-" in raw_effect:
        raw_stat, raw_value = re.split(r"[+-]", raw_effect)
    elif raw_effect.count(" ") == 1:
        raw_stat, raw_value = raw_effect.split(" ")
    else:
        raise ValueError()
    raw_value = raw_value.strip()
    stat = EFFECT_NAMES[raw_stat.strip().upper()]
    assert FLOAT_RE.match(raw_value)
    value = float(raw_value[:-1] if raw_value.endswith("%") else raw_value)
    return stat, value


def parse_effect(raw_effect: str) -> tuple[str, str]:
    try:
        return _parse_effect(raw_effect)
    except:
        raise ValueError(f"Couldn't parse effect '{raw_effect}': Unknown form")

PARSED_METHOD_NAMES = {
    "frying_station": "FRY",
    "grilling_station": "GRILL",
    "boiling_station": "BOIL",
    "beverage_station": "BEVERAGE",
}

def parse_method(tag: bs4.Tag) -> str:
    match = COOKING_IMG_URL_RE.match(tag["src"])
    if match is None:
        raise ValueError(f"Couldn't parse cooking method: '{tag['src']}'")
    return PARSED_METHOD_NAMES[match.group(1)]

def main() -> None:
    resp = requests.get("https://1gamerdash.com/ragnarok-mobile-cooking-recipe-list")
    assert resp.status_code == 200
    soup = bs4.BeautifulSoup(resp.text, features="html.parser")
    recipes = []
    for row in soup.select("#rom-recipe-list tr:not(thead > tr, tfoot > tr)"):
        name_col = row.select_one(".name")
        effect_col = row.select_one(".effect")
        ingredients_col = effect_col.next_sibling
        mastery_col = row.select_one(".mastery")
        method_col = mastery_col.next_sibling
        recipe = {
            "name": name_col.contents[0].replace("â\x80\x99", "'"),
            "num_stars": int(name_col["data-star"]),
            "method": parse_method(method_col.contents[0]),
            "ingredients": get_ing_names(ingredients_col),
            "effects": [
                str(node).strip() for node in effect_col.contents if node.name != "br"
            ],
            "mastery": [
                str(node).strip() for node in mastery_col.contents if node.name != "br"
            ],
        }
        assert len(recipe["mastery"]) == 2
        recipes.append(recipe)
    print(f"Parsed {len(recipes)} recipes")
    with open("csv/cooking_recipes.csv", "w") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "recipe_name",
                "num_stars",
                "method",
                "cook_mastery_effect",
                "cook_mastery_value",
                "taste_mastery_effect",
                "taste_mastery_value",
            ],
        )
        w.writeheader()
        for recipe in recipes:
            cook_effect, cook_value = parse_effect(recipe["mastery"][0])
            taste_effect, taste_value = parse_effect(recipe["mastery"][1])
            w.writerow(
                {
                    "recipe_name": recipe["name"],
                    "num_stars": recipe["num_stars"],
                    "method": recipe["method"],
                    "cook_mastery_effect": cook_effect,
                    "cook_mastery_value": cook_value,
                    "taste_mastery_effect": taste_effect,
                    "taste_mastery_value": taste_value,
                }
            )
    print("Wrote csv/cooking_recipes.csv")
    with open("csv/cooking_recipe_ingredients.csv", "w") as f:
        w = csv.DictWriter(f, fieldnames=["recipe_name", "ingredient_name"])
        w.writeheader()
        for recipe in recipes:
            for ingredient in recipe["ingredients"]:
                w.writerow(
                    {"recipe_name": recipe["name"], "ingredient_name": ingredient}
                )
    print("Wrote csv/cooking_recipe_ingredients.csv")
    with open("csv/cooking_recipe_effects.csv", "w") as f:
        w = csv.DictWriter(f, fieldnames=["recipe_name", "effect", "value"])
        w.writeheader()
        for recipe in recipes:
            for raw_effect in recipe["effects"]:
                if recipe["name"] == "Izlude Pride" and raw_effect.startswith(
                    "Physical Defense"
                ):
                    continue
                effect, value = parse_effect(raw_effect)
                w.writerow(
                    {"recipe_name": recipe["name"], "effect": effect, "value": value}
                )
    print("Wrote csv/cooking_recipe_effects.csv")


if __name__ == "__main__":
    main()
