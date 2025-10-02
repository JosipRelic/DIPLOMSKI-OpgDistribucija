<template>
  <div class="mt-10 flex items-center justify-center gap-x-6 mb-3">
    <div class="hidden sm:block -space-x-2 overflow-hidden">
      <img
        v-for="(r, i) in recenzirao"
        :key="i"
        class="inline-block h-12 w-12 rounded-full ring-2 ring-white object-cover"
        :src="r.slika || 'https://placehold.co/600x400?text=Recenzent'"
        :alt="`${r.ime} ${r.prezime}`"
        :title="`${r.ime} ${r.prezime}`"
      />
    </div>
    <div class="boder-none sm:border-l-2 border-black sm:pl-8">
      <div class="flex justify-center sm:justify-start">
        <h3 class="text-2xl font-semibold mr-2">{{ Number(prosjek).toFixed(1) }}</h3>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36" class="w-5 fill-orange-500">
          <path
            d="M27.287 34.627c-.404 0-.806-.124-1.152-.371L18 28.422l-8.135 5.834a1.97 1.97 0 0 1-2.312-.008a1.971 1.971 0 0 1-.721-2.194l3.034-9.792l-8.062-5.681a1.98 1.98 0 0 1-.708-2.203a1.978 1.978 0 0 1 1.866-1.363L12.947 13l3.179-9.549a1.976 1.976 0 0 1 3.749 0L23 13l10.036.015a1.975 1.975 0 0 1 1.159 3.566l-8.062 5.681l3.034 9.792a1.97 1.97 0 0 1-.72 2.194a1.957 1.957 0 0 1-1.16.379z"
          />
        </svg>
      </div>
      <div>
        <h3 class="text-sm">
          Ocijenjeni od strane <strong>{{ brojRec }}</strong> korisnika.
        </h3>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue"
import { useOpgNadzornaPlocaStore } from "@/stores/nadzornaPlocaOpg"

const nadzorna_ploca = useOpgNadzornaPlocaStore()
onMounted(() => nadzorna_ploca.ucitajNadzornuPlocu())

const prosjek = computed(() => nadzorna_ploca.podaci?.ocjene?.prosjek ?? 0)
const brojRec = computed(() => nadzorna_ploca.podaci?.ocjene?.broj_recenzija ?? 0)
const recenzirao = computed(() => nadzorna_ploca.podaci?.ocjene?.recenzirao ?? [])
</script>
