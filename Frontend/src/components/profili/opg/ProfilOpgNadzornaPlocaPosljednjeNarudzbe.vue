<template>
  <div class="flex justify-center items-center p-5">
    <div class="w-full max-w-7xl rounded-lg overflow-x-auto bg-white shadow-md">
      <div class="p-4 min-w-full">
        <div class="flex justify-between items-center">
          <div><p class="text-2xl font-bold mb-2 ps-4">Posljednje narudžbe</p></div>
          <router-link :to="{ name: 'profilOpgPrimljeneNarudzbe' }">
            <button
              class="bg-orange-500 text-white px-8 py-3 shadow shadow-sm rounded-md cursor-pointer"
            >
              Pogledaj sve narudžbe
            </button>
          </router-link>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-3 p-4">
        <router-link
          v-for="(n, i) in narudzbe"
          :key="i"
          class="block rounded-md border border-gray-100 p-4 shadow-sm sm:p-6"
          :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe', params: { id: n.id } }"
        >
          <div class="sm:flex sm:justify-between sm:gap-4 lg:gap-6">
            <div class="sm:order-last sm:shrink-0">
              <img
                :alt="n.kupac_ime"
                :src="n.kupac_slika || 'https://placehold.co/96x96?text=Kupac'"
                class="size-16 rounded-full object-cover sm:size-[72px]"
              />
            </div>

            <div class="mt-4 sm:mt-0">
              <div class="flex items-center">
                <h3 class="text-lg font-medium text-pretty text-gray-900">
                  {{ n.kupac_ime }} - (Kupac)
                </h3>
                <p
                  class="inline-flex items-center ms-2 justify-center rounded-full px-2 text-sm whitespace-nowrap capitalize"
                  :class="{
                    'bg-emerald-500 text-emerald-100': n.status === 'isporuceno',
                    'bg-amber-500 text-amber-100': n.status === 'u_tijeku',
                    'bg-rose-500 text-rose-100': n.status === 'otkazano',
                  }"
                >
                  {{ n.status.replace("_", " ").replace("c", "č") }}
                </p>
              </div>

              <p class="mt-1 text-sm text-gray-700 text-orange-600 font-medium">
                Narudžba br. {{ n.broj_narudzbe }}
              </p>

              <div class="mt-4">
                <ol class="text-base text-orange-400 ms-2 space-y-1">
                  <li v-if="n.iznos_usluga && n.iznos_usluga !== 0">
                    Usluge - {{ fmtEUR(n.iznos_usluga) }}
                  </li>
                  <li v-if="n.iznos_proizvoda && n.iznos_proizvoda !== 0">
                    Proizvodi - {{ fmtEUR(n.iznos_proizvoda) }}
                  </li>
                  <li>Dostava - {{ n.dostava }}</li>
                </ol>
              </div>
            </div>
          </div>

          <dl class="mt-6 flex gap-4 lg:gap-6">
            <div>
              <dt class="text-sm font-medium text-gray-700">Datum i vrijeme narudžbe</dt>
              <dd class="text-sm text-gray-700">{{ fmtDateTime(n.datum_izrade) }}</dd>
            </div>
            <div>
              <dt class="text-sm font-medium text-gray-700">Ukupan iznos</dt>
              <dd class="text-sm text-gray-700">{{ fmtEUR(n.ukupno) }}</dd>
            </div>
          </dl>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue"
import { useOpgNadzornaPlocaStore } from "@/stores/nadzornaPlocaOpg"

const nadzorna_ploca = useOpgNadzornaPlocaStore()
onMounted(() => {
  if (!nadzorna_ploca.podaci) nadzorna_ploca.ucitajNadzornuPlocu()
})

const narudzbe = computed(() => nadzorna_ploca.podaci?.posljednje_narudzbe ?? [])

function fmtEUR(v) {
  return `${Number(v || 0).toFixed(2)} €`
}
function fmtDateTime(iso) {
  if (!iso) return ""
  const d = new Date(iso)
  return d.toLocaleString("hr-HR", { dateStyle: "short", timeStyle: "short" })
}
</script>
