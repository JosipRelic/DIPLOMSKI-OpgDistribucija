<template>
  <div
    class="mx-auto grid max-w-2xl grid-cols-1 items-center gap-x-8 gap-y-16 px-4 py-12 sm:px-6 sm:py-12 lg:max-w-7xl lg:grid-cols-2 lg:px-8"
  >
    <div>
      <h2 class="text-2xl font-bold text-gray-900 sm:text-3xl">Farma+</h2>
      <p class="mt-4 text-gray-700">
        Trebaš pomoć s oranjem, sjetvom, špricanjem ili berbom? Odaberi neku od dostupnih usluga i
        dogovori suradnju izravno putem aplikacije. Prodaješ stoku viška ili ti treba privremeni
        najam za ispašu, uzgoj? Pronađi ono što ti treba u samo nekoliko klikova.
        <strong class="text-orange-600"
          >Klikni na neku od kategorija ispod i filtriraj usluge.</strong
        >
      </p>

      <dl
        class="mt-10 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 sm:gap-y-14 lg:gap-x-8"
        v-if="farma.kategorije.length"
      >
        <div v-for="k in farma.kategorije" :key="k.id" class="border-t border-gray-200 pt-4">
          <button
            @click="odaberiKategoriju(k.slug)"
            class="font-medium inline-flex text-left items-center gap-2 cursor-pointer"
            :class="aktivna(k.slug) ? 'text-orange-600' : 'text-gray-900 hover:text-orange-700'"
          >
            <span>{{ k.naziv }}</span>
            <span
              class="text-xs rounded-full px-2 py-0.5 border shadow-md"
              :class="brojacKlase(k)"
              title="Broj dostupnih usluga"
            >
              {{ k.dostupni }}
            </span>
          </button>
        </div>
      </dl>

      <div v-else class="mt-8 text-gray-500">Učitavanje kategorija…</div>
    </div>
    <div class="grid grid-cols-2 grid-rows-2 gap-4 sm:gap-6 lg:gap-8">
      <img
        :src="slikeFarmaPlusKraveNaslovna"
        class="rounded-lg h-60 w-80 object-cover mx-auto"
        alt="Slika Krave"
      />
      <img
        :src="slikeFarmaPlusBranjeZitaNaslovna"
        class="rounded-lg h-60 w-80 object-cover mx-auto"
        alt="Slika branje žita"
      />
      <img
        :src="slikeFarmaPlusSpricanjeKukuruzaNaslovna"
        class="rounded-lg h-60 w-80 object-cover mx-auto"
        alt="Slika špricanje kukuruza"
      />
      <img
        :src="slikeFarmaPlusOranjeNaslovna"
        class="rounded-lg h-60 w-80 object-cover mx-auto"
        alt="Slika oranje"
      />
    </div>
  </div>
</template>
<script setup>
import { useFarmaPlusStore } from "@/stores/farmaPlus"
import slikeFarmaPlusKraveNaslovna from "@/assets/slike/farma-plus-krave-naslovna.png"
import slikeFarmaPlusBranjeZitaNaslovna from "@/assets/slike/farma-plus-branjezita-naslovna.png"
import slikeFarmaPlusSpricanjeKukuruzaNaslovna from "@/assets/slike/farma-plus-spricanjekukuruza-naslovna.png"
import slikeFarmaPlusOranjeNaslovna from "@/assets/slike/farma-plus-oranje-naslovna.png"

const farma = useFarmaPlusStore()

function odaberiKategoriju(slug) {
  farma.postaviKategoriju(slug)
}

function aktivna(slug) {
  return farma.kat_slug === slug
}

function brojacKlase(k) {
  if (farma.kat_slug === k.slug) {
    return "border-orange-600 text-white bg-orange-600"
  }

  if (k.dostupni > 0) {
    return "border-[#223c2f] text-white bg-[#223c2f]"
  }

  return "border-gray-200 text-gray-600"
}
</script>
