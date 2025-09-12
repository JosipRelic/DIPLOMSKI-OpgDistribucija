<template>
  <section class="relative overflow-hidden">
    <img
      :src="resolveImg(slika)"
      :alt="naziv_kategorije"
      class="absolute inset-0 w-full h-full object-cover"
    />

    <div class="absolute inset-0 bg-gradient-to-b to-orange-50"></div>

    <div class="relative z-10 px-6 pt-40 text-center max-w-3xl mx-auto">
      <h1 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
        {{ naziv_kategorije }}
      </h1>
      <p class="mt-6 text-lg leading-8 text-gray-600">{{ opis }}</p>
    </div>
  </section>
</template>

<script setup>
const props = defineProps({
  naziv_kategorije: { type: String, required: true },
  opis: { type: String, default: "" },
  slika: { type: String, default: "" },
})
const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"
function resolveImg(src) {
  return src?.startsWith("/") ? `${BASE_URL}${src}` : src
}
</script>
