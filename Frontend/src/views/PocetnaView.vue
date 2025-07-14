<template>
  <h1 class="text-red-500">OVDJE ĆEMO DOHVATITI PODATKE IZ BAZE:</h1>
  {{ test_podaci_iz_baze }}
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const test_podaci_iz_baze = ref([])

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/")
    test_podaci_iz_baze.value = response.data
  } catch (error) {
    console.error("Greška pri dohvaćanju podataka: ", error)
  }
})
</script>
