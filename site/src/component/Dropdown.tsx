import React from "react";

import "./Dropdown.css";

type DropdownProps = {
  title: string;
  children: any;
  style?: React.CSSProperties;
  titleStyle?: React.CSSProperties;
  contentStyle?: React.CSSProperties;
};

const Dropdown = ({
  title,
  children,
  style = {},
  titleStyle = {},
  contentStyle = {},
}: DropdownProps) => (
  <div className="Dropdown" style={style}>
    <span className="Dropdown-Title" style={titleStyle}>
      {title}
    </span>
    <div className="Dropdown-Content" style={contentStyle}>
      {children}
    </div>
  </div>
);

export default Dropdown;
