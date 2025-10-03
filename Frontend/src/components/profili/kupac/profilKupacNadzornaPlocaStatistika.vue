<template>
  <div class="flex justify-center items-center p-4 w-full" v-if="statistika">
    <div class="w-full px-2 sm:w-[90%] md:w-[80%] lg:w-[60%]">
      <div class="grid grid-cols-1 xl:grid-cols-2 gap-4">
        <div class="p-8 bg-white rounded-md shadow-lg flex flex-col items-center justify-center">
          <span class="text-gray-500 font-bold mb-4">Ukupno narudžbi</span>
          <router-link
            :to="{ name: 'profilKupacMojeNarudzbe' }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
          >
            {{ statistika.ukupno_narudzbi ?? 0 }}
          </router-link>
        </div>

        <div class="p-8 bg-white rounded-md shadow-lg flex flex-col items-center justify-center">
          <span class="text-gray-500 font-bold mb-4">Vaš OPG favorit</span>
          <router-link
            v-if="statistika.opg_favorit"
            :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: statistika.opg_favorit.slug } }"
            class="flex items-center gap-3"
          >
            <span class="text-2xl font-bold text-orange-600 hover:text-orange-900">{{
              statistika.opg_favorit.naziv
            }}</span>
          </router-link>
        </div>

        <div class="p-8 bg-white rounded-md shadow-lg flex flex-col items-center justify-center">
          <span class="text-gray-500 font-bold mb-4">Proizvod koji ste najviše kupili</span>
          <router-link
            v-if="statistika.najcesci_proizvod"
            :to="{
              name: 'ETrznicaProizvodDetalji',
              params: {
                katSlug: statistika.najcesci_proizvod.kat_slug,
                proizvodSlugId: statistika.najcesci_proizvod.proizvod_slug_id,
              },
            }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
          >
            {{ statistika.najcesci_proizvod.naziv }}
          </router-link>
          <span v-else class="text-gray-400">—</span>
        </div>

        <div class="p-8 bg-white rounded-md shadow-lg flex flex-col items-center justify-center">
          <span class="text-gray-500 font-bold mb-4">Usluga koju ste najviše rezervirali</span>
          <router-link
            v-if="statistika.najcesca_usluga"
            :to="{
              name: 'farmaPlusDetaljiUsluge',
              params: { uslugaSlugId: statistika.najcesca_usluga.usluga_slug_id },
            }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
          >
            {{ statistika.najcesca_usluga.naziv }}
          </router-link>
          <span v-else class="text-gray-400">—</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useNadzornaPlocaKupacStore } from "@/stores/nadzornaPlocaKupac"
import { computed, onMounted } from "vue"

const np_kupac = useNadzornaPlocaKupacStore()
const statistika = computed(() => np_kupac.statistika)

onMounted(() => np_kupac.ucitaj())
</script>
