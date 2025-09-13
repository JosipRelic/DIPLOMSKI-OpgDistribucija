import { defineStore } from "pinia"
import api from "@/services/api"

export const useEtrznicaOpgoviStore = defineStore("eTrznicaOpgovi", {
  state: () => ({
    opgovi: [],
    ukupno: 0,
    stranica: 1,
    velicina_stranice: 9,
    loading: false,

    filteri: {
      q: "",
      zupanije: [],
      mjesta: [],
      ocjena_min: null,
      bez_recenzija: false,
      sortiranje: "",
    },

    filteriZupanije: [],
    filteriMjesta: [],
    kat_slug: null,

    statistika: {
      broj_registriranih_opgova: 0,
      broj_usluga: 0,
      broj_proizvoda: 0,
    },
  }),

  actions: {
    async ucitajStatistiku() {
      const { data } = await api.get("/e-trznica/statistika")
      this.statistika = data
    },

    postaviKategoriju(slug) {
      this.kat_slug = slug || null
    },

    async ucitajFiltere() {
      const params = {}
      if (this.kat_slug) params.kat_slug = this.kat_slug
      const { data } = await api.get("/e-trznica/filteri-lokacije", { params })
      this.filteriZupanije = data.zupanije
      this.filteriMjesta = data.mjesta
    },

    async ucitajOpgove() {
      this.loading = true
      try {
        const params = {
          q: this.filteri.q || undefined,
          zupanije: this.filteri.zupanije.join(",") || undefined,
          mjesta: this.filteri.mjesta.join(",") || undefined,
          ocjena_min: this.filteri.ocjena_min ?? undefined,
          bez_recenzija: this.filteri.bez_recenzija || undefined,
          sortiranje: this.filteri.sortiranje || undefined,
          stranica: this.stranica,
          velicina_stranice: this.velicina_stranice,
          kat_slug: this.kat_slug || undefined,
        }
        const { data } = await api.get("/e-trznica/opgovi", { params })
        this.opgovi = data.opgovi
        this.ukupno = data.ukupno
      } finally {
        this.loading = false
      }
    },

    promijeniStranicu(s) {
      this.stranica = s
      this.ucitajOpgove()
    },

    ponistiFiltere() {
      this.filteri = {
        q: "",
        zupanije: [],
        mjesta: [],
        ocjena_min: null,
        bez_recenzija: false,
        sortiranje: "",
      }
      this.stranica = 1
      this.ucitajOpgove()
    },

    odabraniFilteri(polje, vrijednost, odabrano) {
      const set = new Set(this.filteri[polje])
      odabrano ? set.add(vrijednost) : set.delete(vrijednost)
      this.filteri[polje] = Array.from(set)
      this.stranica = 1
      this.ucitajOpgove()
    },
  },
})
