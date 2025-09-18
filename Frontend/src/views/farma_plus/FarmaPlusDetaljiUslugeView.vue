<template>
  <div class="min-h-screen text-slate-100 p-8">
    <div class="mx-auto max-w-6xl space-y-6">
      <div class="rounded-2xl bg-white p-6 shadow-xl ring-1">
        <div class="flex flex-wrap gap-4 justify-between">
          <div class="p-4">
            <nav class="text-sm text-gray-500 flex items-center space-x-2 mb-2">
              <span class="hover:underline cursor-pointer"><a href="#">Branje žita</a></span>
              <span>/</span>
              <span class="font-medium">Berba i žetva </span>
            </nav>
            <div>
              <div class="flex items-center space-x-2 text-sm mt-3 font-medium text-green-600">
                <h1 class="text-3xl font-bold text-gray-900">Branje žita</h1>
                <div class="flex pt-2 space-x-1">
                  <svg
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
                  <span>Dostupno</span>
                </div>
              </div>
            </div>

            <p class="text-gray-600 font-normal text-base mt-2 mb-4 max-w-md">
              Višegodišnje iskustvo branja žita u raznim uvjetima, brzo i efikasno.
            </p>
            <div class="flex items-center mt-2 space-x-2 text-sm text-gray-600 mb-4">
              <a href="#" class="hover:underline text-teal-500"> OPG Horvat </a>
              <span class="text-gray-400">•</span>
              <span>Novska, Sisačko-Moslavačka</span>
            </div>

            <div class="text-2xl font-semibold text-gray-900">
              100.00 €
              <span class="text-gray-400"> / ha</span>
              <div class="flex items-center text-sm mb-4">
                <span class="text-gray-600">Trajanje usluge: 1 ha = </span>
                <input
                  v-model="serviceLengthStr"
                  type="time"
                  step="60"
                  class="px-2 py-1.5 rounded-xl text-orange-600"
                />
              </div>
              <div>
                <div class="rounded-sm border border-gray-200 mt-2 w-fit shadow">
                  <button
                    type="button"
                    class="size-10 leading-10 text-gray-600 transition hover:text-red-600"
                    @click="quantity = Math.max(1, (quantity || 1) - 1)"
                  >
                    &minus;
                  </button>

                  <input
                    v-model.number="quantity"
                    type="number"
                    min="1"
                    class="h-10 text-orange-600 w-16 border-transparent text-center [-moz-appearance:_textfield] sm:text-sm [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"
                  />

                  <button
                    type="button"
                    class="size-10 leading-10 text-gray-600 transition hover:text-green-600"
                    @click="quantity = (quantity || 1) + 1"
                  >
                    &plus;
                  </button>
                </div>
              </div>

              <div class="flex items-center mt-2">
                <div class="flex items-center text-lg">
                  <span class="text-orange-600">Ukupno trajanje usluge:</span>
                  <span class="px-3 py-1.5 rounded-xl text-orange-600">{{
                    totalDurationLabel
                  }}</span>
                </div>
              </div>
            </div>
          </div>
          <img
            src="https://images.unsplash.com/photo-1483871788521-4f224a86e166?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGZhcm1pbmd8ZW58MHx8MHx8fDA%3D"
            alt=""
            class="rounded-md object-cover"
          />
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
          <div class="flex items-center justify-between mb-4">
            <button
              class="p-2 rounded-xl font-bold text-orange-600 hover:text-orange-900"
              @click="moveMonth(-1)"
            >
              <
            </button>
            <div class="text-lg font-semibold text-orange-600">{{ monthLabel }}</div>
            <button
              class="p-2 rounded-xl font-bold text-orange-600 hover:text-orange-900"
              @click="moveMonth(1)"
            >
              >
            </button>
          </div>

          <div class="grid grid-cols-7 text-center text-sm text-orange-600 mb-2 select-none">
            <div v-for="(d, i) in weekdayShort" :key="i" class="py-1">{{ d }}</div>
          </div>
          <div class="grid grid-cols-7 gap-2">
            <button
              v-for="day in daysGrid"
              :key="day.key"
              class="relative aspect-square rounded-xl flex items-center justify-center border border-white/5"
              :class="[
                day.inMonth
                  ? 'text-gray-600 font-semibold hover:text-white hover:bg-[#223c2f] shadow-sm'
                  : 'bg-white text-gray-300',
                isSameDate(day.date, selectedDate) && 'shadow-lg bg-[#223c2f] text-white',
                isPastDay(day.date) && 'opacity-30 cursor-not-allowed',
              ]"
              :disabled="!day.inMonth || isPastDay(day.date)"
              @click="selectDate(day.date)"
            >
              {{ day.date.getDate() }}

              <span
                v-if="day.inMonth && dayHasAvailability(day.date)"
                class="absolute bottom-2 left-1/2 -translate-x-1/2 h-2 w-2 rounded-full bg-green-600"
              ></span>
            </button>
          </div>

          <div class="flex gap-3 mt-4">
            <button class="px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10" @click="goToday">
              Today
            </button>
            <button class="px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10" @click="clearDate">
              Clear
            </button>
          </div>
        </div>

        <div class="space-y-4">
          <div class="rounded-2xl bg-white p-6 shadow-xl">
            <div class="flex items-center justify-between mb-4">
              <div>
                <h2 class="text-xl text-orange-600">{{ selectedDateTitle }}</h2>
                <div class="text-teal-500">
                  Raspoloživo:
                  <span v-if="rangeForSelected" class="font-medium">{{
                    rangeLabel(rangeForSelected)
                  }}</span>
                  <span v-else class="text-gray-500">nema dostupnog raspona</span>
                </div>
              </div>
              <div class="text-gray-500">
                Ukupno potrebno: <span class="text-orange-600"> {{ totalDurationLabel }}</span>
              </div>
            </div>

            <div v-if="!selectedDate" class="text-slate-400">Odaberite datum u kalendaru.</div>
            <div v-else-if="!rangeForSelected" class="text-slate-400">
              Za odabrani dan nema radnog vremena.
            </div>
            <div v-else>
              <div class="mb-3 text-gray-400" v-if="suggestions.length === 0">
                Nema dovoljno mjesta u odabranom rasponu za {{ totalDurationLabel }}.
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div
                  v-for="opt in suggestions"
                  :key="opt.key"
                  class="flex items-center justify-between rounded-xl shadow-xl text-gray-600 border-gray-100 bg-white px-4 py-3"
                >
                  <div class="font-medium">
                    {{ formatTime(opt.start) }} – {{ formatTime(opt.end) }}
                  </div>
                  <button
                    class="px-3 py-1.5 rounded-lg text-white bg-teal-500 hover:bg-teal-800 shadow-lg"
                    @click="addToReservation(opt)"
                  >
                    Dodaj u rezervaciju
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold text-orange-600">Rezervirat ćete:</h3>
              <button
                v-if="reservations.length"
                class="px-3 py-1.5 rounded-xl text-red-500"
                @click="reservations = []"
              >
                Isprazni
              </button>
            </div>
            <div v-if="!reservations.length" class="text-gray-400">
              Niste odabrali niti jedan termin.
            </div>
            <div v-else class="space-y-3">
              <div
                v-for="(item, idx) in reservations"
                :key="item.key"
                class="flex items-center justify-between rounded-xl bg-white shadow-lg border border-gray-100 px-4 py-3"
              >
                <div>
                  <div class="font-medium text-orange-600">{{ item.title }}</div>
                  <div class="text-teal-500 text-sm">
                    {{ item.dateLabel }} • {{ item.timeLabel }} • Količina {{ item.quantity }}
                  </div>
                </div>
                <button
                  class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                  @click="reservations.splice(idx, 1)"
                >
                  🗑️
                </button>
              </div>

              <div class="pt-2">
                <button
                  class="px-3 py-2 rounded-lg text-white bg-orange-600 hover:bg-orange-900 shadow-lg"
                  @click="addAllToBasket"
                >
                  Dodaj u košaricu sve termine
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, reactive, ref } from "vue"

