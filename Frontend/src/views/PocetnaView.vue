<template>
  <!--Naslovna sekcija-->
  <section
    class="overflow-hidden bg-cover bg-center bg-no-repeat"
    :style="`background-image: url(${slikeCoverPocetna})`"
  >
    <NaslovnaPocetna />
  </section>

  <!--Najprodavaniji proizvodi-->
  <section>
    <span class="flex items-center py-8">
      <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>

      <span class="shrink-0 px-4 text-gray-900 text-3xl">Najprodavaniji proizvodi</span>

      <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
    </span>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-20 py-8">
      <KarticaProizvoda />
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
      <KarticaOPGa />
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"
import slikeCoverPocetna from "@/assets/slike/cover-pocetna.jpg"
import NaslovnaPocetna from "@/components/pocetna/NaslovnaPocetna.vue"
import KarticaProizvoda from "@/components/dijeljeno/KarticaProizvoda.vue"
import KarticaOPGa from "@/components/dijeljeno/KarticaOPGa.vue"

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
