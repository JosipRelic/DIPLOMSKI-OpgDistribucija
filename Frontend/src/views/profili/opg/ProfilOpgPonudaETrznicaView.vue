<template>
  <div class="relative overflow-x-auto m-4 shadow-md rounded-lg">
    <div class="flex items-center justify-center p-20 py-4 md:py-8 flex-wrap bg-white">
      <button
        type="button"
        class="border border-gray-200 bg-[#223c2f] text-white shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Domaće voće <span class="text-green-600">(4)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Sezonsko povrće <span class="text-green-600">(2)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Jaja i mliječni proizvodi <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Iz košnice <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Domaća pića i rakije <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Ulja iz prirode <span class="text-green-600">(4)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Čajevi i začinsko bilje <span class="text-green-600">(2)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Suhomesnati proizvodi <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Prirodna kozmetika <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Iz šume i dvorišta <span class="text-red-400">(0)</span>
      </button>
    </div>

    <div
      class="relative overflow-x-auto m-4 shadow-md rounded-lg bg-white p-4 flex items-center gap-2 cursor-pointer hover:bg-gray-100"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 32 32">
        <g fill="none">
          <path
            fill="url(#fluentColorAddCircle320)"
            d="M30 16c0 7.732-6.268 14-14 14S2 23.732 2 16S8.268 2 16 2s14 6.268 14 14"
          />
          <path
            fill="url(#fluentColorAddCircle321)"
            d="M15 10a1 1 0 1 1 2 0v5h5a1 1 0 1 1 0 2h-5v5a1 1 0 1 1-2 0v-5h-5a1 1 0 1 1 0-2h5z"
          />
          <defs>
            <linearGradient
              id="fluentColorAddCircle320"
              x1="3"
              x2="22.323"
              y1="7.25"
              y2="27.326"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#52D17C" />
              <stop offset="1" stop-color="#22918B" />
            </linearGradient>
            <linearGradient
              id="fluentColorAddCircle321"
              x1="11.625"
              x2="15.921"
              y1="10.428"
              y2="25.592"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#fff" />
              <stop offset="1" stop-color="#E3FFD9" />
            </linearGradient>
          </defs>
        </g>
      </svg>
      <P class="text-gray-600 rounded-full text-base font-medium">Dodaj novi proizvod</P>
    </div>

    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
      <thead class="text-xs uppercase bg-gray-200 text-gray-700">
        <tr>
          <th scope="col" class="px-16 py-3"></th>
          <th scope="col" class="pe-6 py-3">Proizvod</th>
          <th scope="col" class="px-6 py-3">Opis</th>
          <th scope="col" class="px-4 py-3">Dostupno</th>
          <th scope="col" class="px-6 py-3">Cijena</th>
          <th scope="col" class="px-6 py-3">Mjerna jedinica</th>
          <th scope="col" class="px-6 py-3"></th>
          <th scope="col" class="px-6 py-3"></th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              checked
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
