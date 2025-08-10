<template>
  <section>
    <div class="mx-auto w-full bg-white rounded-xl max-w-7xl px-5 py-12 md:px-10 md:py-20">
      <h2 class="text-center text-3xl font-bold md:text-5xl">Ivan Horvat</h2>
      <span class="flex justify-center items-center">
        <img
          class="my-5 w-30 h-30 object-cover rounded-full"
          src="https://images.unsplash.com/photo-1464746133101-a2c3f88e0dd9?q=80&w=1686&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          alt=""
        />
      </span>

      <div
        class="mx-auto rounded-xl flex w-full max-w-3xl flex-col flex-wrap justify-between gap-5 bg-gray-100 px-16 py-8 sm:flex-row md:gap-6"
      >
        <div class="flex flex-col items-center justify-center">
          <p class="text-sm uppercase">Naručeno kod nas</p>
          <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">5 proizvoda | 1 usluga</h4>
        </div>

        <div class="flex flex-col items-center justify-center">
          <p class="text-sm uppercase">Zadnja narudžba napravljena</p>
          <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">5.8.2025. 12:34:21</h4>
        </div>

        <div class="flex flex-col items-center justify-center">
          <p class="text-sm uppercase">Najčešće kupljeno</p>
          <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">Jabuke</h4>
        </div>

        <div class="flex flex-col items-center justify-center">
          <p class="text-sm uppercase">Vrijednost svih narudžbi</p>
          <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">62.30 €</h4>
        </div>

        <div class="flow-root mt-8 w-full">
          <dl class="divide-y divide-gray-200 text-sm *:even:bg-gray-50">
            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Email</dt>

              <dd class="text-gray-700 sm:col-span-2">ihorvat@gmail.com</dd>
            </div>
            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Broj telefona</dt>

              <dd class="text-gray-700 sm:col-span-2">0998765432</dd>
            </div>

            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Adresa</dt>

              <dd class="text-gray-700 sm:col-span-2">Preradovićeva 99</dd>
            </div>

            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Županija</dt>

              <dd class="text-gray-700 sm:col-span-2">Sisačko-Moslavačka</dd>
            </div>

            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Grad</dt>

              <dd class="text-gray-700 sm:col-span-2">44000 Sisak</dd>
            </div>
          </dl>
        </div>
      </div>
      <div class="w-full overflow-x-auto mt-10">
        <table class="able-auto border-collapse">
          <thead>
            <tr>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[20%]">Broj narudžbe</th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[15%]">Ukupan iznos</th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[45%]">
                Datum i vrijeme narudžbe
              </th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[10%]">Status</th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[10%]"></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#234521</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">23.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[45%]">
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
                <router-link :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                >
              </td>
            </tr>
            <tr>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#543621</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">52.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[45%]">
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
                <router-link :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                >
              </td>
            </tr>
            <tr>
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#623413</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">12.99 €</td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[45%]">
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
                <router-link :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe' }"
                  >Detalji</router-link
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