const pad = (n) => String(n).padStart(2, "0")
const parseTimeToMinutes = (hhmm) => {
  const [h, m] = (hhmm || "00:00").split(":").map(Number)
  return (h || 0) * 60 + (m || 0)
}
const minutesToHM = (min) => `${Math.floor(min / 60)} h ${min % 60} min`
const cloneDate = (d) => new Date(d.getTime())
const setHM = (d, hm) => {
  const [h, m] = hm.split(":").map(Number)
  const x = cloneDate(d)
  x.setHours(h || 0, m || 0, 0, 0)
  return x
}
const addMinutes = (d, m) => {
  const x = cloneDate(d)
  x.setMinutes(x.getMinutes() + m)
  return x
}

const isSameDate = (a, b) =>
  a &&
  b &&
  a.getFullYear() === b.getFullYear() &&
  a.getMonth() === b.getMonth() &&
  a.getDate() === b.getDate()
const isPastDay = (d) => {
  const now = new Date()
  const x = new Date(d.getFullYear(), d.getMonth(), d.getDate())
  const n = new Date(now.getFullYear(), now.getMonth(), now.getDate())
  return x < n
}

const weekdayShort = ["Pon", "Uto", "Sri", "Čet", "Pet", "Sub", "Ned"]
const weekdayLongFmt = new Intl.DateTimeFormat("hr-HR", {
  weekday: "long",
  day: "2-digit",
  month: "long",
  year: "numeric",
})
const monthFmt = new Intl.DateTimeFormat("hr-HR", { month: "long", year: "numeric" })

