<template>
  <div
    class="max-w-6xl mx-auto px-6 py-12 grid grid-cols-1 md:grid-cols-2 gap-16 items-start bg-white rounded-2xl my-14 shadow-lg max-xl:mx-10"
  >
    <div class="space-y-6 ps-4">
      <nav class="text-sm text-gray-500 flex items-center space-x-2">
        <span class="hover:underline cursor-pointer"
          ><router-link :to="{ name: 'ETrznicaKategorijaSezonskoPovrce' }"
            >Sezonsko povrće</router-link
          ></span
        >
        <span>/</span>
        <span>Krastavci</span>
      </nav>

      <div>
        <h1 class="text-3xl font-bold text-gray-900">Krastavci</h1>
        <div class="flex items-center mt-2 space-x-2 text-sm text-gray-600">
          <a href="#" class="hover:underline">Opg Horvat</a>
        </div>
      </div>

      <div class="text-2xl font-semibold text-gray-900">
        2.99 € <span class="text-gray-400"> / kg</span>
      </div>

      <p class="text-gray-600 text-base">
        Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
        obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni
        prirodne svježine i blagih nota koje pristaju svakom jelu.
      </p>

      <div class="flex items-center text-green-600 space-x-2 text-sm font-medium">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-5 h-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5 13l4 4L19 7"
          />
        </svg>
        <span>Dostupno</span>
      </div>

      <div>
        <div class="rounded-sm border border-gray-200 mb-3 w-fit">
          <button
            type="button"
            class="size-10 leading-10 text-gray-600 transition hover:text-red-600"
          >
            &minus;
          </button>

          <input
            type="number"
            id="Kolicina"
            value="1"
            class="h-10 w-16 border-transparent text-center [-moz-appearance:_textfield] sm:text-sm [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"
          />

          <button
            type="button"
            class="size-10 leading-10 text-gray-600 transition hover:text-green-600"
          >
            &plus;
          </button>
        </div>
      </div>

      <button
        class="mt-6 w-full bg-orange-600 hover:bg-orange-900 text-gray-100 py-3 px-6 rounded-lg text-sm font-medium transition"
      >
        Dodaj u košaricu
      </button>
    </div>

    <div class="h-130 max-md:hidden">
      <img
        src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        alt="Krastavci"
        class="w-full rounded-lg shadow object-cover h-130"
      />
    </div>
  </div>
</template>
