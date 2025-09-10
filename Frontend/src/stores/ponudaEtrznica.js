import { defineStore } from "pinia"
import api from "@/services/api"

export const usePonudaEtrznicaStore = defineStore("ponudaEtrznica", {
  state: () => ({
    kategorije: [],
    proizvodi: [],
    aktivnaKategorijaId: null,
    loading: false,
    error: null,
  }),
  actions: {
    async ucitajKategorije() {
      this.loading = true
      try {
        const { data } = await api.get("/opg/ponuda-etrznica/kategorije")
        this.kategorije = data
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška pri dohvaćanju kategorija"
      } finally {
        this.loading = false
      }
    },

    async ucitajProizvode(kategorijaId = null) {
      this.loading = true
      try {
        const { data } = await api.get("/opg/ponuda-etrznica", {
          params: kategorijaId ? { kategorija_id: kategorijaId } : {},
        })
        this.proizvodi = data
        this.aktivnaKategorijaId = kategorijaId
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška pri dohvaćanju proizvoda"
      } finally {
        this.loading = false
      }
    },

    async dodajProizvod(payload) {
      const { data } = await api.post("/opg/ponuda-etrznica", payload)
      this.proizvodi.unshift(data)
      if (data.proizvod_dostupan) {
        const k = this.kategorije.find((k) => k.id === data.kategorija_id)
        if (k) k.broj += 1
      }
      return data
    },

    async urediProizvod(id, patch) {
      const { data } = await api.put(`/opg/ponuda-etrznica/${id}`, patch)
      const idx = this.proizvodi.findIndex((p) => p.id === id)
      if (idx !== -1) this.proizvodi[idx] = data
      await this.ucitajKategorije()
      return data
    },

    async obrisiProizvod(id) {
      const stari = this.proizvodi.find((p) => p.id === id)
      await api.delete(`/opg/ponuda-etrznica/${id}`)
      this.proizvodi = this.proizvodi.filter((p) => p.id !== id)
      if (stari?.proizvod_dostupan) {
        const k = this.kategorije.find((k) => k.id === stari.kategorija_id)
        if (k && k.broj > 0) k.broj -= 1
      }
    },

    async ucitajSlikuProizvoda(id, slika_proizvoda) {
      const forma = new FormData()
      forma.append("slika_proizvoda", slika_proizvoda)
      const { data } = await api.post(`/opg/ponuda-etrznica/${id}/slika`, forma, {
        headers: { "Content-Type": "multipart/form-data" },
      })
      const idx = this.proizvodi.findIndex((p) => p.id === id)
      if (idx !== -1) this.proizvodi[idx] = data
      return data
    },
  },
})
