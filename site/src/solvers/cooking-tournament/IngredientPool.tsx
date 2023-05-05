import { SimpleGrid } from "@mantine/core";

import IngredientPicker from "./IngredientPicker";

type IngredientPoolProps = {
  ingredients: string[];
  items: IngredientPoolItem[];
  onPoolUpdate: (
    itemIndex: number,
    name: string | null,
    taken: boolean
  ) => void;
};

const IngredientPool = ({
  ingredients,
  items,
  onPoolUpdate,
}: IngredientPoolProps) => (
  <SimpleGrid cols={4} spacing="xs" verticalSpacing="xs" ml="xl" mr="xl">
    {items.map(({ ingredient, taken }, i) => (
      <div key={i}>
        <IngredientPicker
          ingredients={ingredients}
          name={ingredient}
          onChange={(name) => onPoolUpdate(i, name, taken)}
        />
      </div>
    ))}
  </SimpleGrid>
);

export default IngredientPool;
