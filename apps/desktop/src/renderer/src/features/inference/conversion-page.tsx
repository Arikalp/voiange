import { PageHeader } from "@/components/page-header";
import { ShellCard } from "@/components/shell-card";

export const ConversionPage = () => {
  return (
    <div className="space-y-8">
      <PageHeader
        eyebrow="Conversion"
        title="Run voice conversion jobs"
        description="Create inference-ready pipelines that combine separated vocals, RVC models, audio cleanup, and export formatting in one guided workspace."
        action={
          <button className="rounded-full border border-fuchsia-400/30 bg-fuchsia-400/10 px-5 py-3 text-sm font-medium text-fuchsia-100 transition hover:bg-fuchsia-400/20">
            New Conversion
          </button>
        }
      />

      <section className="grid gap-5 xl:grid-cols-[1.15fr_0.85fr]">
        <ShellCard title="Conversion pipeline" description="Sequenced local processing steps for a production-ready render flow.">
          <div className="space-y-4">
            {[
              ["1. Source selection", "Lead vocal stem from Project Aurora"],
              ["2. Model routing", "Asteria Lead v3 with pitch protect enabled"],
              ["3. Audio processing", "Noise cleanup, normalization, and loudness staging"],
              ["4. Export", "Merged stereo mix to WAV and MP3 deliverables"]
            ].map(([title, detail]) => (
              <div key={title} className="rounded-2xl border border-white/10 bg-white/[0.03] p-4">
                <p className="text-sm font-medium text-white">{title}</p>
                <p className="mt-2 text-sm text-slate-400">{detail}</p>
              </div>
            ))}
          </div>
        </ShellCard>

        <ShellCard title="Recent renders" description="Last outputs produced by the local inference queue.">
          <div className="space-y-3">
            {[
              ["Aurora Verse A", "Completed", "3m 21s"],
              ["Bridge Harmony Swap", "Queued", "Waiting"],
              ["Chorus Double Pass", "Rendering", "62%"]
            ].map(([name, status, duration]) => (
              <div key={name} className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-4">
                <div>
                  <p className="text-sm font-medium text-white">{name}</p>
                  <p className="mt-1 text-xs text-slate-400">{status}</p>
                </div>
                <span className="text-sm text-slate-300">{duration}</span>
              </div>
            ))}
          </div>
        </ShellCard>
      </section>
    </div>
  );
};
