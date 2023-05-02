import { useEffect, useState } from "react";

import CookingTournament from "../solvers/cooking-tournament/CookingTournament";
import RomDatabase from "../RomDatabase";

type LoadingState = {
  loading: true;
};

type LoadedState = {
  loading: false;
  database: RomDatabase;
  ingredients: string[];
};

type PageState = LoadingState | LoadedState;

const CookingTournamentPage = () => {
  const [state, setState] = useState<PageState>({ loading: true });
  useEffect(() => {
    if (!state.loading) {
      return;
    }
    (async () => {
      const database = await RomDatabase.create();
      const ingredients = await database.getRecipeIngredients();
      setState({
        loading: false,
        database,
        ingredients,
      });
    })();
  }, []);
  return state.loading ? (
    <span>Loading...</span>
  ) : (
    <CookingTournament
      ingredients={state.ingredients}
      database={state.database}
    />
  );
};

export default CookingTournamentPage;
