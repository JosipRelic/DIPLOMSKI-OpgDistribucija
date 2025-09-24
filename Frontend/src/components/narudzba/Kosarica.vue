<template>
  <section>
    <div
      class="mx-auto my-12 py-12 max-w-2xl sm:px-6 max-xl:px-10 sm:py-12 lg:px-8 bg-white rounded-2xl shadow-lg max-md:mx-10"
    >
      <div class="mx-auto max-w-3xl">
        <header class="text-center">
          <h1 class="text-2xl font-bold text-gray-900 sm:text-3xl">Košarica</h1>
        </header>

        <div class="mt-8 space-y-8">
          <div v-if="proizvodi.length">
            <h2 class="text-lg font-semibold text-orange-600 mb-3 border-b-1 border-gray-200 pb-1">
              Proizvodi
            </h2>
            <ul class="space-y-4">
              <li v-for="st in proizvodi" :key="st.id" class="flex items-center gap-4">
                <img
                  :src="st.slika || 'https://placehold.co/100x100?text=Proizvod'"
                  alt=""
                  class="size-24 rounded-sm object-cover"
                />
                <div>
                  <h3 class="text-lg text-gray-900">{{ st.naziv }}</h3>
                  <dl class="mt-0.5 space-y-px text-sm text-gray-600">
                    <div>
                      <dt class="inline">Cijena:</dt>
                      <dd class="inline ml-1 font-bold">{{ fmt(st.cijena) }}</dd>
                    </div>
                    <div>
                      <dt class="inline">Jedinica:</dt>
                      <dd class="inline ml-1">{{ st.mjerna_jedinica }}</dd>
                    </div>
                    <div v-if="st.opg_slug" class="mt-1">
                      <router-link
                        class="rounded-full bg-orange-600 px-2.5 py-0.5 text-sm whitespace-nowrap text-white hover:bg-orange-900"
                        :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: st.opg_slug } }"
                        >{{ st.opg_naziv }}</router-link
                      >
                    </div>
                  </dl>
                </div>

                <div class="flex flex-1 items-center justify-end gap-2">
                  <input
                    v-if="mozeMijenjatiKolicinu(st)"
                    type="number"
                    :value="st.kolicina"
                    min="1"
                    class="h-8 w-12 rounded-sm border border-gray-200 shadow-sm bg-white p-0 text-center text-xs text-gray-900 [-moz-appearance:_textfield] focus:outline-hidden [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"
                    @change="(e) => kosarica.promijeniKolicinu(st.id, Number(e.target.value || 1))"
                  />
                  <span v-else class="text-sm text-gray-600">Količina: {{ st.kolicina }}</span>

                  <button
                    class="text-gray-600 transition hover:text-red-600"
                    @click="kosarica.ukloni(st.id)"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="size-4"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="1.5"
                        d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673A2.25 2.25 0 0 1 15.916 21.75H8.084A2.25 2.25 0 0 1 5.84 19.673L4.772 5.79m14.456 0a48.11 48.11 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0A48.11 48.11 0 0 1 8.094 4.791m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.023-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
                      />
                    </svg>
                  </button>
                </div>
              </li>
            </ul>
          </div>

          <div v-if="usluge.length">
            <h2 class="text-lg font-semibold text-orange-600 mb-3 border-b-1 border-gray-200 pb-1">
              Usluge
            </h2>
            <ul class="space-y-4">
              <li v-for="st in usluge" :key="st.id" class="flex items-center gap-4">
                <img
                  :src="st.slika || 'https://placehold.co/100x100?text=Usluga'"
                  alt=""
                  class="size-24 rounded-sm object-cover"
                />
                <div>
                  <h3 class="text-lg text-gray-900">{{ st.naziv }}</h3>
                  <dl class="mt-0.5 space-y-px text-sm text-gray-600">
                    <div>
                      <dt class="inline">Cijena:</dt>
                      <dd class="inline ml-1 font-bold">{{ fmt(st.cijena) }}</dd>
                    </div>
                    <div>
                      <dt class="inline">Jedinica:</dt>
                      <dd class="inline ml-1">{{ st.mjerna_jedinica }}</dd>
                    </div>
                    <div v-if="st.termin_od && st.termin_do">
                      <dt class="inline">Termin:</dt>
                      <dd class="inline ml-1 text-teal-500">
                        {{ fmtHR(st.termin_od) }} <span class="text-gray-600">-></span>
                        {{ fmtHR(st.termin_do) }}
                      </dd>
                    </div>
                    <div v-if="st.opg_slug" class="mt-1">
                      <router-link
                        class="rounded-full bg-orange-600 px-2.5 py-0.5 text-sm whitespace-nowrap text-white hover:bg-orange-900"
                        :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: st.opg_slug } }"
                        >{{ st.opg_naziv }}</router-link
                      >
                    </div>
                  </dl>
                </div>

                <div class="flex flex-1 items-center justify-end gap-2">
                  <input
                    v-if="mozeMijenjatiKolicinu(st)"
                    type="number"
                    :value="st.kolicina"
                    min="1"
                    class="h-8 w-12 rounded-sm border border-gray-200 shadow-sm bg-white p-0 text-center text-xs text-gray-900"
                    @change="(e) => kosarica.promijeniKolicinu(st.id, Number(e.target.value || 1))"
                  />
                  <span v-else class="text-sm text-gray-600">Količina: {{ st.kolicina }}</span>

                  <button
                    class="text-gray-600 transition hover:text-red-600"
                    @click="kosarica.ukloni(st.id)"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="size-4"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="1.5"
                        d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673A2.25 2.25 0 0 1 15.916 21.75H8.084A2.25 2.25 0 0 1 5.84 19.673L4.772 5.79m14.456 0a48.11 48.11 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0A48.11 48.11 0 0 1 8.094 4.791m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.023-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
                      />
                    </svg>
                  </button>
                </div>
              </li>
            </ul>
          </div>

          <div v-if="!proizvodi.length && !usluge.length" class="text-center text-gray-600 py-8">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="100"
              height="100"
              viewBox="0 0 1024 1025"
              class="mx-auto mb-2"
            >
              <path
                fill="currentColor"
                d="M960 513H64q-27 0-45.5-18.5T0 449.5T18.5 404T64 385h56q20 30 51.5 47t68.5 17t68.5-17t51.5-47h304q20 30 51.5 47t68.5 17t68.5-17t51.5-47h56q27 0 45.5 19t18.5 45.5t-19 45t-45 18.5zM806 379q-19 11-40 5t-32-25L583 81q-11-19-5.5-40.5T602 8t40-5t32 25l151 278q11 19 5.5 40.5T806 379zm-516-20q-11 19-32 25t-40-5t-24.5-32.5T199 306L350 28q11-19 32-25t40 5t24.5 32.5T441 81zm606 602q-8 40-29.5 52t-65.5 12H227q-45 0-68-12t-31-52L64 577h896zM736 769H480q-13 0-22.5 9.5T448 801t9.5 22.5T480 833h256q13 0 22.5-9.5T768 801t-9.5-22.5T736 769z"
              />
            </svg>
            Košarica je prazna.
          </div>

          <div
            v-if="proizvodi.length || usluge.length"
            class="mt-8 flex justify-end border-t border-gray-400 pt-8"
          >
            <div class="w-screen max-w-lg space-y-4">
              <dl class="space-y-0.5 text-sm text-gray-700">
                <div class="flex justify-between">
                  <dt>Ukupan iznos bez PDV-a</dt>
                  <dd>{{ fmt(iznos_bez_pdva) }}</dd>
                </div>
                <div class="flex justify-between">
                  <dt>PDV (25%)</dt>
                  <dd>{{ fmt(pdv) }}</dd>
                </div>
                <div class="flex justify-between !text-base font-medium">
                  <dt>Ukupan iznos s PDV-om</dt>
                  <dd>{{ fmt(ukupno_s_pdvom) }}</dd>
                </div>
              </dl>

              <div class="flex justify-end">
                <router-link
                  :to="{ name: 'pregledNarudzbe' }"
                  class="block rounded-md bg-teal-600 px-5 py-3 text-base text-white transition hover:bg-teal-800"
                  >Nastavi prema plaćanju</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import { onMounted, computed } from "vue"
