<template>
  <div class="min-h-screen flex flex-col bg-orange-50">
    <Navbar />

    <main class="flex-grow">
      <router-view />
      <GlobalneObavijesti />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
import GlobalneObavijesti from "./components/GlobalneObavijesti.vue"
</script>

<style scoped></style>
