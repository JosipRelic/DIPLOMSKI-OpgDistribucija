<template>
  <div class="max-w-6xl mx-auto bg-white rounded-xl shadow-lg p-10">
    <h1 class="text-2xl font-bold mb-3">Nadolazeće rezervacije usluga</h1>
    <div class="mx-auto mb-12">
      <label for="pretragaBrojNarudzbe">
        <div class="relative">
          <input
            type="text"
            id="pretragaBrojNarudzbe"
            placeholder="Pretraži po broju narudžbe, nazivu usluge ili kategorije..."
            class="mt-0.5 w-full rounded bg-white border border-gray-200 pe-10 shadow-md sm:text-sm p-3 h-10"
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
    <ol class="relative border-s border-orange-500 ms-6">
      <li class="mb-10 ms-8">
        <span
          class="absolute flex items-center justify-center w-6 h-6 bg-orange-600 rounded-full -start-3 ring-8 ring-orange-600"
        >
          <svg
            class="w-4 h-4 text-white"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
            />
          </svg>
        </span>
        <h3 class="flex items-center mb-1 text-lg font-semibold text-orange-600">
          26. siječnja 2025.
        </h3>
        <ol class="mt-3 divide-y divide-gray-200">
          <li>
            <a href="#" class="items-center block p-3 ps-0 sm:flex">
              <img
                class="w-20 h-20 mb-3 me-3 rounded-xl sm:mb-0"
                src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?q=80&w=1548&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                alt="Oranje"
              />
              <div class="text-gray-600">
                <div class="text-base font-normal">
                  Kategorija:
                  <span class="font-medium text-gray-900">Priprema tla |</span>
                  Usluga:
                  <span class="font-medium text-gray-900">Oranje |</span> Količina:
                  <span class="font-medium text-gray-900"> 1 hektar |</span> Broj radnih sati:
                  <span class="font-medium text-gray-900"> 1:00 </span>
                </div>
                <div class="text-sm font-bold text-teal-500">12:00 -> 13:00</div>
                <div class="inline-flex items-center text-sm font-normal">
                  <div class="text-gray-900 mr-2">
                    Narudžba br:
                    <span class="text-orange-600 hover:underline font-semibold">#223c2f</span>
                  </div>
                  <div class="text-gray-900 mr-2">
                    | Kupac:
                    <span class="text-orange-600 hover:underline font-semibold">Josip Relić</span>
                  </div>
                </div>
              </div>
            </a>
          </li>
        </ol>
      </li>
      <li class="mb-10 ms-8">
        <span
          class="absolute flex items-center justify-center w-6 h-6 bg-orange-600 rounded-full -start-3 ring-8 ring-orange-600"
        >
          <svg
            class="w-4 h-4 text-white"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
            />
          </svg>
        </span>
        <h3 class="mb-1 text-lg font-semibold text-orange-600">25. siječnja 2025.</h3>
        <ol class="mt-3 divide-y divide-gray-200">
          <li>
            <a href="#" class="items-center block p-3 ps-0 sm:flex">
              <img
                class="w-20 h-20 mb-3 me-3 rounded-xl sm:mb-0"
                src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?q=80&w=1548&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                alt="Oranje"
              />
              <div class="text-gray-600">
                <div class="text-base font-normal">
                  Kategorija:
                  <span class="font-medium text-gray-900">Priprema tla |</span>
                  Usluga:
                  <span class="font-medium text-gray-900">Oranje |</span> Količina:
                  <span class="font-medium text-gray-900"> 1 hektar |</span> Broj radnih sati:
                  <span class="font-medium text-gray-900"> 5:00 </span>
                </div>
                <div class="text-sm font-bold text-teal-500">11:00 -> 16:00</div>
                <div class="inline-flex items-center text-sm font-normal">
                  <div class="text-gray-900 mr-2">
                    Narudžba br:
                    <span class="text-orange-600 hover:underline font-semibold">#223c2f</span>
                  </div>
                  <div class="text-gray-900 mr-2">
                    | Kupac:
                    <span class="text-orange-600 hover:underline font-semibold">Josip Relić</span>
                  </div>
                </div>
              </div>
            </a>
          </li>
        </ol>
      </li>
      <li class="mb-10 ms-8">
        <span
          class="absolute flex items-center justify-center w-6 h-6 bg-orange-600 rounded-full -start-3 ring-8 ring-orange-600"
        >
          <svg
            class="w-6 h-6 text-white"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
          >
            <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2">
              <path stroke-linejoin="round" d="M8 2L2 8.156V16l6 6h8l6-6V8.156L16 2H8Z" />
              <path d="M16 12H8" />
            </g>
          </svg>
        </span>
        <h3 class="mb-1 text-lg font-semibold text-orange-600">Nemate više rezervacija.</h3>
      </li>
    </ol>
  </div>
</template>
