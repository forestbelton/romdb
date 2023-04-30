import csv
import re

import bs4
import requests

ING_IMG_URL_RE = re.compile(
    r"^https://1gamerdash.com/wp-content/themes/ogd/assets/images/cooking/(.*?)\.png\?x26807$"
)


def get_ing_name(src: str) -> str:
    m = ING_IMG_URL_RE.match(src)
    img_name = m.group(1)
    return " ".join([word.title() for word in img_name.split("-")])


def get_ing_names(col: bs4.Tag) -> list[str]:
    if len(col.contents) == 1 and isinstance(col.contents[0], bs4.NavigableString):
        return [str(col.contents[0])]
    return [get_ing_name(node["src"]) for node in col.contents]


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
        recipe = {
            "name": name_col.contents[0].replace("â\x80\x99", "'"),
            "num_stars": int(name_col["data-star"]),
            "ingredients": get_ing_names(ingredients_col),
            "effects": [
                str(node).strip() for node in effect_col.contents if node.name != "br"
            ],
            "mastery": [
                str(node).strip() for node in mastery_col.contents if node.name != "br"
            ],
        }
        recipes.append(recipe)
    print(f"Parsed {len(recipes)} recipes")
    with open("csv/cooking_recipes.csv", "w") as f:
        w = csv.DictWriter(f, fieldnames=["recipe_name", "num_stars"])
        w.writeheader()
        for recipe in recipes:
            w.writerow(
                {"recipe_name": recipe["name"], "num_stars": recipe["num_stars"]}
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


if __name__ == "__main__":
    main()
