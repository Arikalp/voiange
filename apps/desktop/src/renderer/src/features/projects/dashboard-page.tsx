import { PageHeader } from "@/components/page-header";
import { ProgressList } from "@/components/progress-list";
import { ShellCard } from "@/components/shell-card";
import { StatCard } from "@/components/stat-card";

const queueItems = [
  { label: "Model sync queue", detail: "2 active downloads from Hugging Face", value: 68 },
  { label: "Training queue", detail: "Feature extraction running on RTX 4070", value: 41 },
  { label: "Conversion queue", detail: "One pending render for chorus take", value: 84 }
];

export const DashboardPage = () => {
  return (
    <div className="space-y-8">
      <PageHeader
        eyebrow="Overview"
        title="VoiceAI Studio control center"
        description="Monitor the full local workflow across downloads, datasets, training, inference, and export jobs from one desktop shell."
        action={
          <button className="rounded-full border border-teal-400/30 bg-teal-400/10 px-5 py-3 text-sm font-medium text-teal-100 transition hover:bg-teal-400/20">
            New Project
          </button>
        }
      />

      <section className="grid gap-4 xl:grid-cols-4">
        <StatCard label="Projects" value="12" detail="3 active sessions with recent outputs" />
        <StatCard label="Models" value="28" detail="19 downloaded, 9 trained locally" />
        <StatCard label="Datasets" value="41h" detail="Validated speech material across 8 collections" />
        <StatCard label="GPU Load" value="74%" detail="Healthy throughput with one training worker" />
      </section>

      <section className="grid gap-5 xl:grid-cols-[1.35fr_0.95fr]">
        <ShellCard
          title="Live pipeline status"
          description="All long-running tasks are treated as queue-backed jobs with persisted progress."
        >
          <ProgressList items={queueItems} />
        </ShellCard>

        <ShellCard title="System readiness" description="Local runtime state for the desktop shell.">
          <div className="grid gap-3">
            {[
              ["Python RPC", "Connected"],
              ["SQLite metadata", "Healthy"],
              ["FFmpeg binary", "Bundled"],
              ["GPU acceleration", "CUDA available"]
            ].map(([label, status]) => (
              <div key={label} className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                <span className="text-sm text-slate-300">{label}</span>
                <span className="rounded-full border border-emerald-400/30 bg-emerald-400/10 px-3 py-1 text-xs text-emerald-200">
                  {status}
                </span>
              </div>
            ))}
          </div>
        </ShellCard>
      </section>
    </div>
  );
};