const today = new Date()
const viewMonth = ref(new Date(today.getFullYear(), today.getMonth(), 1))
const selectedDate = ref(today)

const startOfMonth = (d) => new Date(d.getFullYear(), d.getMonth(), 1)
const endOfMonth = (d) => new Date(d.getFullYear(), d.getMonth() + 1, 0)
const addMonths = (d, n) => new Date(d.getFullYear(), d.getMonth() + n, 1)

const monthLabel = computed(() =>
  monthFmt.format(viewMonth.value).replace(/^./, (c) => c.toUpperCase()),
)

const daysGrid = computed(() => {
  const start = startOfMonth(viewMonth.value)
  const end = endOfMonth(viewMonth.value)
  const startIdx = (start.getDay() + 6) % 7
  const days = []
  for (let i = startIdx; i > 0; i--) {
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
    const d = new Date(days[days.length - 1].date)
    d.setDate(d.getDate() + 1)
    days.push({ key: "n" + d.getTime(), date: d, inMonth: false })
  }
  return days
})

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
function clearDate() {
  selectedDate.value = null
}

const weeklyAvailability = {
  0: { start: "10:00", end: "17:00" },
  1: { start: "10:00", end: "17:00" },
  2: { start: "10:00", end: "17:00" },
  3: { start: "10:00", end: "17:00" },
  4: { start: "10:00", end: "17:00" },
  5: { start: "10:00", end: "14:00" },
  6: null,
}

const dayHasAvailability = (date) => {
  const idx = (date.getDay() + 6) % 7
  return !!weeklyAvailability[idx]
}

const rangeForSelected = computed(() => {
  if (!selectedDate.value) return null
  const idx = (selectedDate.value.getDay() + 6) % 7
  return weeklyAvailability[idx] || null
})

const rangeLabel = (r) => `${r.start} – ${r.end}`
const selectedDateTitle = computed(() =>
  selectedDate.value ? weekdayLongFmt.format(selectedDate.value) : "Odaberite datum",
)

const serviceLengthStr = ref("01:30")
const quantity = ref(1)

const perUnitMinutes = computed(() => parseTimeToMinutes(serviceLengthStr.value))
const totalMinutes = computed(() => Math.max(0, perUnitMinutes.value * (quantity.value || 0)))
const totalDurationLabel = computed(() => minutesToHM(totalMinutes.value))

const STEP = 30

const suggestions = computed(() => {
  const out = []
  if (!selectedDate.value || !rangeForSelected.value) return out
  if (totalMinutes.value === 0) return out

  const r = rangeForSelected.value
  const start = setHM(selectedDate.value, r.start)
  const end = setHM(selectedDate.value, r.end)

  const latestStart = addMinutes(end, -totalMinutes.value)
  if (latestStart < start) return out

  const now = new Date()
  let iter = cloneDate(start)
  const firstStart = isSameDate(iter, now)
    ? new Date(
        Math.max(
          iter,
          new Date(
            now.getFullYear(),
            now.getMonth(),
            now.getDate(),
            now.getHours(),
            Math.ceil(now.getMinutes() / STEP) * STEP,
          ),
        ),
      )
    : iter

  for (let t = firstStart; t <= latestStart; t = addMinutes(t, STEP)) {
    const e = addMinutes(t, totalMinutes.value)
    out.push({ key: t.getTime() + "", start: t, end: e })
  }
  return out
})

let reservations = reactive([])
let basket = reactive([])

function addToReservation(opt) {
  reservations.push({
    key: opt.key + "-" + Math.random().toString(36).slice(2),
    title: "Rezervacija",
    dateLabel: weekdayLongFmt.format(opt.start),
    timeLabel: `${formatTime(opt.start)} – ${formatTime(opt.end)}`,
    quantity: quantity.value,
    startISO: opt.start.toISOString(),
    endISO: opt.end.toISOString(),
  })
}

function addAllToBasket() {
  basket.push(
    ...reservations.map((r) => ({
      ...r,
      basketKey: r.key + "-b",
    })),
  )
}

function formatTime(d) {
  return `${pad(d.getHours())}:${pad(d.getMinutes())}`
}
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
