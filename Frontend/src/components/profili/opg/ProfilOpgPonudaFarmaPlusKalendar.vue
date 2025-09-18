<template>
  <div class="text-slate-100 p-8">
    <div class="mx-auto max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-8">
      <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-semibold text-orange-600">{{ monthLabel }}</h2>
          <div class="flex items-center gap-2">
            <button
              class="px-3 py-1.5 rounded-xl text-orange-600 hover:text-gray-900"
              @click="goToday"
            >
              Danas
            </button>
            <button
              class="p-2 rounded-xl text-orange-600 hover:text-gray-900"
              @click="moveMonth(-1)"
              aria-label="Prethodni mjesec"
            >
              <
            </button>
            <button
              class="p-2 rounded-xl text-orange-600 hover:text-gray-900"
              @click="moveMonth(1)"
              aria-label="Sljedeći mjesec"
            >
              >
            </button>
          </div>
        </div>

        <div class="grid grid-cols-7 text-center text-sm text-orange-600 mb-2 select-none">
          <div v-for="(d, i) in weekdayShort" :key="i" class="py-2">{{ d }}</div>
        </div>

        <div class="grid grid-cols-7 gap-2">
          <button
            v-for="day in daysGrid"
            :key="day.key"
            class="relative aspect-square rounded-2xl transition-colors flex items-center justify-center"
            :class="[
              day.inMonth
                ? 'text-gray-600 hover:text-white hover:bg-[#223c2f]'
                : 'bg-white text-gray-300',
              isSameDate(day.date, selectedDate) && 'shadow-lg bg-[#223c2f] text-white',
            ]"
            @click="onDayClick(day.date)"
            :disabled="!day.inMonth"
          >
            <span class="text-base font-medium">
              {{ day.date.getDate().toString().padStart(2, "0") }}
            </span>

            <span
              v-if="eventsByDate[isoDate(day.date)]?.length"
              class="absolute bottom-2 left-1/2 -translate-x-1/2 h-2 w-2 rounded-full"
              :style="{ background: eventsByDate[isoDate(day.date)][0].dotColor }"
            />
          </button>
        </div>
      </div>

      <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
        <div
          class="flex flex-row max-sm:flex-col md:flex-row lg:flex-col xl:flex-row items-center justify-between mb-6"
        >
          <div>
            <h2 class="text-3xl text-orange-600 font-semibold">Raspored</h2>
            <p class="text-gray-400 max-sm:mb-2">{{ monthLabel }}</p>
          </div>
          <div class="flex gap-2">
            <button
              class="px-3 py-2 rounded-xl bg-orange-600 hover:bg-orange-900"
              @click="openWeekForm"
            >
              <span class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  class="me-1"
                >
                  <path
                    fill="#ffffff"
                    d="M18 20v-3h-3v-2h3v-3h2v3h3v2h-3v3h-2ZM3 21q-.825 0-1.413-.588T1 19V5q0-.825.588-1.413T3 3h14q.825 0 1.413.588T19 5v5h-2V8H3v11h13v2H3Z"
                  />
                </svg>
                Tjedni raspored
              </span>
            </button>
            <button
              class="px-3 py-2 rounded-xl bg-orange-600 hover:bg-orange-900"
              @click="openDateForm"
            >
              <span class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  class="me-1"
                >
                  <path
                    fill="#ffffff"
                    d="M18 20v-3h-3v-2h3v-3h2v3h3v2h-3v3h-2ZM3 21q-.825 0-1.413-.588T1 19V5q0-.825.588-1.413T3 3h14q.825 0 1.413.588T19 5v5h-2V8H3v11h13v2H3Z"
                  />
                </svg>
                Dnevni raspored
              </span>
            </button>
          </div>
        </div>

        <div class="space-y-4 mb-6">
          <div
            v-if="mode === 'week'"
            class="rounded-2xl bg-white text-gray-600 shadow shadow-lg p-4"
          >
            <div class="flex items-center justify-between mb-3">
              <h3 class="text-lg font-semibold">Ovaj tjedan ({{ weekRangeLabel }})</h3>
              <div class="flex gap-2">
                <button
                  class="px-3 py-1.5 rounded-xl bg-teal-500 hover:bg-teal-800 shadow-lg text-white"
                  @click="applyWeek"
                >
                  Spremi
                </button>
                <button
                  class="px-3 py-1.5 rounded-xl bg-red-700 hover:bg-red-900 shadow-lg text-white"
                  @click="cancelForms"
                >
                  Odustani
                </button>
              </div>
            </div>

            <div class="mt-4 text-sm text-gray-500 flex items-center gap-2">
              <span v-if="!titleEdit" class="italic">Naslov: {{ titleText }}</span>
              <input
                v-else
                type="text"
                v-model="titleText"
                class="px-3 py-1.5 rounded-xl bg-gray-100 shadow-sm text-gray-900 border border-gray-200 mb-2 w-full max-w-md"
              />
              <button
                class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                @click="toggleTitleEdit"
                :title="titleEdit ? 'Spremi naslov' : 'Uredi naslov'"
              >
                <span v-if="titleEdit"> SPREMI </span>
                <span v-else>✏️</span>
              </button>
            </div>
            <div class="divide-y divide-orange-200">
              <div
                v-for="row in weekRows"
                :key="row.key"
                class="flex items-center gap-4 py-3 max-sm:gap-2 lg:gap-2 xl:gap-4"
              >
                <label class="flex items-center gap-2 w-28 max-sm:w-12 lg:w-14 xl:w-28">
                  <input type="checkbox" v-model="row.enabled" class="accent-sky-500 h-4 w-4" />
                  <span class="w-16">{{ row.label }}</span>
                </label>
                <input
                  type="time"
                  v-model="row.from"
                  class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
                />
                <input
                  type="time"
                  v-model="row.to"
                  class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
                />
              </div>
            </div>
          </div>

          <div
            v-if="mode === 'date'"
            class="rounded-2xl shadow-lg text-gray-600 bg-white shadow-lg p-4"
          >
            <div v-if="!pendingDate">
              <p>Odaberite željeni datum u kalendaru.</p>
            </div>
            <div v-else>
              <div class="flex items-center justify-between mb-3">
                <h3 class="text-lg font-semibold">Datum: {{ formatFull(pendingDate) }}</h3>
                <div class="flex gap-2">
                  <button
                    class="px-3 py-1.5 rounded-xl bg-teal-500 hover:bg-teal-800 shadow-lg text-white"
                    @click="applySingleDate"
                  >
                    Spremi
                  </button>
                  <button
                    class="px-3 py-1.5 rounded-xl bg-red-700 hover:bg-red-900 shadow-lg text-white"
                    @click="cancelForms"
                  >
                    Odustani
                  </button>
                </div>
              </div>
              <div class="mt-4 text-sm text-gray-500 flex items-center gap-2">
                <span v-if="!titleEdit" class="italic">Naslov: {{ titleText }}</span>
                <input
                  v-else
                  type="text"
                  v-model="titleText"
                  class="px-3 py-1.5 rounded-xl bg-gray-100 shadow-sm text-gray-900 border border-gray-200 mb-2 w-full max-w-md"
                />
                <button
                  class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                  @click="toggleTitleEdit"
                  :title="titleEdit ? 'Spremi naslov' : 'Uredi naslov'"
                >
                  <span v-if="titleEdit"> SPREMI </span>
                  <span v-else>✏️</span>
                </button>
              </div>
              <div class="flex items-center gap-4">
                <input
                  type="time"
                  v-model="single.from"
                  class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
                />
                <input
                  type="time"
                  v-model="single.to"
                  class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="space-y-4">
          <div v-for="item in monthEvents" :key="item.id" class="flex gap-4 items-stretch">
            <div class="w-20 shrink-0 rounded-2xl bg-white shadow-lg text-center py-3">
              <div class="text-3xl font-bold text-[#223c2f] leading-none">
                {{ dayNum(item.date) }}
              </div>
              <div class="text-orange-600">{{ monthShort(item.date) }}</div>
            </div>

            <div class="flex-1 rounded-2xl shadow-lg bg-white px-5 py-4">
              <div class="flex items-center gap-2 mb-1">
                <span
                  class="inline-block h-3 w-3 rounded-full"
                  :style="{ background: item.dotColor }"
                />
                <h3 class="text-lg font-medium text-gray-600 flex-1">{{ item.title }}</h3>
                <button
                  @click="removeEvent(item.id)"
                  class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                  title="Obriši događaj"
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
              <p class="text-gray-400">
                {{ timeRange(item) }}, {{ weekdayLong(item.date) }}, {{ formatDate(item.date) }}
              </p>
            </div>
          </div>

          <p v-if="!monthEvents.length" class="text-slate-400">Nema događaja u ovom mjesecu.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, reactive, ref } from "vue"
