<template>
  <div>
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-2xl sm:py-16 lg:max-w-none lg:py-2 mb-8">
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
              <span class="absolute inset-0"></span>
              Prodaja i najam životinja
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
              <span class="absolute inset-0"></span> Poljoprivredne usluge
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
    <section class="max-w-400 mx-auto mb-10">
      <span class="flex items-center pb-8">
        <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>

        <span class="shrink-0 px-4 text-gray-900 text-3xl">Najtraženije usluge</span>

        <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
      </span>

      <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6 px-20 py-8">
        <KarticaUsluge
          v-for="u in najtrazenijeUsluge"
          :key="u.usluga.id"
          :usluga="u.usluga"
          :prikazi-ponudaca-usluge="true"
        />
        <div v-if="!najtrazenijeUsluge.length" class="text-center text-gray-500 col-span-full">
          Nema podataka.
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue"
import slikeFarmaPlusUslugePocetna from "@/assets/slike/farma-plus-usluge-pocetna.png"
import slikeFarmaPlusZivotinjePocetna from "@/assets/slike/farma-plus-zivotinje-pocetna.png"
import { usePocetnaStore } from "@/stores/pocetna"
import KarticaUsluge from "@/components/dijeljeno/KarticaUsluge.vue"

const pocetna = usePocetnaStore()
onMounted(() => pocetna.ucitaj())

const najtrazenijeUsluge = computed(() => pocetna.usluge || [])
</script>
