import { createRouter, createWebHistory } from "vue-router"
import PocetnaView from "@/views/PocetnaView.vue"
import ETrznicaView from "@/views/etrznica/ETrznicaView.vue"
import FarmaPlusView from "@/views/farma_plus/FarmaPlusView.vue"
import RegistracijaOPGView from "@/views/autentifikacija/RegistracijaOPGView.vue"
import RegistracijaKupacView from "@/views/autentifikacija/RegistracijaKupacView.vue"
import RegistracijaOdabirKorisnikaView from "@/views/autentifikacija/RegistracijaOdabirKorisnikaView.vue"
import PrijavaView from "@/views/autentifikacija/PrijavaView.vue"
import KosaricaView from "@/views/narudzba/KosaricaView.vue"
import ZaboravljenaLozinkaView from "@/views/autentifikacija/ZaboravljenaLozinkaView.vue"
import PregledNarudzbeView from "@/views/narudzba/PregledNarudzbeView.vue"
import PotvrdaNarudzbeView from "@/views/narudzba/PotvrdaNarudzbeView.vue"
import ProfilKupacView from "@/views/profili/kupac/ProfilKupacView.vue"
import ProfilKupacNadzornaPlocaView from "@/views/profili/kupac/ProfilKupacNadzornaPlocaView.vue"
import ProfilKupacMojeNarudzbeView from "@/views/profili/kupac/ProfilKupacMojeNarudzbeView.vue"
import ProfilKupacPostavkeView from "@/views/profili/kupac/ProfilKupacPostavkeView.vue"
import ProfilKupacMojeNarudzbeDetaljiNarudzbeView from "@/views/profili/kupac/ProfilKupacMojeNarudzbeDetaljiNarudzbeView.vue"
import ProfilOpgView from "@/views/profili/opg/ProfilOpgView.vue"
import ProfilOpgNadzornaPlocaView from "@/views/profili/opg/ProfilOpgNadzornaPlocaView.vue"
import ProfilOpgPrimljeneNarudzbeView from "@/views/profili/opg/ProfilOpgPrimljeneNarudzbeView.vue"
import ProfilOpgPrimljeneNarudzbeDetaljiNarudzbeView from "@/views/profili/opg/ProfilOpgPrimljeneNarudzbeDetaljiNarudzbeView.vue"
import ProfilOpgPostavkeView from "@/views/profili/opg/ProfilOpgPostavkeView.vue"
import ProfilOpgPonudaETrznicaView from "@/views/profili/opg/ProfilOpgPonudaETrznicaView.vue"
import ProfilOpgPonudaFarmaPlusView from "@/views/profili/opg/ProfilOpgPonudaFarmaPlusView.vue"
import ProfilOpgDetaljiKupcaView from "@/views/profili/opg/ProfilOpgDetaljiKupcaView.vue"
import ETrznicaKategorijaProizvodaView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaView.vue"
import ETrznicaProizvodDetaljiView from "@/views/etrznica/kategorije-proizvoda/detalji-proizvoda/ETrznicaProizvodDetaljiView.vue"
import ETrznicaDetaljiOPGaView from "@/views/etrznica/ETrznicaDetaljiOPGaView.vue"
import FarmaPlusDetaljiUslugeView from "@/views/farma_plus/FarmaPlusDetaljiUslugeView.vue"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"

