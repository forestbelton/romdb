import { SimpleGrid, Title } from "@mantine/core";
import IngredientIcon from "../../component/cooking/IngredientIcon";

type ItemSetProps = {
  headerTitle: string;
  items: IngredientName[];
  onItemUpdate: (index: number, name: IngredientName) => void;
};

const ItemSet = ({ headerTitle, items }: ItemSetProps) => (
  <div
    style={{
      display: "inline-flex",
      flexDirection: "column",
      padding: "0 1rem",
    }}
  >
    <Title order={3} mb="lg" align="center">
      {headerTitle}
    </Title>
    <SimpleGrid cols={2} spacing="xs" verticalSpacing="xs">
      {items.map((name, i) => (
        <IngredientIcon
          key={i}
          name={name}
          style={{
            marginRight:
              i === items.length - 1 && items.length % 2 === 1 ? -88 : "auto",
          }}
        />
      ))}
    </SimpleGrid>
  </div>
);

export default ItemSet;
