<template>
  <div class="relative overflow-hidden">
    <img :src="slika" :alt="nazivKategorije" class="absolute inset-0 w-full h-full object-cover" />

    <div class="absolute inset-0 bg-gradient-to-b to-orange-50"></div>

    <div class="relative z-10 px-6 pt-40 text-center max-w-3xl mx-auto">
      <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
        {{ nazivKategorije }}
      </h2>
      <p class="mt-6 text-lg leading-8 text-gray-600">
        {{ opis }}
      </p>
    </div>
  </div>
</template>
<script setup>
defineProps({
  nazivKategorije: String,
  opis: String,
  slika: String,
})
</script>
