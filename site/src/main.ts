import m from "mithril";

import "./style.css";
import { Element, Pet, PetView, Stat } from "./pet";

const pet: Pet = {
  name: "Poring",
  element: Element.WATER,
  skills: [],
  catchInfo: {
    itemName: "Green Apple",
    quantity: 3,
    unitPriceShells: 10,
  },
  hatchInfo: {
    adventureExp: 50,
    bonusStats: [{ name: Stat.MAGIC_DEFENSE, value: 1 }],
  },
};

const root = document.getElementById("app");
if (root !== null) {
  m.render(root, m(PetView, { pet }, []));
}
