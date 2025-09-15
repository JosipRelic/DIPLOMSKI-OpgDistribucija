<template>
  <section class="mx-auto max-w-7xl px-5 md:px-10 mb-20">
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
      <aside class="lg:col-span-1">
        <h2 class="text-2xl font-semibold mb-3">Recenzije kupaca</h2>

        <div class="flex items-center gap-2 mb-2">
          <div class="flex">
            <svg
              v-for="i in 5"
              :key="'p' + i"
              viewBox="0 0 20 20"
              class="w-5 h-5 fill-current"
              :class="i <= Math.round(prosjek) ? 'text-orange-500' : 'text-orange-200'"
            >
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.967 0 1.371 1.24.588 1.81l-2.802 2.035a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118L10.98 14.61a1 1 0 00-1.162 0L6.615 16.28c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              />
            </svg>
          </div>
          <span class="text-sm text-gray-600"> Na temelju {{ ukupnoRecenzija }} recenzije </span>
        </div>

        <ul class="space-y-2 mt-4">
          <li v-for="r in [5, 4, 3, 2, 1]" :key="r" class="flex items-center gap-2">
            <span class="w-5 text-sm">{{ r }}</span>
            <svg viewBox="0 0 20 20" class="w-4 h-4 fill-current text-orange-500">
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.967 0 1.371 1.24.588 1.81l-2.802 2.035a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118L10.98 14.61a1 1 0 00-1.162 0L6.615 16.28c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              />
            </svg>
            <div class="flex-1 h-3 rounded-full bg-gray-100 overflow-hidden">
              <div class="h-full bg-orange-500" :style="{ width: postotak(r) + '%' }"></div>
            </div>
            <span class="w-10 text-sm text-gray-600 text-right">{{ postotak(r).toFixed(0) }}%</span>
          </li>
        </ul>

        <div class="mt-10">
          <p class="text-sm text-gray-600 mb-3">Podijelite svoje iskustvo s ostalim kupcima.</p>

          <button
            v-if="auth.korisnikAutentificiran"
            @click="otvoriFormu"
            class="w-full border border-teal-500 bg-teal-500 hover:bg-teal-700 hover:border-teal-700 shadow-lg text-white hover:text-gray-200 rounded-xl px-4 py-3 transition"
          >
            Napiši recenziju
          </button>

          <button
            v-else
            disabled
            class="w-full border border-gray-200 bg-gray-50 text-gray-400 rounded-xl px-4 py-3 cursor-not-allowed"
            title="Morate biti prijavljeni kako biste ostavili recenziju."
          >
            Prijavite se za recenziju
          </button>
        </div>
      </aside>

      <!-- Desni panel: lista ili forma -->
      <div class="lg:col-span-2">
        <!-- FORMA -->
        <div v-if="prikaziFormu" class="rounded-2xl border border-gray-100 p-6 bg-white shadow">
          <header class="mb-4">
            <h3 class="text-lg font-semibold">Napišite recenziju</h3>
            <p class="text-sm text-gray-600">Vaša ocjena pomaže drugima.</p>
          </header>

          <form @submit.prevent="posalji" class="space-y-4">
            <!-- Ocjena -->
            <div>
              <label class="block text-sm font-medium mb-2">Ocjena</label>
              <div class="flex items-center gap-2">
                <label v-for="i in 5" :key="i" class="relative cursor-pointer">
                  <input
                    type="radio"
                    class="sr-only"
                    name="ocjena"
                    :value="i"
                    v-model.number="forma.ocjena"
                  />
                  <svg
                    viewBox="0 0 20 20"
                    class="w-8 h-8 fill-current transition"
                    :class="
                      i <= forma.ocjena
                        ? 'text-orange-500'
                        : 'text-orange-200 hover:text-orange-300'
                    "
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.967 0 1.371 1.24.588 1.81l-2.802 2.035a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118L10.98 14.61a1 1 0 00-1.162 0L6.615 16.28c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    />
                  </svg>
                </label>
              </div>
              <p v-if="greskaOcjena" class="text-sm text-red-600 mt-1">{{ greskaOcjena }}</p>
            </div>

            <!-- Komentar -->
            <div>
              <label class="block text-sm font-medium mb-2">Komentar (opcionalno)</label>
              <textarea
                v-model.trim="forma.komentar"
                rows="4"
                class="w-full rounded-xl p-3 border border-gray-300 shadow focus:border-orange-500 focus:ring-orange-500"
              ></textarea>
            </div>

            <div class="flex items-center gap-3">
              <button
                type="submit"
                class="rounded-xl bg-orange-600 shadow-md hover:bg-orange-900 text-white px-5 py-2.5 transition disabled:opacity-50"
                :disabled="slanje"
              >
                {{ slanje ? "Slanje…" : "Pošalji recenziju" }}
              </button>
              <button
                type="button"
                class="px-4 py-2 rounded-xl border border-gray-200 shadow-md"
                @click="zatvoriFormu"
                :disabled="slanje"
              >
                Odustani
              </button>
            </div>
          </form>
        </div>

        <!-- LISTA RECENZIJA -->
        <div v-else class="space-y-8">
          <article
            v-for="r in recenzije"
            :key="r.id"
            class="border-t first:border-t-0 pt-8 border-orange-300"
          >
            <div class="flex items-start gap-4">
              <img
                :src="r.slika_korisnika || placeholder"
                alt=""
                class="w-12 h-12 rounded-full object-cover"
              />
              <div class="flex-1">
                <div class="flex items-center justify-between">
                  <div>
                    <h4 class="font-semibold leading-tight pb-2">
                      {{ r.korisnik_ime || "Anonimni korisnik" }}
                    </h4>
                    <div class="flex items-center gap-2">
                      <div class="flex">
                        <svg
                          v-for="i in 5"
                          :key="r.id + 's' + i"
                          viewBox="0 0 20 20"
                          class="w-4 h-4 fill-current"
                          :class="i <= r.ocjena ? 'text-orange-500' : 'text-orange-200'"
                        >
                          <path
                            d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.967 0 1.371 1.24.588 1.81l-2.802 2.035a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118L10.98 14.61a1 1 0 00-1.162 0L6.615 16.28c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                          />
                        </svg>
                      </div>
                      <span class="text-xs text-gray-500">{{ formatDatum(r.datum_izrade) }}</span>
                    </div>
                  </div>
                </div>

                <p v-if="r.komentar" class="mt-3 text-gray-700">
                  {{ r.komentar }}
                </p>
              </div>
            </div>
          </article>

          <div v-if="!recenzije.length" class="text-gray-500">Još nema recenzija.</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue"
