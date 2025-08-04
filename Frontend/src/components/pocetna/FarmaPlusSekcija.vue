<template>
  <div>
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-2xl sm:py-16 lg:max-w-none lg:py-2 mb-16">
        <router-link
          :to="{ name: 'farmaPlus' }"
          class="text-4xl font-bold text-orange-600 hover:text-orange-900"
          >Farma+</router-link
        >
        <p class="mt-1">
          Zatraži ili ponudi poljoprivredne usluge poput oranja, sjetve, špricanja i berbe. Također,
          pregledaj oglase za prodaju i najam domaćih životinja.
        </p>
        <div class="mt-6 space-y-12 lg:grid lg:grid-cols-2 lg:gap-x-6">
          <div class="group relative">
            <img
              :src="slikeFarmaPlusZivotinjePocetna"
              alt="slika životinje"
              class="w-full rounded-lg bg-white object-cover group-hover:opacity-75 max-sm:h-80 sm:aspect-2/1 lg:aspect-square transition duration-500 group-hover:scale-102"
            />
            <h3 class="mt-6 text-md text-gray-500">
              <router-link :to="{ name: 'farmaPlus' }">
                <span class="absolute inset-0"></span>
                Prodaja i najam životinja
              </router-link>
            </h3>
            <p class="text-base font-semibold text-gray-900">
              Pronađi ili ponudi domaće životinje za prodaju ili najam. Jednostavno filtriraj prema
              vrsti, lokaciji i dostupnosti. Idealno za ispašu, uzgoj ili privremene potrebe.
            </p>
          </div>
          <div class="group relative">
            <img
              :src="slikeFarmaPlusUslugePocetna"
              alt="Slika usluge"
              class="w-full rounded-lg bg-white object-cover group-hover:opacity-75 max-sm:h-80 sm:aspect-2/1 lg:aspect-square transition duration-500 group-hover:scale-102"
            />
            <h3 class="mt-6 text-md text-gray-500">
              <router-link :to="{ name: 'farmaPlus' }">
                <span class="absolute inset-0"></span> Poljoprivredne usluge
              </router-link>
            </h3>
            <p class="text-base font-semibold text-gray-900">
              Pregledaj i zatraži različite poljoprivredne usluge od drugih farmera. Od oranja,
              sjetve i špricanja do berbe i baliranja. Brzo pronađi dostupne izvođače u svojoj
              blizini i dogovori suradnju.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import slikeFarmaPlusUslugePocetna from "@/assets/slike/farma-plus-usluge-pocetna.png"
import slikeFarmaPlusZivotinjePocetna from "@/assets/slike/farma-plus-zivotinje-pocetna.png"
</script>
