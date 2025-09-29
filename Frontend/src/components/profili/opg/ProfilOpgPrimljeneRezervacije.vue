<template>
  <div class="max-w-6xl mx-auto bg-white rounded-xl shadow-lg p-10 mt-6 mb-6">
    <h1 class="text-3xl font-bold mb-6">Nadolazeće rezervacije usluga</h1>

    <ol class="relative border-s border-orange-500 ms-6" v-if="sve_rezervacije.length">
      <li v-for="(r, idx) in sve_rezervacije" :key="idx" class="mb-10 ms-8">
        <span
          class="absolute flex items-center justify-center w-6 h-6 bg-orange-600 rounded-full -start-3 ring-8 ring-orange-600"
        >
          <svg
            class="w-4 h-4 text-white"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
            />
          </svg>
        </span>

        <h3 class="flex items-center mb-1 text-lg font-semibold text-orange-600">
          {{
            new Date(r.termin_od).toLocaleDateString("hr-HR", {
              day: "2-digit",
              month: "long",
              year: "numeric",
            })
          }}
          <span class="inline-block h-3 w-3 rounded-full bg-red-600 ms-2" />
        </h3>

        <ol class="mt-3 divide-y divide-gray-200">
          <li class="items-center block p-3 ps-0 sm:flex">
            <img
              class="w-20 h-20 mb-3 me-3 rounded-xl sm:mb-0"
              :src="r.slika || defaultSlikaUsluge"
              :alt="r.usluga"
            />
            <div class="text-gray-600">
              <div class="text-base font-normal">
                Usluga: <span class="font-medium text-gray-900">{{ r.usluga }}</span> | Količina:
                <span class="font-medium text-gray-900"
                  >{{ r.kolicina }} {{ r.mjerna_jedinica }}</span
                >
              </div>
              <div class="text-sm font-bold text-teal-500">
                {{
                  new Date(r.termin_od).toLocaleTimeString("hr-HR", {
                    hour: "2-digit",
                    minute: "2-digit",
                  })
                }}
                ->
                {{
                  new Date(r.termin_do).toLocaleTimeString("hr-HR", {
                    hour: "2-digit",
                    minute: "2-digit",
                  })
                }}
              </div>
              <div class="inline-flex items-center text-sm font-normal">
                <div class="text-gray-900 mr-2">
                  Narudžba br:

                  <router-link
                    :to="{
                      name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe',
                      params: { id: r.narudzba_id },
                    }"
                  >
                    <span class="text-orange-600 hover:underline font-semibold"
                      >#{{ r.broj_narudzbe }}</span
                    ></router-link
                  >
                </div>
                <div class="text-gray-900 mr-2">
                  | Kupac:
                  <span class="text-orange-600 hover:underline font-semibold">{{ r.kupac }}</span>
                </div>
              </div>
            </div>
          </li>
        </ol>
      </li>
    </ol>

    <p v-else class="text-slate-400">Nemate više rezervacija.</p>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue"
import { useRaspolozivostOpgStore } from "@/stores/raspolozivostOpg"

const raspolozivost = useRaspolozivostOpgStore()
const sve_rezervacije = ref([])

const defaultSlikaUsluge = "https://placehold.co/160x160?text=Usluga"

onMounted(async () => {
  sve_rezervacije.value = await raspolozivost.dohvatiSveRezervacije()
})
</script>
