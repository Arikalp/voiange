import type { ReactNode } from "react";

type PageHeaderProps = {
  eyebrow: string;
  title: string;
  description: string;
  action?: ReactNode;
};

export const PageHeader = ({ eyebrow, title, description, action }: PageHeaderProps) => {
  return (
    <header className="flex flex-col gap-4 border-b border-white/10 pb-6 lg:flex-row lg:items-end lg:justify-between">
      <div className="space-y-3">
        <p className="text-xs uppercase tracking-[0.35em] text-teal-300">{eyebrow}</p>
        <div className="space-y-2">
          <h1 className="text-3xl font-semibold text-white">{title}</h1>
          <p className="max-w-3xl text-sm leading-6 text-slate-400">{description}</p>
        </div>
      </div>
      {action ? <div className="shrink-0">{action}</div> : null}
    </header>
  );
};
