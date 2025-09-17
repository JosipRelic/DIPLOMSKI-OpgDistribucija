<template>
  <div class="bg-[#f5ebdc] py-10 sm:py-20">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <dl class="grid grid-cols-1 gap-x-8 gap-y-16 text-center lg:grid-cols-3">
        <div class="mx-auto flex max-w-xs flex-col gap-y-4">
          <dt class="text-base/7 text-gray-900">Registriranih OPG-ova</dt>
          <dd class="order-first text-3xl font-semibold tracking-tight text-[#223c2f] sm:text-5xl">
            {{ opgovi_s.statistika.broj_registriranih_opgova }}
          </dd>
        </div>
        <div class="mx-auto flex max-w-xs flex-col gap-y-4">
          <dt class="text-base/7 text-gray-900">Dodanih proizvoda</dt>
          <dd class="order-first text-3xl font-semibold tracking-tight text-[#223c2f] sm:text-5xl">
            {{ opgovi_s.statistika.broj_proizvoda }}
          </dd>
        </div>
        <div class="mx-auto flex max-w-xs flex-col gap-y-4">
          <dt class="text-base/7 text-gray-900">Dodanih usluga</dt>
          <dd class="order-first text-3xl font-semibold tracking-tight text-[#223c2f] sm:text-5xl">
            {{ opgovi_s.statistika.broj_usluga }}
          </dd>
        </div>
      </dl>
    </div>
  </div>

  <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8 mb-10">
    <header>
      <h2 class="text-xl font-bold text-gray-900 sm:text-3xl">Opg-ovi</h2>

      <p class="mt-4 max-w-md text-gray-500">
        Otkrijte domaće OPG-ove iz svih krajeva Hrvatske. Upoznajte ljude koji stoje iza proizvoda
        koje kupujete. Svaki OPG ima svoju priču, tradiciju i način uzgoja. Filtrirajte prema
        regiji, ponudi ili vrsti proizvoda i pronađite proizvođače koji dijele vaše vrijednosti o
        lokalnom, svježem i održivom.
      </p>
    </header>

    <div class="mt-4 lg:mt-8 grid grid-cols-1 lg:grid-cols-4 gap-8">
      <div class="space-y-4">
        <div>
          <label for="PretragaOPG">
            <span class="block text-xs font-medium text-gray-700 mb-1"> Pretraži po nazivu </span>
            <div class="relative">
              <input
                v-model.trim="q"
                type="text"
                id="PretragaOPG"
                placeholder="Unesi naziv OPG-a..."
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
            v-model="sortiranje"
          >
            <option value="" class="text-gray-900">Sortiraj po...</option>
            <option value="naziv_asc" class="text-gray-900">Naziv, Uzlazno</option>
            <option value="naziv_desc" class="text-gray-900">Naziv, Silazno</option>
            <option value="ocjena_asc" class="text-gray-900">Ocjena, Uzlazno</option>
            <option value="ocjena_desc" class="text-gray-900">Ocjena, Silazno</option>
          </select>
        </div>

        <div>
          <p class="block text-xs font-medium text-gray-700">Filteri</p>

          <div class="mt-1 space-y-2">
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
                    <span class="font-bold">{{ opgovi_s.filteri.zupanije.length }}</span> Odabrano
                  </span>

                  <button
                    type="button"
                    @click="ponistiZupanije"
                    class="text-sm text-gray-900 underline underline-offset-4"
                  >
                    Poništi
                  </button>
                </header>

                <ul class="space-y-1 border-t border-gray-200 p-4">
                  <li v-for="zupanija in opgovi_s.filteriZupanije" :key="zupanija">
                    <label class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                        :checked="opgovi_s.filteri.zupanije.includes(zupanija)"
                        @change="odabranaZupanija(zupanija, $event.target.checked)"
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
                    <span class="font-bold">{{ opgovi_s.filteri.mjesta.length }}</span> Odabrano
                  </span>

                  <button
                    type="button"
                    @click="ponistiMjesta"
                    class="text-sm text-gray-900 underline underline-offset-4"
                  >
                    Poništi
                  </button>
                </header>

                <ul class="space-y-1 border-t border-gray-200 p-4">
                  <li v-for="mjesto in opgovi_s.filteriMjesta" :key="mjesto">
                    <label class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                        :checked="opgovi_s.filteri.mjesta.includes(mjesto)"
                        @change="odabranoMjesto(mjesto, $event.target.checked)"
                      />
                      <span class="text-sm font-medium text-gray-700">{{ mjesto }}</span>
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
                <span class="text-sm font-medium"> Ocjena </span>
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
                    Ocjena: <strong>{{ ocjenaMin ?? "Nije odabrana" }}</strong>
                  </span>

                  <button
                    type="button"
                    class="text-sm text-gray-900 underline underline-offset-4"
                    @click="ponistiOcjene"
                  >
                    Poništi
                  </button>
                </header>

                <ul class="space-y-2 border-t border-gray-200 p-4">
                  <li
                    v-for="val in [5, 4, 3, 2, 1]"
                    :key="val"
                    class="flex items-center justify-between"
                  >
                    <label class="inline-flex items-center gap-2">
                      <input
                        type="radio"
                        name="minOcjena"
                        class="size-5 rounded-sm border-gray-300"
                        :value="val"
                        v-model="ocjenaMin"
                      />
                      <span class="text-sm font-medium text-gray-700">{{ val }}+</span>
                    </label>

                    <div class="flex items-center">
                      <svg
                        v-for="i in 5"
                        :key="i"
                        class="w-4 h-4 me-1 fill-current"
                        :class="i <= val ? 'text-orange-600' : 'text-orange-200'"
                        viewBox="0 0 22 20"
                        xmlns="http://www.w3.org/2000/svg"
                        aria-hidden="true"
                      >
                        <path
                          d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
                        />
                      </svg>
                    </div>
                  </li>
                  <li class="flex items-center justify-between mt-4">
                    <label class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                        v-model="bezRecenzija"
                      />
                      <span class="text-sm font-medium text-gray-700">Bez ocjene</span>
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
            class="text-sm text-gray-600 cursor-pointer border p-2 rounded pr-3 border-gray-200 shadow-md flex items-center gap-3"
            @click="ponisti"
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

      <div class="lg:col-span-3">
        <div
          class="lg:col-span-3 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 px-6 py-8 mb-14"
        >
          <div
            v-if="opgovi_s.loading"
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
          <div
            v-else-if="!opgovi_s.loading && opgovi_s.ukupno === 0 && !imaFiltera"
            class="col-span-full rounded-lg border border-dashed border-gray-300 p-10 mt-4 text-center"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="80"
              height="80"
              viewBox="0 0 24 24"
              class="mx-auto"
            >
              <path
                fill="#000000"
                d="m14.623 10.988l-4.092-4.092q.292-.188.664-.292q.372-.104.843-.104q1.245 0 2.103.868Q15 8.237 15 9.5q0 .413-.113.834q-.114.42-.264.654Zm-8.427 6.497q1.333-.956 2.735-1.47Q10.333 15.5 12 15.5q1.18 0 2.151.288q.97.287 1.593.593l-3.892-3.893q-1.194-.092-1.974-.862t-.853-1.964L6.04 6.677q-.915 1.025-1.477 2.359Q4 10.369 4 12q0 1.667.593 3.025q.594 1.358 1.603 2.46Zm11.835-.239q.838-1.025 1.404-2.32Q20 13.63 20 12q0-3.325-2.337-5.663T12 4q-1.535 0-2.868.527T6.754 5.969L18.03 17.246ZM12 21q-1.877 0-3.52-.701q-1.642-.7-2.86-1.92q-1.218-1.217-1.92-2.86Q3 13.877 3 12q0-1.883.701-3.522q.7-1.64 1.92-2.858q1.217-1.218 2.86-1.919Q10.123 3 12 3q1.883 0 3.522.701q1.64.7 2.858 1.92q1.218 1.217 1.92 2.857q.7 1.64.7 3.522q0 1.877-.701 3.52q-.7 1.642-1.92 2.86q-1.217 1.218-2.857 1.92q-1.64.7-3.522.7Z"
              />
            </svg>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">
              Trenutno nemamo registriranih OPG-ova...
            </h3>
            <p class="text-gray-600">Vratite se kasnije.</p>
          </div>
          <div
            v-else-if="!opgovi_s.loading && opgovi_s.opgovi.length === 0 && imaFiltera"
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

          <KarticaOPGa v-else v-for="opg in opgovi_s.opgovi" :key="opg.id" :opg="opg" />

          <Paginacija
            v-if="opgovi_s.ukupno > opgovi_s.velicina_stranice"
            :stranica="opgovi_s.stranica"
            :ukupno-stranica="opgovi_s.ukupno_stranica"
            @idi-na="opgovi_s.promijeniStranicu"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue"
