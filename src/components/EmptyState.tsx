type EmptyStateProps = {
  title: string;
  description: string;
};

export function EmptyState({ title, description }: EmptyStateProps) {
  return (
    <div className="rounded-[1.1rem] border border-dashed border-[#eacfc4] bg-white/52 px-6 py-10 text-center text-[#8a7066] dark:border-white/14 dark:bg-[#241e2a]/72 dark:text-[#cbb8c2]">
      <p className="text-sm font-semibold text-[#5b4841] dark:text-[#f8edf3]">{title}</p>
      <p className="mt-2 text-sm leading-6">{description}</p>
    </div>
  );
}
