import { defineStore } from "pinia"
import api from "@/services/api"

export const usePocetnaStore = defineStore("Pocetna", {
  state: () => ({
    loading: false,
    proizvodi: [],
    opgovi: [],
    usluge: [],
  }),
  actions: {
    async ucitaj() {
      this.loading = true
      try {
        const { data } = await api.get("/pocetna")
        this.proizvodi = data?.najprodavaniji_proizvodi ?? []
        this.opgovi = data?.najbolje_ocijenjeni_opgovi ?? []
        this.usluge = data?.najtrazenije_usluge ?? []
      } finally {
        this.loading = false
      }
    },
  },
})