import { useEtrznicaOpgoviStore } from "@/stores/eTrznicaOpgovi"
import KarticaOPGa from "@/components/dijeljeno/KarticaOPGa.vue"
import Paginacija from "@/components/dijeljeno/Paginacija.vue"

const opgovi_s = useEtrznicaOpgoviStore()

onMounted(async () => {
  await opgovi_s.ucitajFiltere()
  await opgovi_s.ucitajOpgove()
  await opgovi_s.ucitajStatistiku()
})

const q = computed({
  get: () => opgovi_s.filteri.q,
  set: (v) => {
    opgovi_s.filteri.q = v
    opgovi_s.stranica = 1
    opgovi_s.ucitajOpgove()
  },
})

const sortiranje = computed({
  get: () => opgovi_s.filteri.sortiranje,
  set: (v) => {
    opgovi_s.filteri.sortiranje = v
    opgovi_s.stranica = 1
    opgovi_s.ucitajOpgove()
  },
})

const imaFiltera = computed(() => {
  const f = opgovi_s.filteri
  return (
    !!(f.q && f.q.trim()) ||
    (Array.isArray(f.zupanije) && f.zupanije.length > 0) ||
    (Array.isArray(f.mjesta) && f.mjesta.length > 0) ||
    (f.ocjena_min !== null && f.ocjena_min !== undefined) ||
    !!(opgovi_s.kat_slug && opgovi_s.kat_slug.trim())
  )
})

