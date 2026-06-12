import type { ReactNode } from "react";

export type NavigationItem = {
  label: string;
  description: string;
  path: string;
  icon: ReactNode;
};
