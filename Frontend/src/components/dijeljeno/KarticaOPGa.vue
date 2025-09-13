<template>
  <router-link
    :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: opg.slug } }"
    class="block group shadow-xl rounded-bl-xl"
  >
    <img
      :alt="opg.naziv"
      :src="opg.slika_profila || defaultSlika"
      class="h-56 w-full rounded-tr-3xl rounded-bl-3xl object-cover sm:h-64 lg:h-72 transition duration-500 group-hover:scale-105"
    />

    <div class="mt-4 flex items-center justify-center gap-4 px-4">
      <strong
        class="font-medium text-gray-900 group-hover:text-gray-500 transition duration-500 group-hover:scale-105"
      >
        {{ opg.naziv }}
      </strong>
      <span class="hidden sm:block sm:h-px sm:w-4 sm:bg-orange-700"></span>
      <div class="flex items-center">
        <svg
          v-for="i in 5"
          :key="i"
          class="w-4 h-4 me-1"
          :class="i <= zaokruzeno ? 'text-orange-600' : 'text-orange-200'"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 22 20"
        >
          <path
            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
          />
        </svg>
        <p v-if="opg.prosjecna_ocjena != null" class="ms-1 text-sm font-medium text-gray-500">
          {{ (opg.prosjecna_ocjena ?? 0).toFixed(2) }} ({{ opg.broj_recenzija }})
        </p>
        <p v-else class="ms-1 text-xs font-medium text-gray-500 text-center">BEZ OCJENE</p>
      </div>
    </div>

    <p class="mt-2 mb-4 flex justify-center text-center text-pretty text-gray-700">
      {{ punaAdresa }}
    </p>
  </router-link>
</template>

<script setup>
import { computed } from "vue"

const props = defineProps({ opg: { type: Object, required: true } })
const defaultSlika = "https://placehold.co/600x400?text=OPG"
const zaokruzeno = computed(() => Math.round(props.opg.prosjecna_ocjena ?? 0))
const punaAdresa = computed(() => {
  const o = props.opg
  const parts = [o.adresa, o.postanski_broj + " " + o.grad].filter(Boolean)
  return parts.join(", ")
})
</script>
