import { Route, Router, Switch } from "wouter";

import NavigationBar from "./component/NavigationBar";
import CookingTournamentPage from "./page/CookingTournamentPage";

const DEFAULT_PAGE = CookingTournamentPage;

const App = () => (
  <Router base="/romdb">
    <NavigationBar />
    <div style={{ padding: "1rem" }}>
      <Switch>
        <Route
          path="/tools/cooking-tournament"
          component={CookingTournamentPage}
        />
        <Route component={DEFAULT_PAGE} />
      </Switch>
    </div>
  </Router>
);

export default App;
