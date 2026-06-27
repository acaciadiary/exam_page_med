import { Moon, Stethoscope, Sun } from "lucide-react";
import clsx from "clsx";
import type { ReactNode } from "react";

export type AppTheme = "light" | "clinical" | "dark";

type ThemeToggleProps = {
  theme: AppTheme;
  onChange: (theme: AppTheme) => void;
  compact?: boolean;
};

const options: Array<{ value: AppTheme; label: string; icon: ReactNode }> = [
  { value: "light", label: "質感粉", icon: <Sun size={15} /> },
  { value: "clinical", label: "專業藍", icon: <Stethoscope size={15} /> },
  { value: "dark", label: "深夜黑", icon: <Moon size={15} /> },
];

export function ThemeToggle({ theme, onChange, compact = false }: ThemeToggleProps) {
  return (
    <div
      className={clsx(
        "inline-flex rounded-full border border-[#e6d6c9] bg-white/80 p-1 theme-control",
        compact ? "h-10 min-w-0 flex-1" : "h-11",
      )}
    >
      {options.map((option) => (
        <button
          key={option.value}
          type="button"
          onClick={() => onChange(option.value)}
          className={clsx(
            "inline-flex items-center justify-center rounded-full font-semibold transition",
            compact
              ? "h-8 min-w-0 flex-1 gap-1 px-2 text-[10px] leading-none"
              : "min-h-9 min-w-9 gap-1.5 px-3 text-xs",
            theme === option.value
              ? "bg-[#ffddea] text-[#9a496b] shadow-[0_8px_18px_rgba(181,133,117,0.16)]"
              : "text-[#6f5b50] hover:bg-white",
          )}
          aria-label={`切換到${option.label}主題`}
        >
          {option.icon}
          <span className={clsx("whitespace-nowrap", compact ? "inline" : "hidden sm:inline")}>
            {option.label}
          </span>
        </button>
      ))}
    </div>
  );
}
