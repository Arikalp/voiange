import { PageHeader } from "@/components/page-header";
import { ProgressList } from "@/components/progress-list";
import { ShellCard } from "@/components/shell-card";

const stages = [
  { label: "Dataset validation", detail: "Clip integrity, duration, silence detection", value: 100 },
  { label: "Feature extraction", detail: "GPU worker 0 processing mel and pitch features", value: 58 },
  { label: "Checkpoint training", detail: "Epoch 96 / 220 with autosave every 20 epochs", value: 43 }
];

export const TrainingPage = () => {
  return (
    <div className="space-y-8">
      <PageHeader
        eyebrow="Training"
        title="Train local voice models"
        description="Launch and monitor dataset preprocessing, feature extraction, checkpointing, and final model registration without leaving the desktop app."
        action={
          <button className="rounded-full border border-cyan-400/30 bg-cyan-400/10 px-5 py-3 text-sm font-medium text-cyan-100 transition hover:bg-cyan-400/20">
            Start Training Run
          </button>
        }
      />

      <section className="grid gap-5 xl:grid-cols-[1fr_1fr]">
        <ShellCard title="Active run" description="Current training progress with stage-by-stage breakdown.">
          <ProgressList items={stages} />
        </ShellCard>

        <ShellCard title="Run configuration" description="Recommended controls for production-grade local runs.">
          <div className="grid gap-3 sm:grid-cols-2">
            {[
              ["Dataset", "Studio Alto Cleanroom"],
              ["Target epochs", "220"],
              ["Batch size", "8"],
              ["Checkpoint cadence", "Every 20 epochs"],
              ["GPU strategy", "Single exclusive worker"],
              ["Output path", "models/trained/studio-alto-v2"]
            ].map(([label, value]) => (
              <div key={label} className="rounded-2xl border border-white/10 bg-white/[0.03] p-4">
                <p className="text-xs uppercase tracking-[0.25em] text-slate-400">{label}</p>
                <p className="mt-2 text-sm font-medium text-white">{value}</p>
              </div>
            ))}
          </div>
        </ShellCard>
      </section>
    </div>
  );
};
