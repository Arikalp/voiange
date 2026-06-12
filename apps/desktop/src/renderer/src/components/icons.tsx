import type { SVGProps } from "react";

type IconProps = SVGProps<SVGSVGElement>;

const baseProps = {
  fill: "none",
  stroke: "currentColor",
  strokeLinecap: "round",
  strokeLinejoin: "round",
  strokeWidth: 1.8,
  viewBox: "0 0 24 24"
} satisfies IconProps;

export const DashboardIcon = (props: IconProps) => (
  <svg {...baseProps} {...props}>
    <path d="M4 13h7V4H4z" />
    <path d="M13 20h7v-9h-7z" />
    <path d="M13 10h7V4h-7z" />
    <path d="M4 20h7v-5H4z" />
  </svg>
);

export const ModelsIcon = (props: IconProps) => (
  <svg {...baseProps} {...props}>
    <path d="M12 3 4 7v10l8 4 8-4V7z" />
    <path d="m4 7 8 4 8-4" />
    <path d="v10" />
  </svg>
);

export const TrainingIcon = (props: IconProps) => (
  <svg {...baseProps} {...props}>
    <path d="M4 20h16" />
    <path d="M7 16V9" />
    <path d="M12 16V4" />
    <path d="M17 16v-6" />
  </svg>
);

export const ConversionIcon = (props: IconProps) => (
  <svg {...baseProps} {...props}>
    <path d="M7 7h10" />
    <path d="m13 3 4 4-4 4" />
    <path d="M17 17H7" />
    <path d="m11 21-4-4 4-4" />
  </svg>
);

export const SettingsIcon = (props: IconProps) => (
  <svg {...baseProps} {...props}>
    <path d="M12 15.5A3.5 3.5 0 1 0 12 8.5a3.5 3.5 0 0 0 0 7Z" />
    <path d="M19.4 15a1.7 1.7 0 0 0 .34 1.87l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.7 1.7 0 0 0-1.87-.34 1.7 1.7 0 0 0-1.04 1.55V21a2 2 0 1 1-4 0v-.09A1.7 1.7 0 0 0 8.96 19.4a1.7 1.7 0 0 0-1.87.34l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.7 1.7 0 0 0 4.6 15a1.7 1.7 0 0 0-1.55-1.04H3a2 2 0 1 1 0-4h.09A1.7 1.7 0 0 0 4.6 8.96a1.7 1.7 0 0 0-.34-1.87l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.7 1.7 0 0 0 8.96 4.6a1.7 1.7 0 0 0 1.04-1.55V3a2 2 0 1 1 4 0v.09A1.7 1.7 0 0 0 15.04 4.6a1.7 1.7 0 0 0 1.87-.34l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.7 1.7 0 0 0 19.4 8.96c.66.27 1.1.91 1.1 1.62V11a2 2 0 1 1 0 2v.42c0 .71-.44 1.35-1.1 1.58Z" />
  </svg>
);
