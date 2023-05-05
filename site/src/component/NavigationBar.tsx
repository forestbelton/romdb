import { Link } from "wouter";
import { Anchor, Group, Menu, Title } from "@mantine/core";

const NavigationBar = () => (
  <Group spacing="xl" ml="md">
    <Title order={1} weight="bold">
      ROMDB
    </Title>
    <Anchor component={Link} href="/" size="1.625rem" weight="bold">
      Search
    </Anchor>
    <Menu shadow="md" trigger="hover">
      <Menu.Target>
        <Title order={2} style={{ cursor: "pointer" }}>
          Tools
        </Title>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Label>Cloudsea Archipelago</Menu.Label>
        <Menu.Item>
          <Anchor component={Link} href="/tools/cooking-tournament">
            Cooking Tournament
          </Anchor>
        </Menu.Item>
      </Menu.Dropdown>
    </Menu>
  </Group>
);

export default NavigationBar;
