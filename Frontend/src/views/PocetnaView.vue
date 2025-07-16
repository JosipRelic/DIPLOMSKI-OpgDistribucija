<template>
  <!--Naslovna sekcija-->
  <section
    class="overflow-hidden bg-cover bg-center bg-no-repeat"
    :style="`background-image: url(${slikeCoverPocetna})`"
  >
    <div class="bg-black/50 p-8 md:p-12 lg:px-16 lg:py-40">
      <div class="text-center ltr:sm:text-left rtl:sm:text-right">
        <h2 class="text-2xl font-bold text-gray-100 sm:text-3xl md:text-5xl">
          Svježe s naših polja
        </h2>

        <p class="hidden max-w-lg text-gray-100 md:mt-6 md:block md:text-lg md:leading-relaxed">
          Kupujte izravno od hrvatskih OPG-ova putem naše E-Tržnice.
        </p>

        <div class="mt-4 sm:mt-8">
          <a
            href="#"
            class="inline-block rounded-full bg-orange-700 px-12 py-3 text-sm font-medium text-gray-100 transition hover:bg-orange-900 focus:ring-3 focus:ring-yellow-400 focus:outline-hidden"
          >
            Posjetite našu E-Tržnicu
          </a>
        </div>
      </div>
    </div>
  </section>

  <!--Najprodavaniji proizvodi-->
  <section>
    <span class="flex items-center py-8">
      <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>

      <span class="shrink-0 px-4 text-gray-900 text-3xl">Najprodavaniji proizvodi</span>

      <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
    </span>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-20 py-8">
      <a
        href="#"
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

          <p
            class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105"
          >
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
      </a>

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

          <p
            class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105"
          >
            Zrela, mirisna i sunčana - rajčica kakvu pamtimo s bakine tržnice. Dodajte je u salatu
            ili jednostavno pojedite s malo soli!
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

          <p
            class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105"
          >
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

          <p
            class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105"
          >
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
    </div>
  </section>

  <!--Najbolje ocijenjeni opg-ovi-->

  <section>
    <span class="flex items-center py-6">
      <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>

      <span class="shrink-0 px-4 text-gray-900 text-3xl">Najbolje ocijenjeni OPG-ovi</span>

      <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
    </span>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-20 py-8 mb-14">
      <a href="#" class="block group">
        <img
          alt=""
          src="https://images.unsplash.com/photo-1461354464878-ad92f492a5a0?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          class="h-56 w-full rounded-tr-3xl rounded-bl-3xl object-cover sm:h-64 lg:h-72 transition duration-500 group-hover:scale-105"
        />

        <div class="mt-4 sm:flex sm:items-center sm:justify-center sm:gap-4">
          <strong
            class="font-medium text-gray-900 hover:text-gray-500 transition duration-500 group-hover:scale-105"
            >Opg Jurić</strong
          >

          <span class="hidden sm:block sm:h-px sm:w-4 sm:bg-orange-700"></span>

          <div class="flex items-center">
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-gray-300 me-1 dark:text-gray-500"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <p class="ms-1 text-sm font-medium text-gray-500 hover:underline">5.00 (839)</p>
          </div>
        </div>
        <p class="mt-1 flex justify-center text-pretty text-gray-700">
          Nikole Mikca 34, 44000 Sisak
        </p>
      </a>

      <a href="#" class="block group">
        <img
          alt=""
          src="https://images.unsplash.com/photo-1605000797499-95a51c5269ae?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          class="h-56 w-full rounded-tr-3xl rounded-bl-3xl object-cover sm:h-64 lg:h-72 transition duration-500 group-hover:scale-105"
        />

        <div class="mt-4 sm:flex sm:items-center sm:justify-center sm:gap-4">
          <strong
            class="font-medium text-gray-900 hover:text-gray-400 transition duration-500 group-hover:scale-105"
            >Opg Horvat</strong
          >

          <span class="hidden sm:block sm:h-px sm:w-4 sm:bg-orange-700"></span>

          <div class="flex items-center">
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-gray-300 me-1 dark:text-gray-500"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <p class="ms-1 text-sm font-medium text-gray-500 hover:underline">4.95 (520)</p>
          </div>
        </div>
        <p class="mt-1 flex justify-center text-pretty text-gray-700">
          Ljudevita Posavskog 27, 43500 Daruvar
        </p>
      </a>

      <a href="#" class="block group">
        <img
          alt=""
          src="https://images.unsplash.com/photo-1610385272823-add81c4520eb?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          class="h-56 w-full rounded-tr-3xl rounded-bl-3xl object-cover sm:h-64 lg:h-72 transition duration-500 group-hover:scale-105"
        />

        <div class="mt-4 sm:flex sm:items-center sm:justify-center sm:gap-4">
          <strong
            class="font-medium text-gray-900 hover:text-gray-500 transition duration-500 group-hover:scale-105"
            >Opg Marić</strong
          >

          <span class="hidden sm:block sm:h-px sm:w-4 sm:bg-orange-700"></span>

          <div class="flex items-center">
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-gray-300 me-1 dark:text-gray-500"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <p class="ms-1 text-sm font-medium text-gray-500 hover:underline">4.80 (421)</p>
          </div>
        </div>
        <p class="mt-1 flex justify-center text-pretty text-gray-700">
          Zagrebačka 23, 44330 Novska
        </p>
      </a>

      <a href="#" class="block group">
        <img
          alt=""
          src="https://images.unsplash.com/photo-1427434846691-47fc561d1179?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          class="h-56 w-full rounded-tr-3xl rounded-bl-3xl object-cover sm:h-64 lg:h-72 transition duration-500 group-hover:scale-105"
        />

        <div class="mt-4 sm:flex sm:items-center sm:justify-center sm:gap-4">
          <strong
            class="font-medium text-gray-900 hover:text-gray-500 transition duration-500 group-hover:scale-105"
            >Opg Novak</strong
          >

          <span class="hidden sm:block sm:h-px sm:w-4 sm:bg-orange-700"></span>

          <div class="flex items-center">
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-yellow-300 me-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <svg
              class="w-4 h-4 text-gray-300 me-1 dark:text-gray-500"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 20"
            >
              <path
                d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
              />
            </svg>
            <p class="ms-1 text-sm font-medium text-gray-500 hover:underline">4.70 (230)</p>
          </div>
        </div>
        <p class="mt-1 flex justify-center text-pretty text-gray-700">
          Petra Preradovića 2, 44334 Kutina
        </p>
      </a>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"
import slikeCoverPocetna from "@/assets/slike/cover-pocetna.jpg"

const test_podaci_iz_baze = ref([])

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/")
    test_podaci_iz_baze.value = response.data
  } catch (error) {
    console.error("Greška pri dohvaćanju podataka: ", error)
  }
})
</script>
