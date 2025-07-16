<template>
  <div class="min-h-screen flex flex-col bg-orange-50">
    <Navbar />

    <main class="flex-grow">
      <router-view />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
</script>

<style scoped></style>
