import { defineStore } from "pinia"
import api from "@/services/api"

export const usePonudaFarmaPlusStore = defineStore("ponudaFarmaPlus", {
  state: () => ({
    kategorije: [],
    usluge: [],
    aktivnaKategorijaId: null,
    loading: false,
    error: null,
  }),
  actions: {
    async ucitajKategorije() {
      this.loading = true
      try {
        const { data } = await api.get("/opg/ponuda-farmaplus/kategorije")
        this.kategorije = data
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška pri dohvaćanju kategorija"
      } finally {
        this.loading = false
      }
    },

    async ucitajUsluge(kategorijaId = null) {
      this.loading = true
      try {
        const { data } = await api.get("/opg/ponuda-farmaplus", {
          params: kategorijaId ? { kategorija_id: kategorijaId } : {},
        })
        this.usluge = data
        this.aktivnaKategorijaId = kategorijaId
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška pri dohvaćanju usluge"
      } finally {
        this.loading = false
      }
    },

    async dodajUslugu(payload) {
      const { data } = await api.post("/opg/ponuda-farmaplus", payload)
      this.usluge.unshift(data)
      if (data.usluga_dostupna) {
        const k = this.kategorije.find((k) => k.id === data.kategorija_id)
        if (k) {
          k.ukupno = (k.ukupno ?? 0) + 1
          if (data.usluga_dostupna) {
            k.dostupni = (k.dostupni ?? 0) + 1
          } else {
            k.nedostupni = (k.nedostupni ?? 0) + 1
          }
        }
      }
      return data
    },

    async urediUslugu(id, patch) {
      const { data } = await api.put(`/opg/ponuda-farmaplus/${id}`, patch)
      const idx = this.usluge.findIndex((p) => p.id === id)
      if (idx !== -1) this.usluge[idx] = data
      await this.ucitajKategorije()
      return data
    },

    async obrisiUslugu(id) {
      const stari = this.usluge.find((p) => p.id === id)
      await api.delete(`/opg/ponuda-farmaplus/${id}`)
      this.usluge = this.usluge.filter((p) => p.id !== id)

      const k = this.kategorije.find((k) => k.id === stari.kategorija_id)
      if (k) {
        k.ukupno = Math.max(0, (k.ukupno ?? 0) - 1)
        if (stari.usluga_dostupna) {
          k.dostupni = Math.max(0, (k.dostupni ?? 0) - 1)
        } else {
          k.nedostupni = Math.max(0, (k.nedostupni ?? 0) - 1)
        }
      }
    },

    async ucitajSlikuUsluge(id, slika_usluge) {
      const forma = new FormData()
      forma.append("slika_usluge", slika_usluge)
      const { data } = await api.post(`/opg/ponuda-farmaplus/${id}/slika`, forma, {
        headers: { "Content-Type": "multipart/form-data" },
      })
      const idx = this.usluge.findIndex((p) => p.id === id)
      if (idx !== -1) this.usluge[idx] = data
      return data
    },
  },
})
