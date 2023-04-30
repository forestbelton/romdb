import IngredientItem from "./IngredientItem";

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
  <div
    style={{
      boxSizing: "border-box",
      display: "grid",
      gridGap: "2rem 1rem",
      gridTemplateColumns: "repeat(4, 1fr)",
    }}
  >
    {items.map(({ ingredient, taken }, i) => (
      <div
        key={i}
        style={{
          display: "inline-flex",
        }}
      >
        <input
          type="checkbox"
          checked={taken}
          onChange={(ev) => {
            onPoolUpdate(i, ingredient, ev.target.checked);
          }}
        />
        <IngredientItem
          ingredients={ingredients}
          name={ingredient}
          onItemUpdate={(name) => onPoolUpdate(i, name, taken)}
        />
      </div>
    ))}
  </div>
);

export default IngredientPool;
