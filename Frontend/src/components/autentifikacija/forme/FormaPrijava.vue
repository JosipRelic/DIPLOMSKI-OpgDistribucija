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
          <form class="w-full flex-1 mt-8" @submit.prevent="posaljiPodatkeZaPrijavu">
            <div class="flex flex-col items-center">
              <button
                class="w-full max-w-xs font-bold shadow-sm hover:bg-red-400 rounded-lg py-3 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
              >
                <div class="bg-white p-2 rounded-full">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    class="w-6 text-red-600"
                  >
                    <path
                      fill="currentColor"
                      d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
                    />
                  </svg>
                </div>
                <span class="ml-4"> Ispunite glasovno pomoću AI </span>
              </button>
              <small class="pt-2 w-full max-w-xs"
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
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                type="text"
                placeholder="Email ili korisničko ime"
                v-model="email_ili_korisnicko_ime"
              />

              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="password"
                placeholder="Lozinka"
                v-model="lozinka"
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
              <p v-if="autentifikacija.error" class="text-red-600">{{ autentifikacija.error }}</p>
              <p class="mt-6 text-sm text-gray-800 text-center">
                <router-link
                  :to="{ name: 'zaboravljenaLozinka' }"
                  class="mt-6 text-center text-md border-b border-gray-500 border-dotted"
                >
                  Zaboravili ste lozinku?
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
import { ref } from "vue"
import { useRouter } from "vue-router"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"

const email_ili_korisnicko_ime = ref("")
const lozinka = ref("")
const autentifikacija = useAutentifikacijskiStore()
const router = useRouter()

const posaljiPodatkeZaPrijavu = async () => {
  const ok = await autentifikacija.prijava({
    email_ili_korisnicko_ime: email_ili_korisnicko_ime.value,
    lozinka: lozinka.value,
  })

  if (ok) {
    router.push({ name: "profilKupacNadzornaPloca" })
  }
}
</script>
