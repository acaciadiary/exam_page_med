import clsx from "clsx";
import { useHorizontalDragScroll } from "../hooks/useHorizontalDragScroll";
import type { CategoryOption } from "../lib/categoryFilters";

type CategoryFilterProps = {
  options: CategoryOption[];
  activeCategory: string;
  onChange: (category: string) => void;
};

export function CategoryFilter({
  options,
  activeCategory,
  onChange,
}: CategoryFilterProps) {
  const dragScrollProps = useHorizontalDragScroll();
  const hasAssignedCategory = options.some(
    (option) =>
      option.id !== "__all__" &&
      option.id !== "__uncategorized__" &&
      option.count > 0,
  );

  return (
    <div className="font-hand mb-6 rounded-[1.2rem] border border-white/80 bg-white/68 p-3 shadow-[0_14px_42px_rgba(181,133,117,0.12)] backdrop-blur-2xl">
      <div
        {...dragScrollProps}
        className="horizontal-drag-scroll flex gap-2 pb-1"
        aria-label="科目可左右滑動"
      >
        {options.map((option) => (
          <button
            key={option.id}
            type="button"
            disabled={option.disabled}
            onPointerDown={(event) => event.stopPropagation()}
            onClick={() => onChange(option.id)}
            className={clsx(
              "shrink-0 rounded-full px-4 py-2 text-sm font-semibold transition",
              activeCategory === option.id
                ? "bg-[#b8e2d4] text-[#355249] shadow-[0_8px_22px_rgba(123,190,168,0.28)]"
                : "bg-white/70 text-[#7d6259] hover:bg-[#fff3f8] hover:text-[#4b3b35]",
              option.disabled &&
                "cursor-not-allowed opacity-45 hover:bg-white/70 hover:text-[#7d6259]",
            )}
          >
            {option.label}
            <span className="ml-2 text-xs opacity-70">{option.count}</span>
          </button>
        ))}
      </div>

      {!hasAssignedCategory && (
        <p className="mt-2 px-2 text-xs leading-5 text-[#8a7066]">
          已建立科目按鈕，但目前國考題還沒有題號區間對應，所以題目暫時集中在「未分類」。提供每科題號範圍後即可批次回填。
        </p>
      )}
    </div>
  );
}
