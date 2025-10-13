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
          <h1 class="text-2xl xl:text-3xl font-extrabold">Registracija OPG-a</h1>
          <form class="w-full flex-1 mt-8" @submit.prevent="posaljiPodatkeZaRegistracijuOpga">
            <div class="flex flex-col items-center">
              <GumbZaGlasovnoPopunjavanje
                strukturaUpita="registracija_opg"
                @popuni="glasovnoPopuniFormuRegistracijeOpga"
              />
              <small class="pt-2 w-full max-w-xs"
                >Pritisnite gumb i popunite obrazac glasom npr. "Zovem se Ivan Horvat. Moja email
                adresa je ihorvat@gmail.com. Naziv opg-a itd..."</small
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
                type="email"
                placeholder="Email"
                v-model="email"
                required
                @invalid="(e) => e.target.setCustomValidity('Molimo unesite email adresu')"
                @input="(e) => e.target.setCustomValidity('')"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="text"
                placeholder="Korisničko Ime"
                v-model="korisnicko_ime"
                required
                @invalid="(e) => e.target.setCustomValidity('Molimo unesite korisničko ime')"
                @input="(e) => e.target.setCustomValidity('')"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="password"
                placeholder="Lozinka"
                v-model="lozinka"
                required
                minlength="8"
                @invalid="
                  (e) => e.target.setCustomValidity('Lozinka mora imati najmanje 8 znakova')
                "
                @input="(e) => e.target.setCustomValidity('')"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="password"
                placeholder="Potvrdite lozinku"
                v-model="potvrda_lozinke"
                required
                minlength="8"
                @invalid="
                  (e) => e.target.setCustomValidity('Lozinka mora imati najmanje 8 znakova')
                "
                @input="(e) => e.target.setCustomValidity('')"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="text"
                placeholder="Naziv OPG-a"
                v-model="naziv"
                required
                @invalid="(e) => e.target.setCustomValidity('Molimo unesite naziv vašeg OPG-a')"
                @input="(e) => e.target.setCustomValidity('')"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="text"
                placeholder="Ime vlasnika"
                v-model="ime"
                required
                @invalid="(e) => e.target.setCustomValidity('Molimo unesite ime vlasnika OPG-a')"
                @input="(e) => e.target.setCustomValidity('')"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="text"
                placeholder="Prezime vlasnika"
                v-model="prezime"
                required
                @invalid="(e) => e.target.setCustomValidity('Molimo unesite email adresu')"
                @input="(e) => e.target.setCustomValidity('')"
              />

              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white mt-5"
                type="number"
                placeholder="Identifikacijski broj PG-a (MIBPG)"
                v-model="identifikacijski_broj_mibpg"
                required
                minlength="1"
                @invalid="(e) => e.target.setCustomValidity('MIBPG mora imati najmanje 1 znak')"
                @input="(e) => e.target.setCustomValidity('')"
              />

              <button
                type="submit"
                class="mt-5 tracking-wide font-semibold bg-teal-600 hover:bg-teal-900 text-gray-100 w-full py-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none disabled:bg-gray-500"
                :disabled="autentifikacija.loading"
              >
                <svg
                  class="w-6 h-6 -ml-2"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                  <circle cx="8.5" cy="7" r="4" />
                  <path d="M20 8v6M23 11h-6" />
                </svg>
                <span class="ml-3">
                  {{ autentifikacija.loading ? "Registriram..." : "Registracija" }}
                </span>
              </button>

              <p v-if="autentifikacija.error" class="mt-3 text-red-600 text-sm text-center">
                {{ autentifikacija.error }}
              </p>

              <p class="mt-6 text-sm text-gray-800 text-center">
                <router-link
                  :to="{ name: 'prijava' }"
                  class="mt-6 text-center text-md border-b border-gray-500 border-dotted"
                >
                  Već ste registrirani?
                </router-link>
              </p>
            </div>
          </form>
        </div>
      </div>
      <div
        class="flex-1 bg-indigo-100 text-center bg-cover bg-center hidden lg:flex"
        :style="`background-image: url(${slikeFormaRegistracijeOpg});`"
      ></div>
    </div>
  </div>
</template>
<script setup>
import slikeLogo from "@/assets/slike/logo.png"
import slikeFormaRegistracijeOpg from "@/assets/slike/forma-registracije-opg.png"
import { ref } from "vue"
import { useRouter } from "vue-router"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import GumbZaGlasovnoPopunjavanje from "@/components/ai/GumbZaGlasovnoPopunjavanje.vue"

const email = ref("")
const korisnicko_ime = ref("")
const lozinka = ref("")
const potvrda_lozinke = ref("")
const naziv = ref("")
const ime = ref("")
const prezime = ref("")
const identifikacijski_broj_mibpg = ref("")

const autentifikacija = useAutentifikacijskiStore()
const router = useRouter()

const posaljiPodatkeZaRegistracijuOpga = async () => {
  const ok = await autentifikacija.registrirajOpg({
    email: email.value,
    korisnicko_ime: korisnicko_ime.value,
    lozinka: lozinka.value,
    potvrda_lozinke: potvrda_lozinke.value,
    naziv: naziv.value,
    ime: ime.value,
    prezime: prezime.value,
    identifikacijski_broj_mibpg: identifikacijski_broj_mibpg.value,
  })
}

function glasovnoPopuniFormuRegistracijeOpga(e) {
  const sp = e.podaci || {}
  email.value = sp.email ?? email.value
  korisnicko_ime.value = sp.korisnicko_ime ?? korisnicko_ime.value
  lozinka.value = sp.lozinka ?? lozinka.value
  potvrda_lozinke.value = sp.potvrda_lozinke ?? potvrda_lozinke.value
  naziv.value = sp.naziv ?? naziv.value
  ime.value = sp.ime ?? ime.value
  prezime.value = sp.prezime ?? prezime.value
  identifikacijski_broj_mibpg.value =
    sp.identifikacijski_broj_mibpg ?? identifikacijski_broj_mibpg.value
}
</script>
