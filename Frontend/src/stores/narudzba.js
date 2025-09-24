import { defineStore } from "pinia"
import api from "@/services/api"

export const useNarudzbaStore = defineStore("narudzbe", {
  state: () => ({
    aktivna: null,
    loading: false,
    error: null,
  }),

  actions: {
    async kreirajNarudzbu(payload) {
      this.loading = true
      this.error = null
      try {
        const { data } = await api.post("/narudzbe", payload)
        this.aktivna = data
        return data
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška kod narudžbe"
        throw e
      } finally {
        this.loading = false
      }
    },
  },
})
