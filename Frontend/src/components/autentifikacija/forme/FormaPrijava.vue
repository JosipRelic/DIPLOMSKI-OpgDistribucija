<template>
  <div class="min-h-screen text-gray-900 flex justify-center">
    <div
      class="max-w-screen-xl m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1"
    >
      <div class="lg:w-1/2 xl:w-5/12 p-6 sm:p-12">
        <div>
          <img :src="slikeLogo" class="w-16 mx-auto" />
        </div>
        <div class="mt-12 flex flex-col items-center">
          <h1 class="text-2xl xl:text-3xl font-extrabold">Prijava</h1>
          <div v-if="showExpired" class="mt-6 rounded-lg bg-amber-50 text-amber-800 px-3 py-2">
            Vaša sesija je istekla. Prijavite se ponovno.
          </div>
          <form class="w-full flex-1 mt-8" @submit.prevent="posaljiPodatkeZaPrijavu">
            <div class="flex flex-col items-center">
              <GumbZaGlasovnoPopunjavanje strukturaUpita="prijava" @popuni="popuniFormuPomocuAI" />
              <small class="ps-2 pt-2 w-full max-w-xs"
                >Pritisnite gumb i popunite obrazac glasom npr. "Moja email adresa je
                ihorvat@gmail.com"</small
              >
            </div>

            <div class="my-12 border-b text-center">
              <div
                class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
              >
                ili unesite podatke ručno
              </div>
            </div>

            <div class="mx-auto max-w-xs">
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white"
                type="text"
                placeholder="Email ili korisničko ime"
                v-model="formaPrijave.email_ili_korisnicko_ime"
              />

              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="password"
                placeholder="Lozinka"
                v-model="formaPrijave.lozinka"
              />

              <button
                class="mt-5 tracking-wide font-semibold bg-teal-600 hover:bg-teal-900 text-gray-100 w-full py-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none"
                type="submit"
                :disabled="autentifikacija.loading"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 16 17">
                  <g fill="currentColor" fill-rule="evenodd">
                    <path
                      d="M11.959 4.917V1H1.096L9 3.666v12.251L1.219 14l-.215.829L9.959 17v-3.085h2v-2.873l-2.865-3l2.865-3.125z"
                    />
                    <path
                      d="m11.1 8.102l2.87 2.931V8.968h2.046V6.98H13.97V5.068L11.1 8.102zM7 9h.958v.916H7z"
                    />
                  </g>
                </svg>
                <span class="ml-3">
                  {{ autentifikacija.loading ? "Prijavljujem..." : "Prijava" }}
                </span>
              </button>

              <p v-if="autentifikacija.error" class="text-red-600 mt-1">
                {{ autentifikacija.error }}
              </p>

              <p class="mt-6 text-sm text-gray-800 text-center">
                <router-link
                  :to="{ name: 'zaboravljenaLozinka' }"
                  class="mt-6 text-center text-md border-b border-gray-500 border-dotted"
                >
                  Zaboravili ste lozinku?
                </router-link>
              </p>
              <p class="mt-2 text-sm text-gray-800 text-center">
                <router-link
                  :to="{ name: 'registracija' }"
                  class="mt-6 text-center text-md border-b border-gray-500 border-dotted"
                >
                  Nemate račun? Registrirajte se ovdje.
                </router-link>
              </p>
            </div>
          </form>
        </div>
      </div>
      <div
        class="flex-1 bg-indigo-100 text-center bg-cover bg-center hidden lg:flex"
        :style="`background-image: url(${slikeFormaPrijave});`"
      ></div>
    </div>
  </div>
</template>
<script setup>
import slikeLogo from "@/assets/slike/logo.png"
import slikeFormaPrijave from "@/assets/slike/forma-prijave.png"
import { ref, watch, reactive, onUnmounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import GumbZaGlasovnoPopunjavanje from "@/components/ai/GumbZaGlasovnoPopunjavanje.vue"
import { primijeniPodatkeOdAIuFormu } from "@/ai/primijeniPodatkeOdAIuFormu"

const autentifikacija = useAutentifikacijskiStore()
const router = useRouter()
const route = useRoute()

const formaPrijave = reactive({
  email_ili_korisnicko_ime: "",
  lozinka: "",
})

const showExpired = ref(false)
let hideTimer = null

function clearExpiredParam() {
  if (route.query.expired) {
    const q = { ...route.query }
    delete q.expired
    router.replace({ query: q })
  }
}

watch(
  () => route.query.expired,
  (val) => {
    if (val === "1") {
      showExpired.value = true
      if (hideTimer) clearTimeout(hideTimer)
      hideTimer = setTimeout(() => {
        showExpired.value = false
        clearExpiredParam()
      }, 5000)
    }
  },
  { immediate: true },
)

onUnmounted(() => {
  if (hideTimer) clearTimeout(hideTimer)
})

const posaljiPodatkeZaPrijavu = async () => {
  showExpired.value = false
  clearExpiredParam()
  autentifikacija.error = null

  const ok = await autentifikacija.prijava({
    email_ili_korisnicko_ime: formaPrijave.email_ili_korisnicko_ime,
    lozinka: formaPrijave.lozinka,
  })

  if (ok) {
    if (autentifikacija.tip_korisnika === "Kupac") {
      router.push({ name: "profilKupacNadzornaPloca" })
    } else if (autentifikacija.tip_korisnika === "Opg") {
      router.push({ name: "profilOpgNadzornaPloca" })
    } else {
      router.push({ name: "pocetna" })
    }
  }
}

function popuniFormuPomocuAI({ podaci }) {
  primijeniPodatkeOdAIuFormu(formaPrijave, podaci)
}
</script>
