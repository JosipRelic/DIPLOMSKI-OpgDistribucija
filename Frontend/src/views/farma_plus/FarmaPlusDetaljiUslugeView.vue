<template>
  <div class="mx-auto max-w-6xl space-y-6">
    <div class="rounded-2xl bg-white p-6 shadow-xl mt-10" :class="{ 'mb-15': !imaTerminaGlobal }">
      <div class="flex flex-wrap gap-4 justify-between">
        <div class="p-4">
          <nav class="text-sm text-gray-500 flex items-center space-x-2 mb-2">
            <span class="hover:underline cursor-pointer"
              ><router-link :to="{ name: 'farmaPlus' }">Farma+</router-link></span
            >
            <span>/</span>
            <span class="font-medium">{{ usluga?.naziv || "Usluga" }}</span>
          </nav>

          <div>
            <div
              class="flex items-center space-x-2 text-sm mt-3 font-medium"
              :class="usluga?.usluga_dostupna ? 'text-green-600' : 'text-red-500'"
            >
              <h1 class="text-3xl font-bold text-gray-900">
                {{ usluga?.naziv || "Usluga" }}
              </h1>
              <div class="flex pt-2 space-x-1">
                <svg
                  v-if="usluga?.usluga_dostupna"
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-5 h-5 ms-2"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M5 13l4 4L19 7"
                  />
                </svg>
                <svg
                  v-else
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-5 h-5 ms-2"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 18L18 6M6 6l12 12"
                  />
                </svg>
                <span>{{ usluga?.usluga_dostupna ? "Dostupno" : "Nedostupno" }}</span>
              </div>
            </div>
          </div>

          <p class="text-gray-600 font-normal text-base mt-2 mb-4 max-w-md">
            {{ usluga?.opis || "Opis usluge nije dostupan." }}
          </p>

          <div class="flex items-center mt-2 space-x-2 text-sm text-gray-600 mb-4">
            <router-link
              v-if="usluga?.opg_slug && usluga?.opg_naziv"
              class="hover:underline text-teal-500"
              :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: usluga.opg_slug } }"
            >
              {{ usluga.opg_naziv }}
            </router-link>
            <span v-if="usluga?.opg_naziv" class="text-gray-400">•</span>
            <span v-if="usluga?.grad || usluga?.zupanija">
              {{ [usluga?.grad, usluga?.zupanija].filter(Boolean).join(", ") }}
            </span>
          </div>

          <div class="text-2xl font-semibold text-gray-900">
            {{ cijenaLabel }}
            <span class="text-gray-400"> / {{ usluga?.mjerna_jedinica }}</span>

            <div class="flex items-center text-sm mb-4 mt-3">
              <span class="text-gray-600">Trajanje usluge: 1 {{ usluga?.mjerna_jedinica }} = </span>
              <input
                :value="trajanjeHHMM"
                type="time"
                step="60"
                class="px-2 py-1.5 rounded-xl text-orange-600"
                disabled
              />
            </div>

            <div>
              <div class="rounded-sm border border-gray-200 mt-2 w-fit shadow">
                <button
                  type="button"
                  class="size-10 leading-10 text-gray-600 transition hover:text-red-600"
                  @click="kolicina = Math.max(1, (kolicina || 1) - 1)"
                >
                  &minus;
                </button>

                <input
                  v-model.number="kolicina"
                  type="number"
                  min="1"
                  class="h-10 text-orange-600 w-16 border-transparent text-center [-moz-appearance:_textfield] sm:text-sm [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m=0 [&::-webkit-outer-spin-button]:appearance-none"
                />

                <button
                  type="button"
                  class="size-10 leading-10 text-gray-600 transition hover:text-green-600"
                  @click="kolicina = (kolicina || 1) + 1"
                >
                  &plus;
                </button>
              </div>
            </div>

            <div class="flex items-center mt-2">
              <div class="flex items-center text-lg">
                <span class="text-orange-600">Ukupno trajanje usluge:</span>
                <span class="px-3 py-1.5 rounded-xl text-orange-600">{{
                  ukupnoTrajanjeLabel
                }}</span>
              </div>
            </div>

            <div v-if="imaTerminaGlobal === false">
              <div
                class="rounded-xl text-sm border-s-4 max-w-xs border-amber-200 bg-amber-50 p-4 mb-2 mt-1 text-amber-700"
              >
                Ovaj OPG nema definiranih termina. Dogovor oko obavljanja usluge ostvarujete izravno
                s OPG-om nakon narudžbe.
              </div>
              <div class="pt-2">
                <button
                  class="px-3 py-2 text-md rounded-lg w-full text-base text-white bg-orange-600 hover:bg-orange-900 shadow-lg"
                  @click="dodajUsluguBezTermina"
                >
                  Dodaj u košaricu
                </button>
              </div>
            </div>
          </div>
        </div>

        <img
          :src="
            usluga?.slika_usluge ||
            'https://images.unsplash.com/photo-1483871788521-4f224a86e166?w=600&auto=format&fit=crop&q=60'
          "
          :alt="usluga?.naziv || 'Usluga'"
          class="rounded-md object-cover aspect-video"
        />
      </div>
    </div>

    <div v-if="imaTerminaGlobal === true" class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-10">
      <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
        <div class="flex items-center justify-between mb-4">
          <button
            class="p-2 rounded-xl font-bold text-orange-600 hover:text-orange-900"
            @click="pomakniMjesec(-1)"
          >
            &lt;
          </button>
          <div class="text-lg font-semibold text-orange-600">{{ naslovMjeseca }}</div>
          <button
            class="p-2 rounded-xl font-bold text-orange-600 hover:text-orange-900"
            @click="pomakniMjesec(1)"
          >
            &gt;
          </button>
        </div>

        <div class="grid grid-cols-7 text-center text-sm text-orange-600 mb-2 select-none">
          <div v-for="(d, i) in kratkiDani" :key="i" class="py-1">{{ d }}</div>
        </div>

        <div class="grid grid-cols-7 gap-2">
          <button
            v-for="dan in daniMreza"
            :key="dan.key"
            class="relative aspect-square rounded-xl flex items-center justify-center border border-white/5"
            :class="[
              dan.uMjesecu
                ? 'text-gray-600 font-semibold hover:text-white hover:bg-[#223c2f] shadow-sm'
                : 'bg-white text-gray-300',
              jednakiDatumi(dan.datum, odabraniDatum) && 'shadow-lg bg-[#223c2f] text-white',
              jeProsliDan(dan.datum) && 'opacity-30 cursor-not-allowed',
            ]"
            :disabled="!dan.uMjesecu || jeProsliDan(dan.datum)"
            @click="odaberiDatum(dan.datum)"
          >
            {{ dan.datum.getDate() }}

            <span
              v-if="tipZaDatum(dan.datum) === 'green'"
              class="absolute bottom-2 left-1/2 -translate-x-1/2 h-2 w-2 rounded-full bg-green-600"
            />
            <span
              v-else-if="tipZaDatum(dan.datum) === 'yellow'"
              class="absolute bottom-2 left-1/2 -translate-x-1/2 h-2 w-2 rounded-full bg-yellow-400"
            />
          </button>
        </div>

        <div class="flex gap-3 mt-4">
          <button
            class="px-3 py-1.5 rounded-xl text-orange-600 hover:text-orange-900"
            @click="idiDanas"
          >
            Danas
          </button>
          <button
            class="px-3 py-1.5 rounded-xl text-gray-600 hover:text-gray-900"
            @click="ocistiDatum"
          >
            Očisti
          </button>
        </div>
      </div>

      <div class="space-y-4">
        <div class="rounded-2xl bg-white p-6 shadow-xl">
          <div class="flex items-center justify-between mb-4">
            <div>
              <h2 class="text-xl text-orange-600">{{ naslovOdabranogDatuma }}</h2>
              <div class="text-teal-500">
                <template v-if="rasponiLabel">
                  <span class="font-medium">{{ rasponiLabel }}</span>
                </template>
                <span v-else class="text-gray-500">nema dostupnog raspona</span>
              </div>
            </div>
            <div class="text-gray-500">
              <div>
                • Ukupno potrebno:
                <span class="text-teal-500">{{ ukupnoTrajanjeLabel }}</span>
              </div>

              <template v-if="preostaloMinuta > 0">
                • Preostalo:
                <span class="text-red-500">{{ preostaloLabel }}</span>
              </template>
              <template v-else>
                • <span class="text-green-600 font-medium">pokriveno ✓</span>
              </template>
            </div>
          </div>

          <div v-if="!odabraniDatum" class="text-slate-400">Odaberite datum u kalendaru.</div>
          <div v-else-if="rasponiZaOdabrani.length === 0" class="text-slate-400">
            OPG nije raspoloživ za obavljanje usluga na odabrani datum.
          </div>
          <div v-else>
            <div v-if="preostaloMinuta === 0" class="text-green-600">
              Pokrili ste ukupno trajanje usluge.
            </div>

            <div
              v-else-if="tipOdabranogDana === 'green'"
              class="grid grid-cols-1 md:grid-cols-2 gap-3 border-t-1 border-gray-100 pt-2"
            >
              <div
                v-for="opt in prijedlozi"
                :key="opt.key"
                class="flex items-center justify-between rounded-xl shadow-xl text-gray-600 border-gray-100 bg-white px-4 py-3"
              >
                <div class="font-medium">
                  {{ formatHM(opt.startMin) }} - {{ formatHM(opt.endMin) }}
                </div>
                <button
                  class="px-3 py-1.5 rounded-lg text-white bg-teal-500 hover:bg-teal-800 shadow-lg disabled:opacity-40"
                  @click="dodajURezervaciju(opt)"
                  :disabled="preostaloMinuta === 0"
                >
                  Dodaj u rezervaciju
                </button>
              </div>
            </div>

            <div v-else-if="tipOdabranogDana === 'yellow'">
              <h3 class="text-lg font-semibold text-orange-600 border-t-1 border-gray-100 pt-3">
                Kombiniraj termine
              </h3>
              <p class="text-gray-500 mb-3">
                Ukupno trajanje usluge premašuje rasploživost OPG-a za odabrani datum, predlažemo
                kombinaciju termina ispod:
              </p>

              <div v-if="!kombinacijaMultiDan">
                <p class="text-red-400">
                  Nije moguće pokriti preostalih {{ preostaloLabel }} kombiniranjem od ovog datuma
                  jer nadalje više nemamo termina.
                </p>
              </div>

              <div v-else class="space-y-2">
                <div
                  v-for="(s, i) in kombinacijaMultiDan.stavke"
                  :key="i"
                  class="flex items-center justify-between rounded-xl bg-white shadow border border-gray-100 px-4 py-2"
                >
                  <div class="text-gray-600">
                    <div class="font-medium text-orange-600">{{ labelDatuma(s.dateKey) }}</div>
                    <div class="text-teal-500 text-sm">
                      {{ formatHM(s.startMin) }} - {{ formatHM(s.endMin) }}
                    </div>
                  </div>
                  <span class="text-gray-500 text-md font-semibold">{{
                    trajanjeLabel(s.endMin - s.startMin)
                  }}</span>
                </div>

                <button
                  class="mt-2 px-3 py-2 rounded-lg text-white bg-orange-600 hover:bg-orange-900 shadow-lg disabled:opacity-40"
                  @click="dodajKombinacijuMultiDan"
                  :disabled="!kombinacijaMultiDan || preostaloMinuta === 0"
                >
                  Dodaj kombinaciju u rezervaciju
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-orange-600">Rezervirat ćete:</h3>
            <button
              v-if="rezervacije.length"
              class="px-3 py-1.5 rounded-xl text-red-500"
              @click="isprazniRezervacije"
            >
              Isprazni
            </button>
          </div>

          <div v-if="!rezervacije.length" class="text-gray-400">
            Niste odabrali niti jedan termin.
          </div>

          <div v-else class="space-y-3">
            <div
              v-for="(stavka, idx) in rezervacije"
              :key="stavka.key"
              class="flex items-center justify-between rounded-xl bg-white shadow-lg border border-gray-100 px-4 py-3"
            >
              <div>
                <div class="font-medium text-orange-600">{{ stavka.title }}</div>
                <div class="text-teal-500 text-sm">
                  {{ stavka.dateLabel }} • {{ stavka.timeLabel }} • Količina {{ stavka.quantity }}
                </div>
              </div>
              <button
                class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                @click="rezervacije.splice(idx, 1)"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 2048 2048"
                  class="text-red-500"
                >
                  <path
                    fill="currentColor"
                    d="M1664 128h384v1792H0V128h384V0h128v128h1024V0h128v128zM384 256H128v256h1792V256h-256v128h-128V256H512v128H384V256zM128 1792h1792V640H128v1152zm1171-941l90 90l-274 275l274 275l-90 90l-275-275l-275 275l-90-90l274-275l-274-275l90-90l275 275l275-275z"
                  />
                </svg>
              </button>
            </div>

            <div class="pt-2">
              <button
                class="px-3 py-2 rounded-lg text-white bg-orange-600 hover:bg-orange-900 shadow-lg disabled:opacity-40"
                @click="dodajSveUKosaricu"
                :disabled="uslugaVecUKosarici || preostaloMinuta > 0 || !rezervacije.length"
              >
                {{
                  uslugaVecUKosarici
                    ? "Već imate odabran termin za ovu uslugu u košarici"
                    : preostaloMinuta > 0
                      ? `Dodajte još termina da biste pokrili preostalo vrijeme (${preostaloLabel})`
                      : "Dodaj u košaricu sve termine"
                }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, reactive, ref, onMounted, watch } from "vue"
