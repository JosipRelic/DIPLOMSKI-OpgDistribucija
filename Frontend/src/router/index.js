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
        path: "moje-narudzbe/detalji-narudzbe",
        name: "profilKupacMojeNarudzbeDetaljiNarudzbe",
        component: ProfilKupacMojeNarudzbeDetaljiNarudzbeView,
      },
      {
        path: "postavke-profila",
        name: "profilKupacPostavke",
        component: ProfilKupacPostavkeView,
      },
    ],
  },
  {
    path: "/profil/opg",
    component: ProfilOpgView,
    children: [
      {
        path: "",
        name: "profilOpgNadzornaPloca",
        component: ProfilOpgNadzornaPlocaView,
      },
      {
        path: "primljene-narudzbe",
        name: "profilOpgPrimljeneNarudzbe",
        component: ProfilOpgPrimljeneNarudzbeView,
      },
      {
        path: "primljene-narudzbe/detalji-narudzbe",
        name: "profilOpgPrimljeneNarudzbeDetaljiNarudzbe",
        component: ProfilOpgPrimljeneNarudzbeDetaljiNarudzbeView,
      },
      {
        path: "postavke-profila",
        name: "profilOpgPostavke",
        component: ProfilOpgPostavkeView,
      },
      {
        path: "ponuda-etrznica",
        name: "profilOpgPonudaETrznica",
        component: ProfilOpgPonudaETrznicaView,
      },
      {
        path: "ponuda-farmaplus",
        name: "profilOpgPonudaFarmaPlus",
        component: ProfilOpgPonudaFarmaPlusView,
      },
      {
        path: "detalji-kupca",
        name: "profilOpgDetaljiKupca",
        component: ProfilOpgDetaljiKupcaView,
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
