import { createRouter, createWebHistory } from "vue-router"
import PocetnaView from "@/views/PocetnaView.vue"
import ETrznicaView from "@/views/etrznica/ETrznicaView.vue"
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
import ETrznicaKategorijaProizvodaView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaView.vue"
import ETrznicaKategorijaProizvodaDomaceVoceView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaDomaceVoceView.vue"
import ETrznicaKategorijaProizvodaSezonskoPovrceView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaSezonskoPovrceView.vue"
import ETrznicaKategorijaProizvodaJajaiMlijecniProizvodiView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaJajaiMlijecniProizvodiView.vue"
import ETrznicaKategorijaProizvodaIzKosniceView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaIzKosniceView.vue"
import ETrznicaKategorijaProizvodaPicaiRakijeView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaPicaiRakijeView.vue"
import ETrznicaKategorijaProizvodaUljaizPrirodeView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaUljaizPrirodeView.vue"
import ETrznicaKategorijaProizvodaCajeviZacinskoBiljeView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaCajeviZacinskoBiljeView.vue"
import ETrznicaKategorijaProizvodaSuhomesnatoView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaSuhomesnatoView.vue"
import ETrznicaKategorijaProizvodaPrirodnaKozmetikaView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaPrirodnaKozmetikaView.vue"
import ETrznicaKategorijaProizvodaIzSumeiDvoristaView from "@/views/etrznica/kategorije-proizvoda/ETrznicaKategorijaProizvodaIzSumeiDvoristaView.vue"
import ProizvodDetaljiView from "@/views/etrznica/kategorije-proizvoda/detalji-proizvoda/ProizvodDetaljiView.vue"
import ETrznicaDetaljiOPGaView from "@/views/etrznica/ETrznicaDetaljiOPGaView.vue"
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
    meta: { requiresAuth: true },
    children: [
      {
        path: "",
        redirect: { name: "profilKupacNadzornaPloca" },
      },
      {
        path: "nadzorna-ploca",
        name: "profilKupacNadzornaPloca",
        component: ProfilKupacNadzornaPlocaView,
        meta: { requiresAuth: true },
      },
      {
        path: "moje-narudzbe",
        name: "profilKupacMojeNarudzbe",
        component: ProfilKupacMojeNarudzbeView,
        meta: { requiresAuth: true },
      },
      {
        path: "moje-narudzbe/detalji-narudzbe",
        name: "profilKupacMojeNarudzbeDetaljiNarudzbe",
        component: ProfilKupacMojeNarudzbeDetaljiNarudzbeView,
        meta: { requiresAuth: true },
      },
      {
        path: "postavke-profila",
        name: "profilKupacPostavke",
        component: ProfilKupacPostavkeView,
        meta: { requiresAuth: true },
      },
    ],
  },
  {
    path: "/profil/opg",
    component: ProfilOpgView,
    meta: { requiresAuth: true },
    children: [
      {
        path: "",
        redirect: { name: "profilOpgNadzornaPloca" },
      },
      {
        path: "nadzorna-ploca",
        name: "profilOpgNadzornaPloca",
        component: ProfilOpgNadzornaPlocaView,
        meta: { requiresAuth: true },
      },
      {
        path: "primljene-narudzbe",
        name: "profilOpgPrimljeneNarudzbe",
        component: ProfilOpgPrimljeneNarudzbeView,
        meta: { requiresAuth: true },
      },
      {
        path: "primljene-narudzbe/detalji-narudzbe",
        name: "profilOpgPrimljeneNarudzbeDetaljiNarudzbe",
        component: ProfilOpgPrimljeneNarudzbeDetaljiNarudzbeView,
        meta: { requiresAuth: true },
      },
      {
        path: "postavke-profila",
        name: "profilOpgPostavke",
        component: ProfilOpgPostavkeView,
        meta: { requiresAuth: true },
      },
      {
        path: "ponuda-etrznica",
        name: "profilOpgPonudaETrznica",
        component: ProfilOpgPonudaETrznicaView,
        meta: { requiresAuth: true },
      },

      {
        path: "ponuda-farmaplus",
        name: "profilOpgPonudaFarmaPlus",
        component: ProfilOpgPonudaFarmaPlusView,
        meta: { requiresAuth: true },
      },
      {
        path: "detalji-kupca",
        name: "profilOpgDetaljiKupca",
        component: ProfilOpgDetaljiKupcaView,
        meta: { requiresAuth: true },
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
    path: "/e-trznica/detalji-opga",
    component: ETrznicaDetaljiOPGaView,
  },
  {
    path: "/e-trznica/kategorija-proizvoda",
    component: ETrznicaKategorijaProizvodaView,
    children: [
      {
        path: "",
        redirect: { name: "e-trznica" },
      },
      {
        name: "ETrznicaKategorijaDomaceVoce",
        path: "domace-voce",
        component: ETrznicaKategorijaProizvodaDomaceVoceView,
      },
      {
        name: "ETrznicaKategorijaSezonskoPovrce",
        path: "sezonsko-povrce",
        component: ETrznicaKategorijaProizvodaSezonskoPovrceView,
      },
      {
        name: "ETrznicaKategorijaJajaiMlijecniProizvodi",
        path: "jaja-i-mlijecni-proizvodi",
        component: ETrznicaKategorijaProizvodaJajaiMlijecniProizvodiView,
      },
      {
        name: "ETrznicaKategorijaIzKosnice",
        path: "iz-kosnice",
        component: ETrznicaKategorijaProizvodaIzKosniceView,
      },
      {
        name: "ETrznicaKategorijaPicaiRakije",
        path: "pica-i-rakije",
        component: ETrznicaKategorijaProizvodaPicaiRakijeView,
      },
      {
        name: "ETrznicaKategorijaUljaizPrirode",
        path: "ulja-iz-prirode",
        component: ETrznicaKategorijaProizvodaUljaizPrirodeView,
      },
      {
        name: "ETrznicaKategorijaCajeviZacinskoBilje",
        path: "cajevi-i-zacinsko-bilje",
        component: ETrznicaKategorijaProizvodaCajeviZacinskoBiljeView,
      },
      {
        name: "ETrznicaKategorijaSuhomesnato",
        path: "suhomesnati-proizvodi",
        component: ETrznicaKategorijaProizvodaSuhomesnatoView,
      },
      {
        name: "ETrznicaKategorijaPrirodnaKozmetika",
        path: "prirodna-kozmetika",
        component: ETrznicaKategorijaProizvodaPrirodnaKozmetikaView,
      },
      {
        name: "ETrznicaKategorijaIzSumeiDvorista",
        path: "iz-sume-i-dvorista",
        component: ETrznicaKategorijaProizvodaIzSumeiDvoristaView,
      },
    ],
  },
  {
    name: "krastavci",
    path: "/e-trznica/kategorija-proizvoda/sezonsko-povrce/krastavci",
    component: ProizvodDetaljiView,
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

router.beforeEach((to, from, next) => {
  const autentifikacija = useAutentifikacijskiStore()
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!autentifikacija.korisnikAutentificiran) {
      return next({ name: "prijava" })
    }
  }
  next()
})

export default router
