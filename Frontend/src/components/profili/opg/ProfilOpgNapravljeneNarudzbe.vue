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
              placeholder="Pretraži po broju narudžbe"
              class="mt-0.5 w-full rounded border-gray-300 pe-10 shadow-sm sm:text-sm p-3 h-10"
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

      <table class="w-full text-left">
        <thead>
          <tr>
            <th class="px-8 py-3 border-b border-gray-300 w-[20%]">Naručeno od</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[20%]">Broj narudžbe</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[15%]">Ukupan iznos</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[25%]">Datum i vrijeme narudžbe</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[10%]">Status</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[10%]"></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
              <a href="#" class="text-orange-600 hover:text-orange-900 hover:underline"
                >OPG Marić</a
              >
            </td>
            <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
              <p class="text-gray-500">1759182692664-624812</p>
            </td>
            <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">23.99 €</td>
            <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
              23.09.2025 15:32:25
            </td>
            <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
              <div class="flex items-center gap-2">
                <span
                  class="inline-flex items-center justify-center rounded-full bg-amber-500 text-amber-100 px-2.5 py-0.5"
                >
                  <p class="text-sm whitespace-nowrap capitalize">U tijeku</p>
                </span>
              </div>
            </td>
            <td
              class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
            >
              <router-link :to="{ name: 'profilOpgNapravljeneNarudzbeDetaljiNarudzbe' }"
                >Detalji</router-link
              >
            </td>
          </tr>
        </tbody>
      </table>

      <div class="flex items-center p-5 justify-center min-w-full">
        <div class="flex border border-gray-200 shadow rounded-md">
          <button
            class="text-black border-r border-gray-200 font-semibold px-4 py-2 cursor-pointer"
          >
            Prethodna
          </button>
          <div class="flex space-x-2">
            <button class="px-4 py-2 bg-orange-500 text-white">1</button>
          </div>
          <button
            class="text-black border-l border-gray-200 font-semibold px-4 py-2 cursor-pointer"
          >
            Sljedeća
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
