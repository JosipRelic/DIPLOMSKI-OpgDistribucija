import { createRouter, createWebHistory } from "vue-router"
import PocetnaView from "@/views/PocetnaView.vue"
import ETrznicaView from "@/views/ETrznicaView.vue"
import FarmaPlusView from "@/views/FarmaPlusView.vue"
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
import ProfilKupacPostavkeView from "@/views/profili/kupac/ProfilKupacPostavke.vue"

const routes = [
  {
    name: "pocetna",
    path: "/",
    component: PocetnaView,
  },
  {
    path: "/profil/kupac",
    component: ProfilKupacView,
    children: [
      {
        path: "",
        name: "profilKupacNadzornaPloca",
        component: ProfilKupacNadzornaPlocaView,
      },
      {
        path: "moje-narudzbe",
        name: "profilKupacMojeNarudzbe",
        component: ProfilKupacMojeNarudzbeView,
      },
      {
        path: "postavke-profila",
        name: "profilKupacPostavke",
        component: ProfilKupacPostavkeView,
      },
    ],
  },
  {
    name: "e-trznica",
    path: "/e-trznica",
    component: ETrznicaView,
  },
  {
    name: "farmaPlus",
    path: "/farma-plus",
    component: FarmaPlusView,
  },
  {
    name: "kosarica",
    path: "/kosarica",
    component: KosaricaView,
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

export default router