import { useUiStore } from "@/stores/ui"

const ui = useUiStore()
const isoDate = (d) => d.toISOString().slice(0, 10)
const startOfMonth = (d) => new Date(d.getFullYear(), d.getMonth(), 1)
const endOfMonth = (d) => new Date(d.getFullYear(), d.getMonth() + 1, 0)
const addMonths = (d, n) => new Date(d.getFullYear(), d.getMonth() + n, 1)
const isSameDate = (a, b) =>
  a &&
  b &&
  a.getFullYear() === b.getFullYear() &&
  a.getMonth() === b.getMonth() &&
  a.getDate() === b.getDate()
const getMonday = (d) => {
  const dd = new Date(d)
  const day = (dd.getDay() + 6) % 7
  dd.setDate(dd.getDate() - day)
  dd.setHours(0, 0, 0, 0)
  return dd
}
const addDays = (d, n) => {
  const x = new Date(d)
  x.setDate(x.getDate() + n)
  return x
}

const combineDateTime = (date, hhmm) => {
  const [h, m] = (hhmm || "00:00").split(":").map(Number)
  const d = new Date(date)
  d.setHours(h ?? 0, m ?? 0, 0, 0)
  return d
}
const isInPast = (date, hhmm) => combineDateTime(date, hhmm) < new Date()

