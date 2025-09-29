import { defineStore } from "pinia"
import api from "@/services/api"

export const usePrimljeneNarudzbeOpgStore = defineStore("PrimljeneNarudzbeOpg", {
  state: () => ({
    narudzbe: [],
    ukupno: 0,
    ukupnoStranica: 0,
    stranica: 1,
    velicina: 8,
    p: "",
    loading: false,
    detalji: null,

    kupac: null,
    kupacStatistika: null,
    kupacNarudzbe: { stavke: [], ukupno: 0, stranica: 1, velicina: 8 },
    kupacLoading: false,
    kupacP: "",
    kupacSlug: null,
  }),

  actions: {
    async ucitajNarudzbe() {
      this.loading = true
      try {
        const { data } = await api.get("/opg/primljene-narudzbe", {
          params: { stranica: this.stranica, velicina: this.velicina, p: this.p || undefined },
        })
        this.narudzbe = data.narudzbe || []
        this.ukupno = data.ukupno || 0
        this.ukupnoStranica = data.ukupno_stranica || 0
      } finally {
        this.loading = false
      }
    },

    async ucitajDetaljeNarudzbe(id) {
      this.loading = true
      try {
        const { data } = await api.get(`/opg/primljene-narudzbe/detalji-narudzbe/${id}`)
        this.detalji = data
      } finally {
        this.loading = false
      }
    },

    async promijeniStatusNarudzbe(id, status) {
      await api.patch(`/opg/primljene-narudzbe/detalji-narudzbe/${id}/status`, { status })

      if (this.detalji?.id === id) this.detalji.status = status

      this.narudzbe = this.narudzbe.map((n) => (n.id === id ? { ...n, status } : n))
    },

    idiNa(str) {
      this.stranica = str
      return this.ucitajNarudzbe()
    },
    postaviP(v) {
      this.p = v
      this.stranica = 1
      return this.ucitajNarudzbe()
    },

    async ucitajKupca(slug, { stranica = 1, velicina = 8, p } = {}) {
      this.kupacLoading = true
      this.kupacSlug = slug
      try {
        const params = { stranica, velicina }
        if (p && p.trim()) params.p = p.trim()

        const { data } = await api.get(`/opg/primljene-narudzbe/detalji-kupca/${slug}`, { params })

        this.kupac = data.kupac
        this.kupacStatistika = data.statistika
        this.kupacNarudzbe = {
          ...data.narudzbe,
          stranica,
          velicina,
        }
        this.kupacP = p || this.kupacP
      } finally {
        this.kupacLoading = false
      }
    },

    idiNaKupac(str) {
      return this.ucitajKupca(this.kupacSlug, {
        stranica: str,
        velicina: this.kupacNarudzbe.velicina,
        p: this.kupacP,
      })
    },
    postaviKupacP(v) {
      this.kupacP = v
      return this.ucitajKupca(this.kupacSlug, {
        stranica: 1,
        velicina: this.kupacNarudzbe.velicina,
        p: v,
      })
    },
  },
})
