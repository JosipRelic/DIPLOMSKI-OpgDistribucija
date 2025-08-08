<template>
  <section>
    <KategorijeProizvodaProizvodiNaslovna
      nazivKategorije="Domaće voće"
      opis="Uživajte u bogatstvu okusa i mirisa domaćeg voća uzgojenog s pažnjom i ljubavlju na hrvatskim OPG-ovima."
      :slika="slikeETrznicaKategorijeVoce"
    />
  </section>
  <section>
    <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
      <div class="mt-4 lg:mt-8 grid grid-cols-1 lg:grid-cols-4 gap-8">
        <KategorijeProizvodaProizvodiFilteri />

        <div
          class="lg:col-span-3 grid grid-cols-1 max-sm:grid-cols-2 sm:grid-cols-2 md:grid-cols-3 gap-6 px-4 py-8 mb-14"
        >
          <KarticaProizvoda />
          <Paginacija />
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import KategorijeProizvodaProizvodiNaslovna from "@/components/etrznica/kategorije-proizvoda/KategorijeProizvodaProizvodiNaslovna.vue"
import KategorijeProizvodaProizvodiFilteri from "@/components/etrznica/kategorije-proizvoda/KategorijeProizvodaProizvodiFilteri.vue"
import KarticaProizvoda from "@/components/dijeljeno/KarticaProizvoda.vue"
import Paginacija from "@/components/etrznica/PaginacijaETrznica.vue"
import slikeETrznicaKategorijeVoce from "@/assets/slike/etrznica-kategorije-voce.jpg"
</script>
