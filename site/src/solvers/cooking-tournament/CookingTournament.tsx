import React, { useState } from "react";
import SectionHeader from "./SectionHeader";
import TournamentState from "./TournamentState";
import IngredientPool from "./IngredientPool";
import ItemSet from "./ItemSet";
import RomDatabase from "../../RomDatabase";
import RecipeItem from "./RecipeItem";

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
      <div style={{ fontSize: "2rem", fontWeight: "bold" }}>
        Cooking Tournament
      </div>
      <div style={{ margin: "1rem 0", textAlign: "left" }}>
        <button onClick={resetState}>Reset</button>
      </div>
      <div
        style={{
          display: "flex",
        }}
      >
        <ItemSet
          headerTitle="Player Items"
          ingredients={ingredients}
          items={state.playerIngredients}
          onItemUpdate={onPlayerItemUpdate}
        />
        <div
          style={{
            boxSizing: "border-box",
            padding: "0 1rem",
            border: "2px solid rgba(255,255,255,0.87)",
            borderBottom: "0",
            borderTop: "0",
          }}
        >
          <SectionHeader>Ingredient Pool</SectionHeader>
          <IngredientPool
            ingredients={ingredients}
            items={state.ingredientPool}
            onPoolUpdate={onPoolUpdate}
          />
          <SectionHeader style={{ marginBottom: "2rem", marginTop: "2rem" }}>
            Best Recipes
          </SectionHeader>
          <div style={{ textAlign: "left" }}>
            {bestRecipes.map((recipe, i) => (
              <div key={i} style={{ marginBottom: "2rem" }}>
                <RecipeItem recipe={recipe} />
              </div>
            ))}
          </div>
        </div>
        <ItemSet
          headerTitle="Muctung Items"
          ingredients={ingredients}
          items={state.mateIngredients}
          onItemUpdate={onMateItemUpdate}
        />
      </div>
    </div>
  );
};

export default CookingTournament;
