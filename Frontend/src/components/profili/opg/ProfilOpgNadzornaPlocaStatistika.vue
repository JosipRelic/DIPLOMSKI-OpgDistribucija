<template>
  <div class="flex justify-center items-center p-4 w-full">
    <div class="w-full px-2 sm:w-[90%] md:w-[80%] lg:w-[60%]">
      <div class="grid grid-cols-1 xl:grid-cols-3 gap-4">
        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Ukupno zaprimljenih narudžbi</span>
          </div>
          <router-link
            :to="{ name: 'profilOpgPrimljeneNarudzbe' }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
          >
            {{ st.ukupno_narudzbi ?? 0 }}
          </router-link>
        </div>

        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Zarada ovaj mjesec</span>
          </div>
          <p class="text-2xl font-bold text-green-600">{{ eur(st.zarada_ovaj_mjesec) }}</p>
        </div>

        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Ukupna zarada</span>
          </div>
          <p class="text-2xl font-bold text-green-600">{{ eur(st.zarada_ukupno) }}</p>
        </div>

        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Najprodavaniji proizvod</span>
          </div>
          <router-link
            v-if="st.najprodavaniji_proizvod && linkProizvod"
            :to="linkProizvod"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
          >
            {{ st.najprodavaniji_proizvod.naziv }}
          </router-link>
          <span v-else class="text-2xl font-bold text-orange-600">—</span>
        </div>

        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Najvjerniji kupac</span>
          </div>
          <router-link
            v-if="st.najvjerniji_kupac && linkNajvjerniji"
            :to="linkNajvjerniji"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
          >
            {{ st.najvjerniji_kupac.ime }} {{ st.najvjerniji_kupac.prezime }}
          </router-link>
          <span v-else class="text-2xl font-bold text-orange-600">
            <template v-if="st.najvjerniji_kupac"
              >{{ st.najvjerniji_kupac.ime }} {{ st.najvjerniji_kupac.prezime }}</template
            >
            <template v-else>—</template>
          </span>
        </div>

        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Najtraženija usluga</span>
          </div>
          <router-link
            v-if="st.najtrazenija_usluga && linkUsluga"
            :to="linkUsluga"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
          >
            {{ st.najtrazenija_usluga.naziv }}
          </router-link>
          <span v-else class="text-2xl font-bold text-orange-600">—</span>
        </div>
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
const st = computed(() => nadzorna_ploca.podaci?.statistika ?? {})

function eur(v) {
  return `${Number(v || 0).toFixed(2)} €`
}

const linkProizvod = computed(() => {
  const p = st.value.najprodavaniji_proizvod
  if (!p) return null
  return {
    name: "ETrznicaProizvodDetalji",
    params: {
      katSlug: p.kategorija_slug,
      proizvodSlugId: `${p.slug}-${p.id}`,
    },
  }
})

const linkUsluga = computed(() => {
  const u = st.value.najtrazenija_usluga
  if (!u) return null
  return {
    name: "farmaPlusDetaljiUsluge",
    params: { uslugaSlugId: `${u.slug}-${u.id}` },
  }
})

const linkNajvjerniji = computed(() => {
  const k = st.value.najvjerniji_kupac
  if (!k) return null
  if (k.tip === "Opg" && k.opg_slug) {
    return { name: "ETrznicaDetaljiOPGa", params: { opgSlug: k.opg_slug } }
  }
  if (k.tip === "Kupac" && k.kupac_slug) {
    return { name: "profilOpgDetaljiKupca", params: { kupacSlug: k.kupac_slug } }
  }
  return null
})
</script>
