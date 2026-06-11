type EmptyStateProps = {
  title: string;
  description: string;
};

export function EmptyState({ title, description }: EmptyStateProps) {
  return (
    <div className="rounded-[1.1rem] border border-dashed border-[#eacfc4] bg-white/52 px-6 py-10 text-center text-[#8a7066]">
      <p className="text-sm font-semibold text-[#5b4841]">{title}</p>
      <p className="mt-2 text-sm leading-6">{description}</p>
    </div>
  );
}
