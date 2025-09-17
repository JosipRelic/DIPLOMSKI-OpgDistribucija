import { defineStore } from "pinia"
import api from "@/services/api"

export const useFarmaPlusStore = defineStore("farmaPlus", {
  state: () => ({
    kategorije: [],
    kat_slug: null,

    usluge: [],
    ukupno_usluga: 0,
    ukupno_stranica: 1,

    stranica: 1,
    velicina_stranice: 12,

    filteri: {
      q: "",
      zupanije: [],
      mjesta: [],
      usluge: [],
      sortiranje: "novo",
    },

    filteriZupanije: [],
    filterMjesta: [],
    filteriUsluge: [],

    loading: false,
    error: null,
  }),

  getters: {
    ukupnoStranica: (s) =>
      s.ukupno_usluga > 0
        ? Math.max(1, Math.ceil(s.ukupno_usluga / s.velicina_stranice))
        : s.ukupno_stranica || 1,
    imaUsluga: (s) => s.usluge.length > 0 && s.ukupno_usluga > 0,
    nemaRezultata: (s) => s.usluge.length === 0 && s.ukupno_usluga > 0,
    kategorijaOdabrana: (s) => !!s.kat_slug,
  },

  actions: {
    async ucitajKategorije() {
      this.error = null
      try {
        const { data } = await api.get("/farma-plus/kategorije")
        this.kategorije = data
      } catch (e) {
        this.error = e?.response?.data?.detail || "Greška pri učitavanju kategorija"
        this.kategorije = []
      }
    },

    postaviKategoriju(slug) {
      this.kat_slug = slug || null
      this.stranica = 1
      this.filteri.q = ""
      this.filteri.zupanije = []
      this.filteri.mjesta = []
      this.filteri.usluge = []
      this.filteri.sortiranje = "novo"
      this.filteriZupanije = []
      this.filterMjesta = []
      this.filteriUsluge = []
    },

    resetirajStranice() {
      this.stranica = 1
    },

    async ucitajFiltere() {
      if (!this.kat_slug) return
      this.error = null
      try {
        const { data } = await api.get("/farma-plus/filteri-lokacije", {
          params: { kat_slug: this.kat_slug },
        })
        this.filteriZupanije = data.zupanije || []
        this.filterMjesta = data.mjesta || []
        this.filteriUsluge = data.usluge || []
      } catch (e) {
        this.error = e?.response?.data?.detail || "Greška pri učitavanju filtera"
        this.filteriZupanije = []
        this.filterMjesta = []
        this.filteriUsluge = []
      }
    },

    async ucitajUsluge() {
      if (!this.kat_slug) return
      this.loading = true
      this.error = null

      try {
        const params = new URLSearchParams()
        params.append("kat_slug", this.kat_slug)
        if (this.filteri.q) params.append("q", this.filteri.q)

        for (const z of this.filteri.zupanije) params.append("zupanije", z)
        for (const m of this.filteri.mjesta) params.append("mjesta", m)
        for (const u of this.filteri.usluge) params.append("usluge", u)

        if (this.filteri.sortiranje) params.append("sortiranje", this.filteri.sortiranje)
        params.append("stranica", String(this.stranica))
        params.append("velicina_stranice", String(this.velicina_stranice))

        const { data } = await api.get("/farma-plus/usluge", { params })

        this.usluge = data.usluge || []
        this.ukupno_usluga = data.ukupno_usluga ?? 0
        this.ukupno_stranica = data.ukupno_stranica ?? 1
      } catch (e) {
        this.error = e?.response?.data?.detail || "Greška pri učitavanju usluga"
        this.usluge = []
        this.ukupno_usluga = 0
        this.ukupno_stranica = 1
      } finally {
        this.loading = false
      }
    },

    setQ(v) {
      if (this.filteri.q !== v) this.filteri.q = v
      this.stranica = 1
      this.ucitajUsluge()
    },

    odabraniFilteri(polje, vrijednost, odabrano) {
      const set = new Set(this.filteri[polje])
      odabrano ? set.add(vrijednost) : set.delete(vrijednost)
      this.filteri[polje] = Array.from(set)
      this.stranica = 1
      this.ucitajUsluge()
    },

    postaviSortiranje(v) {
      if (this.filteri.sortiranje !== v) this.filteri.sortiranje = v
      this.stranica = 1
      this.ucitajUsluge()
    },

    promijeniStranicu(n) {
      this.stranica = n
      this.ucitajUsluge()
    },

    ponistiFiltere() {
      this.filteri.q = ""
      this.filteri.zupanije = []
      this.filteri.mjesta = []
      this.filteri.usluge = []
      this.filteri.sortiranje = "novo"
      this.stranica = 1
      this.ucitajUsluge()
    },

    ponistiZupanije() {
      this.filteri.zupanije = []
      this.stranica = 1
      this.ucitajUsluge()
    },

    ponistiMjesta() {
      this.filteri.mjesta = []
      this.stranica = 1
      this.ucitajUsluge()
    },

    ponistiUslugeNazivi() {
      this.filteri.usluge = []
      this.stranica = 1
      this.ucitajUsluge()
    },
  },
})