const routes = [
  {
    name: "pocetna",
    path: "/",
    component: PocetnaView,
  },
  {
    path: "/profil/kupac",
    component: ProfilKupacView,
    meta: { requiresAuth: true, roles: ["Kupac"] },
    children: [
      {
        path: "",
        redirect: { name: "profilKupacNadzornaPloca" },
      },
      {
        path: "nadzorna-ploca",
        name: "profilKupacNadzornaPloca",
        component: ProfilKupacNadzornaPlocaView,
        meta: { requiresAuth: true, roles: ["Kupac"] },
      },
      {
        path: "moje-narudzbe",
        name: "profilKupacMojeNarudzbe",
        component: ProfilKupacMojeNarudzbeView,
        meta: { requiresAuth: true, roles: ["Kupac"] },
      },
      {
        path: "moje-narudzbe/detalji-narudzbe",
        name: "profilKupacMojeNarudzbeDetaljiNarudzbe",
        component: ProfilKupacMojeNarudzbeDetaljiNarudzbeView,
        meta: { requiresAuth: true, roles: ["Kupac"] },
      },
      {
        path: "postavke-profila",
        name: "profilKupacPostavke",
        component: ProfilKupacPostavkeView,
        meta: { requiresAuth: true, roles: ["Kupac"] },
      },
    ],
  },
  {
    path: "/profil/opg",
    component: ProfilOpgView,
    meta: { requiresAuth: true, roles: ["Opg"] },
    children: [
      {
        path: "",
        redirect: { name: "profilOpgNadzornaPloca" },
      },
      {
        path: "nadzorna-ploca",
        name: "profilOpgNadzornaPloca",
        component: ProfilOpgNadzornaPlocaView,
        meta: { requiresAuth: true, roles: ["Opg"] },
      },
      {
        path: "primljene-narudzbe",
        name: "profilOpgPrimljeneNarudzbe",
        component: ProfilOpgPrimljeneNarudzbeView,
        meta: { requiresAuth: true, roles: ["Opg"] },
      },
      {
        path: "primljene-narudzbe/detalji-narudzbe",
        name: "profilOpgPrimljeneNarudzbeDetaljiNarudzbe",
        component: ProfilOpgPrimljeneNarudzbeDetaljiNarudzbeView,
        meta: { requiresAuth: true, roles: ["Opg"] },
      },
      {
        path: "postavke-profila",
        name: "profilOpgPostavke",
        component: ProfilOpgPostavkeView,
        meta: { requiresAuth: true, roles: ["Opg"] },
      },
      {
        path: "ponuda-etrznica",
        name: "profilOpgPonudaETrznica",
        component: ProfilOpgPonudaETrznicaView,
        meta: { requiresAuth: true, roles: ["Opg"] },
      },

      {
        path: "ponuda-farmaplus",
        name: "profilOpgPonudaFarmaPlus",
        component: ProfilOpgPonudaFarmaPlusView,
        meta: { requiresAuth: true, roles: ["Opg"] },
      },
      {
        path: "detalji-kupca",
        name: "profilOpgDetaljiKupca",
        component: ProfilOpgDetaljiKupcaView,
        meta: { requiresAuth: true, roles: ["Opg"] },
      },
    ],
  },

  {
    name: "e-trznica",
    path: "/e-trznica",
    component: ETrznicaView,
  },
  {
    name: "ETrznicaDetaljiOPGa",
    path: "/e-trznica/detalji-opga/:opgSlug",
    component: ETrznicaDetaljiOPGaView,
  },
  {
    path: "/e-trznica/kategorija-proizvoda/:slug",
    component: ETrznicaKategorijaProizvodaView,
    name: "ETrznicaKategorija",
  },
  {
    name: "ETrznicaProizvodDetalji",
    path: "/e-trznica/kategorija-proizvoda/:katSlug/:proizvodSlugId",
    component: ETrznicaProizvodDetaljiView,
  },

  {
    name: "farmaPlus",
    path: "/farma-plus",
    component: FarmaPlusView,
  },
  {
    name: "farmaPlusDetaljiUsluge",
    path: "/farma-plus/detalji-usluge/:uslugaSlugId",
    component: FarmaPlusDetaljiUslugeView,
  },
  {
    name: "kosarica",
    path: "/kosarica",
    component: KosaricaView,
    meta: { requiresAuth: true },
  },
  {
    name: "pregledNarudzbe",
    path: "/pregled-narudzbe",
    component: PregledNarudzbeView,
  },
  {
    name: "potvrdaNarudzbe",
    path: "/potvrda-narudzbe",
    component: PotvrdaNarudzbeView,
  },
  {
    name: "registracija",
    path: "/registracija",
    component: RegistracijaOdabirKorisnikaView,
  },

  {
    name: "registracijaKupac",
    path: "/registracija/kupac",
    component: RegistracijaKupacView,
  },

  {
    name: "registracijaOPG",
    path: "/registracija/opg",
    component: RegistracijaOPGView,
  },

  {
    name: "prijava",
    path: "/prijava",
    component: PrijavaView,
  },
  {
    name: "zaboravljenaLozinka",
    path: "/zaboravljena-lozinka",
    component: ZaboravljenaLozinkaView,
  },
  {
    path: "/:catchAll(.*)",
    redirect: { name: "pocetna" },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

router.beforeEach(async (to) => {
  const auth = useAutentifikacijskiStore()

  if (auth.token && auth.expires_at && Date.now() >= auth.expires_at) {
    await auth.odjava("expired", { redirect: false })
    return { name: "prijava", query: { redirect: to.fullPath, expired: 1 } }
  }

  const requiresAuth = to.matched.some((r) => r.meta?.requiresAuth)
  if (requiresAuth && !auth.korisnikAutentificiran) {
    return { name: "prijava", query: { redirect: to.fullPath } }
  }

  const rec = [...to.matched].reverse().find((r) => r.meta?.roles)
  const allowed = rec?.meta?.roles || null
  if (!allowed) return true

  let role = auth.tip_korisnika

  if (!role && auth.korisnikAutentificiran) {
    try {
      await auth.dohvatiProfil()
      role = auth.tip_korisnika || auth.korisnicki_profil?.tip_korisnika
    } catch (e) {
      const expired = e?.response?.status === 401
      await auth.odjava(expired ? "expired" : "manual", { redirect: false })
      return { name: "prijava", query: { redirect: to.fullPath, expired: expired ? 1 : undefined } }
    }
  }

  if (!role || !allowed.includes(role)) {
    if (role === "Kupac") return { name: "profilKupacNadzornaPloca" }
    if (role === "Opg") return { name: "profilOpgNadzornaPloca" }
    return { name: "pocetna" }
  }

  return true
})

export default router
