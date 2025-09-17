<template>
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 mb-2">
    <template v-if="farma.kategorijaOdabrana">
      <span class="flex items-center mb-6">
        <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="40"
          height="40"
          viewBox="0 0 24 24"
          class="text-orange-600"
        >
          <path
            fill="currentColor"
            d="m12 19.164l6.207-6.207l-1.414-1.414L12 16.336l-4.793-4.793l-1.414 1.414L12 19.164Zm0-5.65l6.207-6.207l-1.414-1.414L12 10.686L7.207 5.893L5.793 7.307L12 13.514Z"
          />
        </svg>
        <span class="shrink-0 px-4 text-gray-900 max-sm:w-50 text-3xl">{{ aktivnaNaziv }}</span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="40"
          height="40"
          viewBox="0 0 24 24"
          class="text-orange-600"
        >
          <path
            fill="currentColor"
            d="m12 19.164l6.207-6.207l-1.414-1.414L12 16.336l-4.793-4.793l-1.414 1.414L12 19.164Zm0-5.65l6.207-6.207l-1.414-1.414L12 10.686L7.207 5.893L5.793 7.307L12 13.514Z"
          />
        </svg>
        <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
      </span>

      <div v-if="praznaKategorija" class="px-2 md:px-6 mt-14 mb-10">
        <div
          class="col-span-full rounded-lg border border-dashed border-gray-300 p-10 mt-4 text-center"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="200"
            height="200"
            viewBox="0 0 24 24"
            fill="currentColor"
            class="mx-auto"
          >
            <g fill="none" fill-rule="evenodd">
              <path
                d="m12.594 23.258l-.012.002l-.071.035l-.02.004l-.014-.004l-.071-.036q-.016-.004-.024.006l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.16-.016-.018m.264-.113l-.014.002l-.184.093l-.01.01l-.003.011l.018.43l.005.012l.008.008l.201.092q.019.005.029-.008l.004-.014l-.034-.614q-.005-.019-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.003-.011l.018-.43l-.003-.012l-.01-.01z"
              />
              <path
                fill="currentColor"
                d="M11.084 3.244a3 3 0 0 1 1.607-.063l.225.063L19.45 5.34c.19.063.361.181.486.346l.07.105l2.75 4.747a1 1 0 0 1-.44 1.407l-.12.047l-2.051.658v4.33a2 2 0 0 1-1.237 1.848l-.152.056l-5.84 1.872a3 3 0 0 1-1.607.063l-.225-.062l-5.84-1.873a2 2 0 0 1-1.382-1.743l-.007-.162V12.65l-2.051-.658a1 1 0 0 1-.617-1.338l.057-.116l2.75-4.747a1 1 0 0 1 .445-.406l.11-.045zM13 12.305v6.324l5.145-1.65v-3.687l-3.09.991a1 1 0 0 1-1.106-.353l-.064-.098zm-2 0l-.885 1.527a1 1 0 0 1-1.17.451l-3.09-.991v3.687L11 18.63zM5.32 7.49l-1.723 2.977l5.191 1.666l1.725-2.977zm13.36 0l-5.193 1.666l1.724 2.977l5.192-1.666zm-6.375-2.342a1 1 0 0 0-.49-.03l-.12.03L8.13 6.292L12 7.533l3.87-1.241z"
              />
            </g>
          </svg>
          <h3 class="text-lg font-semibold text-gray-900 mb-2">
            Trenutno nemamo usluga u ovoj kategoriji...
          </h3>
          <p class="text-gray-600">Istražite neku drugu kategoriju ili se vratite kasnije.</p>
        </div>
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-[300px_1fr] gap-8">
        <div class="px-2 md:px-6">
          <div class="pb-6 border-b border-gray-100">
            <label for="PretragaUsluga">
              <span class="block text-xs font-medium text-gray-700 mb-1"> Pretraži po nazivu </span>
              <div class="relative">
                <input
                  v-model.trim="q"
                  type="text"
                  id="PretragaUsluga"
                  placeholder="Unesi uslugu ili OPG..."
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

          <div class="pb-6 border-b border-gray-100 mt-3">
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

          <div class="pb-6 border-b border-gray-100 mb-6 mt-3">
            <div class="flex justify-between items-center mb-4">
              <p class="font-bold">Usluge</p>
              <button class="text-sm text-gray-600" @click="farma.ponistiUslugeNazivi">
                Poništi
              </button>
            </div>
            <div class="flex flex-wrap gap-2">
              <button
                v-for="u in farma.filteriUsluge"
                :key="u"
                type="button"
                @click="poNazivu(u)"
                class="p-2 flex items-center gap-2 text-sm font-semibold rounded-md shadow-md border border-gray-200"
                :class="
                  farma.filteri.usluge.includes(u)
                    ? 'bg-orange-600 text-white hover:bg-orange-900 border-orange-600 hover:border-orange-900'
                    : 'bg-white hover:bg-orange-900 hover:text-white hover:border-orange-900'
                "
              >
                {{ u }}
              </button>
            </div>
          </div>

          <div>
            <p class="block text-xs font-medium text-gray-700">Filteri</p>
            <div class="space-y-2 mt-1 mb-4">
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
                      <span class="font-bold">{{ farma.filteri.zupanije.length }}</span> Odabrano
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
                    <li v-for="zupanija in farma.filteriZupanije" :key="zupanija">
                      <label class="inline-flex items-center gap-2">
                        <input
                          type="checkbox"
                          class="size-5 rounded-sm border-gray-300 shadow-sm"
                          :checked="farma.filteri.zupanije.includes(zupanija)"
                          @change="odabirFiltera('zupanije', zupanija, $event.target.checked)"
                        />
                        <span class="text-sm font-medium text-gray-700">{{ zupanija }}</span>
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
                      <span class="font-bold">{{ farma.filteri.mjesta.length }}</span> Odabrano
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
                    <li v-for="mjesto in farma.filterMjesta" :key="mjesto">
                      <label class="inline-flex items-center gap-2">
                        <input
                          type="checkbox"
                          class="size-5 rounded-sm border-gray-300 shadow-sm"
                          :checked="farma.filteri.mjesta.includes(mjesto)"
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
              @click="farma.ponistiFiltere()"
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

        <div class="p-2 md:p-6 rounded-md">
          <div
            v-if="farma.loading"
            class="py-8 text-center text-gray-500 col-span-full mx-auto text-lg font-semibold"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="80"
              height="80"
              viewBox="0 0 24 24"
              fill="#000000"
              class="mx-auto"
            >
              <g fill="#000000">
                <path
                  d="M8.55 10.55a1 1 0 1 1-2 0a1 1 0 0 1 2 0Zm2 1a1 1 0 1 0 0-2a1 1 0 0 0 0 2Zm3 0a1 1 0 1 0 0-2a1 1 0 0 0 0 2Z"
                />
                <path
                  fill-rule="evenodd"
                  d="M16.207 4.893a8.001 8.001 0 0 1 .662 10.565c.016.013.03.027.045.042l4.243 4.243a1 1 0 0 1-1.414 1.414L15.5 16.914a.933.933 0 0 1-.042-.045A8.001 8.001 0 0 1 4.893 4.893a8 8 0 0 1 11.314 0Zm-9.9 9.9a6 6 0 1 0 8.486-8.485a6 6 0 0 0-8.485 8.485Z"
                  clip-rule="evenodd"
                />
              </g>
            </svg>
            Učitavanje…
          </div>

          <div v-else class="lg:col-span-3">
            <div
              class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-2 gap-6 px-4 py-8 mb-14"
            >
              <div
                v-if="farma.ukupno_usluga === 0"
                class="col-span-full rounded-lg border border-dashed border-gray-300 p-10 mt-4 text-center"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="80"
                  height="80"
                  class="mx-auto"
                  viewBox="0 0 512 512"
                >
                  <path
                    fill="#000000"
                    fill-rule="evenodd"
                    d="m310.109 279.878l142.31 142.309l-30.17 30.17l-139.292-139.293l-5.623 6.874v149.334h-42.667V319.938h-.448L42.667 85.272L64 85.27l25.752-25.75zM175.841 85.271h293.493l-132.072 161.42l-30.312-30.312l72.357-88.44l-160.798-.001z"
                  />
                </svg>
                <h3 class="text-lg font-semibold text-gray-900 mb-2">
                  Nema rezultata za zadane kriterije.
                </h3>
                <p class="text-gray-600">Promijenite pretragu ili filtere.</p>
              </div>

              <KarticaUsluge
                v-else
                v-for="u in farma.usluge"
                :key="u.id"
                :usluga="u"
                :prikaziPonudacaUsluge="true"
              />
            </div>

            <Paginacija
              v-if="farma.imaUsluga && farma.ukupnoStranica > 1"
              :stranica="farma.stranica"
              :ukupnoStranica="farma.ukupnoStranica"
              @idi-na="farma.promijeniStranicu"
            />
          </div>
        </div>
      </div>
    </template>
    <template v-else>
      <div class="text-center text-gray-600 py-8">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="100"
          height="100"
          class="mx-auto mb-3"
          viewBox="0 0 512 512"
        >
          <path
            fill="#000000"
            d="M459.15 269.75a133.197 133.197 0 0 1-55.862 179.975l-42.782 22.541l-10.52 5.533a71.277 71.277 0 0 1-62.966 1.685l-167.077-71.38l15.733-46.676l99.363 19.194l-51.458-97.78l-82.843-157.411l40.357-21.232l82.844 157.457l19.934-10.485l-36.521-69.445l40.335-21.22l36.52 69.445l19.935-10.485l-28.2-53.598l40.358-21.232l28.2 53.598l19.945-10.576l-19.354-36.886l40.346-21.174l19.354 36.885l54.348 103.301zM73.268 146.674a60.03 60.03 0 0 1 42.361-102.459a60.098 60.098 0 0 1 56.58 80.169l10.588 20.013A78.29 78.29 0 0 0 115.708 26a78.233 78.233 0 0 0-5.635 156.262L99.428 162.02a59.688 59.688 0 0 1-26.16-15.346z"
          />
        </svg>
        Odaberi neku od kategorija iznad da prikažemo dostupne usluge i filtre.
      </div>
    </template>
  </div>
