const PLAYER_ITEM_SIZE = 5;
const INGREDIENT_POOL_SIZE = 12;

class TournamentState {
  playerIngredients: IngredientName[];
  mateIngredients: IngredientName[];
  ingredientPool: IngredientPoolItem[];

  constructor(
    playerIngredients: IngredientName[],
    mateIngredients: IngredientName[],
    ingredientPool: IngredientPoolItem[]
  ) {
    this.playerIngredients = playerIngredients;
    this.mateIngredients = mateIngredients;
    this.ingredientPool = ingredientPool;
  }

  static create() {
    return new TournamentState(
      new Array(PLAYER_ITEM_SIZE).fill(null),
      new Array(PLAYER_ITEM_SIZE).fill(null),
      new Array(INGREDIENT_POOL_SIZE).fill({
        ingredient: null,
        taken: false,
      })
    );
  }

  updatePlayerIngredient(index: number, name: IngredientName) {
    const { mateIngredients, ingredientPool } = this;
    const playerIngredients = [...this.playerIngredients];
    playerIngredients[index] = name;
    return new TournamentState(
      playerIngredients,
      mateIngredients,
      ingredientPool
    );
  }

  updateMateIngredient(index: number, name: IngredientName) {
    const { playerIngredients, ingredientPool } = this;
    const mateIngredients = [...this.mateIngredients];
    mateIngredients[index] = name;
    return new TournamentState(
      playerIngredients,
      mateIngredients,
      ingredientPool
    );
  }

  updateIngredientPool(
    index: number,
    ingredient: IngredientName,
    taken: boolean
  ) {
    const { mateIngredients, playerIngredients } = this;
    const ingredientPool = [...this.ingredientPool];
    ingredientPool[index] = { ingredient: ingredient, taken };
    return new TournamentState(
      playerIngredients,
      mateIngredients,
      ingredientPool
    );
  }

  getAvailableIngredients(): string[] {
    // @ts-ignore
    const poolIngredients: string[] = this.ingredientPool
      .filter(({ taken }) => !taken)
      .map(({ ingredient }) => ingredient)
      .filter((ingredient) => ingredient !== null);
    // @ts-ignore
    const playerIngredients: string[] = this.playerIngredients.filter(
      (ingredient) => ingredient !== null
    );
    return [...poolIngredients, ...playerIngredients];
  }
}

export default TournamentState;
