<template>
  <article
    class="group relative overflow-hidden rounded-2xl border border-gray-100 shadow-xl transition-transform duration-200 ease-out hover:scale-[1.02] hover:shadow-md"
  >
    <img
      :src="props.usluga.slika_usluge || defaultSlika"
      :alt="props.usluga.naziv"
      class="h-40 w-full object-cover"
    />
    <div class="flex flex-col gap-3 p-4">
      <header class="flex items-start justify-between gap-2">
        <h3 class="text-lg font-semibold leading-snug">{{ props.usluga.naziv }}</h3>
        <span class="shrink-0 rounded-full bg-[#223c2f] px-3 py-1 text-xs font-medium text-gray-100"
          >Datum po dogovoru</span
        >
      </header>
      <p class="text-sm text-gray-700">
        {{ props.usluga.opis }}
      </p>
      <div class="mt-1 flex items-center justify-between">
        <div>
          <span class="text-xs uppercase tracking-wide text-neutral-500">Cijena</span>
          <div class="text-base font-semibold">
            {{ cijena }} / {{ props.usluga.mjerna_jedinica }}
          </div>
        </div>
        <div v-if="prikaziPonudacaUsluge" class="text-right">
          <span class="text-xs uppercase tracking-wide text-neutral-500">Uslugu nudi</span>
          <div class="text-sm font-medium hover:underline text-teal-500">
            <a href="">{{ props.usluga.opg_naziv }}</a>
          </div>
        </div>
      </div>
      <div>
        <span class="flex justify-center text-center text-xs">Unesite količinu</span>
        <div
          class="flex items-center justify-center shadow mt-1 mx-auto rounded-sm border border-gray-200 mb-3 w-fit"
        >
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
        class="mt-auto block rounded-xl border border-orange-600 bg-orange-600 px-5 py-3 text-sm font-medium tracking-widest text-gray-100 uppercase transition-colors hover:bg-orange-900"
      >
        Naruči uslugu
      </button>
    </div>
  </article>
</template>

<script setup>
import { computed } from "vue"

const props = defineProps({
  usluga: { type: Object, required: true },
  prikaziPonudacaUsluge: { type: Boolean, default: true },
})
const defaultSlika = "https://placehold.co/600x600?text=Usluga"
const cijena = computed(() => {
  const n = Number(props.usluga.cijena || 0)
  return `${n.toFixed(2)} €`
})
</script>
