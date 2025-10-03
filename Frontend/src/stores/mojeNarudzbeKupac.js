import { defineStore } from "pinia"
import api from "@/services/api"

export const useMojeNarudzbeKupacStore = defineStore("MojeNarudzbeKupac", {
  state: () => ({
    loading: false,
    stranica: 1,
    velicina: 10,
    p: "",

    ukupno: 0,
    stavke: [],
    detalji: null,
  }),
  getters: {
    ukupnoStranica(state) {
      return Math.max(1, Math.ceil((state.ukupno || 0) / state.velicina))
    },
  },
  actions: {
    async ucitajMojeNarudzbe() {
      this.loading = true
      try {
        const { data } = await api.get("/kupac/moje-narudzbe", {
          params: {
            stranica: this.stranica,
            velicina: this.velicina,
            p: this.p || undefined,
          },
        })
        this.ukupno = data?.ukupno ?? 0
        this.stavke = data?.stavke ?? []
        this.stranica = data?.stranica ?? this.stranica
        this.velicina = data?.velicina ?? this.velicina
      } finally {
        this.loading = false
      }
    },

    async ucitajDetaljeNarudzbe(id) {
      this.loading = true
      try {
        const { data } = await api.get(`/kupac/moje-narudzbe/detalji-narudzbe/${id}`)
        this.detalji = data?.detalji || null
      } finally {
        this.loading = false
      }
    },

    idiNa(str) {
      const cilj = Math.min(Math.max(1, Number(str || 1)), this.ukupnoStranica)
      this.stranica = cilj
      return this.ucitajMojeNarudzbe()
    },

    postaviP(v) {
      this.p = (v ?? "").toString().trim()
      this.stranica = 1
      return this.ucitajMojeNarudzbe()
    },
  },
})
