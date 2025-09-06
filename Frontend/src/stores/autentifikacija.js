import { defineStore } from "pinia"
import axios from "axios"

const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

const api = axios.create({
  baseURL: BASE_URL,
})

function postaviAutentifikacijskiHeader(token) {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`
  } else {
    delete api.defaults.headers.common["Authorization"]
  }
}

export const useAutentifikacijskiStore = defineStore("autentifikacija", {
  state: () => ({
    token: localStorage.getItem("token") || null,
    tip_korisnika: localStorage.getItem("tip_korisnika") || null,
    loading: false,
    error: null,
  }),

  getters: {
    korisnikAutentificiran: (state) => !!state.token,
  },

  actions: {
    init() {
      if (this.token) postaviAutentifikacijskiHeader(this.token)
    },

    async registrirajKupca(payload) {
      this.loading = true
      this.error = null
      try {
        const { data } = await api.post("/autentifikacija/registracija/kupac", payload)
        this.token = data.access_token
        this.tip_korisnika = data.tip_korisnika
        localStorage.setItem("token", this.token)
        localStorage.setItem("tip_korisnika", this.tip_korisnika)
        postaviAutentifikacijskiHeader(this.token)
        return true
      } catch (e) {
        this.error = e?.response?.data?.detail || e?.message || "Greška pri registraciji"
        return false
      } finally {
        this.loading = false
      }
    },

    async registrirajOpg(payload) {
      this.loading = true
      this.error = null
      try {
        const { data } = await api.post("/autentifikacija/registracija/opg", payload)
        this.token = data.access_token
        this.tip_korisnika = data.tip_korisnika
        localStorage.setItem("token", this.token)
        localStorage.setItem("tip_korisnika", this.tip_korisnika)
        postaviAutentifikacijskiHeader(this.token)
        return true
      } catch (e) {
        this.error = e?.response?.data?.detail || e?.message || "Greška pri registraciji"
        return false
      } finally {
        this.loading = false
      }
    },

    async prijava({ email_ili_korisnicko_ime, lozinka }) {
      this.loading = true
      this.error = null
      try {
        const { data } = await api.post("/autentifikacija/prijava", {
          email_ili_korisnicko_ime: email_ili_korisnicko_ime,
          lozinka,
        })
        this.token = data.access_token
        this.tip_korisnika = data.tip_korisnika
        localStorage.setItem("token", this.token)
        localStorage.setItem("tip_korisnika", this.tip_korisnika)
        postaviAutentifikacijskiHeader(this.token)
        return true
      } catch (e) {
        console.error(e?.response?.data)
        this.error = e?.response?.data?.detail || e?.message || "Neuspješna prijava"
        return false
      } finally {
        this.loading = false
      }
    },

    odjava() {
      this.token = null
      this.tip_korisnika = null
      this.error = null
      localStorage.removeItem("token")
      localStorage.removeItem("tip_korisnika")
      postaviAutentifikacijskiHeader(null)
    },
  },
})
