import { createRouter, createWebHistory } from "vue-router"
import PocetnaView from "@/views/PocetnaView.vue"
import ETrznicaView from "@/views/ETrznicaView.vue"
import FarmaPlusView from "@/views/FarmaPlusView.vue"
import RegistracijaOPGView from "@/views/autentifikacija/RegistracijaOPGView.vue"
import RegistracijaKupacView from "@/views/autentifikacija/RegistracijaKupacView.vue"
import RegistracijaOdabirKorisnikaView from "@/views/autentifikacija/RegistracijaOdabirKorisnikaView.vue"
import PrijavaView from "@/views/autentifikacija/PrijavaView.vue"

const routes = [
  {
    name: "pocetna",
    path: "/",
    component: PocetnaView,
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
    path: "/:catchAll(.*)",
    redirect: { name: "pocetna" },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
