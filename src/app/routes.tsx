export type AppPage = "exam" | "progress" | "mistakes" | "favorites" | "notes" | "diseases";

const pageParam = "page";

export function readPageFromSearch(search: string): AppPage {
  const params = new URLSearchParams(search);
  const page = params.get(pageParam);

  if (
    page === "progress" ||
    page === "mistakes" ||
    page === "favorites" ||
    page === "notes" ||
    page === "diseases"
  ) {
    return page;
  }

  return "exam";
}

export function buildSearchForPage(page: AppPage, currentSearch: string) {
  const params = new URLSearchParams(currentSearch);

  if (page === "exam") {
    params.delete(pageParam);
  } else {
    params.set(pageParam, page);
  }

  const nextSearch = params.toString();
  return nextSearch ? `?${nextSearch}` : "";
}