function ponisti() {
  opgovi_s.ponistiFiltere()
}

function odabranaZupanija(z, checked) {
  opgovi_s.odabraniFilteri("zupanije", z, checked)
}
function odabranoMjesto(m, checked) {
  opgovi_s.odabraniFilteri("mjesta", m, checked)
}

const ocjenaMin = computed({
  get: () => opgovi_s.filteri.ocjena_min,
  set: (v) => {
    opgovi_s.filteri.ocjena_min = v != null ? Number(v) : null
    opgovi_s.stranica = 1
    opgovi_s.ucitajOpgove()
  },
})

const bezRecenzija = computed({
  get: () => opgovi_s.filteri.bez_recenzija,
  set: (v) => {
    opgovi_s.filteri.bez_recenzija = !!v
    if (v) opgovi_s.filteri.ocjena_min = null
    opgovi_s.stranica = 1
    opgovi_s.ucitajOpgove()
  },
})

function ponistiOcjene() {
  ocjenaMin.value = null
  bezRecenzija.value = false
}

function ponistiZupanije() {
  opgovi_s.filteri.zupanije = []
  opgovi_s.ucitajOpgove()
}
function ponistiMjesta() {
  opgovi_s.filteri.mjesta = []
  opgovi_s.ucitajOpgove()
}
</script>
