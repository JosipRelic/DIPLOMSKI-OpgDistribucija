import { createRouter, createWebHistory } from "vue-router"
import PocetnaView from "@/views/PocetnaView.vue"
import ETrznicaView from "@/views/ETrznicaView.vue"

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
    path: "/:catchAll(.*)",
    redirect: { name: "pocetna" },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
