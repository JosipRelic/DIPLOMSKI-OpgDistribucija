import { createRouter, createWebHistory } from "vue-router"
import PocetnaView from "@/views/PocetnaView.vue"

const routes = [
  {
    name: "pocetna",
    path: "/",
    component: PocetnaView,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
