import "./assets/base.css"

import { createApp } from "vue"
import { createPinia } from "pinia"

import App from "./App.vue"
import router from "./router"
import { useAutentifikacijskiStore } from "./stores/autentifikacija"

const app = createApp(App)

app.use(createPinia())
app.use(router)
const autentifikacija = useAutentifikacijskiStore()
autentifikacija.init()

app.mount("#app")
