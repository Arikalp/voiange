import { PageHeader } from "@/components/page-header";
import { ShellCard } from "@/components/shell-card";

const modelRows = [
  {
    name: "Asteria Lead v3",
    family: "RVC",
    source: "Hugging Face",
    status: "Ready",
    footprint: "2.3 GB"
  },
  {
    name: "Demucs Hybrid HQ",
    family: "Demucs",
    source: "Bundled",
    status: "Ready",
    footprint: "1.1 GB"
  },
  {
    name: "Studio Alto v2",
    family: "RVC",
    source: "Local training",
    status: "Indexing",
    footprint: "890 MB"
  }
];

export const ModelsPage = () => {
  return (
    <div className="space-y-8">
      <PageHeader
        eyebrow="Models"
        title="Local model registry"
        description="Manage downloaded Hugging Face assets, trained voice models, separation models, and compatibility metadata from one place."
        action={
          <button className="rounded-full border border-amber-300/30 bg-amber-300/10 px-5 py-3 text-sm font-medium text-amber-100 transition hover:bg-amber-300/20">
            Download Model
          </button>
        }
      />

      <section className="grid gap-5 xl:grid-cols-[1.1fr_0.9fr]">
        <ShellCard title="Registry inventory" description="Storage-aware model catalog with source and readiness state.">
          <div className="overflow-hidden rounded-3xl border border-white/10">
            <table className="min-w-full divide-y divide-white/10 text-left text-sm">
              <thead className="bg-white/[0.04] text-slate-400">
                <tr>
                  <th className="px-4 py-3 font-medium">Model</th>
                  <th className="px-4 py-3 font-medium">Family</th>
                  <th className="px-4 py-3 font-medium">Source</th>
                  <th className="px-4 py-3 font-medium">Status</th>
                  <th className="px-4 py-3 font-medium">Size</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/10">
                {modelRows.map((row) => (
                  <tr key={row.name} className="bg-slate-950/20">
                    <td className="px-4 py-4 text-white">{row.name}</td>
                    <td className="px-4 py-4 text-slate-300">{row.family}</td>
                    <td className="px-4 py-4 text-slate-300">{row.source}</td>
                    <td className="px-4 py-4">
                      <span className="rounded-full border border-teal-400/30 bg-teal-400/10 px-3 py-1 text-xs text-teal-200">
                        {row.status}
                      </span>
                    </td>
                    <td className="px-4 py-4 text-slate-300">{row.footprint}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </ShellCard>

        <ShellCard title="Download queue" description="Concurrent transfer slots with resumable model fetches.">
          <div className="space-y-4">
            {[
              ["rvc/broadcast-voice-pack", "Downloading", "74%"],
              ["demucs/htdemucs_ft", "Queued", "Waiting"],
              ["rvc/choral-index-pack", "Verifying", "Checksum"]
            ].map(([name, status, progress]) => (
              <article key={name} className="rounded-2xl border border-white/10 bg-white/[0.03] p-4">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="text-sm font-medium text-white">{name}</p>
                    <p className="mt-1 text-xs text-slate-400">{status}</p>
                  </div>
                  <span className="text-sm text-slate-300">{progress}</span>
                </div>
                <div className="mt-3 h-2 rounded-full bg-slate-800">
                  <div className="h-2 w-3/4 rounded-full bg-gradient-to-r from-amber-300 via-orange-300 to-teal-300" />
                </div>
              </article>
            ))}
          </div>
        </ShellCard>
      </section>
    </div>
  );
};
