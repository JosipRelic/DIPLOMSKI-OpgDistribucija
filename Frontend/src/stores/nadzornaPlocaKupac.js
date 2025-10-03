import { defineStore } from "pinia"
import api from "@/services/api"

export const useNadzornaPlocaKupacStore = defineStore("NadzornaPlocaKupac", {
  state: () => ({
    loading: false,
    statistika: null,
    posljednje: { proizvodi: [], usluge: [] },
  }),
  actions: {
    async ucitaj() {
      this.loading = true
      try {
        const { data } = await api.get("/kupac/nadzorna-ploca")
        this.statistika = data?.statistika || null
        this.posljednje = data?.posljednje || { proizvodi: [], usluge: [] }
      } finally {
        this.loading = false
      }
    },
  },
})
