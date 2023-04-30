import IngredientItem from "./IngredientItem";
import SectionHeader from "./SectionHeader";

type ItemSetProps = {
  headerTitle: string;
  ingredients: string[];
  items: IngredientName[];
  onItemUpdate: (index: number, name: IngredientName) => void;
};

const ItemSet = ({
  headerTitle,
  ingredients,
  items,
  onItemUpdate,
}: ItemSetProps) => (
  <div
    style={{
      display: "inline-flex",
      flexDirection: "column",
      padding: "0 1rem",
    }}
  >
    <SectionHeader>{headerTitle}</SectionHeader>
    <div
      style={{
        display: "grid",
        gridGap: "2rem 1rem",
        gridTemplateColumns: "repeat(4, 1fr)",
        justifyContent: "space-evently",
      }}
    >
      {items.map((item, i) => (
        <div
          key={i}
          style={{
            gridColumn:
              i === items.length - 1 && items.length % 2 == 1
                ? "2 / span 2"
                : "span 2",
          }}
        >
          <IngredientItem
            ingredients={ingredients}
            name={item}
            onItemUpdate={(name) => onItemUpdate(i, name)}
          />
        </div>
      ))}
    </div>
  </div>
);

export default ItemSet;
