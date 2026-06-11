import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { useState } from "react";
import { describe, expect, it } from "vitest";
import { useLocalStorage } from "../../src/hooks/useLocalStorage";

function LocalStorageHarness() {
  const [storageKey, setStorageKey] = useState("answers:exam-a");
  const [value, setValue] = useLocalStorage<Record<string, string>>(storageKey, {});

  return (
    <div>
      <div data-testid="active-key">{storageKey}</div>
      <div data-testid="value">{JSON.stringify(value)}</div>
      <button type="button" onClick={() => setStorageKey("answers:exam-b")}>
        切換考科
      </button>
      <button
        type="button"
        onClick={() => setValue((current) => ({ ...current, q2: "B" }))}
      >
        作答
      </button>
    </div>
  );
}

describe("useLocalStorage", () => {
  it("reloads the correct value after the storage key changes", async () => {
    const user = userEvent.setup();

    window.localStorage.setItem("answers:exam-a", JSON.stringify({ q1: "A" }));
    window.localStorage.setItem("answers:exam-b", JSON.stringify({ q9: "D" }));

    render(<LocalStorageHarness />);

    expect(screen.getByTestId("active-key")).toHaveTextContent("answers:exam-a");
    expect(screen.getByTestId("value")).toHaveTextContent('{"q1":"A"}');

    await user.click(screen.getByRole("button", { name: "切換考科" }));

    expect(screen.getByTestId("active-key")).toHaveTextContent("answers:exam-b");
    expect(screen.getByTestId("value")).toHaveTextContent('{"q9":"D"}');
  });

  it("does not overwrite the next key with stale data during a key switch", async () => {
    const user = userEvent.setup();

    window.localStorage.setItem("answers:exam-a", JSON.stringify({ q1: "A" }));
    window.localStorage.setItem("answers:exam-b", JSON.stringify({ q9: "D" }));

    render(<LocalStorageHarness />);

    await user.click(screen.getByRole("button", { name: "切換考科" }));
    await user.click(screen.getByRole("button", { name: "作答" }));

    expect(JSON.parse(window.localStorage.getItem("answers:exam-a") ?? "{}")).toEqual({
      q1: "A",
    });
    expect(JSON.parse(window.localStorage.getItem("answers:exam-b") ?? "{}")).toEqual({
      q9: "D",
      q2: "B",
    });
  });
});
