import React, { useState } from "react";
import { Button, Flex, Group, Title } from "@mantine/core";

import TournamentState from "./TournamentState";
import IngredientPool from "./IngredientPool";
import ItemSet from "./ItemSet";
import RomDatabase from "../../RomDatabase";
import Recipe from "../../component/cooking/Recipe";

type CookingTournamentProps = {
  ingredients: string[];
  database: RomDatabase;
};

const CookingTournament = ({
  ingredients,
  database,
}: CookingTournamentProps) => {
  const [state, setState] = useState(TournamentState.create);
  const onPoolUpdate = (
    index: number,
    ingredient: IngredientName,
    taken: boolean
  ) => {
    setState(state.updateIngredientPool(index, ingredient, taken));
  };
  const onMateItemUpdate = (index: number, name: IngredientName) => {
    setState(state.updateMateIngredient(index, name));
  };
  const onPlayerItemUpdate = (index: number, name: IngredientName) => {
    setState(state.updatePlayerIngredient(index, name));
  };
  const resetState = (ev: React.MouseEvent<HTMLButtonElement>) => {
    ev.preventDefault();
    setState(TournamentState.create);
  };
  const availableIngredients = state.getAvailableIngredients();
  const bestRecipes = database.getMatchingCookingRecipes(availableIngredients);
  return (
    <div>
      <Group spacing="xl" mb="lg">
        <Title order={2}>Cooking Tournament</Title>
        <Button size="xs" onClick={resetState}>
          Reset
        </Button>
      </Group>
      <Flex>
        <ItemSet
          headerTitle="Player Items"
          items={state.playerIngredients}
          onItemUpdate={onPlayerItemUpdate}
        />
        <div>
          <Title order={3} mb="lg" align="center">
            Ingredient Pool
          </Title>
          <IngredientPool
            ingredients={ingredients}
            items={state.ingredientPool}
            onPoolUpdate={onPoolUpdate}
          />
          <Title order={3} mb="lg" mt="lg">
            Best Recipes
          </Title>
          <Flex direction="column" gap="lg">
            {bestRecipes.map((recipe, i) => (
              <Recipe key={i} recipe={recipe} />
            ))}
          </Flex>
        </div>
        <ItemSet
          headerTitle="Muctung Items"
          items={state.mateIngredients}
          onItemUpdate={onMateItemUpdate}
        />
      </Flex>
    </div>
  );
};

export default CookingTournament;
