<template>
  <div
    class="max-w-6xl mx-auto bg-white shadow-xl rounded-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2 my-20"
  >
    <div class="p-8">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="100"
        height="100"
        viewBox="0 0 32 32"
        class="mx-auto"
      >
        <path
          class="fill-orange-600"
          d="M29.755 21.345A1 1 0 0 0 29 21h-2v-2c0-1.102-.897-2-2-2h-4c-1.103 0-2 .898-2 2v2h-2a1.001 1.001 0 0 0-.99 1.142l1 7A1 1 0 0 0 18 30h10a1 1 0 0 0 .99-.858l1-7a1.001 1.001 0 0 0-.235-.797M21 19h4v2h-4zm6.133 9h-8.266l-.714-5h9.694zM10 20h2v10h-2z"
        />
        <path
          class="fill-gray-900"
          d="m16.78 17.875l-1.906-2.384l-1.442-3.605A2.986 2.986 0 0 0 10.646 10H5c-1.654 0-3 1.346-3 3v7c0 1.103.897 2 2 2h1v8h2V20H4v-7a1 1 0 0 1 1-1h5.646c.411 0 .776.247.928.629l1.645 3.996l2 2.5zM4 5c0-2.206 1.794-4 4-4s4 1.794 4 4s-1.794 4-4 4s-4-1.794-4-4m2 0c0 1.103.897 2 2 2s2-.897 2-2s-.897-2-2-2s-2 .897-2 2"
        />
      </svg>

      <h2 class="text-2xl xl:text-3xl font-extrabold text-gray-800 mb-6 flex flex-col items-center">
        Podaci o kupcu
      </h2>

      <div class="flex flex-col items-center">
        <button
          class="w-full max-w-xs font-bold shadow-sm hover:bg-red-400 rounded-lg py-3 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
        >
          <div class="bg-white p-2 rounded-full">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-6 text-red-600">
              <path
                fill="currentColor"
                d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
              />
            </svg>
          </div>
          <span class="ml-4"> Ispunite glasovno pomoću AI </span>
        </button>
        <small class="pt-2 w-full max-w-xs text-xs"
          >Pritisnite gumb i popunite obrazac glasom npr. "Zovem se Ivan Horvat. Moja email adresa
          je ihorvat@gmail.com itd..."</small
        >
      </div>
      <div class="my-8 border-b text-center">
        <div
          class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
        >
          ili unesite podatke ručno
        </div>
      </div>
      <form class="space-y-5">
        <div class="flex gap-4">
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Ime</label>
            <input
              type="text"
              placeholder="Ivan"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Prezime</label>
            <input
              type="text"
              placeholder="Horvat"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
        </div>
        <div>
          <label class="block mb-1 text-sm text-gray-600">Email</label>
          <input
            type="text"
            placeholder="ihorvat@gmail.com"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>
        <div>
          <label class="block mb-1 text-sm text-gray-600">Broj telefona</label>
          <input
            type="text"
            placeholder="0998765432"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>
        <div>
          <label class="block mb-1 text-sm text-gray-600">Adresa</label>
          <input
            type="text"
            placeholder="Preradovićeva 99"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>
        <div>
          <label class="block mb-1 text-sm text-gray-600">Država</label>
          <input
            type="text"
            placeholder="Hrvatska"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>
        <div>
          <label class="block mb-1 text-sm text-gray-600">Županija</label>
          <input
            type="text"
            placeholder="Sisačko-Moslavačka"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>
        <div class="flex gap-4">
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Grad</label>
            <input
              type="text"
              placeholder="Sisak"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Poštanski broj</label>
            <input
              type="text"
              placeholder="44000"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
        </div>
      </form>
    </div>

    <div class="bg-gray-50 p-8 border-l border-gray-200">
      <h3 class="text-xl font-semibold text-gray-700 mb-2">Naručit ćete</h3>
      <div class="mb-1 text-orange-400 border-b border-orange-200 mb-2">Proizvodi</div>
      <ul class="space-y-4 mb-4">
        <li class="flex items-center gap-4">
          <img
            src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt=""
            class="size-20 rounded-sm object-cover"
          />

          <div>
            <h3 class="text-lg text-gray-900">Krastavci</h3>

            <dl class="mt-0.5 space-y-px text-sm text-gray-600">
              <div>
                <dt class="inline">Cijena:</dt>
                <dd class="inline ml-1 font-bold">2.99 €</dd>
              </div>
              <div>
                <dt class="inline">Količina:</dt>
                <dd class="inline ml-1 font-bold">1 / kg</dd>
              </div>
            </dl>
          </div>
        </li>
        <li class="flex items-center gap-4">
          <img
            src="https://images.unsplash.com/photo-1518977956812-cd3dbadaaf31?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt=""
            class="size-20 rounded-sm object-cover"
          />

          <div>
            <h3 class="text-lg text-gray-900">Luk</h3>

            <dl class="mt-0.5 space-y-px text-sm text-gray-600">
              <div>
                <dt class="inline">Cijena:</dt>
                <dd class="inline ml-1 font-bold">0.99 €</dd>
              </div>
              <div>
                <dt class="inline">Količina:</dt>
                <dd class="inline ml-1 font-bold">1 / kg</dd>
              </div>
            </dl>
          </div>
        </li>
      </ul>

      <div class="text-orange-400 border-b border-orange-200 mb-2">Usluge</div>
      <ul class="space-y-4 mb-4">
        <li class="flex items-center gap-4">
          <img
            src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGZhcm1pbmd8ZW58MHx8MHx8fDI%3D"
            alt=""
            class="size-20 rounded-sm object-cover"
          />

          <div>
            <h3 class="text-lg text-gray-900">Oranje</h3>

            <dl class="mt-0.5 space-y-px text-sm text-gray-600">
              <div class="text-xs">
                <dt class="inline">Cijena:</dt>
                <dd class="inline ml-1 font-bold">200.00 €</dd>
              </div>
              <div class="text-xs">
                <dt class="inline">Količina:</dt>
                <dd class="inline ml-1 font-bold">1 / hektar</dd>
              </div>

              <div class="text-xs">
                <dt class="inline">Termin:</dt>
                <dd class="inline ml-1 font-bold">
                  26. rujna 2025. 11:00 -> 26. rujna 2025. 13:00
                </dd>
              </div>
            </dl>
          </div>
        </li>
      </ul>
      <h3 class="text-xl font-semibold text-gray-700 mb-6 mt-10 border-t pt-6">
        Odaberite način plaćanja
      </h3>

      <div class="space-y-4">
        <div
          class="flex items-center p-4 bg-white rounded-lg shadow-sm border border-gray-300 hover:shadow-md transition"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            viewBox="0 0 48 48"
            class="mr-4"
          >
            <path
              fill="#78909C"
              d="M40 41H8c-2.2 0-4-1.8-4-4V16.1c0-1.3.6-2.5 1.7-3.3L24 0l18.3 12.8c1.1.7 1.7 2 1.7 3.3V37c0 2.2-1.8 4-4 4z"
            />
            <path fill="#AED581" d="M14 1h20v31H14z" />
            <g fill="#558B2F">
              <path d="M13 0v33h22V0H13zm20 31H15V2h18v29z" />
              <path
                d="M34 3c0 1.7-.3 3-2 3s-3-1.3-3-3s1.3-2 3-2s2 .3 2 2zM16 1c1.7 0 3 .3 3 2s-1.3 3-3 3s-2-1.3-2-3s.3-2 2-2z"
              />
              <circle cx="24" cy="8" r="2" />
              <circle cx="24" cy="20" r="6" />
            </g>
            <path fill="#CFD8DC" d="M40 41H8c-2.2 0-4-1.8-4-4V17l20 13l20-13v20c0 2.2-1.8 4-4 4z" />
          </svg>
          <p class="text-gray-700 font-medium">Pouzećem</p>
        </div>

        <div
          class="flex items-center p-4 bg-white rounded-lg shadow-sm border border-gray-300 hover:shadow-md transition"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            viewBox="0 0 256 302"
            class="mr-4"
          >
            <path
              fill="#27346A"
              d="M217.168 23.507C203.234 7.625 178.046.816 145.823.816h-93.52A13.393 13.393 0 0 0 39.076 12.11L.136 259.077c-.774 4.87 2.997 9.28 7.933 9.28h57.736l14.5-91.971l-.45 2.88c1.033-6.501 6.593-11.296 13.177-11.296h27.436c53.898 0 96.101-21.892 108.429-85.221c.366-1.873.683-3.696.957-5.477c-1.556-.824-1.556-.824 0 0c3.671-23.407-.025-39.34-12.686-53.765"
            />
            <path
              fill="#27346A"
              d="M102.397 68.84a11.737 11.737 0 0 1 5.053-1.14h73.318c8.682 0 16.78.565 24.18 1.756a101.6 101.6 0 0 1 6.177 1.182a89.928 89.928 0 0 1 8.59 2.347c3.638 1.215 7.026 2.63 10.14 4.287c3.67-23.416-.026-39.34-12.687-53.765C203.226 7.625 178.046.816 145.823.816H52.295C45.71.816 40.108 5.61 39.076 12.11L.136 259.068c-.774 4.878 2.997 9.282 7.925 9.282h57.744L95.888 77.58a11.717 11.717 0 0 1 6.509-8.74Z"
            />
            <path
              fill="#2790C3"
              d="M228.897 82.749c-12.328 63.32-54.53 85.221-108.429 85.221H93.024c-6.584 0-12.145 4.795-13.168 11.296L61.817 293.621c-.674 4.262 2.622 8.124 6.934 8.124h48.67a11.71 11.71 0 0 0 11.563-9.88l.474-2.48l9.173-58.136l.591-3.213a11.71 11.71 0 0 1 11.562-9.88h7.284c47.147 0 84.064-19.154 94.852-74.55c4.503-23.15 2.173-42.478-9.739-56.054c-3.613-4.112-8.1-7.508-13.327-10.28c-.283 1.79-.59 3.604-.957 5.477Z"
            />
            <path
              fill="#1F264F"
              d="M216.952 72.128a89.928 89.928 0 0 0-5.818-1.49a109.904 109.904 0 0 0-6.177-1.174c-7.408-1.199-15.5-1.765-24.19-1.765h-73.309a11.57 11.57 0 0 0-5.053 1.149a11.683 11.683 0 0 0-6.51 8.74l-15.582 98.798l-.45 2.88c1.025-6.501 6.585-11.296 13.17-11.296h27.444c53.898 0 96.1-21.892 108.428-85.221c.367-1.873.675-3.688.958-5.477c-3.122-1.648-6.501-3.072-10.14-4.279a83.26 83.26 0 0 0-2.77-.865"
            />
          </svg>
          <p class="text-gray-700 font-medium">PayPal</p>
        </div>
      </div>

      <h3 class="text-xl font-semibold text-gray-700 mb-6 mt-10 border-t pt-6">
        Odaberite način dostave
      </h3>

      <div class="space-y-4">
        <div
          class="flex items-center p-4 bg-white rounded-lg shadow-sm border border-gray-300 hover:shadow-md transition"
        >
          <input id="bordered-radio-1" type="radio" value="" name="bordered-radio" />

          <label for="bordered-radio-1" class="w-full py-4 ms-2 text-sm font-medium text-gray-900"
            >Dostava na adresu (5€)</label
          >

          <input checked id="bordered-radio-2" type="radio" value="" name="bordered-radio" />
          <label for="bordered-radio-2" class="w-full py-4 ms-2 text-sm font-medium text-gray-900"
            >Osobno preuzimanje (Besplatno)</label
          >
        </div>
      </div>

      <div class="mt-10 border-t pt-6">
        <h4 class="text-gray-700 font-semibold mb-2">Za platiti</h4>
        <div class="flex justify-between text-gray-600">
          <span>Ukupan iznos bez PDV-a</span>
          <span>4.18 €</span>
        </div>
        <div class="flex justify-between text-gray-600 mt-1">
          <span>PDV (25%)</span>
          <span>1.39 €</span>
        </div>
        <div class="flex justify-between text-gray-600 mt-1">
          <span>Dostava</span>
          <span>Besplatna (osobno preuzimanje)</span>
        </div>
        <div class="flex justify-between text-lg font-bold text-gray-800 mt-4">
          <span>Ukupan iznos s PDV-om</span>
          <span>5.57 €</span>
        </div>
      </div>
      <router-link :to="{ name: 'potvrdaNarudzbe' }"
        ><button
          class="w-full mt-4 bg-teal-600 hover:bg-teal-900 text-gray-100 text-lg py-3 rounded-lg transition"
        >
          Naruči
        </button></router-link
      >
    </div>
  </div>
</template>
