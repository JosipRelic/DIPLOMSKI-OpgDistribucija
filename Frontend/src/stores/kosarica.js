import { defineStore } from "pinia"
import api from "@/services/api"

const STOPA_PDV = 0.25
const BRUTO_DIV = 1 + STOPA_PDV
const r2 = (n) => Math.round((n + Number.EPSILON) * 100) / 100

function iznos(n) {
  const x = Number(n || 0)
  return Number.isFinite(x) ? x : 0
}

export const useKosaricaStore = defineStore("kosarica", {
  state: () => ({
    stavke: [],
    loading: false,
  }),

  getters: {
    brojArtikala: (s) => s.stavke.reduce((acc, x) => acc + (x.kolicina || 0), 0),
    proizvodi: (s) => s.stavke.filter((x) => x.tip === "proizvod"),
    usluge: (s) => s.stavke.filter((x) => x.tip === "usluga"),
    iznos_bez_pdva: (s) =>
      s.stavke.reduce((acc, x) => {
        const k = x.kolicina || 0
        const bruto = iznos(x.cijena)
        const netoUnit = r2(bruto / BRUTO_DIV)
        return acc + r2(netoUnit * k)
      }, 0),

    pdv: (s) =>
      s.stavke.reduce((acc, x) => {
        const k = x.kolicina || 0
        const bruto = iznos(x.cijena)
        const netoUnit = r2(bruto / BRUTO_DIV)
        const pdvUnit = r2(bruto - netoUnit)
        return acc + r2(pdvUnit * k)
      }, 0),

    ukupno_s_pdvom: (s) =>
      s.stavke.reduce((acc, x) => {
        const k = x.kolicina || 0
        const bruto = iznos(x.cijena)
        return acc + r2(bruto * k)
      }, 0),
  },

  actions: {
    async osvjezi() {
      this.loading = true
      try {
        const { data } = await api.get("/kosarica")
        this.stavke = data.stavke || []
      } finally {
        this.loading = false
      }
    },

    async dodajProizvod({ proizvod_id, kolicina = 1 }) {
      const { data } = await api.post("/kosarica/proizvodi", { proizvod_id, kolicina })
      this.stavke = data.stavke || []
    },

    async dodajUslugu({ usluga_id, kolicina = 1 }) {
      const { data } = await api.post("/kosarica/usluge", { usluga_id, kolicina })
      this.stavke = data.stavke || []
    },

    async dodajUsluguSTerminom({ usluga_id, kolicina = 1, termin_od, termin_do }) {
      const { data } = await api.post("/kosarica/usluge", {
        usluga_id,
        kolicina,
        termin_od,
        termin_do,
      })
      this.stavke = data.stavke || []
    },

    async promijeniKolicinu(stavkaId, kolicina) {
      const { data } = await api.patch(`/kosarica/stavke/${stavkaId}`, { kolicina })
      this.stavke = data.stavke || []
    },

    async ukloni(stavkaId) {
      const { data } = await api.delete(`/kosarica/stavke/${stavkaId}`)
      this.stavke = data.stavke || []
    },

    reset() {
      this.stavke = []
      this.loading = false
    },
  },
})
