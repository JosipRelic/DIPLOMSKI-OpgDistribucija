<template>
  <section>
    <NaslovnaFarmaPlus />
  </section>

  <section>
    <FilteriPoKategorijiFarmaPlus />
  </section>
</template>

<script setup>
import { onMounted, watch } from "vue"
import { useFarmaPlusStore } from "@/stores/farmaPlus"
import NaslovnaFarmaPlus from "@/components/farmaplus/NaslovnaFarmaPlus.vue"
import FilteriPoKategorijiFarmaPlus from "@/components/farmaplus/FilteriPoKategorijiFarmaPlus.vue"

const farma = useFarmaPlusStore()

onMounted(async () => {
  await farma.ucitajKategorije()
})

watch(
  () => farma.kat_slug,
  async (slug) => {
    if (!slug) return
    farma.resetirajStranice()
    await farma.ucitajUsluge()
    if (farma.ukupno_usluga > 0) {
      await farma.ucitajFiltere()
    } else {
      farma.filteriZupanije = []
      farma.filterMjesta = []
      farma.filteriUsluge = []
    }
  },
)
</script>
