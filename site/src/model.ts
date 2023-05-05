export enum CookingMethod {
  FRY = "FRY",
  GRILL = "GRILL",
  BOIL = "BOIL",
  BEVERAGE = "BEVERAGE",
};

export type CookingRecipe = {
  name: string;
  method: CookingMethod;
  numStars: number;
  ingredients: string[];
};
