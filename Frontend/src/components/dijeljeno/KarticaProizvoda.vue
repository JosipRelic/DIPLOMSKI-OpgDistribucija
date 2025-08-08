<template>
  <router-link
    :to="{ name: 'krastavci' }"
    class="group relative block rounded-tr-3xl border border-gray-100 flex flex-col h-full"
  >
    <span
      class="absolute -top-px -right-px rounded-tr-3xl rounded-bl-3xl bg-[#223c2f] px-6 py-4 font-medium tracking-widest text-gray-100 uppercase transition duration-500 group-hover:scale-105"
    >
      2.99 €
    </span>
    <img
      src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
      alt=""
      class="aspect-square w-full object-cover rounded-tr-3xl"
    />

    <div class="p-4 text-center flex flex-col justify-between h-full">
      <strong
        class="text-xl font-medium text-gray-900 transition duration-500 group-hover:scale-105"
      >
        Krastavci
      </strong>
      <small class="text-sm text-gray-500 hover:underline">Opg Horvat</small>

      <p class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105">
        Hrskavi i osvježavajući - naši krastavci su idealni za ljetne salate i zdravi međuobrok.
        Prava svježina u svakom zalogaju!
      </p>

      <div>
        <div
          class="flex items-center justify-center mx-auto rounded-sm border border-gray-200 mb-3 w-fit"
        >
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

      <span
        class="mt-auto block rounded-md border border-orange-700 bg-orange-700 px-5 py-3 text-sm font-medium tracking-widest text-gray-100 uppercase transition-colors hover:bg-orange-900"
      >
        Dodaj u košaricu
      </span>
    </div>
  </router-link>

  <a
    href="#"
    class="group relative block rounded-tr-3xl border border-gray-100 flex flex-col h-full"
  >
    <span
      class="absolute -top-px -right-px rounded-tr-3xl rounded-bl-3xl bg-[#223c2f] px-6 py-4 font-medium tracking-widest text-gray-100 uppercase transition duration-500 group-hover:scale-105"
    >
      1.99 €
    </span>
    <img
      src="https://images.unsplash.com/photo-1517666005606-69dea9b54865?q=80&w=1752&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
      alt=""
      class="aspect-square w-full object-cover rounded-tr-3xl"
    />

    <div class="p-4 text-center flex flex-col justify-between h-full">
      <strong
        class="text-xl font-medium text-gray-900 transition duration-500 group-hover:scale-105"
      >
        Rajčica
      </strong>
      <small class="text-sm text-gray-500 hover:underline">Opg Novak</small>

      <p class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105">
        Zrela, mirisna i sunčana - rajčica kakvu pamtimo s bakine tržnice. Dodajte je u salatu ili
        jednostavno pojedite s malo soli!
      </p>

      <div>
        <div
          class="flex items-center justify-center mx-auto rounded-sm border border-gray-200 mb-3 w-fit"
        >
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

      <span
        class="mt-auto block rounded-md border border-orange-700 bg-orange-700 px-5 py-3 text-sm font-medium tracking-widest text-gray-100 uppercase transition-colors hover:bg-orange-900"
      >
        Dodaj u košaricu
      </span>
    </div>
  </a>

  <a
    href="#"
    class="group relative block rounded-tr-3xl border border-gray-100 flex flex-col h-full"
  >
    <span
      class="absolute -top-px -right-px rounded-tr-3xl rounded-bl-3xl bg-[#223c2f] px-6 py-4 font-medium tracking-widest text-gray-100 uppercase transition duration-500 group-hover:scale-105"
    >
      1.59 €
    </span>
    <img
      src="https://images.unsplash.com/photo-1669863347362-1630fe821708?q=80&w=1548&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
      alt=""
      class="aspect-square w-full object-cover rounded-tr-3xl"
    />

    <div class="p-4 text-center flex flex-col justify-between h-full">
      <strong
        class="text-xl font-medium text-gray-900 transition duration-500 group-hover:scale-105"
      >
        Paprika
      </strong>
      <small class="text-sm text-gray-500 hover:underline">Opg Jurić</small>

      <p class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105">
        Sočna, šarena i puna okusa - naša paprika dolazi ravno iz domaćih vrtova. Savršena za
        salate, roštilj i punjenje.
      </p>

      <div>
        <div
          class="flex items-center justify-center mx-auto rounded-sm border border-gray-200 mb-3 w-fit"
        >
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

      <span
        class="mt-auto block rounded-md border border-orange-700 bg-orange-700 px-5 py-3 text-sm font-medium tracking-widest text-gray-100 uppercase transition-colors hover:bg-orange-900"
      >
        Dodaj u košaricu
      </span>
    </div>
  </a>

  <a
    href="#"
    class="group relative block rounded-tr-3xl border border-gray-100 flex flex-col h-full"
  >
    <span
      class="absolute -top-px -right-px rounded-tr-3xl rounded-bl-3xl bg-[#223c2f] px-6 py-4 font-medium tracking-widest text-gray-100 uppercase transition duration-500 group-hover:scale-105"
    >
      0.99 €
    </span>
    <img
      src="https://images.unsplash.com/photo-1518977956812-cd3dbadaaf31?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
      alt=""
      class="aspect-square w-full object-cover rounded-tr-3xl"
    />

    <div class="p-4 text-center flex flex-col justify-between h-full">
      <strong
        class="text-xl font-medium text-gray-900 transition duration-500 group-hover:scale-105"
      >
        Luk
      </strong>
      <small class="text-sm text-gray-500 hover:underline">Opg Marić</small>

      <p class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105">
        Neodoljivo aromatičan i uvijek svjež - naš domaći luk podiže svako jelo na višu razinu.
        Idealno za kuhinje svih stilova!
      </p>

      <div>
        <div
          class="flex items-center justify-center mx-auto rounded-sm border border-gray-200 mb-3 w-fit"
        >
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

      <span
        class="mt-auto block rounded-md border border-orange-700 bg-orange-700 px-5 py-3 text-sm font-medium tracking-widest text-gray-100 uppercase transition-colors hover:bg-orange-900"
      >
        Dodaj u košaricu
      </span>
    </div>
  </a>
</template>
