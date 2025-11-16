export function primijeniPodatkeOdAIuFormu(forma, podaci, mapiranje = {}) {
  if (!podaci || typeof podaci !== "object") return
  Object.entries(podaci).forEach(([kljuc, vrijednost]) => {
    if (vrijednost === null || vrijednost === undefined || vrijednost === "") return
    const polje = mapiranje[kljuc] ?? kljuc
    if (polje in forma) {
      forma[polje] =
        typeof forma[polje] === "boolean"
          ? ["true", "1"].includes(String(vrijednost).toLocaleLowerCase())
          : vrijednost
    }
  })
}
