import { NavLink } from "react-router-dom";
import { cn } from "@/lib/cn";
import type { NavigationItem } from "@/types/navigation";

type SidebarNavProps = {
  items: NavigationItem[];
};

export const SidebarNav = ({ items }: SidebarNavProps) => {
  return (
    <nav className="space-y-2">
      {items.map((item) => (
        <NavLink
          key={item.path}
          to={item.path}
          className={({ isActive }) =>
            cn(
              "group flex items-center gap-4 rounded-2xl border px-4 py-3 transition-all duration-200",
              isActive
                ? "border-teal-400/40 bg-teal-400/10 text-white shadow-[0_18px_30px_rgba(20,184,166,0.12)]"
                : "border-white/5 bg-white/[0.03] text-slate-300 hover:border-white/10 hover:bg-white/[0.06] hover:text-white"
            )
          }
        >
          <span className="flex h-11 w-11 items-center justify-center rounded-xl border border-white/10 bg-slate-950/60 text-slate-200">
            <span className="h-5 w-5">{item.icon}</span>
          </span>
          <span className="min-w-0">
            <span className="block text-sm font-medium">{item.label}</span>
            <span className="block truncate text-xs text-slate-400">{item.description}</span>
          </span>
        </NavLink>
      ))}
    </nav>
  );
};
