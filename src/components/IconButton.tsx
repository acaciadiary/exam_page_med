import type { ButtonHTMLAttributes, ReactNode } from "react";
import clsx from "clsx";

type IconButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  label: string;
  active?: boolean;
  children: ReactNode;
};

export function IconButton({
  label,
  active = false,
  children,
  className,
  ...props
}: IconButtonProps) {
  return (
    <button
      type="button"
      aria-label={label}
      title={label}
      className={clsx(
        "inline-flex h-10 w-10 items-center justify-center rounded-full border transition",
        active
          ? "border-[#f1aac8] bg-[#ffddea] text-[#9a496b] shadow-[0_8px_24px_rgba(238,148,185,0.28)]"
          : "border-[#efd9d0] bg-white/74 text-[#80665c] hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]",
        className,
      )}
      {...props}
    >
      {children}
    </button>
  );
}
