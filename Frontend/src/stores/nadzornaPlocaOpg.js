import { defineStore } from "pinia"
import api from "@/services/api"

export const useOpgNadzornaPlocaStore = defineStore("OpgNadzornaPloca", {
  state: () => ({
    loading: false,
    podaci: null,
  }),
  actions: {
    async ucitajNadzornuPlocu() {
      this.loading = true
      try {
        const { data } = await api.get("/opg/nadzorna-ploca")
        this.podaci = data || null
      } finally {
        this.loading = false
      }
    },
  },
})
