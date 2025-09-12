import { defineStore } from "pinia"
import api from "@/services/api"

export const useEtrznicaProizvodiStore = defineStore("eTrznicaProizvodi", {
  state: () => ({
    proizvodi: [],
    ukupno: 0,
    ukupno_u_kategoriji: 0,
    stranica: 1,
    velicina_stranice: 12,
    loading: false,
    kat_slug: null,

    filteri: {
      q: "",
      zupanije: [],
      mjesta: [],
      sortiranje: "novo",
    },

    filteriZupanije: [],
    filteriMjesta: [],
  }),

  getters: {
    ukupnoStranica: (s) => Math.max(1, Math.ceil(s.ukupno / s.velicina_stranice)),
    kategorijaPrazna: (s) => s.ukupno_u_kategoriji === 0,
    nemaRezultata: (s) => s.ukupno === 0 && s.ukupno_u_kategoriji > 0,
    imaProizvoda: (s) => s.ukupno > 0 && s.proizvodi.length > 0,
  },

  actions: {
    postaviKategoriju(slug) {
      this.kat_slug = slug || null
      this.stranica = 1
    },

    async ucitajFiltere() {
      const params = {}
      if (this.kat_slug) params.kat_slug = this.kat_slug
      const { data } = await api.get("/e-trznica/filteri-lokacije", { params })
      this.filteriZupanije = data.zupanije
      this.filteriMjesta = data.mjesta
    },

    async ucitajProizvode() {
      if (!this.kat_slug) return
      this.loading = true
      try {
        const params = {
          kat_slug: this.kat_slug,
          q: this.filteri.q || undefined,
          zupanije: this.filteri.zupanije.join(",") || undefined,
          mjesta: this.filteri.mjesta.join(",") || undefined,
          sortiranje: this.filteri.sortiranje || undefined,
          stranica: this.stranica,
          velicina_stranice: this.velicina_stranice,
        }
        const { data } = await api.get("/e-trznica/proizvodi", { params })
        this.proizvodi = data.proizvodi
        this.ukupno = data.ukupno
        this.ukupno_u_kategoriji = data.ukupno_u_kategoriji
      } finally {
        this.loading = false
      }
    },

    promijeniStranicu(s) {
      this.stranica = s
      this.ucitajProizvode()
    },

    ponistiFiltere() {
      this.filteri = { q: "", zupanije: [], mjesta: [], sortiranje: "novo" }
      this.stranica = 1
      this.ucitajProizvode()
    },

    setQ(v) {
      this.filteri.q = v
      this.stranica = 1
      this.ucitajProizvode()
    },

    odabraniFilteri(polje, vrijednost, odabrano) {
      const set = new Set(this.filteri[polje])
      odabrano ? set.add(vrijednost) : set.delete(vrijednost)
      this.filteri[polje] = Array.from(set)
      this.stranica = 1
      this.ucitajProizvode()
    },

    postaviSortiranje(v) {
      this.filteri.sortiranje = v
      this.stranica = 1
      this.ucitajProizvode()
    },

    resetirajStranice() {
      this.stranica = 1
    },
  },
})
