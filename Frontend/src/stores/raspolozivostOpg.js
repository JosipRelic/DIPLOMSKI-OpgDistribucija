import { defineStore } from "pinia"
import api from "@/services/api"

export const useRaspolozivostOpgStore = defineStore("raspolozivostOpg", {
  state: () => ({
    tjedno: [],
    datumi: [],
    kalendar: {},
    loading: false,
    error: null,
  }),

  actions: {
    async dohvatiTjedno() {
      this.loading = true
      try {
        const { data } = await api.get("/opg/raspolozivost/tjedno")
        this.tjedno = data
      } finally {
        this.loading = false
      }
    },

    async spremiTjedno(payload) {
      const { data } = await api.put("/opg/raspolozivost/tjedno", payload)
      this.tjedno = data
    },

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
