type StatusBadgeProps = {
  label: string;
};

export const StatusBadge = ({ label }: StatusBadgeProps) => {
  return (
    <span className="inline-flex rounded-full border border-slate-700 px-3 py-1 text-xs text-slate-300">
      {label}
    </span>
  );
};
