<template>
  <section>
    <div class="flex flex-col lg:flex-row min-h-screen">
      <div class="w-full lg:w-80 bg-white">
        <ProfilOpgIzbornik />
      </div>

      <main class="flex-1 w-full p-4">
        <router-view />
      </main>
    </div>
  </section>
</template>
<script setup>
import ProfilOpgIzbornik from "@/components/profili/opg/ProfilOpgIzbornik.vue"
</script>
