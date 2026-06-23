import { Moon, Stethoscope, Sun } from "lucide-react";
import clsx from "clsx";
import type { ReactNode } from "react";

export type AppTheme = "light" | "clinical" | "dark";

type ThemeToggleProps = {
  theme: AppTheme;
  onChange: (theme: AppTheme) => void;
};

const options: Array<{ value: AppTheme; label: string; icon: ReactNode }> = [
  { value: "light", label: "筆記", icon: <Sun size={15} /> },
  { value: "clinical", label: "專業藍", icon: <Stethoscope size={15} /> },
  { value: "dark", label: "黑暗", icon: <Moon size={15} /> },
];

export function ThemeToggle({ theme, onChange }: ThemeToggleProps) {
  return (
    <div className="inline-flex h-11 rounded-full border border-[#e6d6c9] bg-white/80 p-1 theme-control">
      {options.map((option) => (
        <button
          key={option.value}
          type="button"
          onClick={() => onChange(option.value)}
          className={clsx(
            "inline-flex items-center justify-center gap-1.5 rounded-full px-3 text-xs font-semibold transition",
            theme === option.value
              ? "bg-[#ffddea] text-[#9a496b] shadow-[0_8px_18px_rgba(181,133,117,0.16)]"
              : "text-[#6f5b50] hover:bg-white",
          )}
          aria-label={`切換為${option.label}主題`}
        >
          {option.icon}
          <span className="hidden sm:inline">{option.label}</span>
        </button>
      ))}
    </div>
  );
}
