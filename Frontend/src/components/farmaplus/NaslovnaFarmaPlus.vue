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

      <dl class="mt-10 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 sm:gap-y-14 lg:gap-x-8">
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-orange-600" href="#">Priprema tla</a>
        </div>
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-gray-900" href="#">Sjetva i sadnja</a>
        </div>
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-gray-900" href="#">Navodnjavanje</a>
        </div>
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-gray-900" href="#">Zaštita bilja i gnojidba</a>
        </div>
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-gray-900" href="#">Berba i žetva</a>
        </div>
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-gray-900" href="#">Skladištenje i prijevoz</a>
        </div>
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-gray-900" href="#">Održavanje i dodatne usluge</a>
        </div>
        <div class="border-t border-gray-200 pt-4">
          <a class="font-medium text-gray-900" href="#">Prodaja/najam stoke i stočarska pomoć</a>
        </div>
      </dl>
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
import slikeFarmaPlusKraveNaslovna from "@/assets/slike/farma-plus-krave-naslovna.png"
import slikeFarmaPlusBranjeZitaNaslovna from "@/assets/slike/farma-plus-branjezita-naslovna.png"
import slikeFarmaPlusSpricanjeKukuruzaNaslovna from "@/assets/slike/farma-plus-spricanjekukuruza-naslovna.png"
import slikeFarmaPlusOranjeNaslovna from "@/assets/slike/farma-plus-oranje-naslovna.png"
</script>
