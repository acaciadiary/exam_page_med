import { useCallback } from "react";
import { useLocalStorage } from "./useLocalStorage";

export function useMarkedItems(key: string) {
  const [marked, setMarked] = useLocalStorage<string[]>(key, []);
  const markedSet = new Set(marked);

  const toggleMarked = useCallback(
    (id: string) => {
      setMarked((current) =>
        current.includes(id)
          ? current.filter((item) => item !== id)
          : [...current, id],
      );
    },
    [setMarked],
  );

  const clearMarked = useCallback(() => {
    setMarked([]);
  }, [setMarked]);

  const removeMarked = useCallback(
    (id: string) => {
      setMarked((current) => current.filter((item) => item !== id));
    },
    [setMarked],
  );

  return { marked, markedSet, toggleMarked, clearMarked, removeMarked };
}
