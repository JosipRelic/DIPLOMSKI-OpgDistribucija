import { defineStore } from "pinia"
import api from "@/services/api"

export const useRaspolozivostOpgStore = defineStore("raspolozivostOpg", {
  state: () => ({
    datumi: [],
    kalendar: {},
    loading: false,
    error: null,
  }),

  actions: {
    async dohvatiMjesecneDatume({ godina, mjesec }) {
      const { data } = await api.get("/opg/raspolozivost/dani", { params: { godina, mjesec } })
      this.datumi = data
    },

    async dodajDatum({ datum, pocetno_vrijeme, zavrsno_vrijeme, naslov }) {
      const { data } = await api.post("/opg/raspolozivost/dani", {
        datum,
        pocetno_vrijeme,
        zavrsno_vrijeme,
        naslov,
      })
      this.datumi.push(data)
    },

    async urediDatum(id, { datum, pocetno_vrijeme, zavrsno_vrijeme, naslov }) {
      const { data } = await api.put(`/opg/raspolozivost/dani/${id}`, {
        datum,
        pocetno_vrijeme,
        zavrsno_vrijeme,
        naslov,
      })
      const i = this.datumi.findIndex((d) => d.id === id)
      if (i !== -1) this.datumi[i] = data
      return data
    },

    async obrisiDatum(id) {
      await api.delete(`/opg/raspolozivost/dani/${id}`)
      this.datumi = this.datumi.filter((d) => d.id !== id)
    },

    async dohvatiKalendar({ opg_id, godina, mjesec }) {
      const { data } = await api.get("/opg/raspolozivost/kalendar", {
        params: { opg_id, godina, mjesec },
      })
      this.kalendar = data.slotovi || {}
    },
  },
})
