import type { ReactNode } from "react";

type ShellCardProps = {
  title: string;
  description?: string;
  children: ReactNode;
};

export const ShellCard = ({ title, description, children }: ShellCardProps) => {
  return (
    <section className="rounded-3xl border border-white/10 bg-slate-950/40 p-6 shadow-[0_20px_50px_rgba(2,6,23,0.35)] backdrop-blur">
      <div className="mb-5 space-y-1">
        <h2 className="text-lg font-medium text-white">{title}</h2>
        {description ? <p className="text-sm text-slate-400">{description}</p> : null}
      </div>
      {children}
    </section>
  );
};
