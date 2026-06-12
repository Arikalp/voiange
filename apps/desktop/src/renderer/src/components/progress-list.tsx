type ProgressItem = {
  label: string;
  detail: string;
  value: number;
};

type ProgressListProps = {
  items: ProgressItem[];
};

export const ProgressList = ({ items }: ProgressListProps) => {
  return (
    <div className="space-y-4">
      {items.map((item) => (
        <div key={item.label} className="space-y-2">
          <div className="flex items-center justify-between gap-4">
            <div>
              <p className="text-sm font-medium text-white">{item.label}</p>
              <p className="text-xs text-slate-400">{item.detail}</p>
            </div>
            <span className="text-sm text-slate-300">{item.value}%</span>
          </div>
          <div className="h-2 rounded-full bg-slate-800">
            <div
              className="h-2 rounded-full bg-gradient-to-r from-teal-400 via-cyan-400 to-amber-300"
              style={{ width: `${item.value}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
};
