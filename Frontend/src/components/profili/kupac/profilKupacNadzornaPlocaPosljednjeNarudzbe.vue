<template>
  <section>
    <div class="flex justify-center items-center p-5">
      <div class="w-full max-w-7xl rounded-lg overflow-x-auto bg-white shadow-md">
        <div class="p-4 min-w-full">
          <div class="flex justify-between items-center">
            <div>
              <p class="text-2xl font-bold mb-2 ps-4">Posljednje narudžbe</p>
            </div>
            <!--  <router-link :to="{ name: 'profilKupacMojeNarudzbe' }">
              <button class="bg-orange-500 text-gray-100 px-8 py-3 rounded-md cursor-pointer">
                Pogledaj sve narudžbe
              </button>
            </router-link> -->
          </div>
        </div>

        <table class="w-full text-left">
          <thead>
            <tr>
              <th class="px-8 py-3 border-b border-gray-300 w-[20%]">Naziv OPG-a</th>
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
                <a class="text-orange-600 hover:text-orange-900 hover:underline" href="#"
                  >OPG Marić</a
                >
              </td>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#234521</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">23.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
                15.07.2025. 12:32:52
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full bg-red-600 px-2.5 py-0.5 text-red-100"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="-ms-1 me-1.5 size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z"
                    />
                  </svg>

                  <p class="text-sm whitespace-nowrap">Otkazano</p>
                </span>
              </td>
              <td
                class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
              >
                <!--  <router-link :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                > -->
              </td>
            </tr>
            <tr>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <a class="text-orange-600 hover:text-orange-900 hover:underline" href="#"
                  >OPG Marić</a
                >
              </td>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#234521</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">52.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
                15.07.2025. 12:32:52
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full bg-amber-500 px-2.5 py-0.5 text-amber-100"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    class="-ms-1 me-1.5 size-3"
                  >
                    <path
                      fill="none"
                      stroke="currentColor"
                      stroke-width="1.5"
                      d="M1 1h22M10 4.5h4V6c0 1-2 2-2 2s-2-1-2-2V4.5ZM5 1v5c0 3 5 3.235 5 6s-5 3-5 6v5M19 1v5c0 3-5 3.235-5 6s5 3 5 6v5M1 23h22M8 21c0-2 4-4 4-4s4 2 4 4v2H8v-2Z"
                    />
                  </svg>

                  <p class="text-sm whitespace-nowrap">U tijeku</p>
                </span>
              </td>
              <td
                class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
              >
                <!--   <router-link :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                > -->
              </td>
            </tr>
            <tr>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <a class="text-orange-600 hover:text-orange-900 hover:underline" href="#"
                  >OPG Marić</a
                >
              </td>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#234521</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">12.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
                15.07.2025. 12:32:52
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full bg-emerald-100 px-2.5 py-0.5 text-emerald-700"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="-ms-1 me-1.5 size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>

                  <p class="text-sm whitespace-nowrap">Isporučeno</p>
                </span>
              </td>
              <td
                class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
              >
                <!--  <router-link :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                > -->
              </td>
            </tr>
            <tr>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <a class="text-orange-600 hover:text-orange-900 hover:underline" href="#"
                  >OPG Marić</a
                >
              </td>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#234521</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">16.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
                15.07.2025. 12:32:52
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full bg-emerald-100 px-2.5 py-0.5 text-emerald-700"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="-ms-1 me-1.5 size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>

                  <p class="text-sm whitespace-nowrap">Isporučeno</p>
                </span>
              </td>
              <td
                class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
              >
                <!--  <router-link :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                > -->
              </td>
            </tr>

            <tr>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <a class="text-orange-600 hover:text-orange-900 hover:underline" href="#"
                  >OPG Marić</a
                >
              </td>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#234521</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">32.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
                15.07.2025. 12:32:52
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full bg-emerald-100 px-2.5 py-0.5 text-emerald-700"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="-ms-1 me-1.5 size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>

                  <p class="text-sm whitespace-nowrap">Isporučeno</p>
                </span>
              </td>
              <td
                class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
              >
                <!--   <router-link :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                > -->
              </td>
            </tr>
            <tr>
              <td class="px-8 py-5 w-[20%]">
                <a class="text-orange-600 hover:text-orange-900 hover:underline" href="#"
                  >OPG Marić</a
                >
              </td>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#234521</p>
              </td>
              <td class="px-8 py-5 text-gray-500 w-[15%]">18.99 €</td>
              <td class="px-8 py-5 text-gray-500 w-[25%]">15.07.2025. 12:32:52</td>
              <td class="px-8 py-5 text-gray-500 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full bg-emerald-100 px-2.5 py-0.5 text-emerald-700"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="-ms-1 me-1.5 size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>

                  <p class="text-sm whitespace-nowrap">Isporučeno</p>
                </span>
              </td>
              <td class="px-8 py-5 text-orange-600 hover:text-orange-900 hover:underline w-[10%]">
                <!--    <router-link :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                > -->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
