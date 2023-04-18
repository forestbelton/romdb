import m from "mithril";

export enum Stat {
  ATTACK = "ATTACK",
  MAGIC_ATTACK = "MAGIC_ATTACK",
  DEFENSE = "DEFENSE",
  MAGIC_DEFENSE = "MAGIC_DEFENSE",
  MAX_HP = "MAX_HP",
}

const STAT_NAMES: Record<Stat, string> = {
  ATTACK: "Atk",
  MAGIC_ATTACK: "M.Atk",
  DEFENSE: "Def",
  MAGIC_DEFENSE: "M.Def",
  MAX_HP: "Max HP",
};

export type StatValue = {
  name: Stat;
  value: number;
};

export enum Element {
  WIND = "WIND",
  EARTH = "EARTH",
  WATER = "WATER",
  FIRE = "FIRE",
  NEUTRAL = "NEUTRAL",
  HOLY = "HOLY",
  DARK = "DARK",
  GHOST = "GHOST",
  UNDEAD = "UNDEAD",
  POISON = "POISON",
}

export enum PetSkillType {
  ACTIVE,
  PASSIVE,
}

export type PetSkill = {
  name: string;
  type: PetSkillType;
  description: string;
};

export type PetHatchInfo = {
  adventureExp: number;
  bonusStats: StatValue[];
};

export type PetCatchInfo = {
  itemName: string;
  quantity: number;
  unitPriceShells: number;
};

// TODO: Add intimacy bonus information
export type Pet = {
  name: string;
  element: Element;
  skills: PetSkill[];
  catchInfo: PetCatchInfo;
  hatchInfo: PetHatchInfo;
};

export const PetCatchView: m.Component<{ catchInfo: PetCatchInfo }> = {
  view: (vnode) =>
    m(
      "div",
      m(
        "div",
        { class: "pet-info-field" },
        m("span", { class: "pet-info-label" }, "Catch Item:"),
        m(
          "span",
          `${vnode.attrs.catchInfo.itemName} (${vnode.attrs.catchInfo.quantity} for 100% chance)`
        )
      )
    ),
};

export const PetHatchView: m.Component<{ hatchInfo: PetHatchInfo }> = {
  view: (vnode) =>
    m(
      "div",
      m(
        "div",
        { class: "pet-info-field" },
        m("span", { class: "pet-info-label" }, "Hatch EXP:"),
        m("span", vnode.attrs.hatchInfo.adventureExp)
      ),
      m(
        "div",
        { class: "pet-info-field" },
        m("span", { class: "pet-info-label" }, "Hatch stats:"),
        m(
          "span",
          vnode.attrs.hatchInfo.bonusStats
            .map(({ name, value }) => `${STAT_NAMES[name]} +${value}`)
            .join(", ")
        )
      )
    ),
};

export const PetSkillsView: m.Component<{ skills: PetSkill[] }> = {
  view: (vnode) => null,
};

export const PetView: m.Component<{ pet: Pet }> = {
  view: (vnode) =>
    m(
      "div",
      m(
        "div",
        { class: "pet-info-field" },
        m("span", { class: "pet-info-label" }, "Name:"),
        m("span", vnode.attrs.pet.name)
      ),
      m(
        "div",
        { class: "pet-info-field" },
        m("span", { class: "pet-info-label" }, "Element:"),
        m("span", vnode.attrs.pet.element)
      ),
      m(PetCatchView, { catchInfo: vnode.attrs.pet.catchInfo }),
      m(PetHatchView, { hatchInfo: vnode.attrs.pet.hatchInfo }),
      m(PetSkillsView, { skills: vnode.attrs.pet.skills })
    ),
};
