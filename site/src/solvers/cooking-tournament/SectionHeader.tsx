const DEFAULT_SECTION_HEADER_STYLE = {
  display: "inline-block",
  fontSize: "1.5rem",
  fontWeight: "bold",
  marginBottom: "3rem",
};

const SectionHeader = ({
  children,
  style = {},
}: {
  children: React.ReactNode;
  style?: object;
}) => (
  <div style={{ ...DEFAULT_SECTION_HEADER_STYLE, ...style }}>{children}</div>
);

export default SectionHeader;
