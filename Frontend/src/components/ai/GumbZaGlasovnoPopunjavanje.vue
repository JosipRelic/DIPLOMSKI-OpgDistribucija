<template>
  <div class="flex flex-col items-center">
    <button
      :disabled="obradaUTijeku"
      type="button"
      class="w-full p-4 max-w-xs font-bold shadow-sm rounded-lg py-3 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
      :class="[
        obradaUTijeku ? 'bg-gray-500 text-white cursor-not-allowed opacity-80' : '',
        snimam && !obradaUTijeku ? 'bg-red-400 text-gray-900 animate-bounce' : '',
        !snimam && !obradaUTijeku ? 'bg-red-300 hover:bg-red-400 text-gray-900' : '',
        klasaGumba,
      ]"
      @click.prevent="klikNaGumb"
    >
      <div class="bg-white p-2 rounded-full">
        <svg
          v-if="!snimam"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          class="w-6"
          :class="snimam || obradaUTijeku ? 'text-gray-700' : 'text-red-600'"
        >
          <path
            fill="currentColor"
            d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
          />
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-6 text-red-600" viewBox="0 0 24 24">
          <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2">
            <rect width="4" height="14" x="6" y="5" rx="1" />
            <rect width="4" height="14" x="14" y="5" rx="1" />
          </g>
        </svg>
      </div>
      <span class="ml-4" :class="obradaUTijeku ? 'text-sm' : 'text-base'">{{ tekstGumba }}</span>
    </button>
    <p v-if="snimam" class="mt-2 text-sm text-amber-700 bg-amber-50 px-3 py-2 rounded-md shadow-md">
      Snimam… jasno i razgovijetno izgovorite podatke.
    </p>
    <p
      v-else-if="obradaUTijeku"
      class="mt-2 text-sm text-teal-500 bg-teal-50 px-3 py-2 rounded-md shadow-md"
    >
      Dohvaćam podatke iz snimke…
    </p>
    <p
      v-else-if="zadnjiTranskript"
      class="mt-2 text-sm text-teal-800 bg-teal-50 px-3 py-2 rounded-md shadow-md"
    >
      AI je čuo: "<i>{{ zadnjiTranskript }}</i
      >"
      <br />
      <span class="text-xs font-bold"
        >* Ako nešto nije dobro popunjeno možete kliknuti ponovno na gumb i reći npr. 'Ispravi
        prezime u Horvat' *</span
      >
    </p>
    <p v-if="greska" class="mt-2 text-sm text-red-700 bg-red-50 px-3 py-2 rounded-md shadow-md">
      {{ greska }}
    </p>
  </div>
</template>

<script setup>
import { koristiGlasovnoPopunjavanje } from "@/ai/koristiGlasovnoPopunjavanje"

const props = defineProps({
  strukturaUpita: { type: String, required: true },
})

const emit = defineEmits(["popuni"])

const {
  snimam,
  obradaUTijeku,
  tekstGumba,
  klasaGumba,
  greska,
  zadnjiTranskript,
  zapocniSnimanje,
  zaustaviSnimanjeIVratiTranskript,
  strukturirajTekst,
} = koristiGlasovnoPopunjavanje()

async function klikNaGumb() {
  if (!snimam.value) {
    await zapocniSnimanje()
  } else {
    const { ok, tekst } = await zaustaviSnimanjeIVratiTranskript()
    if (!ok || !tekst) return
    const strukturiraj_tekst = await strukturirajTekst(tekst, props.strukturaUpita)
    if (strukturiraj_tekst.ok)
      emit("popuni", { podaci: strukturiraj_tekst.podaci, transkript: tekst })
  }
}
</script>
