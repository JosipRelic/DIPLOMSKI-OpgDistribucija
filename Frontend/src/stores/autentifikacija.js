import { defineStore } from "pinia"
import api from "@/services/api"
import { useUiStore } from "./ui"
import { useKosaricaStore } from "./kosarica"

function postaviAutentifikacijskiHeader(token) {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`
  } else {
    delete api.defaults.headers.common["Authorization"]
  }
}

function decodeExpMs(token) {
  try {
    const { exp } = JSON.parse(atob(token.split(".")[1]))
    return exp ? exp * 1000 : null
  } catch {
    return null
  }
}

export const useAutentifikacijskiStore = defineStore("autentifikacija", {
  state: () => ({
    token: localStorage.getItem("token") || null,
    tip_korisnika: localStorage.getItem("tip_korisnika") || null,
    korisnicki_profil: null,
    loading: false,
    error: null,
    expires_at: Number(localStorage.getItem("expires_at") || 0),
    _logoutTimerId: null,
    _axiosInterceptorAttached: false,
  }),

  getters: {
    korisnikAutentificiran: (state) => !!state.token,
  },

  actions: {
    _scheduleAutoLogout(ms) {
      if (this._logoutTimerId) clearTimeout(this._logoutTimerId)
      if (ms > 0) {
        this._logoutTimerId = setTimeout(() => this.odjava("expired"), ms)
      }
    },

    init() {
      if (this.token) {
        postaviAutentifikacijskiHeader(this.token)
        const expMs = decodeExpMs(this.token)
        if (expMs) {
          this.expires_at = expMs
          localStorage.setItem("expires_at", String(expMs))
          if (Date.now() >= expMs) {
            this.odjava("expired")
          } else {
            this._scheduleAutoLogout(expMs - Date.now())
            this.dohvatiProfil().catch(() => {})

            try {
              useKosaricaStore().osvjezi()
            } catch {}
          }
        }
      }

      window.addEventListener("storage", (e) => {
        if (e.key === "token" && !e.newValue) this.odjava()
      })

      if (!this._axiosInterceptorAttached) {
        api.interceptors.response.use(
          (res) => res,
          (err) => {
            const status = err?.response?.status
            const url = (err?.config?.url || "").toString()
            const isAuthCall =
              url.includes("/autentifikacija/prijava") ||
              url.includes("/autentifikacija/registracija")

            if (status === 401 && this.token && !isAuthCall) {
              this.odjava("expired")
            }
            return Promise.reject(err)
          },
        )
        this._axiosInterceptorAttached = true
      }
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

        const expMs = decodeExpMs(this.token)
        if (expMs) {
          this.expires_at = expMs
          localStorage.setItem("expires_at", String(expMs))
          this._scheduleAutoLogout(expMs - Date.now())
        }

        await this.dohvatiProfil()
        await useKosaricaStore().osvjezi()
        useUiStore().obavijest({
          tekst: "Registacija uspješna. Dobrodošli!",
          tip_obavijesti: "uspjeh",
        })
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

        const expMs = decodeExpMs(this.token)
        if (expMs) {
          this.expires_at = expMs
          localStorage.setItem("expires_at", String(expMs))
          this._scheduleAutoLogout(expMs - Date.now())
        }

        await this.dohvatiProfil()
        await useKosaricaStore().osvjezi()
        useUiStore().obavijest({
          tekst: "Registacija uspješna. Dobrodošli!",
          tip_obavijesti: "uspjeh",
        })
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

        const expMs = decodeExpMs(this.token)
        if (expMs) {
          this.expires_at = expMs
          localStorage.setItem("expires_at", String(expMs))
          this._scheduleAutoLogout(expMs - Date.now())
        }

        await this.dohvatiProfil()
        await useKosaricaStore().osvjezi()
        useUiStore().obavijest({
          tekst: "Prijava uspješna. Dobrodošli!",
          tip_obavijesti: "uspjeh",
        })
        return true
      } catch (e) {
        console.error(e?.response?.data)
        this.error = e?.response?.data?.detail || e?.message || "Neuspješna prijava"
        return false
      } finally {
        this.loading = false
      }
    },

    async odjava(reason = "manual", { redirect = true } = {}) {
      if (this._logoutTimerId) {
        clearTimeout(this._logoutTimerId)
        this._logoutTimerId = null
      }
      this.token = null
      this.tip_korisnika = null
      this.error = null
      this.expires_at = 0
      localStorage.removeItem("token")
      localStorage.removeItem("tip_korisnika")
      localStorage.removeItem("expires_at")
      postaviAutentifikacijskiHeader(null)

      try {
        useKosaricaStore().reset()
      } catch {}

      const ui = useUiStore()
      if (reason === "expired") {
        ui.obavijest({
          tekst: "Vaša sesija je istekla. Prijavite se ponovno.",
          tip_obavijesti: "upozorenje",
        })
      }

      if (reason === "manual") {
        ui.obavijest({
          tekst: "Odjavljeni ste.",
          tip_obavijesti: "uspjeh",
        })
      }

      if (redirect) {
        const { default: router } = await import("@/router")
        const cur = router.currentRoute.value
        const authRoutes = new Set([
          "prijava",
          "registracija",
          "registracijaKupac",
          "registracijaOPG",
          "zaboravljenaLozinka",
        ])
        if (!authRoutes.has(cur.name)) {
          router.replace({
            name: "prijava",
            query: { redirect: cur.fullPath, expired: reason === "expired" ? 1 : undefined },
          })
        }
      }
    },

    async dohvatiProfil() {
      if (!this.token) return null
      try {
        const { data } = await api.get("/profil/moj-profil")
        this.korisnicki_profil = data
        return data
      } catch (e) {
        throw e
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

    async zatraziLinkZaOporavak(email) {
      try {
        await api.post("/autentifikacija/zaboravljena-lozinka", null, { params: { email } })
        return { ok: true }
      } catch (e) {
        return {
          ok: false,
          error: e?.response?.data?.detail || e?.message || "Greška pri slanju zahtjeva",
        }
      }
    },

    async promijeniLozinkuToken({ token, nova_lozinka, potvrda_lozinke }) {
      try {
        await api.post("/autentifikacija/promjena-lozinke", {
          token,
          nova_lozinka,
          potvrda_lozinke,
        })
        return { ok: true }
      } catch (e) {
        return {
          ok: false,
          error: e?.response?.data?.detail || e?.message || "Neuspješna promjena lozinke",
        }
      }
    },

    async obrisiProfil() {
      try {
        await api.delete("/profil")
        useKosaricaStore().reset()
        this.korisnicki_profil = null
        this.token = null
        localStorage.removeItem("token")
        return true
      } catch (e) {
        this.error = e.response?.data?.detail || "Greška pri brisanju profila"
        return false
      }
    },
  },
})
