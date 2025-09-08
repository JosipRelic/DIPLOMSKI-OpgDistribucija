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
    korisnicki_profil: null,
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
        await this.dohvatiProfil()
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
        await this.dohvatiProfil()
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
        await this.dohvatiProfil()
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

    async dohvatiProfil() {
      if (!this.token) return null
      try {
        const { data } = await api.get("/profil/moj-profil")
        this.korisnicki_profil = data
        return data
      } catch (e) {
        this.token = null
        this.korisnicki_profil = null
        localStorage.removeItem("token")
        postaviAutentifikacijskiHeader(null)
        return null
      }
    },

    async azurirajProfil(payload) {
      this.loading = true
      this.error = null
      try {
        const { data } = await api.put("/profil", payload)
        this.korisnicki_profil = data
        return true
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška pri ažuriranju profila."
        return false
      } finally {
        this.loading = false
      }
    },

    async ucitajSlikuProfila(slika) {
      const form = new FormData()
      form.append("slika", slika)
      try {
        const { data } = await api.post("/profil/slika-profila", form, {
          headers: { "Content-Type": "multipart/form-data" },
        })
        this.korisnicki_profil = data
        return true
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška pri učitavanju slike"
        return false
      } finally {
        this.loading = false
      }
    },
  },
})
