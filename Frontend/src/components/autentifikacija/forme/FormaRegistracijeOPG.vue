<template>
  <div class="min-h-screen text-gray-900 flex justify-center">
    <div
      class="max-w-screen-xl m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1"
    >
      <div class="lg:w-1/2 xl:w-5/12 p-6 sm:p-12">
        <div>
          <img :src="slikeLogo" class="w-16 mx-auto" />
        </div>
        <div class="mt-12 flex flex-col items-center">
          <h1 class="text-2xl xl:text-3xl font-extrabold">Registracija OPG-a</h1>
          <div class="w-full flex-1 mt-8">
            <div class="flex flex-col items-center">
              <button
                class="w-full max-w-xs font-bold shadow-sm hover:bg-red-400 rounded-lg py-3 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
              >
                <div class="bg-white p-2 rounded-full">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    class="w-6 text-red-600"
                  >
                    <path
                      fill="currentColor"
                      d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
                    />
                  </svg>
                </div>
                <span class="ml-4"> Ispunite glasovno pomoću AI </span>
              </button>
              <small class="pt-2 w-full max-w-xs"
                >Pritisnite gumb i popunite obrazac glasom npr. "Zovem se Ivan Horvat. Moja email
                adresa je ihorvat@gmail.com. Naziv opg-a itd..."</small
              >
            </div>

            <div class="my-12 border-b text-center">
              <div
                class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
              >
                ili unesite podatke ručno
              </div>
            </div>

            <div class="mx-auto max-w-xs">
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                type="email"
                placeholder="Email"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="text"
                placeholder="Korisničko Ime"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="password"
                placeholder="Lozinka"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="password"
                placeholder="Potvrdite lozinku"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="text"
                placeholder="Naziv OPG-a"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="text"
                placeholder="Ime vlasnika"
              />
              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="text"
                placeholder="Prezime vlasnika"
              />

              <input
                class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                type="text"
                placeholder="Identifikacijski broj PG-a (MIBPG)"
              />

              <button
                class="mt-5 tracking-wide font-semibold bg-teal-600 hover:bg-teal-900 text-gray-100 w-full py-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none"
              >
                <svg
                  class="w-6 h-6 -ml-2"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                  <circle cx="8.5" cy="7" r="4" />
                  <path d="M20 8v6M23 11h-6" />
                </svg>
                <span class="ml-3"> Registracija </span>
              </button>
              <p class="mt-6 text-sm text-gray-800 text-center">
                <router-link
                  :to="{ name: 'prijava' }"
                  class="mt-6 text-center text-md border-b border-gray-500 border-dotted"
                >
                  Već ste registrirani?
                </router-link>
              </p>
            </div>
          </div>
        </div>
      </div>
      <div
        class="flex-1 bg-indigo-100 text-center bg-cover bg-center hidden lg:flex"
        style="
          background-image: url(https://images.unsplash.com/photo-1526410393023-6aace519592a?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fGZhcm1pbmclMjBmYW1pbHl8ZW58MHwxfDB8fHww);
        "
      ></div>
    </div>
  </div>
</template>
<script setup>
import slikeLogo from "@/assets/slike/logo.png"
</script>
