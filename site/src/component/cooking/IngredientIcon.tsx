import { Flex, Image, Tooltip } from "@mantine/core";
import React from "react";

const ICON_SIZE = 64;

const toImageName = (name: string | null) =>
  (name || "unknown").toLowerCase().replace(/ /g, "-") + ".png";

type IngredientIconProps = {
  name: string | null;
  style?: React.CSSProperties;
};

const IngredientIcon = ({ name, style = {} }: IngredientIconProps) => {
  const img = (
    <Image
      style={{
        width: 80,
      }}
      styles={{
        figure: {
          alignItems: "center",
          display: "flex",
          flexDirection: "column",
          height: "100%",
        },
        imageWrapper: {
          width: ICON_SIZE,
          height: ICON_SIZE,
        },
      }}
      src={`/romdb/img/icon/cooking/${toImageName(name)}`}
      alt={name || ""}
    />
  );
  return (
    <Flex justify="center" style={style}>
      {name !== null ? <Tooltip label={name}>{img}</Tooltip> : img}
    </Flex>
  );
};

export default IngredientIcon;
