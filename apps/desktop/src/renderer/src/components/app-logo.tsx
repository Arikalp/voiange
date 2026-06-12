export const AppLogo = () => {
  return (
    <div className="relative flex h-12 w-12 items-center justify-center overflow-hidden rounded-2xl border border-white/10 bg-slate-900 shadow-[0_18px_40px_rgba(8,15,33,0.45)]">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(45,212,191,0.45),_transparent_60%)]" />
      <div className="absolute inset-x-3 top-3 h-1 rounded-full bg-amber-300/70" />
      <div className="absolute inset-y-3 left-4 w-1 rounded-full bg-teal-300/80" />
      <div className="absolute inset-y-3 right-4 w-1 rounded-full bg-cyan-400/80" />
      <span className="relative text-sm font-semibold tracking-[0.25em] text-white">VA</span>
    </div>
  );
};
