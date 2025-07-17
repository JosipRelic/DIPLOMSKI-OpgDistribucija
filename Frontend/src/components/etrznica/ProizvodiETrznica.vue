<template>
  <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
    <header>
      <h2 class="text-xl font-bold text-gray-900 sm:text-3xl">Proizvodi</h2>

      <p class="mt-4 max-w-md text-gray-500">
        Na našoj E-Tržnici pronaći ćete pažljivo odabrane proizvode domaćih OPG-ova. Od svježeg voća
        i povrća do raznih delicija i prirodnih proizvoda. Svaki proizvod dolazi izravno s hrvatskih
        farmi, s naglaskom na kvalitetu, svježinu i lokalnu proizvodnju. Pregledajte ponudu i
        pronađite sve što vam treba, brzo i jednostavno.
      </p>
    </header>

    <div class="mt-8 block lg:hidden">
      <button
        class="flex cursor-pointer items-center gap-2 border-b border-gray-400 pb-1 text-gray-900 transition hover:border-gray-600"
      >
        <span class="text-sm font-medium"> Filtriraj i Sortiraj </span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="size-4 rtl:rotate-180"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
        </svg>
      </button>
    </div>

    <div class="mt-4 lg:mt-8 lg:grid lg:grid-cols-4 lg:items-start lg:gap-8">
      <div class="hidden space-y-4 lg:block">
        <div>
          <label for="Sortiraj" class="block text-xs font-medium text-gray-700"> Sortiraj </label>

          <select id="Sortiraj" class="mt-1 rounded-sm border-gray-300 text-sm">
            <option>Sortiraj po</option>
            <option value="Naziv, Silazno">Naziv, Silazno</option>
            <option value="Naziv, Uzlazno">Naziv, Uzlazno</option>
            <option value="Cijena, Silazno">Cijena, Silazno</option>
            <option value="Cijena, Uzlazno">Cijena, Uzlazno</option>
          </select>
        </div>

        <div>
          <p class="block text-xs font-medium text-gray-700">Filteri</p>

          <div class="mt-1 space-y-2">
            <details
              class="overflow-hidden rounded-sm border border-gray-300 [&_summary::-webkit-details-marker]:hidden"
            >
              <summary
                class="flex cursor-pointer items-center justify-between gap-2 p-4 text-gray-900 transition"
              >
                <span class="text-sm font-medium"> Dostupnost </span>

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
                  <span class="text-sm text-gray-700"> 0 odabrano </span>

                  <button
                    type="button"
                    class="text-sm text-gray-900 underline underline-offset-4 hover:no-underline"
                  >
                    Poništi
                  </button>
                </header>

                <ul class="space-y-1 border-t border-gray-200 p-4">
                  <li>
                    <label for="FilterInStock" class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        id="FilterInStock"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                      />

                      <span class="text-sm font-medium text-gray-700"> Dostupno (5+) </span>
                    </label>
                  </li>

                  <li>
                    <label for="FilterOutOfStock" class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        id="FilterOutOfStock"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                      />

                      <span class="text-sm font-medium text-gray-700"> Rasprodano (10+) </span>
                    </label>
                  </li>
                </ul>
              </div>
            </details>

            <details
              class="overflow-hidden rounded-sm border border-gray-300 [&_summary::-webkit-details-marker]:hidden"
            >
              <summary
                class="flex cursor-pointer items-center justify-between gap-2 p-4 text-gray-900 transition"
              >
                <span class="text-sm font-medium"> Cijena </span>

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
                  <span class="text-sm text-gray-700"> Najviša cijena je 300 € </span>

                  <button
                    type="button"
                    class="text-sm text-gray-900 underline underline-offset-4 hover:no-underline"
                  >
                    Poništi
                  </button>
                </header>

                <div class="border-t border-gray-200 p-4">
                  <div class="flex justify-between gap-4">
                    <label for="FiltrirajCijenuOd" class="flex items-center gap-2">
                      <span class="text-sm text-gray-600">€</span>

                      <input
                        type="number"
                        id="FiltrirajCijenuOd"
                        placeholder="Od"
                        class="w-full rounded-md border-gray-200 shadow-xs sm:text-sm"
                      />
                    </label>

                    <label for="FiltrirajCijenuDo" class="flex items-center gap-2">
                      <span class="text-sm text-gray-600">€</span>

                      <input
                        type="number"
                        id="FiltrirajCijenuDo"
                        placeholder="Do"
                        class="w-full rounded-md border-gray-200 shadow-xs sm:text-sm"
                      />
                    </label>
                  </div>
                </div>
              </div>
            </details>

            <details
              class="overflow-hidden rounded-sm border border-gray-300 [&_summary::-webkit-details-marker]:hidden"
            >
              <summary
                class="flex cursor-pointer items-center justify-between gap-2 p-4 text-gray-900 transition"
              >
                <span class="text-sm font-medium"> Kategorije </span>

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
                  <span class="text-sm text-gray-700"> 0 Odabrano </span>

                  <button type="button" class="text-sm text-gray-900 underline underline-offset-4">
                    Poništi
                  </button>
                </header>

                <ul class="space-y-1 border-t border-gray-200 p-4">
                  <li>
                    <label for="FiltrirajVoce" class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        id="FiltrirajVoce"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                      />

                      <span class="text-sm font-medium text-gray-700"> Voće </span>
                    </label>
                  </li>

                  <li>
                    <label for="FiltrirajPovrce" class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        id="FiltrirajPovrce"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                      />

                      <span class="text-sm font-medium text-gray-700"> Povrće </span>
                    </label>
                  </li>

                  <li>
                    <label for="FiltrirajAlkoholnaPica" class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        id="FiltrirajAlkoholnaPica"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                      />

                      <span class="text-sm font-medium text-gray-700"> Alkoholna Pića </span>
                    </label>
                  </li>

                  <li>
                    <label for="FiltrirajZimnice" class="inline-flex items-center gap-2">
                      <input
                        type="checkbox"
                        id="FiltrirajZimnice"
                        class="size-5 rounded-sm border-gray-300 shadow-sm"
                      />

                      <span class="text-sm font-medium text-gray-700"> Zimnice </span>
                    </label>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </div>

        <div>
          <label for="PretragaProizvoda">
            <span class="block text-xs font-medium text-gray-700"> Pretraži po nazivu </span>

            <div class="relative">
              <input
                type="text"
                id="PretragaProizvoda"
                class="mt-0.5 w-full h-10 rounded border-gray-300 pe-10 shadow-sm sm:text-sm bg-white p-3"
              />

              <span class="absolute inset-y-0 right-2 grid w-8 place-content-center">
                <button
                  type="button"
                  aria-label="Submit"
                  class="rounded-full p-1.5 text-gray-700 transition-colors hover:bg-gray-100"
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
      </div>

      <div
        class="lg:col-span-3 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 px-20 py-8 mb-14"
      >
        <KarticaProizvoda />

        <Paginacija />
      </div>
    </div>
  </div>
</template>

<script setup>
import KarticaProizvoda from "@/components/dijeljeno/KarticaProizvoda.vue"
import Paginacija from "@/components/etrznica/PaginacijaETrznica.vue"
</script>
