import { CookingRecipe } from "../../model";

const FULL_STAR = "★";
const HALF_STAR = "☆";

const recipeStars = (numStars: number) => {
  const fullStars = new Array(Math.floor(numStars / 2))
    .fill(FULL_STAR)
    .join("");
  const halfStars = new Array(numStars % 2).fill(HALF_STAR).join("");
  return `${fullStars}${halfStars}`;
};

const RecipeItem = ({ recipe }: { recipe: CookingRecipe }) => (
  <div>
    <strong>{recipe.name}</strong>
    <span style={{ marginLeft: "0.5rem" }}>
      ({recipeStars(recipe.numStars)})
    </span>
    <div
      style={{
        paddingLeft: "0.5rem",
      }}
    >
      <div style={{ fontWeight: "bold", marginTop: "0.5rem" }}>Ingredients</div>
      <ul
        style={{
          listStyleType: "none",
          margin: "0 0 0 1rem",
          padding: "0",
        }}
      >
        {recipe.ingredients.map((name: string, i: number) => (
          <li key={i}>{name}</li>
        ))}
      </ul>
    </div>
  </div>
);

export default RecipeItem;
