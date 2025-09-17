<template>
  <div
    class="max-w-6xl mx-auto px-6 py-12 grid grid-cols-1 md:grid-cols-2 gap-16 items-start bg-white rounded-2xl my-14 shadow-lg max-xl:mx-10"
  >
    <div v-if="loading" class="md:col-span-2 text-center text-gray-500 py-16">Učitavanje…</div>
    <div v-else-if="!loading && !proizvod" class="md:col-span-2 text-center text-gray-500 py-16">
      Proizvod nije pronađen.
    </div>
    <template v-else>
      <div class="space-y-6 ps-4">
        <nav class="text-sm text-gray-500 flex items-center space-x-2">
          <span class="hover:underline cursor-pointer"
            ><router-link
              :to="{ name: 'ETrznicaKategorija', params: { slug: proizvod.kategorija.slug } }"
              >{{ proizvod.kategorija.naziv }}</router-link
            ></span
          >
          <span>/</span>
          <span class="font-medium">{{ proizvod.naziv }}</span>
        </nav>

        <div>
          <h1 class="text-3xl font-bold text-gray-900">{{ proizvod.naziv }}</h1>
          <div class="flex items-center mt-2 space-x-2 text-sm text-gray-600">
            <router-link
              :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: proizvod.opg.slug } }"
              href="#"
              class="hover:underline text-teal-500"
            >
              {{ proizvod.opg.naziv }}
            </router-link>
            <span class="text-gray-400">•</span>
            <span
              >{{ proizvod.opg.grad
              }}<template v-if="proizvod.opg.zupanija"
                >, {{ proizvod.opg.zupanija }}</template
              ></span
            >
          </div>
        </div>

        <div class="text-2xl font-semibold text-gray-900">
          {{ formatiranjeCijena(proizvod.cijena) }}
          <span class="text-gray-400"> / {{ proizvod.mjerna_jedinica }}</span>
          <div>
            <div class="rounded-sm border border-gray-200 mt-2 w-fit shadow">
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
                class="h-10 text-orange-600 w-16 border-transparent text-center [-moz-appearance:_textfield] sm:text-sm [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"
              />

              <button
                type="button"
                class="size-10 leading-10 text-gray-600 transition hover:text-green-600"
              >
                &plus;
              </button>
            </div>
          </div>
        </div>

        <p class="text-gray-600 text-base">
          {{ proizvod.opis }}
        </p>

        <div
          class="flex items-center space-x-2 text-sm font-medium"
          :class="proizvod.proizvod_dostupan ? 'text-green-600' : 'text-red-500'"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-5 h-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              v-if="proizvod.proizvod_dostupan"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M5 13l4 4L19 7"
            />
            <path
              v-else
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
          <span>{{ proizvod.proizvod_dostupan ? "Dostupno" : "Nedostupno" }}</span>
        </div>

        <button
          class="w-full bg-orange-600 shadow-md border border-orange-600 cursor-pointer hover:bg-orange-900 hover:border-orange-900 text-gray-100 py-3 px-6 rounded-lg text-sm font-medium transition"
        >
          Dodaj u košaricu
        </button>
      </div>

      <div class="h-130 max-md:hidden flex justify-center items-start" v-if="!loading && proizvod">
        <img
          :src="proizvod.slika_proizvoda || defaultSlika"
          :alt="proizvod.naziv"
          class="w-full rounded-lg shadow object-cover h-130"
        />
      </div>
    </template>
  </div>
</template>
<script setup>
import { ref, onMounted, watch } from "vue"
import { useRoute } from "vue-router"
import api from "@/services/api"

const route = useRoute()
const loading = ref(false)
const proizvod = ref(null)
const defaultSlika = "https://placehold.co/800x800?text=Proizvod"

function dohvatiId(slugId) {
  const m = String(slugId || "").match(/-(\d+)$/)
  return m ? Number(m[1]) : NaN
}

async function dohvatiProizvod() {
  loading.value = true
  proizvod.value = null
  try {
    const id = dohvatiId(route.params.proizvodSlugId)
    if (!id) return
    const { data } = await api.get(`/e-trznica/proizvodi/${id}`)
    proizvod.value = data
  } finally {
    loading.value = false
  }
}

function formatiranjeCijena(c) {
  const cijena = Number(c || 0)
  return `${cijena.toFixed(2)} €`
}

onMounted(dohvatiProizvod)
watch(() => route.params.proizvodSlugId, dohvatiProizvod)
</script>
