<template>
  <article
    class="group relative overflow-hidden rounded-2xl border border-gray-100 shadow-xl transition-transform duration-200 ease-out hover:scale-[1.02] hover:shadow-md cursor-pointer"
    :aria-label="`Pogledaj uslugu ${props.usluga.naziv}`"
    @click="otvoriDetalje"
  >
    <img
      :src="props.usluga.slika_usluge || defaultSlika"
      :alt="props.usluga.naziv"
      class="h-40 w-full object-cover"
    />
    <div class="flex flex-col gap-3 p-4">
      <header class="flex items-start justify-between gap-2">
        <h3 class="text-lg font-semibold leading-snug">{{ props.usluga.naziv }}</h3>
        <span
          :class="['shrink-0 rounded-full px-3 py-1 text-xs font-medium shadow-md', badgeClass]"
        >
          {{ badgeText }}
        </span>
      </header>

      <p class="text-sm text-gray-700">
        {{ props.usluga.opis }}
      </p>

      <div class="mt-1 flex items-center justify-between">
        <div>
          <span class="text-xs uppercase tracking-wide text-neutral-500">Cijena</span>
          <div class="text-base font-semibold">
            {{ cijena }} / {{ props.usluga.mjerna_jedinica }}
          </div>
        </div>

        <div v-if="prikaziPonudacaUsluge" class="text-right">
          <span class="text-xs uppercase tracking-wide text-neutral-500">Uslugu nudi</span>
          <div class="text-sm font-medium hover:underline text-teal-500">
            <router-link
              :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: props.usluga.opg_slug } }"
              @click.stop
            >
              {{ props.usluga.opg_naziv }}
            </router-link>
          </div>
        </div>
      </div>

      <div class="hidden">
        <span class="flex justify-center text-center text-xs">Unesite količinu</span>
        <div
          class="flex items-center justify-center shadow mt-1 mx-auto rounded-sm border border-gray-200 mb-3 w-fit"
        >
          <button
            type="button"
            class="size-10 leading-10 text-gray-600 transition hover:text-red-600"
          >
            &minus;
          </button>

          <input
            type="number"
            id="Kolicina"
            value="1"
            class="h-10 w-16 text-orange-600 border-transparent text-center [-moz-appearance:_textfield] sm:text-sm [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"
          />

          <button
            type="button"
            class="size-10 leading-10 text-gray-600 transition hover:text-green-600"
          >
            &plus;
          </button>
        </div>
      </div>

      <button
        class="mt-auto block rounded-xl border border-orange-600 bg-orange-600 hover:border-orange-900 px-5 py-3 text-sm font-medium tracking-widest text-gray-100 uppercase transition-colors hover:bg-orange-900"
        @click.stop="otvoriDetalje"
      >
        <router-link :to="linkDetalji" class="block w-full h-full text-center">
          Prikaži uslugu
        </router-link>
      </button>
    </div>
  </article>
</template>

<script setup>
import { computed, onMounted, ref } from "vue"
import api from "@/services/api"
import { useRouter } from "vue-router"

const props = defineProps({
  usluga: { type: Object, required: true },
  prikaziPonudacaUsluge: { type: Boolean, default: true },
  overrideImaTermina: { type: [Boolean, null], default: null },
})

const router = useRouter()

const defaultSlika = "https://placehold.co/600x600?text=Usluga"
const cijena = computed(() => {
  const n = Number(props.usluga.cijena || 0)
  return `${n.toFixed(2)} €`
})

const uslugaSlugId = computed(() => `${props.usluga.slug}-${props.usluga.id}`)

const linkDetalji = computed(() => ({
  name: "farmaPlusDetaljiUsluge",
  params: { uslugaSlugId: uslugaSlugId.value },
}))

function otvoriDetalje() {
  router.push(linkDetalji.value)
}

const _terminiCache = Object.create(null)

const imaTermina = ref(null)

const effectiveImaTermina = computed(() =>
  props.overrideImaTermina !== null ? props.overrideImaTermina : imaTermina.value,
)

const badgeText = computed(() => {
  if (effectiveImaTermina.value === null) return "Provjera termina…"
  return effectiveImaTermina.value ? "Dostupni termini" : "Datum po dogovoru"
})
const badgeClass = computed(() => {
  if (effectiveImaTermina.value === null) return "bg-gray-200 text-gray-700"
  return effectiveImaTermina.value ? "bg-[#223c2f] text-gray-100" : "bg-amber-500 text-white"
})

async function provjeriImaTerminaKartica(opgId, horizon = 3) {
  if (!opgId) {
    imaTermina.value = false
    return
  }
  if (_terminiCache[opgId] !== undefined) {
    imaTermina.value = _terminiCache[opgId]
    return
  }

  const now = new Date()
  let found = false
  for (let i = 0; i < horizon; i++) {
    const d = new Date(now.getFullYear(), now.getMonth() + i, 1)
    try {
      const { data } = await api.get("/opg/raspolozivost/kalendar", {
        params: { opg_id: opgId, godina: d.getFullYear(), mjesec: d.getMonth() + 1 },
      })
      if (data?.slotovi && Object.keys(data.slotovi).length > 0) {
        found = true
        break
      }
    } catch (e) {}
  }
  _terminiCache[opgId] = found
  imaTermina.value = found
}

onMounted(() => {
  provjeriImaTerminaKartica(props.usluga.opg_id)
})
</script>
