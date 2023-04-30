import initSqlJs, { Database } from "sql.js";
import { CookingRecipe } from "./model";

const SQLJS_WASM_BASEURL = "https://sql.js.org/dist";
const ROMDB_SQLITE_PATH = "/romdb/romdb.sqlite3";

const GET_ALL_INGREDIENTS_QUERY = `
SELECT DISTINCT ingredient_name
FROM cooking_recipe_ingredients
WHERE NOT (ingredient_name LIKE '1 Any %')
ORDER BY ingredient_name ASC;
`;

const GET_COOKING_RECIPE_INGREDIENTS_QUERY = `
SELECT ingredient_name
FROM cooking_recipe_ingredients
WHERE recipe_id = ?;
`;

const GET_MATCHING_RECIPE_IDS_QUERY = (params: string) => `
WITH recipe_ingredient_counts AS (
  SELECT
    recipe_id,
    ingredient_name,
    (ingredient_name IN (${params})) AS has_ingredient
  FROM cooking_recipe_ingredients
  WHERE recipe_id IN (
    SELECT DISTINCT recipe_id
    FROM cooking_recipe_ingredients
    WHERE ingredient_name IN (${params})
  )
),
candidate_recipe_ids AS (
  SELECT DISTINCT recipe_id
  FROM recipe_ingredient_counts ric
  WHERE NOT EXISTS (
    SELECT 1 FROM recipe_ingredient_counts
    WHERE recipe_id = ric.recipe_id AND has_ingredient = 0
  )
)
SELECT id, name, num_stars
FROM cooking_recipes cr
JOIN candidate_recipe_ids cri ON cr.id = cri.recipe_id
ORDER BY num_stars DESC;
`;

class RomDatabase {
  database: Database;

  constructor(database: Database) {
    this.database = database;
  }

  static async create() {
    const sqlPromise = initSqlJs({
      locateFile: (file) => `${SQLJS_WASM_BASEURL}/${file}`,
    });
    const dataPromise = fetch(ROMDB_SQLITE_PATH).then((res) =>
      res.arrayBuffer()
    );
    const [SQL, buf] = await Promise.all([sqlPromise, dataPromise]);
    const database = new SQL.Database(new Uint8Array(buf));
    return new RomDatabase(database);
  }

  getRecipeIngredients(): string[] {
    const result = this.database.exec(GET_ALL_INGREDIENTS_QUERY);
    // @ts-ignore
    return result[0].values.map((value) => value[0]);
  }

  getMatchingCookingRecipes(items: string[]): CookingRecipe[] {
    const params = items.map((_) => "?").join(",");
    const result = this.database.exec(
      GET_MATCHING_RECIPE_IDS_QUERY(params),
      items.concat(items)
    );
    if (result.length === 0) {
      return [];
    }
    // @ts-ignore
    return result[0].values.map((value) => {
      const [recipeId, name, numStars] = value;
      // @ts-ignore
      const ingredients = this.getCookingRecipeIngredients(recipeId);
      return {
        name,
        numStars,
        ingredients,
      };
    });
  }

  getCookingRecipeIngredients(recipeId: number): string[] {
    const result = this.database.exec(GET_COOKING_RECIPE_INGREDIENTS_QUERY, [
      recipeId,
    ]);
    // @ts-ignore
    return result[0].values.map((value) => value[0]);
  }
}

export default RomDatabase;
