<template>
  <header class="bg-[#223c2f]">
    <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
      <div class="flex h-16 items-center justify-between">
        <div class="flex items-center gap-2">
          <router-link :to="{ name: 'pocetna' }" class="block text-teal-600 group">
            <img
              :src="slikeLogo"
              alt="logo"
              class="w-10 h-auto transition duration-500 group-hover:scale-105"
            />
          </router-link>
          <p class="block text-gray-100">OPG Distribucija</p>
        </div>

        <div class="md:flex md:items-center md:gap-6">
          <nav aria-label="Global" class="hidden md:block">
            <ul class="flex items-center gap-4 text-sm">
              <li>
                <router-link
                  :to="{ name: 'e-trznica' }"
                  class="text-gray-100 transition hover:text-gray-500/75"
                >
                  E-Tržnica
                </router-link>
              </li>
              <li>
                <router-link
                  :to="{ name: 'farmaPlus' }"
                  class="text-gray-100 transition hover:text-gray-500/75"
                >
                  Farma+
                </router-link>
              </li>
            </ul>
          </nav>

          <div class="flex items-center gap-4">
            <div class="sm:flex sm:gap-4">
              <router-link
                :to="{ name: 'prijava' }"
                class="rounded-md bg-teal-600 transition hover:bg-teal-900 px-5 py-2.5 text-sm font-medium text-gray-100 hover:text-gray-300 shadow-sm"
              >
                Prijava
              </router-link>

              <div class="hidden sm:flex">
                <router-link
                  class="rounded-md bg-gray-100 transition hover:bg-gray-300 px-5 py-2.5 text-sm font-medium text-teal-600 hover:text-teal-900"
                  :to="{ name: 'registracija' }"
                >
                  Registracija
                </router-link>
              </div>
            </div>

            <div class="relative inline-block">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="size-6 stroke-gray-100 transition hover:stroke-gray-500/75"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
                />
              </svg>
              <span
                class="absolute -top-2 -right-2 inline-flex items-center justify-center px-1.5 py-0.5 text-xs font-bold leading-none text-white bg-orange-600 rounded-full"
              >
                0
              </span>
            </div>

            <div class="block md:hidden">
              <button
                class="rounded-sm bg-gray-100 p-2 text-gray-600 transition hover:text-gray-600/75"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="size-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import slikeLogo from "@/assets/slike/logo.png"
</script>
