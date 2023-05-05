import { Flex, Menu } from "@mantine/core";

import IngredientIcon from "../../component/cooking/IngredientIcon";

type IngredientPickerProps = {
  ingredients: string[];
  name: string | null;
  disabled?: boolean;
  onChange: (name: string) => void;
};

const IngredientPicker = ({
  ingredients,
  name,
  onChange,
}: IngredientPickerProps) => (
  <Flex direction="column" align="center">
    <Menu>
      <Menu.Target>
        <div>
          <IngredientIcon name={name} style={{ cursor: "pointer" }} />
        </div>
      </Menu.Target>
      <Menu.Dropdown style={{ overflowY: "scroll", maxHeight: 200 }}>
        {ingredients.map((ing, i) => (
          <Menu.Item key={i} onClick={() => onChange(ing)}>
            <IngredientIcon name={ing} />
          </Menu.Item>
        ))}
      </Menu.Dropdown>
    </Menu>
  </Flex>
);

export default IngredientPicker;
