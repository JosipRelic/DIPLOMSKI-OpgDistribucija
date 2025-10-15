export function primijeniPodatkeOdAIuFormu(forma, podaci, mapiranje = {}) {
  if (!podaci || typeof podaci !== "object") return
  Object.entries(podaci).forEach(([kljuc, vrijednost]) => {
    if (vrijednost === null || vrijednost === undefined || vrijednost === "") return
    const cilj = mapiranje[kljuc] ?? kljuc
    if (cilj in forma) {
      forma[cilj] =
        typeof forma[cilj] === "boolean"
          ? ["true", "1"].includes(String(vrijednost).toLocaleLowerCase())
          : vrijednost
    }
  })
}
