<template>
  <section>
    <div class="flex flex-col lg:flex-row min-h-screen">
      <div class="w-full lg:w-80 bg-white">
        <ProfilKupacIzbornik />
      </div>

      <main class="flex-1 w-full p-4">
        <router-view />
      </main>
    </div>
  </section>
</template>
<script setup>
import ProfilKupacIzbornik from "@/components/profili/kupac/ProfilKupacIzbornik.vue"
</script>
