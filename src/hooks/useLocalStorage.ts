import { useCallback, useEffect, useRef, useState } from "react";

function readStoredValue<T>(key: string, initialValue: T) {
  if (typeof window === "undefined") return initialValue;

  try {
    const stored = window.localStorage.getItem(key);
    return stored ? (JSON.parse(stored) as T) : initialValue;
  } catch {
    return initialValue;
  }
}

export function useLocalStorage<T>(key: string, initialValue: T) {
  const skipPersistRef = useRef(false);
  const initialValueRef = useRef(initialValue);

  useEffect(() => {
    initialValueRef.current = initialValue;
  }, [initialValue]);

  const [value, setValue] = useState<T>(() => readStoredValue(key, initialValueRef.current));

  useEffect(() => {
    skipPersistRef.current = true;
    setValue(readStoredValue(key, initialValueRef.current));
  }, [key]);

  useEffect(() => {
    if (skipPersistRef.current) {
      skipPersistRef.current = false;
      return;
    }

    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // Local storage can be unavailable in private browsing.
    }
  }, [key, value]);

  useEffect(() => {
    function handleStorage(event: StorageEvent) {
      if (event.key !== key) return;
      setValue(readStoredValue(key, initialValueRef.current));
    }

    window.addEventListener("storage", handleStorage);
    return () => window.removeEventListener("storage", handleStorage);
  }, [key]);

  const reset = useCallback(() => setValue(initialValueRef.current), []);

  return [value, setValue, reset] as const;
}
