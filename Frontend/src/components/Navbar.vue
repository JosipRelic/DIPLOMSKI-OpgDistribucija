<template>
  <header class="bg-[#223c2f]">
    <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
      <div class="flex h-16 items-center justify-between">
        <router-link :to="{ name: 'pocetna' }" class="block text-teal-600 group">
          <div class="flex items-center gap-2">
            <img
              :src="slikeLogo"
              alt="logo"
              class="w-10 h-auto transition duration-500 group-hover:scale-105"
            />

            <p class="block text-gray-100">OPG Distribucija</p>
          </div>
        </router-link>

        <div class="md:flex md:items-center md:gap-6">
          <nav aria-label="Global" class="hidden md:block">
            <ul class="flex items-center gap-4 text-sm">
              <li>
                <router-link
                  :to="{ name: 'e-trznica' }"
                  class="text-gray-100 transition hover:text-gray-500/75"
                  :class="{ 'text-orange-600': $route.path.includes('e-trznica') }"
                >
                  E-Tržnica
                </router-link>
              </li>
              <li>
                <router-link
                  :to="{ name: 'farmaPlus' }"
                  class="text-gray-100 transition hover:text-gray-500/75"
                  :class="{ 'text-orange-600': $route.path.includes('farma-plus') }"
                >
                  Farma+
                </router-link>
              </li>
            </ul>
          </nav>

          <div class="flex items-center gap-4">
            <template v-if="!autentifikacija.korisnikAutentificiran">
              <div class="sm:flex sm:gap-4">
                <router-link
                  :to="{ name: 'prijava' }"
                  class="rounded-md bg-teal-600 transition hover:bg-teal-900 px-5 py-2.5 text-sm font-medium text-gray-100 hover:text-gray-300 shadow-sm"
                >
                  Prijava
                </router-link>

                <div class="hidden sm:flex">
                  <router-link
                    class="rounded-md bg-gray-100 transition hover:bg-gray-300 px-5 py-2.5 text-sm font-medium text-teal-600 hover:text-teal-900"
                    :to="{ name: 'registracija' }"
                  >
                    Registracija
                  </router-link>
                </div>
              </div>
            </template>
            <template v-else>
              <button
                @click="idiNaMojProfil"
                class="rounded-md inline-flex bg-teal-600 transition hover:bg-teal-900 px-4 py-2.5 text-sm font-medium text-gray-100 hover:text-gray-300 shadow-sm"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 36 32"
                  fill="#ffffff"
                  stroke-width="600px"
                >
                  <path
                    fill="#ffffff"
                    d="M.5 31.983a.503.503 0 0 0 .612-.354c1.03-3.843 5.216-4.839 7.718-5.435c.627-.149 1.122-.267 1.444-.406c2.85-1.237 3.779-3.227 4.057-4.679a.5.5 0 0 0-.165-.473c-1.484-1.281-2.736-3.204-3.526-5.416a.492.492 0 0 0-.103-.171c-1.045-1.136-1.645-2.337-1.645-3.294c0-.559.211-.934.686-1.217a.5.5 0 0 0 .243-.408C10.042 5.036 13.67 1.026 18.12 1l.107.007c4.472.062 8.077 4.158 8.206 9.324a.498.498 0 0 0 .178.369c.313.265.459.601.459 1.057c0 .801-.427 1.786-1.201 2.772a.522.522 0 0 0-.084.158c-.8 2.536-2.236 4.775-3.938 6.145a.502.502 0 0 0-.178.483c.278 1.451 1.207 3.44 4.057 4.679c.337.146.86.26 1.523.403c2.477.536 6.622 1.435 7.639 5.232a.5.5 0 0 0 .966-.26c-1.175-4.387-5.871-5.404-8.393-5.95c-.585-.127-1.09-.236-1.336-.344c-1.86-.808-3.006-2.039-3.411-3.665c1.727-1.483 3.172-3.771 3.998-6.337c.877-1.14 1.359-2.314 1.359-3.317c0-.669-.216-1.227-.644-1.663C27.189 4.489 23.19.076 18.227.005l-.149-.002c-4.873.026-8.889 4.323-9.24 9.83c-.626.46-.944 1.105-.944 1.924c0 1.183.669 2.598 1.84 3.896c.809 2.223 2.063 4.176 3.556 5.543c-.403 1.632-1.55 2.867-3.414 3.676c-.241.105-.721.22-1.277.352c-2.541.604-7.269 1.729-8.453 6.147a.5.5 0 0 0 .354.612z"
                  />
                </svg>
                <span class="ml-2 max-sm:hidden">Moj profil</span>
              </button>
              <button
                @click="odjavaKorisnika"
                class="rounded-md bg-red-700 transition hover:bg-red-900 px-5 py-2.5 text-sm font-medium text-gray-100 hover:text-gray-300"
              >
                Odjava
              </button>
            </template>

            <div v-if="autentifikacija.korisnikAutentificiran" class="relative inline-block">
              <router-link :to="{ name: 'kosarica' }">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="size-6 stroke-gray-100 transition hover:stroke-gray-500/75"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
                  />
                </svg>
                <span
                  class="absolute -top-2 -right-2 inline-flex items-center justify-center px-1.5 py-0.5 text-xs font-bold leading-none text-white rounded-full"
                  :class="brojKosarice == 0 ? 'bg-gray-500' : 'bg-orange-600'"
                >
                  {{ brojKosarice }}
                </span>
              </router-link>
            </div>

            <div class="block md:hidden">
              <button
                class="rounded-sm bg-orange-50 p-2 ml-1 text-[#223c2f] transition hover:text-gray-600/75"
                @click="otvoriIzbornikNaManjemEkranu"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="size-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                </svg>
              </button>
            </div>

            <div
              v-if="izbornikNaManjemEkranuOtvoren"
              class="absolute top-16 left-0 w-full bg-[#223c2f] px-4 py-4 space-y-2 shadow-lg z-50 md:hidden"
            >
              <template v-if="!autentifikacija.korisnikAutentificiran">
                <router-link
                  :to="{ name: 'registracija' }"
                  class="block text-gray-100 hover:text-gray-300 sm:hidden"
                  @click="izbornikNaManjemEkranuOtvoren = false"
                >
                  Registracija
                </router-link>
              </template>
              <router-link
                :to="{ name: 'e-trznica' }"
                class="block text-gray-100 hover:text-gray-300"
                @click="izbornikNaManjemEkranuOtvoren = false"
              >
                E-Tržnica
              </router-link>
              <router-link
                :to="{ name: 'farmaPlus' }"
                class="block text-gray-100 hover:text-gray-300"
                @click="izbornikNaManjemEkranuOtvoren = false"
              >
                Farma+
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed, onMounted, ref } from "vue"
import slikeLogo from "@/assets/slike/logo.png"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import { useRoute, useRouter } from "vue-router"
import { useKosaricaStore } from "@/stores/kosarica"

const autentifikacija = useAutentifikacijskiStore()
const kosarica = useKosaricaStore()
const router = useRouter()
const route = useRoute()

onMounted(() => {
  if (autentifikacija.korisnikAutentificiran) {
    kosarica.osvjezi()
  }
})

const brojKosarice = computed(() => kosarica.brojArtikala)

const izbornikNaManjemEkranuOtvoren = ref(false)

function otvoriIzbornikNaManjemEkranu() {
  izbornikNaManjemEkranuOtvoren.value = !izbornikNaManjemEkranuOtvoren.value
}

const idiNaMojProfil = () => {
  if (!autentifikacija.korisnikAutentificiran) {
    return router.push({ name: "prijava" })
  }
  if (autentifikacija.tip_korisnika === "Kupac") {
    return router.push({ name: "profilKupacNadzornaPloca" })
  }
  if (autentifikacija.tip_korisnika === "Opg") {
    return router.push({ name: "profilOpgNadzornaPloca" })
  }
  return router.push({ name: "pocetna" })
}

const odjavaKorisnika = () => {
  autentifikacija.odjava()
  router.push({ name: "prijava" })
}
</script>
