<template>
  <section>
    <div class="flex justify-center items-center p-5">
      <div class="w-full max-w-7xl rounded-lg overflow-x-auto bg-white shadow-md">
        <div class="p-4 min-w-full">
          <div class="flex justify-between items-center">
            <p class="text-2xl font-bold ps-4">Sve narudžbe</p>
          </div>
        </div>

        <div class="max-w-sm ps-8 pb-5">
          <label for="pretragaBrojNarudzbe">
            <div class="relative">
              <input
                v-model="pretraga"
                type="text"
                id="pretragaBrojNarudzbe"
                placeholder="Pretraži po broju narudžbe"
                class="mt-0.5 w-full rounded border-gray-300 pe-10 shadow-sm sm:text-sm p-3 h-10"
              />
              <span class="absolute inset-y-0 right-2 grid w-8 place-content-center">
                <button
                  type="button"
                  aria-label="Submit"
                  class="rounded-full p-1.5 text-gray-700 transition-colors hover:bg-gray-100"
                  @click="pretraga"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.5"
                    class="size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
                    />
                  </svg>
                </button>
              </span>
            </div>
          </label>
        </div>

        <table class="w-full text-left">
          <thead>
            <tr>
              <th class="px-8 py-3 border-b border-gray-300 w-[20%]">Naručeno od</th>
              <th class="px-8 py-3 border-b border-gray-300 w-[20%]">Broj narudžbe</th>
              <th class="px-8 py-3 border-b border-gray-300 w-[15%]">Ukupan iznos</th>
              <th class="px-8 py-3 border-b border-gray-300 w-[25%]">Datum i vrijeme</th>
              <th class="px-8 py-3 border-b border-gray-300 w-[10%]">Status</th>
              <th class="px-8 py-3 border-b border-gray-300 w-[10%]"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="n in stavke" :key="n.narudzba_id">
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <template v-if="n.opgovi?.length">
                  <template v-for="(o, idx) in n.opgovi" :key="o.slug">
                    <router-link
                      class="text-orange-600 hover:text-orange-900 hover:underline"
                      :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: o.slug } }"
                    >
                      {{ o.naziv }}
                    </router-link>
                    <span v-if="idx < n.opgovi.length - 1" class="text-gray-400"> | </span>
                  </template>
                </template>
                <span v-else>—</span>
              </td>

              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#{{ n.broj_narudzbe }}</p>
              </td>

              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">
                {{ fmtEUR(n.ukupno) }}
              </td>

              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
                {{ fmtDatumVrijeme(n.datum_izrade) }}
              </td>

              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full px-2.5 py-0.5"
                  :class="{
                    'bg-rose-600 text-rose-100': n.status === 'otkazano',
                    'bg-amber-500 text-amber-100': n.status === 'u_tijeku',
                    'bg-emerald-100 text-emerald-700': n.status === 'isporuceno',
                  }"
                >
                  <p class="text-sm whitespace-nowrap capitalize">
                    {{ n.status.replace("_", " ").replace("c", "č") }}
                  </p>
                </span>
              </td>

              <td
                class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
              >
                <router-link
                  :to="{
                    name: 'profilKupacMojeNarudzbeDetaljiNarudzbe',
                    params: { id: n.narudzba_id },
                  }"
                >
                  Detalji
                </router-link>
              </td>
            </tr>

            <tr v-if="!stavke?.length">
              <td class="px-8 py-8 text-center text-gray-500" colspan="6">Nema narudžbi.</td>
            </tr>
          </tbody>
        </table>

        <div
          class="flex items-center p-5 justify-center min-w-full"
          v-if="ukupno > 0 && ukupnoStranica > 1"
        >
          <div class="flex border border-gray-200 shadow rounded-md">
            <button
              class="text-black border-r border-gray-200 font-semibold px-4 py-2 cursor-pointer disabled:opacity-50"
              :disabled="stranica <= 1"
              @click="prethodna"
            >
              Prethodna
            </button>

            <div class="flex space-x-2 px-2">
              <span class="px-4 py-2 bg-orange-500 text-white rounded">{{ stranica }}</span>
              <span class="px-4 py-2">/ {{ ukupnoStranica }}</span>
            </div>

            <button
              class="text-black border-l border-gray-200 font-semibold px-4 py-2 cursor-pointer disabled:opacity-50"
              :disabled="stranica >= ukupnoStranica"
              @click="sljedeca"
            >
              Sljedeća
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import { onMounted, ref, computed, watch } from "vue"
import { useMojeNarudzbeKupacStore } from "@/stores/mojeNarudzbeKupac"

const moje_narudzbe = useMojeNarudzbeKupacStore()
const pretraga = ref(moje_narudzbe.p)

onMounted(() => moje_narudzbe.ucitajMojeNarudzbe())

const stavke = computed(() => moje_narudzbe.stavke)
const ukupno = computed(() => moje_narudzbe.ukupno)
const stranica = computed(() => moje_narudzbe.stranica)
const ukupnoStranica = computed(() => moje_narudzbe.ukupnoStranica)

function fmtEUR(v) {
  return `${Number(v || 0).toFixed(2)} €`
}
function fmtDatumVrijeme(iso) {
  if (!iso) return ""
  const d = new Date(iso)
  return d.toLocaleString("hr-HR")
}

function primijeniPretragu() {
  moje_narudzbe.postaviP(pretraga.value)
}

let t = null
watch(
  pretraga,
  (v) => {
    clearTimeout(t)
    t = setTimeout(() => {
      moje_narudzbe.postaviP(v || "")
    }, 300)
  },
  { immediate: true },
)
function prethodna() {
  moje_narudzbe.idiNa(moje_narudzbe.stranica - 1)
}
function sljedeca() {
  moje_narudzbe.idiNa(moje_narudzbe.stranica + 1)
}
</script>
