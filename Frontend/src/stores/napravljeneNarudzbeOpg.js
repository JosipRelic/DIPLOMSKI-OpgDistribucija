import { defineStore } from "pinia"
import api from "@/services/api"

export const useNapravljeneNarudzbeOpgStore = defineStore("NapravljeneNarudzbeOpg", {
  state: () => ({
    narudzbe: [],
    ukupno: 0,
    ukupnoStranica: 0,
    stranica: 1,
    velicina: 8,
    p: "",
    loading: false,
    detalji: null,
  }),

  actions: {
    async ucitajNarudzbe() {
      this.loading = true
      try {
        const params = {
          stranica: this.stranica,
          velicina: this.velicina,
        }
        if (this.p && this.p.trim()) params.p = this.p.trim()

        const { data } = await api.get("/opg/napravljene-narudzbe", { params })
        this.narudzbe = data.narudzbe || []
        this.ukupno = data.ukupno || 0
        this.ukupnoStranica = data.ukupno_stranica || 0
      } finally {
        this.loading = false
      }
    },

    async ucitajDetaljeNarudzbe(narudzba_id) {
      this.loading = true
      try {
        const { data } = await api.get(`/opg/napravljene-narudzbe/detalji-narudzbe/${narudzba_id}`)
        this.detalji = data
      } finally {
        this.loading = false
      }
    },

    idiNa(str) {
      this.stranica = str
      return this.ucitajNarudzbe()
    },

    postaviP(v) {
      this.p = v || ""
      this.stranica = 1
      return this.ucitajNarudzbe()
    },
  },
})
