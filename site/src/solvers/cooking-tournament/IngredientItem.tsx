type IngredientItemProps = {
  ingredients: string[];
  onItemUpdate: (name: string) => void;
  name: string | null;
};

const IngredientItem = ({
  ingredients,
  name,
  onItemUpdate,
}: IngredientItemProps) => {
  return (
    <select
      style={{ width: "8rem", textAlign: "center" }}
      value={name || ""}
      onChange={(ev) => {
        ev.preventDefault();
        onItemUpdate(ev.target.value);
      }}
    >
      <option disabled value="">
        Select ingredient
      </option>
      {ingredients.map((opt, j) => (
        <option key={j} value={opt}>
          {opt}
        </option>
      ))}
    </select>
  );
};

export default IngredientItem;
