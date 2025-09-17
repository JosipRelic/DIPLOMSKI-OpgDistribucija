<template>
  <div class="space-y-4">
    <div>
      <label for="PretragaProizvoda">
        <span class="block text-xs font-medium text-gray-700 mb-1"> Pretraži po nazivu </span>
        <div class="relative">
          <input
            v-model.trim="q"
            type="text"
            id="PretragaProizvoda"
            placeholder="Unesi proizvod ili OPG..."
            class="mt-0.5 w-full h-10 rounded border-gray-300 pe-10 shadow-md sm:text-sm bg-white p-3"
          />
          <span class="absolute inset-y-0 right-2 grid w-8 place-content-center">
            <button
              type="button"
              aria-label="Submit"
              class="rounded-full p-1.5 text-gray-700 hover:bg-gray-100"
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

    <div>
      <label for="Sortiraj" class="block text-xs font-medium text-gray-700"> Sortiraj </label>
      <select
        id="Sortiraj"
        class="mt-1 rounded shadow shadow-md p-2 text-sm border border-gray-200 cursor-pointer"
        v-model="sortiraj"
      >
        <option value="novo" class="text-gray-900">Najnovije</option>
        <option value="naziv_asc" class="text-gray-900">Naziv, Uzlazno</option>
        <option value="naziv_desc" class="text-gray-900">Naziv, Silazno</option>
        <option value="cijena_asc" class="text-gray-900">Cijena, Uzlazno</option>
        <option value="cijena_desc" class="text-gray-900">Cijena, Silazno</option>
      </select>
    </div>

    <div>
      <p class="block text-xs font-medium text-gray-700">Filteri</p>
      <div class="space-y-2 mt-1">
        <details
          class="overflow-hidden rounded shadow-md border border-gray-200 [&_summary::-webkit-details-marker]:hidden"
        >
          <summary
            class="flex cursor-pointer items-center justify-between gap-2 p-4 text-gray-900 transition"
          >
            <span class="text-sm font-medium"> Županija </span>
            <span class="transition group-open:-rotate-180">
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
                  d="M19.5 8.25l-7.5 7.5-7.5-7.5"
                />
              </svg>
            </span>
          </summary>

          <div class="border-t border-gray-200 bg-white">
            <header class="flex items-center justify-between p-4">
              <span class="text-sm text-gray-700">
                <span class="font-bold">{{ proizvodi_s.filteri.zupanije.length }}</span> Odabrano
              </span>
              <button
                type="button"
                @click="ponistiZupanije"
                class="text-sm text-gray-900 underline underline-offset-4 cursor-pointer"
              >
                Poništi
              </button>
            </header>

            <ul class="space-y-1 border-t border-gray-200 p-4 max-h-64 overflow-auto">
              <li v-for="zupanije in proizvodi_s.filteriZupanije" :key="zupanije">
                <label class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                    :checked="proizvodi_s.filteri.zupanije.includes(zupanije)"
                    @change="odabirFiltera('zupanije', zupanije, $event.target.checked)"
                  />
                  <span class="text-sm font-medium text-gray-700">{{ zupanije }}</span>
                </label>
              </li>
            </ul>
          </div>
        </details>

        <details
          class="overflow-hidden rounded shadow-md border border-gray-200 [&_summary::-webkit-details-marker]:hidden"
        >
          <summary
            class="flex cursor-pointer items-center justify-between gap-2 p-4 text-gray-900 transition"
          >
            <span class="text-sm font-medium"> Mjesto </span>
            <span class="transition group-open:-rotate-180">
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
                  d="M19.5 8.25l-7.5 7.5-7.5-7.5"
                />
              </svg>
            </span>
          </summary>

          <div class="border-t border-gray-200 bg-white">
            <header class="flex items-center justify-between p-4">
              <span class="text-sm text-gray-700">
                <span class="font-bold">{{ proizvodi_s.filteri.mjesta.length }}</span> Odabrano
              </span>
              <button
                type="button"
                @click="ponistiMjesta"
                class="text-sm text-gray-900 underline underline-offset-4 cursor-pointer"
              >
                Poništi
              </button>
            </header>

            <ul class="space-y-1 border-t border-gray-200 p-4 max-h-64 overflow-auto">
              <li v-for="mjesto in proizvodi_s.filteriMjesta" :key="mjesto">
                <label class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                    :checked="proizvodi_s.filteri.mjesta.includes(mjesto)"
                    @change="odabirFiltera('mjesta', mjesto, $event.target.checked)"
                  />
                  <span class="text-sm font-medium text-gray-700">{{ mjesto }}</span>
                </label>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </div>

    <div>
      <button
        type="button"
        @click="proizvodi_s.ponistiFiltere()"
        class="text-sm text-gray-600 cursor-pointer border p-2 rounded pr-3 border-gray-200 shadow-md flex items-center gap-3"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 48 48">
          <path fill="#F57C00" d="M29 23H19L7 9h34z" />
          <path
            fill="#FF9800"
            d="m29 38l-10 6V23h10zM41.5 9h-35C5.7 9 5 8.3 5 7.5S5.7 6 6.5 6h35c.8 0 1.5.7 1.5 1.5S42.3 9 41.5 9z"
          />
          <circle cx="38" cy="38" r="10" fill="#F44336" />
          <path fill="#fff" d="M32 36h12v4H32z" />
        </svg>
        Poništi sve filtere
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue"
import { useEtrznicaProizvodiStore } from "@/stores/eTrznicaProizvodi"

const proizvodi_s = useEtrznicaProizvodiStore()

const q = ref(proizvodi_s.filteri.q)
let t = null
watch(q, (v) => {
  clearTimeout(t)
  t = setTimeout(() => proizvodi_s.setQ(v), 350)
})

const sortiraj = ref(proizvodi_s.filteri.sortiranje)
watch(sortiraj, (v) => proizvodi_s.postaviSortiranje(v))

function odabirFiltera(polje, vrijednost, odabrano) {
  proizvodi_s.odabraniFilteri(polje, vrijednost, odabrano)
}

function ponistiZupanije() {
  proizvodi_s.filteri.zupanije = []
  proizvodi_s.ucitajProizvode()
}
function ponistiMjesta() {
  proizvodi_s.filteri.mjesta = []
  proizvodi_s.ucitajProizvode()
}
</script>
