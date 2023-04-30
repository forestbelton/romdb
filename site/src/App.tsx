import { useEffect, useState } from "react";
import CookingTournament from "./solvers/cooking-tournament/CookingTournament";
import RomDatabase from "./RomDatabase";

type AppState = {
  database: RomDatabase;
  ingredients: string[];
};

function App() {
  const [state, setState] = useState<AppState | null>(null);
  useEffect(() => {
    if (state !== null) {
      return;
    }
    (async () => {
      const database = await RomDatabase.create();
      const ingredients = await database.getRecipeIngredients();
      setState({
        database,
        ingredients,
      });
    })();
  }, []);
  return state === null ? (
    <span>Loading...</span>
  ) : (
    <CookingTournament
      ingredients={state.ingredients}
      database={state.database}
    />
  );
}

export default App;