import { useRoute } from "vue-router"
import { useEtrznicaOpgDetaljiStore } from "@/stores/eTrznicaOpgDetalji"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"

const route = useRoute()
const slug = computed(() => route.params.opgSlug)

const store = useEtrznicaOpgDetaljiStore()
const auth = useAutentifikacijskiStore()

const prikaziFormu = ref(false)
const slanje = ref(false)
const forma = reactive({ ocjena: 0, komentar: "" })
const greskaOcjena = ref(null)

const placeholder = "https://placehold.co/96x96?text=K"

// Učitavanje recenzija
onMounted(async () => {
  await store.ucitajRecenzije(slug.value, { stranica: 1, velicina: 20 }) // ili paginacija po želji
})

// Lista recenzija iz store-a
const recenzije = computed(() => store.recenzije?.lista_recenzija ?? [])

// Prosjek i ukupno (preuzmi iz detalja OPG-a ako ih držiš u store-u)
const prosjek = computed(() => store.opg?.prosjecna_ocjena ?? izracunajProsjek(recenzije.value))
const ukupnoRecenzija = computed(
  () => store.opg?.broj_recenzija ?? store.recenzije?.ukupno_recenzija ?? recenzije.value.length,
)

// Raspodjela zvjezdica
function postotak(zaKoliko) {
  if (!recenzije.value.length) return 0
  const n = recenzije.value.filter((r) => Number(r.ocjena) === zaKoliko).length
  return (n / recenzije.value.length) * 100
}

// Slanje
async function posalji() {
  greskaOcjena.value = null
  if (!forma.ocjena || forma.ocjena < 1 || forma.ocjena > 5) {
    greskaOcjena.value = "Molimo odaberite ocjenu od 1 do 5."
    return
  }
  slanje.value = true
  try {
    await store.posaljiOcjenu(slug.value, {
      ocjena: forma.ocjena,
      komentar: forma.komentar || null,
    })
    // reset i zatvaranje
    forma.ocjena = 0
    forma.komentar = ""
    prikaziFormu.value = false
    // ponovno učitaj recenzije
    await store.ucitajRecenzije(slug.value, { stranica: 1, velicina: 100 })
  } finally {
    slanje.value = false
  }
}

function otvoriFormu() {
  prikaziFormu.value = true
}

function zatvoriFormu() {
  prikaziFormu.value = false
}

// Formatiranje datuma + vremena za hr-HR
function formatDatum(val) {
  if (!val) return ""
  const d = new Date(val)
  if (isNaN(d)) return ""
  return d.toLocaleString("hr-HR", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  })
}

// fallback prosjek ako ga nema iz backend-a
function izracunajProsjek(items) {
  if (!items.length) return 0
  const sum = items.reduce((a, b) => a + Number(b.ocjena || 0), 0)
  return sum / items.length
}
</script>
