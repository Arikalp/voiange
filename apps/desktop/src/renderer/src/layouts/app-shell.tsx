import { Outlet } from "react-router-dom";
import { AppLogo } from "@/components/app-logo";
import {
  ConversionIcon,
  DashboardIcon,
  ModelsIcon,
  SettingsIcon,
  TrainingIcon
} from "@/components/icons";
import { SidebarNav } from "@/components/sidebar-nav";
import type { NavigationItem } from "@/types/navigation";

const navigationItems: NavigationItem[] = [
  {
    label: "Dashboard",
    description: "Workspace overview and queue health",
    path: "/",
    icon: <DashboardIcon />
  },
  {
    label: "Models",
    description: "Registry, Hugging Face downloads, and storage",
    path: "/models",
    icon: <ModelsIcon />
  },
  {
    label: "Training",
    description: "Datasets, runs, checkpoints, and GPU usage",
    path: "/training",
    icon: <TrainingIcon />
  },
  {
    label: "Conversion",
    description: "Inference workflows and output delivery",
    path: "/conversion",
    icon: <ConversionIcon />
  },
  {
    label: "Settings",
    description: "Local paths, runtime, queue limits, and tokens",
    path: "/settings",
    icon: <SettingsIcon />
  }
];

export const AppShell = () => {
  return (
    <div className="min-h-screen bg-transparent px-5 py-5 text-slate-100">
      <div className="grid min-h-[calc(100vh-2.5rem)] grid-cols-1 gap-5 lg:grid-cols-[320px_minmax(0,1fr)]">
        <aside className="rounded-[32px] border border-white/10 bg-slate-950/70 p-6 shadow-[0_30px_60px_rgba(2,6,23,0.45)] backdrop-blur-xl">
          <div className="flex items-center gap-4 border-b border-white/10 pb-6">
            <AppLogo />
            <div>
              <p className="text-xs uppercase tracking-[0.35em] text-teal-300">VoiceAI Studio</p>
              <h1 className="mt-1 text-lg font-semibold text-white">Desktop Control Plane</h1>
            </div>
          </div>

          <div className="mt-6 space-y-6">
            <SidebarNav items={navigationItems} />

            <section className="rounded-3xl border border-white/10 bg-white/[0.03] p-4">
              <p className="text-xs uppercase tracking-[0.3em] text-slate-400">Runtime</p>
              <div className="mt-4 grid gap-3">
                <div className="rounded-2xl border border-white/10 bg-slate-900/70 p-3">
                  <p className="text-sm font-medium text-white">Python backend</p>
                  <p className="mt-1 text-xs text-slate-400">Ready for local RPC orchestration</p>
                </div>
                <div className="rounded-2xl border border-white/10 bg-slate-900/70 p-3">
                  <p className="text-sm font-medium text-white">Download queue</p>
                  <p className="mt-1 text-xs text-slate-400">Concurrent model pulls with retry handling</p>
                </div>
              </div>
            </section>
          </div>
        </aside>

        <main className="rounded-[32px] border border-white/10 bg-slate-900/55 p-6 shadow-[0_30px_60px_rgba(2,6,23,0.35)] backdrop-blur-xl">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
