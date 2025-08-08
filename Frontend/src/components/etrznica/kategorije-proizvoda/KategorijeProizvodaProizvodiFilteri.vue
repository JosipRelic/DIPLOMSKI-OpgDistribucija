<template>
  <div class="space-y-4">
    <div>
      <label for="PretragaProizvoda">
        <span class="block text-xs font-medium text-gray-700"> Pretraži po nazivu</span>

        <div class="relative">
          <input
            type="text"
            id="PretragaProizvoda"
            placeholder="Unesi proizvod ili opg..."
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
    <div>
      <label for="Sortiraj" class="block text-xs font-medium text-gray-700"> Sortiraj </label>

      <select id="Sortiraj" class="mt-1 rounded-sm border-gray-300 text-sm">
        <option>Sortiraj po</option>
        <option value="Naziv, Silazno">Naziv, Silazno</option>
        <option value="Naziv, Uzlazno">Naziv, Uzlazno</option>
        <option value="Cijena, Silazno">Ocjena, Silazno</option>
        <option value="Cijena, Uzlazno">Ocjena, Uzlazno</option>
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
              <span class="text-sm text-gray-700"> 0 Odabrano </span>

              <button type="button" class="text-sm text-gray-900 underline underline-offset-4">
                Poništi
              </button>
            </header>

            <ul class="space-y-1 border-t border-gray-200 p-4">
              <li>
                <label for="FiltrirajZupanije" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajZupanije"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Sisačko-Moslavačka </span>
                </label>
              </li>

              <li>
                <label for="FiltrirajPovrce" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajPovrce"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Zagrebačka </span>
                </label>
              </li>

              <li>
                <label for="FiltrirajAlkoholnaPica" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajAlkoholnaPica"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Krapinsko-Zagorska </span>
                </label>
              </li>

              <li>
                <label for="FiltrirajZimnice" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajZimnice"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Brodsko-Posavska </span>
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
              <span class="text-sm text-gray-700"> 0 Odabrano </span>

              <button type="button" class="text-sm text-gray-900 underline underline-offset-4">
                Poništi
              </button>
            </header>

            <ul class="space-y-1 border-t border-gray-200 p-4">
              <li>
                <label for="FiltrirajMjesto" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajMjesto"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Daruvar </span>
                </label>
              </li>

              <li>
                <label for="FiltrirajMjesto" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajMjesto"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Sisak </span>
                </label>
              </li>

              <li>
                <label for="FiltrirajMjesto" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajMjesto"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Novska </span>
                </label>
              </li>

              <li>
                <label for="FiltrirajMjesto" class="inline-flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="FiltrirajMjesto"
                    class="size-5 rounded-sm border-gray-300 shadow-sm"
                  />

                  <span class="text-sm font-medium text-gray-700"> Kutina </span>
                </label>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </div>
  </div>
</template>