const hrFmt = new Intl.DateTimeFormat("hr-HR", { month: "long", year: "numeric" })
const hrMonthShort = new Intl.DateTimeFormat("hr-HR", { month: "short" })
const hrWeekdayLong = new Intl.DateTimeFormat("hr-HR", { weekday: "long" })

const weekdayShort = ["Pon", "Uto", "Sri", "Čet", "Pet", "Sub", "Ned"]

const today = new Date()
const viewMonth = ref(startOfMonth(today))
const selectedDate = ref(today)

const titleEdit = ref(false)
const titleText = ref("Slobodni za obavljanje usluga")
const toggleTitleEdit = () => (titleEdit.value = !titleEdit.value)

const mode = ref("none")
const pendingDate = ref(null)
const single = reactive({ from: "00:00", to: "00:00" })

const weekRows = reactive([
  { key: "mon", label: "Pon", offset: 0, enabled: true, from: "00:00", to: "00:00" },
  { key: "tue", label: "Uto", offset: 1, enabled: false, from: "00:00", to: "00:00" },
  { key: "wed", label: "Sri", offset: 2, enabled: true, from: "00:00", to: "00:00" },
  { key: "thu", label: "Čet", offset: 3, enabled: false, from: "00:00", to: "00:00" },
  { key: "fri", label: "Pet", offset: 4, enabled: false, from: "00:00", to: "00:00" },
  { key: "sat", label: "Sub", offset: 5, enabled: false, from: "00:00", to: "00:00" },
  { key: "sun", label: "Ned", offset: 6, enabled: false, from: "00:00", to: "00:00" },
])

const events = reactive([
  {
    id: "e1",
    date: new Date("2024-02-09"),
    title: "6209 Nikolaus Club, Tayaland 92911-1095",
    from: "09:00",
    to: "12:00",
    dotColor: "#7fbf24",
  },
  {
    id: "e2",
    date: new Date("2024-02-14"),
    title: "6209 Nikolaus Club, Tayaland 92911-1095",
    from: "09:00",
    to: "12:00",
    dotColor: "#0ea5b7",
  },
  {
    id: "e3",
    date: new Date("2024-02-19"),
    title: "6209 Nikolaus Club, Tayaland 92911-1095",
    from: "09:00",
    to: "12:00",
    dotColor: "#1f9dd1",
  },
  {
    id: "e4",
    date: new Date("2024-02-29"),
    title: "6209 Nikolaus Club, Tayaland 92911-1095",
    from: "09:00",
    to: "12:00",
    dotColor: "#7c3aed",
  },
])

const eventsByDate = computed(() => {
  const map = {}
  for (const e of events) {
    const key = isoDate(e.date)
    ;(map[key] ||= []).push(e)
  }
  return map
})

const monthLabel = computed(() =>
  hrFmt.format(viewMonth.value).replace(/^./, (c) => c.toUpperCase()),
)

