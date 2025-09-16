import { defineStore } from "pinia"
let _id = 1

export const useUiStore = defineStore("ui", {
  state: () => ({
    obavijesti: [],
    potvrda: {
      otvorena: false,
      naslov: "",
      poruka: "",
      potvrdiRadnju: "",
      odustaniOdRadnje: "",
      tip_obavijesti: "zadano",
      odluka: null,
    },
  }),

  actions: {
    obavijest({ tekst, tip_obavijesti = "info", istek_vremena = 4000, akcija = null }) {
      const id = _id++
      this.obavijesti.push({ id, tekst, tip_obavijesti, akcija })
      if (istek_vremena) setTimeout(() => this.zatvori(id), istek_vremena)
      return id
    },

    zatvori(id) {
      this.obavijesti = this.obavijesti.filter((o) => o.id !== id)
    },

    obavijestSaPotvrdom(obavijest = {}) {
      return new Promise((odluka) => {
        this.potvrda.otvorena = true
        this.potvrda.naslov = obavijest.naslov || "Potvrda"
        this.potvrda.poruka = obavijest.poruka || ""
        this.potvrda.potvrdiRadnju = obavijest.potvrdiRadnju || "Potvrdi"
        this.potvrda.odustaniOdRadnje = obavijest.odustaniOdRadnje || "Odustani"
        this.potvrda.tip_obavijesti = obavijest.tip_obavijesti || "zadano"
        this.potvrda.odluka = odluka
      })
    },

    donesenaOdluka(rezultat) {
      const rez = this.potvrda.odluka
      this.potvrda.otvorena = false
      this.potvrda.odluka = null
      if (rez) rez(!!rezultat)
    },
  },
})
