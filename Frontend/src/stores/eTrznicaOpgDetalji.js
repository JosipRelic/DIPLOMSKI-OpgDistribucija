import { defineStore } from "pinia"
import api from "@/services/api"

export const useEtrznicaOpgDetaljiStore = defineStore("eTrznicaOpgDetalji", {
  state: () => ({
    loading: false,
    nijePronadeno: false,
    opg: null,

    proizvodi: { lista_proizvoda: [], ukupno_proizvoda: 0, loading: false },
    usluge: { lista_usluga: [], ukupno_usluga: 0, loading: false },
    recenzije: { lista_recenzija: [], ukupno: 0, loading: false, stranica: 1, velicina: 10 },

    katProizvodi: [],
    katUsluge: [],
    aktivnaKatProizvoda: null,
    aktivnaKatUsluge: null,
  }),
  actions: {
    async ucitajDetaljeOpga(slug) {
      this.loading = true
      ;(this.nijePronadeno = false), (this.opg = null)
      try {
        const { data } = await api.get(`/e-trznica/opgovi/${slug}`)
        this.opg = data
      } catch (e) {
        this.nijePronadeno = e?.response?.status === 404
      } finally {
        this.loading = false
      }
    },

    async ucitajKategorijeProizvoda(slug) {
      const { data } = await api.get(`/e-trznica/opgovi/${slug}/kategorije-proizvoda`)
      this.katProizvodi = data
    },

    async ucitajKategorijeUsluga(slug) {
      const { data } = await api.get(`/e-trznica/opgovi/${slug}/kategorije-usluga`)
      this.katUsluge = data
    },

    async ucitajProizvode(slug, { stranica = 1, velicina = 12 } = {}) {
      this.proizvodi.loading = true
      try {
        const params = { stranica, velicina, kat_slug: this.aktivnaKatProizvoda || undefined }
        const { data } = await api.get(`/e-trznica/opgovi/${slug}/proizvodi`, { params })
        this.proizvodi = { ...data, loading: false }
      } finally {
        this.proizvodi.loading = false
      }
    },

    async ucitajUsluge(slug, { stranica = 1, velicina = 12, kat_slug } = {}) {
      this.usluge.loading = true
      try {
        const params = { stranica, velicina, kat_slug: this.aktivnaKatUsluge || undefined }
        const { data } = await api.get(`/e-trznica/opgovi/${slug}/usluge`, { params })
        this.usluge = { ...data, loading: false }
      } finally {
        this.usluge.loading = false
      }
    },

    async postaviAktivnuKatProizvoda(slug, opgSlug) {
      this.aktivnaKatProizvoda = slug || null
      await this.ucitajProizvode(opgSlug)
    },

    async postaviAktivnuKatUsluge(slug, opgSlug) {
      this.aktivnaKatUsluge = slug || null
      await this.ucitajUsluge(opgSlug)
    },

    async ucitajRecenzije(slug, { stranica = 1, velicina = 10 } = {}) {
      this.recenzije.loading = true
      try {
        const { data } = await api.get(`/e-trznica/opgovi/${slug}/recenzije`, {
          params: { stranica, velicina },
        })
        this.recenzije.lista_recenzija = data.recenzije || []
        this.recenzije.ukupno = data.ukupno_recenzija || 0
        this.recenzije.stranica = stranica
        this.recenzije.velicina = velicina
      } finally {
        this.recenzije.loading = false
      }
    },

    async posaljiOcjenu(slug, { ocjena, komentar }) {
      try {
        await api.post(`/e-trznica/opgovi/${slug}/recenzije`, { ocjena, komentar })
        await Promise.all([
          this.ucitajDetaljeOpga(slug),
          this.ucitajRecenzije(slug, { stranica: 1, velicina: this.recenzije.velicina }),
        ])
        return { ok: true }
      } catch (e) {
        const status = e?.response?.status
        if (status === 401) {
          return { ok: false, reason: "unauth" }
        }
        return { ok: false, reason: "other", message: e?.response?.data?.detail || "Greška" }
      }
    },
  },
})