const daysGrid = computed(() => {
  const start = startOfMonth(viewMonth.value)
  const end = endOfMonth(viewMonth.value)

  const startWeekdayMonFirst = (start.getDay() + 6) % 7
  const days = []

  for (let i = startWeekdayMonFirst - 0; i > 0; i--) {
    const d = new Date(start)
    d.setDate(d.getDate() - i)
    days.push({ key: "p" + i + d.getTime(), date: d, inMonth: false })
  }

  for (let i = 1; i <= end.getDate(); i++) {
    const d = new Date(start)
    d.setDate(i)
    days.push({ key: "m" + i, date: d, inMonth: true })
  }

  while (days.length % 7 !== 0 || days.length < 42) {
    const last = days[days.length - 1].date
    const d = new Date(last)
    d.setDate(d.getDate() + 1)
    days.push({ key: "n" + d.getTime(), date: d, inMonth: false })
  }

  return days
})

const monthEvents = computed(() =>
  events
    .filter(
      (e) =>
        e.date.getFullYear() === viewMonth.value.getFullYear() &&
        e.date.getMonth() === viewMonth.value.getMonth(),
    )
    .sort((a, b) => a.date - b.date),
)

function selectDate(d) {
  selectedDate.value = d
}
function moveMonth(n) {
  viewMonth.value = addMonths(viewMonth.value, n)
}
function goToday() {
  viewMonth.value = startOfMonth(today)
  selectedDate.value = today
}

function onDayClick(d) {
  selectDate(d)
  if (mode.value === "date") {
    pendingDate.value = d
  }
}

function openWeekForm() {
  mode.value = "week"
  pendingDate.value = null
}
function openDateForm() {
  mode.value = "date"
  pendingDate.value = null
}
function cancelForms() {
  mode.value = "none"
  pendingDate.value = null
  titleEdit.value = false
}

const weekRangeLabel = computed(() => {
  const base = getMonday(selectedDate.value || today)
  const sun = addDays(base, 6)
  const fmt = (d) => d.toLocaleDateString("hr-HR", { day: "2-digit", month: "2-digit" })
  return `${fmt(base)} – ${fmt(sun)}`
})

function applyWeek() {
  const base = getMonday(selectedDate.value || today)
  const blocked = []

  for (const row of weekRows) {
    if (!row.enabled) continue
    const d = addDays(base, row.offset)
    const ok = addEvent({ date: d, from: row.from, to: row.to, title: titleText.value })
    if (!ok) blocked.push(row.label)
  }

  if (blocked.length) {
    ui.obavijest({
      tekst: `Nije moguće dodati termine u prošlosti: ${blocked.join(", ")}`,
      tip_obavijesti: "greska",
    })
  }
  if (!blocked.length)
    ui.obavijest({ tekst: "Uspješno ste dodali termine", tip_obavijesti: "uspjeh" })
  cancelForms()
}

function applySingleDate() {
  if (!pendingDate.value) return
  const ok = addEvent({
    date: pendingDate.value,
    from: single.from,
    to: single.to,
    title: titleText.value,
  })
  if (!ok) {
    ui.obavijest({ tekst: "Odabrani datum ili vrijeme su u prošlosti", tip_obavijesti: "greska" })
    return
  }
  if (ok) {
    if (ok) ui.obavijest({ tekst: "Uspješno ste dodali termin", tip_obavijesti: "uspjeh" })
  }
  cancelForms()
}

function addEvent({ date, from, to, title }) {
  if (isInPast(date, from)) return false

  const id = "e" + Math.random().toString(36).slice(2)
  events.push({ id, date: new Date(date), title, from, to, dotColor: "#22c55e" })
  return true
}

async function removeEvent(id) {
  const potvrda = await ui.obavijestSaPotvrdom({
    naslov: "Obrisati termin?",
    poruka: `Termin će biti trajno uklonjen.`,
    tip_obavijesti: "upozorenje",
    potvrdiRadnju: "Obriši",
    odustaniOdRadnje: "Odustani",
  })
  if (!potvrda) return
  const idx = events.findIndex((e) => e.id === id)
  if (idx !== -1) events.splice(idx, 1)
}

const dayNum = (d) => String(d.getDate()).padStart(2, "0")
const monthShort = (d) => hrMonthShort.format(d)
const weekdayLong = (d) => hrWeekdayLong.format(d)
const formatDate = (d) => d.toLocaleDateString("hr-HR", { day: "2-digit", month: "long" })
const formatFull = (d) =>
  d.toLocaleDateString("hr-HR", { day: "2-digit", month: "long", year: "numeric" })
const timeRange = (e) => `${e.from} – ${e.to}`
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
