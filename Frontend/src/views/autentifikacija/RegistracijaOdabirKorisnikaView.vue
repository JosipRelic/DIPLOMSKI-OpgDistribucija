<template>
  <section class="flex h-screen">
    <RouterLink
      :to="{ name: 'registracijaKupac' }"
      class="group relative w-1/2 overflow-hidden transition-all duration-500 hover:w-[55%]"
    >
      <img
        :src="slikeOdabirKorisnikaKupac"
        alt="Registracija kupca"
        class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
      />
      <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
        <h2 class="text-gray-100 text-3xl font-semibold group-hover:scale-105 p-10 transition">
          Kupac
        </h2>
      </div>
    </RouterLink>

    <RouterLink
      :to="{ name: 'registracijaOPG' }"
      class="group relative w-1/2 overflow-hidden transition-all duration-500 hover:w-[55%]"
    >
      <img
        :src="slikeOdabirKorisnikaOpg"
        alt="Registracija OPG-a"
        class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
      />
      <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
        <h2 class="text-white text-3xl font-semibold group-hover:scale-105 p-10 transition">OPG</h2>
      </div>
    </RouterLink>
  </section>
</template>

<script setup>
import slikeOdabirKorisnikaKupac from "@/assets/slike/odabir-korisnika-kupac.png"
import slikeOdabirKorisnikaOpg from "@/assets/slike/odabir-korisnika-opg.png"
</script>
