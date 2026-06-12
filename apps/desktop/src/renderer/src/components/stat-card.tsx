type StatCardProps = {
  label: string;
  value: string;
  detail: string;
};

export const StatCard = ({ label, value, detail }: StatCardProps) => {
  return (
    <article className="rounded-3xl border border-white/10 bg-white/[0.03] p-5">
      <p className="text-xs uppercase tracking-[0.25em] text-slate-400">{label}</p>
      <p className="mt-3 text-3xl font-semibold text-white">{value}</p>
      <p className="mt-2 text-sm text-slate-400">{detail}</p>
    </article>
  );
};
