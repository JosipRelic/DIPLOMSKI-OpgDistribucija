<template>
  <section>
    <div class="flex md:min-h-screen">
      <ProfilKupacIzbornik />

      <main class="md:flex-1 md:block p-6 hidden">
        <router-view />
      </main>
    </div>
  </section>
</template>
<script setup>
import ProfilKupacIzbornik from "@/components/profili/kupac/profilKupacIzbornik.vue"
</script>