import { useKosaricaStore } from "@/stores/kosarica"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import { useRouter } from "vue-router"

const kosarica = useKosaricaStore()
const autentifikacija = useAutentifikacijskiStore()
const router = useRouter()

onMounted(async () => {
  if (!autentifikacija.korisnikAutentificiran) return router.push({ name: "prijava" })
  await kosarica.osvjezi()
})

const proizvodi = computed(() => kosarica.proizvodi)
const usluge = computed(() => kosarica.usluge)
const iznos_bez_pdva = computed(() => kosarica.iznos_bez_pdva)
const pdv = computed(() => kosarica.pdv)
const ukupno_s_pdvom = computed(() => kosarica.ukupno_s_pdvom)

function fmt(n) {
  return `${Number(n || 0).toFixed(2)} €`
}

function pad(n) {
  return String(n).padStart(2, "0")
}
function fmtHR(iso) {
  const d = new Date(iso)
  if (isNaN(d)) return iso
  const dd = pad(d.getDate())
  const mm = pad(d.getMonth() + 1)
  const yyyy = d.getFullYear()
  const hh = pad(d.getHours())
  const mi = pad(d.getMinutes())
  return `${dd}-${mm}-${yyyy} ${hh}:${mi}`
}

function mozeMijenjatiKolicinu(st) {
  if (st.tip === "proizvod") return true
  if (st.tip === "usluga" && st.termin_od && st.termin_do) return false
  return true
}
</script>
