<template>
  <div class="flex justify-center items-center p-5">
    <div class="w-full max-w-7xl rounded-lg overflow-x-auto bg-white shadow-md">
      <div class="p-4 min-w-full">
        <div class="flex justify-between items-center">
          <div class="ps-4">
            <p class="text-3xl font-bold">Napravljene narudžbe</p>
            <small class="text-gray-500">Sve što ste naručili od drugih OPG-ova</small>
          </div>
        </div>
      </div>

      <div class="max-w-sm ps-8 pb-5">
        <label for="pretragaBrojNarudzbe">
          <div class="relative">
            <input
              type="text"
              id="pretragaBrojNarudzbe"
              v-model="pretraga"
              placeholder="Pretraži po broju narudžbe"
              class="mt-0.5 w-full rounded border-gray-300 pe-10 shadow-sm sm:text-sm p-3 h-10"
            />
            <span class="absolute inset-y-0 right-2 grid w-8 place-content-center">
              <button
                type="button"
                aria-label="Submit"
                class="rounded-full p-1.5 text-gray-700 transition-colors hover:bg-gray-100"
                @click="primijeniPretragu"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
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
            <th class="px-8 py-3 border-b border-gray-300 w-[28%]">Naručeno od</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[22%]">Broj narudžbe</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[15%]">Ukupan iznos</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[25%]">Datum i vrijeme narudžbe</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[10%]"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="napravljene_narudzbe.loading">
            <td colspan="5" class="px-8 py-5 text-center text-gray-500">Učitavanje…</td>
          </tr>

          <tr v-else-if="!napravljene_narudzbe.narudzbe.length">
            <td colspan="5" class="px-8 py-5 text-center text-gray-500">Nema narudžbi.</td>
          </tr>

          <tr v-else v-for="n in napravljene_narudzbe.narudzbe" :key="n.narudzba_id">
            <td class="px-8 py-5 border-b border-gray-200">
              <template v-for="(o, idx) in n.opgovi || []" :key="`${n.narudzba_id}-o-${idx}`">
                <router-link
                  :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: o.slug } }"
                  class="text-orange-600 hover:text-orange-900 hover:underline"
                >
                  {{ o.naziv }}
                </router-link>
                <span v-if="idx < (n.opgovi?.length || 0) - 1" class="text-gray-400"> | </span>
              </template>
            </td>

            <td class="px-8 py-5 border-b border-gray-200">
              <span class="text-gray-600">#{{ n.broj_narudzbe }}</span>
            </td>

            <td class="px-8 py-5 text-gray-600 border-b border-gray-200">
              {{ formatCijena(n.ukupno) }}
            </td>

            <td class="px-8 py-5 text-gray-500 border-b border-gray-200">
              {{ formatHR(n.datum_izrade) }}
            </td>

            <td
              class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline"
            >
              <router-link
                :to="{
                  name: 'profilOpgNapravljeneNarudzbeDetaljiNarudzbe',
                  params: { narudzbaId: n.narudzba_id },
                }"
              >
                Detalji
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>

      <div
        v-if="napravljene_narudzbe.ukupnoStranica > 1"
        class="flex items-center p-5 justify-center min-w-full"
      >
        <div class="flex border border-gray-200 shadow rounded-md">
          <button
            class="text-black border-r border-gray-200 font-semibold px-4 py-2 cursor-pointer"
            :disabled="napravljene_narudzbe.stranica === 1"
            @click="idiNa(napravljene_narudzbe.stranica - 1)"
          >
            Prethodna
          </button>
          <div class="flex space-x-2">
            <button
              v-for="s in stranice"
              :key="s"
              class="px-4 py-2"
              :class="s === napravljene_narudzbe.stranica ? 'bg-orange-500 text-white' : ''"
              @click="idiNa(s)"
            >
              {{ s }}
            </button>
          </div>
          <button
            class="text-black border-l border-gray-200 font-semibold px-4 py-2 cursor-pointer"
            :disabled="napravljene_narudzbe.stranica === napravljene_narudzbe.ukupnoStranica"
            @click="idiNa(napravljene_narudzbe.stranica + 1)"
          >
            Sljedeća
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, watch } from "vue"
import { useNapravljeneNarudzbeOpgStore } from "@/stores/napravljeneNarudzbeOpg"

const napravljene_narudzbe = useNapravljeneNarudzbeOpgStore()
const pretraga = ref(napravljene_narudzbe.p)

function formatCijena(v) {
  const n = Number(v || 0)
  return `${n.toFixed(2)} €`
}
function formatHR(iso) {
  try {
    const d = new Date(iso)
    return d.toLocaleString("hr-HR")
  } catch {
    return iso
  }
}

const stranice = computed(() => {
  const str = []
  for (let i = 1; i <= napravljene_narudzbe.ukupnoStranica; i++) str.push(i)
  return str
})

function idiNa(p) {
  if (p < 1 || p > napravljene_narudzbe.ukupnoStranica) return
  napravljene_narudzbe.idiNa(p)
}
function primijeniPretragu() {
  napravljene_narudzbe.postaviP(pretraga.value)
}

let t = null
watch(
  pretraga,
  (v) => {
    clearTimeout(t)
    t = setTimeout(() => {
      napravljene_narudzbe.postaviP(v || "")
    }, 300)
  },
  { immediate: true },
)

onMounted(() => napravljene_narudzbe.ucitajNarudzbe())
</script>