</template>
<script setup>
import { computed, ref, watch } from "vue"
import { useFarmaPlusStore } from "@/stores/farmaPlus"
import KarticaUsluge from "@/components/dijeljeno/KarticaUsluge.vue"
import Paginacija from "@/components/dijeljeno/Paginacija.vue"

const farma = useFarmaPlusStore()

const praznaKategorija = computed(
  () => farma.kategorijaOdabrana && !farma.loading && farma.ukupno_usluga === 0,
)

const q = ref(farma.filteri.q)
let t = null
watch(q, (v) => {
  clearTimeout(t)
  t = setTimeout(() => farma.setQ(v), 350)
})

watch(
  () => farma.kat_slug,
  () => {
    q.value = ""
  },
)

const sortiraj = ref(farma.filteri.sortiranje)
watch(sortiraj, (v) => farma.postaviSortiranje(v))

function poNazivu(naziv) {
  const vecOdabrano = farma.filteri.usluge.includes(naziv)
  farma.odabraniFilteri("usluge", naziv, !vecOdabrano)
}

function odabirFiltera(polje, vrijednost, odabrano) {
  farma.odabraniFilteri(polje, vrijednost, odabrano)
}

function ponistiZupanije() {
  farma.ponistiZupanije()
}
function ponistiMjesta() {
  farma.ponistiMjesta()
}

const aktivnaNaziv = computed(() => {
  const k = farma.kategorije.find((x) => x.slug === farma.kat_slug)
  return k?.naziv || "Usluge"
})
</script>
