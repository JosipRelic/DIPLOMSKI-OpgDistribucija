<template>
  <div class="fixed z-[1000] right-4 bottom-4 space-y-2 pointer-events-none">
    <TransitionGroup name="toast" tag="div">
      <div
        v-for="o in ui.obavijesti"
        :key="o.id"
        class="pointer-events-auto min-w-[260px] max-w-[420px] rounded-xl shadow-xl px-4 py-3 text-white flex items-start gap-3"
        :class="pozadinaObavijesti(o.tip_obavijesti)"
        role="status"
        aria-live="polite"
      >
        <div class="flex-1">
          <p class="text-lg leading-snug whitespace-pre-line">{{ o.tekst }}</p>
          <div v-if="o.akcija" class="mt-2">
            <button
              class="text-sm underline underline-offset-2 hover:opacity-90"
              @click="klikniAkciju(o)"
            >
              {{ o.akcija.label || "Akcija" }}
            </button>
          </div>
        </div>
        <button
          class="ml-2 opacity-90 hover:opacity-100"
          aria-label="Zatvori obavijest"
          @click="ui.zatvori(o.id)"
        >
          ✕
        </button>
      </div>
    </TransitionGroup>
  </div>

  <div v-if="ui.potvrda.otvorena" class="fixed inset-0 z-[1100]">
    <div class="absolute inset-0 bg-black/40" @click="odustani()" />

    <div
      class="relative mx-auto mt-24 w-[92%] max-w-md rounded-2xl bg-white p-5 shadow-2xl"
      role="dialog"
      aria-modal="true"
      :aria-labelledby="labelId"
      @keydown.esc.prevent.stop="odustani()"
      @keydown.enter.prevent.stop="potvrdi()"
      tabindex="0"
      ref="modalEl"
    >
      <h3 class="text-lg font-semibold mb-2" :id="labelId">
        {{ ui.potvrda.naslov || "Potvrda" }}
      </h3>
      <p class="text-sm text-gray-700 mb-5 whitespace-pre-line">
        {{ ui.potvrda.poruka }}
      </p>
      <div class="flex justify-end gap-2">
        <button class="px-4 py-2 rounded-xl border border-gray-200 shadow-lg" @click="odustani()">
          {{ ui.potvrda.odustaniOdRadnje || "Odustani" }}
        </button>
        <button
          class="px-4 py-2 rounded-xl shadow-lg text-white"
          :class="obavijestSaPotvrdomBtn(ui.potvrda.tip_obavijesti)"
          @click="potvrdi()"
          data-testid="confirm-btn"
        >
          {{ ui.potvrda.potvrdiRadnju || "Potvrdi" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, ref, watch } from "vue"
import { useUiStore } from "@/stores/ui"

const ui = useUiStore()
const modalEl = ref(null)
const labelId = `dlg-title-${Math.random().toString(36).slice(2)}`

function pozadinaObavijesti(tip) {
  switch (tip) {
    case "uspjeh":
      return "bg-green-600"
    case "upozorenje":
      return "bg-amber-600"
    case "greska":
      return "bg-red-600"
    case "informacija":
    case "zadano":
    default:
      return "bg-slate-800"
  }
}
function obavijestSaPotvrdomBtn(tip) {
  switch (tip) {
    case "opasnost":
    case "greska":
      return "bg-red-600 hover:bg-red-700"
    case "upozorenje":
      return "bg-amber-600 hover:bg-amber-700"
    default:
      return "bg-slate-900 hover:bg-slate-800"
  }
}

function potvrdi() {
  ui.donesenaOdluka(true)
}
function odustani() {
  ui.donesenaOdluka(false)
}

function klikniAkciju(o) {
  try {
    o.akcija?.onClick?.()
  } catch {}
  ui.zatvori(o.id)
}

watch(
  () => ui.potvrda.otvorena,
  (open) => {
    if (open) {
      document.documentElement.classList.add("overflow-hidden")
      setTimeout(() => modalEl.value?.focus(), 0)
    } else {
      document.documentElement.classList.remove("overflow-hidden")
    }
  },
)
onUnmounted(() => document.documentElement.classList.remove("overflow-hidden"))
</script>

<style scoped>
.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(8px) scale(0.98);
}
.toast-enter-active,
.toast-leave-active {
  transition: all 0.18s ease;
}
</style>
