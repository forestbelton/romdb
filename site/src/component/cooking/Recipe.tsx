import { Badge, Card, Group, List, Text } from "@mantine/core";
import { CookingMethod, CookingRecipe } from "../../model";
import IngredientIcon from "./IngredientIcon";

const RECIPE_METHOD_NAMES: { [k in CookingMethod]: string } = {
  [CookingMethod.FRY]: "Sauté",
  [CookingMethod.GRILL]: "BBQ",
  [CookingMethod.BOIL]: "Braise",
  [CookingMethod.BEVERAGE]: "Sashimi",
};

const FULL_STAR = "★";
const HALF_STAR = "☆";

const recipeStars = (numStars: number) => {
  const fullStars = new Array(Math.floor(numStars / 2))
    .fill(FULL_STAR)
    .join("");
  const halfStars = new Array(numStars % 2).fill(HALF_STAR).join("");
  return `${fullStars}${halfStars}`;
};

const Recipe = ({ recipe }: { recipe: CookingRecipe }) => (
  <Card shadow="sm" radius="md" padding="xs" withBorder>
    <Group position="apart" mb="xs">
      <Text weight="bold">{recipe.name}</Text>
      <Group position="center">
        <Badge color="green" variant="light">
          {RECIPE_METHOD_NAMES[recipe.method]}
        </Badge>
        <Badge color="blue" variant="light">
          {recipeStars(recipe.numStars)}
        </Badge>
      </Group>
    </Group>
    <Group mt="sm" mb="sm">
      {recipe.ingredients.map((name, i) => (
        <IngredientIcon key={i} name={name} />
      ))}
    </Group>
  </Card>
);

export default Recipe;
