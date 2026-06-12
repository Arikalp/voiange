import { PageHeader } from "@/components/page-header";
import { ShellCard } from "@/components/shell-card";

const settingsSections = [
  {
    title: "Storage paths",
    items: ["Projects root", "Model cache", "Dataset library", "Temporary processing"]
  },
  {
    title: "Runtime controls",
    items: ["Python executable", "FFmpeg binary", "GPU queue policy", "Background worker cap"]
  },
  {
    title: "External access",
    items: ["Hugging Face token", "Gated model permissions", "Download concurrency", "Retry policy"]
  }
];

export const SettingsPage = () => {
  return (
    <div className="space-y-8">
      <PageHeader
        eyebrow="Settings"
        title="Desktop runtime configuration"
        description="Control local directories, Python runtime behavior, queue limits, and authentication for direct model downloads without exposing the renderer to system APIs."
      />

      <section className="grid gap-5 xl:grid-cols-3">
        {settingsSections.map((section) => (
          <ShellCard key={section.title} title={section.title} description="Recommended settings groups for the shell.">
            <div className="space-y-3">
              {section.items.map((item) => (
                <div key={item} className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                  <span className="text-sm text-slate-300">{item}</span>
                  <button className="rounded-full border border-white/10 px-3 py-1 text-xs text-slate-200 transition hover:border-teal-300/30 hover:text-white">
                    Configure
                  </button>
                </div>
              ))}
            </div>
          </ShellCard>
        ))}
      </section>
    </div>
  );
};
