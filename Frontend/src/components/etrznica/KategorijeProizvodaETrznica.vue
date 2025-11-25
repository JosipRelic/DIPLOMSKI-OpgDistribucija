<template>
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-10 mb-12">
    <div class="flex items-center justify-between mb-2">
      <h2 class="text-2xl font-bold text-gray-900">
        Odaberite kategoriju kako biste pregledali njezine proizvode.
      </h2>
    </div>
    <p class="mb-8 max-w-3xl text-gray-500">
      Na našoj E-Tržnici pronaći ćete pažljivo odabrane proizvode domaćih OPG-ova. Od svježeg voća i
      povrća do raznih delicija i prirodnih proizvoda. Svaki proizvod dolazi izravno s hrvatskih
      farmi, s naglaskom na kvalitetu, svježinu i lokalnu proizvodnju. Pregledajte ponudu i
      pronađite sve što vam treba, brzo i jednostavno.
    </p>
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-4"
    >
      <router-link
        v-for="kategorija in kategorije_s.kategorije"
        :key="kategorija.id"
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer block"
        :to="{ name: 'ETrznicaKategorija', params: { slug: kategorija.slug } }"
      >
        <img
          :src="resolveImg(kategorija.slika_kategorije)"
          :alt="kategorija.naziv"
          class="w-full h-52 object-cover bg-gray-100"
        />
        <div class="p-4 text-center text-lg font-semibold text-gray-800">
          {{ kategorija.naziv }}
        </div>
      </router-link>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from "vue"
import { useEtrznicaKategorijeStore } from "@/stores/eTrznicaKategorije"

const kategorije_s = useEtrznicaKategorijeStore()
onMounted(() => kategorije_s.ucitajSveKategorije())

const BACKEND_URL = import.meta.env.VITE_API_URL || ""
function resolveImg(src) {
  if (!src) return ""
  if (src.startsWith("http")) return src
  return `${BACKEND_URL}${src}`
}
</script>
