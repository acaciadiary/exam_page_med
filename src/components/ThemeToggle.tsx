import { Moon, Sun } from "lucide-react";
import { IconButton } from "./IconButton";

type ThemeToggleProps = {
  theme: "light" | "dark";
  onToggle: () => void;
};

export function ThemeToggle({ theme, onToggle }: ThemeToggleProps) {
  return (
    <IconButton
      label={theme === "dark" ? "切換淺色模式" : "切換深色模式"}
      onClick={onToggle}
    >
      {theme === "dark" ? <Sun size={18} /> : <Moon size={18} />}
    </IconButton>
  );
}
