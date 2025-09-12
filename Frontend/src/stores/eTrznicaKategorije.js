import { defineStore } from "pinia"
import api from "@/services/api"

export const useEtrznicaKategorijeStore = defineStore("eTrznicaKategorije", {
  state: () => ({
    kategorije: [],
    aktivna: null,
    loading: false,
  }),

  actions: {
    async ucitajSveKategorije() {
      this.loading = true
      try {
        const { data } = await api.get("/e-trznica/kategorije")
        this.kategorije = data
      } finally {
        this.loading = false
      }
    },

    async ucitajPojedinuKategoriju(slug) {
      this.loading = true
      try {
        const { data } = await api.get(`/e-trznica/kategorije/${slug}`)
        this.aktivna = data
      } finally {
        this.loading = false
      }
    },
  },
})
