<template>
  <router-link
    :to="{
      name: 'ETrznicaProizvodDetalji',
      params: { katSlug, proizvodSlugId },
    }"
  >
    <div
      class="group relative block rounded-tr-3xl border border-gray-100 flex flex-col h-full cursor-pointer"
    >
      <span
        class="absolute -top-px -right-px rounded-tr-3xl rounded-bl-3xl bg-[#223c2f] px-6 py-4 font-medium tracking-widest text-gray-100 uppercase transition duration-500 group-hover:scale-105"
      >
        {{ cijena }} <span class="lowercase">/ {{ proizvod.mjerna_jedinica }}</span>
      </span>

      <img
        :src="proizvod.slika_proizvoda || defaultSlika"
        :alt="proizvod.naziv"
        class="aspect-square w-full object-cover rounded-tr-3xl"
      />

      <div class="p-4 text-center flex flex-col rounded-xl shadow-xl justify-between h-full">
        <strong
          class="text-xl font-medium text-gray-900 transition duration-500 group-hover:scale-105"
        >
          {{ proizvod.naziv }}
        </strong>
        <small
          v-if="prikaziLinkPremaOpgu && opgProfilSlug"
          class="text-sm text-teal-500 hover:underline cursor-pointer"
        >
          <router-link :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: opgProfilSlug } }">{{
            proizvod.opg_naziv
          }}</router-link>
        </small>

        <p
          v-if="proizvod.opis"
          class="mt-2 mb-4 text-pretty text-gray-700 transition duration-500 group-hover:scale-105 line-clamp-3"
        >
          {{ proizvod.opis }}
        </p>

        <span class="flex justify-center text-center text-xs pb-1">Unesite količinu</span>
        <div>
          <div
            class="flex shadow items-center justify-center mx-auto rounded-sm border border-gray-200 mb-3 w-fit"
          >
            <button
              type="button"
              class="size-10 leading-10 text-gray-600 transition hover:text-red-600"
            >
              &minus;
            </button>
            <input
              type="number"
              value="1"
              class="h-10 w-16 text-orange-600 border-transparent text-center [-moz-appearance:_textfield] sm:text-sm [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"
            />
            <button
              type="button"
              class="size-10 leading-10 text-gray-600 transition hover:text-green-600"
            >
              &plus;
            </button>
          </div>
        </div>

        <button
          class="mt-auto shadow-md block rounded-xl border border-orange-600 bg-orange-600 px-5 py-3 text-sm font-medium tracking-widest text-white uppercase transition-colors hover:bg-orange-900 hover:border-orange-900"
        >
          Dodaj u košaricu
        </button>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { computed } from "vue"

const props = defineProps({
  proizvod: { type: Object, required: true },
  katSlug: { type: String, required: true },
  prikaziLinkPremaOpgu: { type: Boolean, default: true },
})
const defaultSlika = "https://placehold.co/600x600?text=Proizvod"
const cijena = computed(() => {
  const n = Number(props.proizvod.cijena || 0)
  return `${n.toFixed(2)} €`
})

const proizvodSlugId = computed(() => {
  const slug = props.proizvod.slug || `${props.proizvod.naziv}`.toLowerCase().replace(/\s+/g, "-")
  return `${slug}-${props.proizvod.id}`
})

const opgProfilSlug = computed(() => props.proizvod.opg_slug || null)
</script>