import { useRoute, useRouter } from "vue-router"
import api from "@/services/api"
import { useRaspolozivostOpgStore } from "@/stores/raspolozivostOpg"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import { useKosaricaStore } from "@/stores/kosarica"
import { useUiStore } from "@/stores/ui"

const autentifikacija = useAutentifikacijskiStore()
const kosarica_s = useKosaricaStore()
const router = useRouter()
const ui = useUiStore()

const pad = (n) => String(n).padStart(2, "0")
const HM = (h, m) => `${pad(h)}:${pad(m)}`
const hm2min = (hm) => {
  const [h, m] = (hm || "00:00").split(":").map(Number)
  return (h || 0) * 60 + (m || 0)
}
const min2hm = (m) => HM(Math.floor(m / 60), m % 60)
const trajanjeLabel = (m) => `${Math.floor(m / 60)} h ${m % 60} min`
const localKey = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`
const jednakiDatumi = (a, b) =>
  a &&
  b &&
  a.getFullYear() === b.getFullYear() &&
  a.getMonth() === b.getMonth() &&
  a.getDate() === b.getDate()
const jeProsliDan = (d) => {
  const n = new Date()
  const A = new Date(d.getFullYear(), d.getMonth(), d.getDate())
  const B = new Date(n.getFullYear(), n.getMonth(), n.getDate())
  return A < B
}
const formatHM = (min) => min2hm(min)
const labelDatuma = (k) =>
  new Date(k + "T00:00:00").toLocaleDateString("hr-HR", {
    weekday: "long",
    day: "2-digit",
    month: "long",
    year: "numeric",
  })

const pocetakMjeseca = (d) => new Date(d.getFullYear(), d.getMonth(), 1)
const krajMjeseca = (d) => new Date(d.getFullYear(), d.getMonth() + 1, 0)
const dodajMjesece = (d, n) => new Date(d.getFullYear(), d.getMonth() + n, 1)

const fmtDanDug = new Intl.DateTimeFormat("hr-HR", {
  weekday: "long",
  day: "2-digit",
  month: "long",
  year: "numeric",
})
const fmtMjesec = new Intl.DateTimeFormat("hr-HR", { month: "long", year: "numeric" })
const kratkiDani = ["Pon", "Uto", "Sri", "Čet", "Pet", "Sub", "Ned"]

const ruta = useRoute()
const idUsluge = computed(() =>
  Number(
    String(ruta.params.uslugaSlugId || "")
      .split("-")
      .pop(),
  ),
)

const raspolozivost = useRaspolozivostOpgStore()

const usluga = ref(null)
const ucitavanje = ref(true)

const danas = new Date()
const prikazMjeseca = ref(pocetakMjeseca(danas))
const odabraniDatum = ref(danas)

const naslovMjeseca = computed(() =>
  fmtMjesec.format(prikazMjeseca.value).replace(/^./, (c) => c.toUpperCase()),
)
const naslovOdabranogDatuma = computed(() =>
  odabraniDatum.value ? fmtDanDug.format(odabraniDatum.value) : "Odaberite datum",
)

onMounted(async () => {
  try {
    usluga.value = history.state?.usluga || null
    if (!usluga.value && idUsluge.value) {
      try {
        const { data } = await api.get(`/farma-plus/usluga/${idUsluge.value}`)
        usluga.value = data
      } catch (e) {
        console.warn("Ne mogu dohvatiti detalje usluge s API-ja.", e?.response?.data || e)
      }
    }
  } finally {
    ucitavanje.value = false
  }
})

watch(
  [prikazMjeseca, () => usluga.value?.opg_id],
  async ([m, opgId]) => {
    if (!opgId || !m) return
    await raspolozivost.dohvatiKalendar({
      opg_id: opgId,
      godina: m.getFullYear(),
      mjesec: m.getMonth() + 1,
    })
  },
  { immediate: true },
)

const daniMreza = computed(() => {
  const start = pocetakMjeseca(prikazMjeseca.value)
  const end = krajMjeseca(prikazMjeseca.value)
  const startIdx = (start.getDay() + 6) % 7
  const dani = []
  for (let i = startIdx; i > 0; i--) {
    const d = new Date(start)
    d.setDate(d.getDate() - i)
    dani.push({ key: "p" + i + d.getTime(), datum: d, uMjesecu: false })
  }
  for (let i = 1; i <= end.getDate(); i++) {
    const d = new Date(start)
    d.setDate(i)
    dani.push({ key: "m" + i, datum: d, uMjesecu: true })
  }
  while (dani.length % 7 !== 0 || dani.length < 42) {
    const d = new Date(dani[dani.length - 1].datum)
    d.setDate(d.getDate() + 1)
    dani.push({ key: "n" + d.getTime(), datum: d, uMjesecu: false })
  }
  return dani
})
function odaberiDatum(d) {
  odabraniDatum.value = d
}
function pomakniMjesec(n) {
  prikazMjeseca.value = dodajMjesece(prikazMjeseca.value, n)
}
function idiDanas() {
  prikazMjeseca.value = pocetakMjeseca(danas)
  odabraniDatum.value = danas
}
function ocistiDatum() {
  odabraniDatum.value = null
}

const cijenaLabel = computed(() => `${Number(usluga.value?.cijena || 0).toFixed(2)} €`)
const trajanjeHHMM = computed(() => {
  const min = Number(usluga.value?.trajanje_po_mjernoj_jedinici || 0)
  return HM(Math.floor(min / 60), min % 60)
})
const kolicina = ref(1)
const ukupnoMinuta = computed(() =>
  Math.max(0, Number(usluga.value?.trajanje_po_mjernoj_jedinici || 0) * (kolicina.value || 0)),
)
const ukupnoTrajanjeLabel = computed(() => trajanjeLabel(ukupnoMinuta.value))

let rezervacije = reactive([])

const rezerviranoMinuta = computed(() =>
  rezervacije.reduce((s, r) => s + Math.max(0, r.endMin - r.startMin), 0),
)
const preostaloMinuta = computed(() => Math.max(0, ukupnoMinuta.value - rezerviranoMinuta.value))
const preostaloLabel = computed(() => trajanjeLabel(preostaloMinuta.value))

const KORAK_MIN = 30

function rawSlotoviZaKey(key) {
  const slots = (raspolozivost.kalendar && raspolozivost.kalendar[key]) || []
  return slots
    .map((s) => [hm2min(s.od), hm2min(s["do"])])
    .filter(([a, b]) => Number.isFinite(a) && Number.isFinite(b) && b > a)
    .sort((a, b) => a[0] - b[0])
}

function slobodniZaKey(key) {
  let segs = rawSlotoviZaKey(key)
  if (!segs.length) return []

  const todayKey = localKey(new Date())
  if (key === todayKey) {
    const now = new Date()
    const nowMin = now.getHours() * 60 + now.getMinutes()
    const cutFrom = Math.ceil(nowMin / KORAK_MIN) * KORAK_MIN
    segs = segs.map(([a, b]) => [Math.max(a, cutFrom), b])
  }

  const rez = rezervacije
    .filter((r) => r.dateKey === key)
    .map((r) => [r.startMin, r.endMin])
    .sort((a, b) => a[0] - b[0])

  for (const [rs, re] of rez) {
    const next = []
    for (const [a, b] of segs) {
      if (re <= a || rs >= b) {
        next.push([a, b])
        continue
      }
      if (rs > a) next.push([a, rs])
      if (re < b) next.push([re, b])
    }
    segs = next
    if (!segs.length) break
  }

  segs = segs.filter(([a, b]) => b - a >= KORAK_MIN)

  return segs
}

const rasponiZaOdabrani = computed(() => {
  if (!odabraniDatum.value) return []
  return raspolozivost.kalendar[localKey(odabraniDatum.value)] || []
})
const rasponiLabel = computed(() =>
  rasponiZaOdabrani.value.length
    ? rasponiZaOdabrani.value
        .map((s) => (s.naslov ? `${s.naslov} (${s.od} - ${s["do"]})` : `${s.od} - ${s["do"]}`))
        .join(", ")
    : null,
)

function tipZaKey(key, need) {
  if (need <= 0) return null
  const free = slobodniZaKey(key)
  if (!free.length) return null
  const maxLen = Math.max(...free.map(([a, b]) => b - a))
  return maxLen >= need ? "green" : "yellow"
}

function tipZaDatum(d) {
  return tipZaKey(localKey(d), preostaloMinuta.value)
}

const tipOdabranogDana = computed(() =>
  odabraniDatum.value ? tipZaDatum(odabraniDatum.value) : null,
)

const prijedlozi = computed(() => {
  const need = preostaloMinuta.value
  if (!odabraniDatum.value || need === 0) return []
  if (tipOdabranogDana.value !== "green") return []

  const key = localKey(odabraniDatum.value)
  const free = slobodniZaKey(key)
  const res = []
  for (const [a, b] of free) {
    if (b - a < need) continue
    for (let t = a; t <= b - need; t += KORAK_MIN) {
      res.push({ key: `${key}-${t}`, dateKey: key, startMin: t, endMin: t + need })
    }
  }
  return res
})

const kombinacijaMultiDan = computed(() => {
  if (!odabraniDatum.value || preostaloMinuta.value <= 0) return null
  let need = preostaloMinuta.value

  const startKey = localKey(odabraniDatum.value)
  const allKeys = Object.keys(raspolozivost.kalendar || {})
    .filter((k) => k >= startKey)
    .sort()

  const parts = []
  for (const key of allKeys) {
    if (need <= 0) break
    const free = slobodniZaKey(key)
    for (const [a, b] of free) {
      if (need <= 0) break
      const take = Math.min(b - a, need)
      if (take <= 0) continue
      parts.push({ dateKey: key, startMin: a, endMin: a + take })
      need -= take
    }
  }

  if (need > 0) return null
  return { stavke: parts }
})

function dodajURezervaciju(opt) {
  if (preostaloMinuta.value === 0) return
  rezervacije.push({
    key: opt.key + "-" + Math.random().toString(36).slice(2),
    title: usluga.value?.naziv || "Rezervacija",
    dateLabel: labelDatuma(opt.dateKey),
    timeLabel: `${formatHM(opt.startMin)} - ${formatHM(opt.endMin)}`,
    quantity: 1,
    dateKey: opt.dateKey,
    startMin: opt.startMin,
    endMin: opt.endMin,
  })
}

function dodajKombinacijuMultiDan() {
  if (!kombinacijaMultiDan.value || preostaloMinuta.value === 0) return
  for (const s of kombinacijaMultiDan.value.stavke) {
    rezervacije.push({
      key: `${s.dateKey}-${s.startMin}-${Math.random().toString(36).slice(2)}`,
      title: usluga.value?.naziv || "Rezervacija",
      dateLabel: labelDatuma(s.dateKey),
      timeLabel: `${formatHM(s.startMin)} - ${formatHM(s.endMin)}`,
      quantity: 1,
      dateKey: s.dateKey,
      startMin: s.startMin,
      endMin: s.endMin,
    })
  }
}

function isprazniRezervacije() {
  rezervacije.splice(0, rezervacije.length)
}

const imaTerminaGlobal = ref(null)

async function provjeriImaTerminaOPGa(opgId, horizon = 3) {
  if (!opgId) {
    imaTerminaGlobal.value = false
    return
  }
  const now = new Date()
  for (let i = 0; i < horizon; i++) {
    const d = new Date(now.getFullYear(), now.getMonth() + i, 1)
    try {
      const { data } = await api.get("/opg/raspolozivost/kalendar", {
        params: { opg_id: opgId, godina: d.getFullYear(), mjesec: d.getMonth() + 1 },
      })
      if (data?.slotovi && Object.keys(data.slotovi).length > 0) {
        imaTerminaGlobal.value = true
        return
      }
    } catch (e) {}
  }
  imaTerminaGlobal.value = false
}

function dtISO(dateKey, minute) {
  const [y, m, d] = dateKey.split("-").map(Number)
  const hh = String(Math.floor(minute / 60)).padStart(2, "0")
  const mm = String(minute % 60).padStart(2, "0")

  return `${y}-${String(m).padStart(2, "0")}-${String(d).padStart(2, "0")}T${hh}:${mm}:00`
}

async function dodajUsluguBezTermina() {
  if (!autentifikacija.korisnikAutentificiran) {
    ui.obavijest({
      tekst: "Za kupovinu je potrebna prijava",
      tip_obavijesti: "informacija",
    })
    return router.push({ name: "prijava", query: { redirect: ruta.fullPath } })
  }
  await kosarica_s.dodajUslugu({
    usluga_id: usluga.value.id,
    kolicina: Number(kolicina.value || 1),
  })
}

const uslugaVecUKosarici = computed(() =>
  kosarica_s.stavke.some((s) => s.usluga_id === usluga.value?.id),
)

async function dodajSveUKosaricu() {
  if (!autentifikacija.korisnikAutentificiran) {
    ui.obavijest({
      tekst: "Za kupovinu je potrebna prijava",
      tip_obavijesti: "informacija",
    })
    return router.push({ name: "prijava", query: { redirect: ruta.fullPath } })
  }
  if (preostaloMinuta.value > 0 || !rezervacije.length) return

  await kosarica_s.osvjezi()

  const jedanTerminPokrivaSve =
    rezervacije.length === 1 &&
    rezervacije[0].endMin - rezervacije[0].startMin >= ukupnoMinuta.value

  const vecImaUslugu = kosarica_s.stavke.some((s) => s.usluga_id === usluga.value?.id)
  if (vecImaUslugu) {
    return router.push({ name: "kosarica" })
  }

  for (const r of rezervacije) {
    const datum_od = dtISO(r.dateKey, r.startMin)
    const datum_do = dtISO(r.dateKey, r.endMin)
    await kosarica_s.dodajUsluguSTerminom({
      usluga_id: usluga.value.id,
      kolicina: jedanTerminPokrivaSve ? r.quantity || 1 : 1,
      termin_od: datum_od,
      termin_do: datum_do,
    })
  }

  await kosarica_s.osvjezi()
  router.push({ name: "kosarica" })
}

watch(
  () => usluga.value?.opg_id,
  (opgId) => {
    if (opgId) provjeriImaTerminaOPGa(opgId)
  },
  { immediate: true },
)
</script>

<style scoped>
button:focus-visible {
  outline: 2px solid rgba(56, 189, 248, 0.6);
  outline-offset: 2px;
}
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
