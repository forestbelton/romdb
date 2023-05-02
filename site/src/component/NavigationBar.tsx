import { CSSProperties } from "react";
import { Link } from "wouter";

import Dropdown from "./Dropdown";

const NAVIGATION_BAR_STYLE: CSSProperties = {
  borderBottom: "1px solid rgba(255, 255, 255, 0.87)",
  boxSizing: "border-box",
  padding: "1rem",
  width: "100%",
};

const NavigationBar = () => (
  <header style={NAVIGATION_BAR_STYLE}>
    <h1 style={{ margin: 0 }}>
      <Link href="/" style={{ fontWeight: "bold", marginRight: "2rem" }}>
        ROMDB
      </Link>
      <Dropdown
        title="Database"
        contentStyle={{ fontSize: "0.75em" }}
        style={{ marginRight: "3rem" }}
      >
        <Link href="/database/items">Items</Link>
        <Link href="/database/monsters">Monsters</Link>
      </Dropdown>
      <Dropdown title="Tools" contentStyle={{ fontSize: "0.75em" }}>
        <Link href="/tools/cooking-tournament">Cooking Tournament</Link>
      </Dropdown>
    </h1>
  </header>
);

export default NavigationBar;
