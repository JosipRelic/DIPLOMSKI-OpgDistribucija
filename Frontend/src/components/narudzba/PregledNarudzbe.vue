<template>
  <div
    class="max-w-6xl mx-auto bg-white shadow-xl rounded-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2 my-20"
  >
    <div class="p-8">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="100"
        height="100"
        viewBox="0 0 32 32"
        class="mx-auto"
      >
        <path
          class="fill-orange-600"
          d="M29.755 21.345A1 1 0 0 0 29 21h-2v-2c0-1.102-.897-2-2-2h-4c-1.103 0-2 .898-2 2v2h-2a1.001 1.001 0 0 0-.99 1.142l1 7A1 1 0 0 0 18 30h10a1 1 0 0 0 .99-.858l1-7a1.001 1.001 0 0 0-.235-.797M21 19h4v2h-4zm6.133 9h-8.266l-.714-5h9.694zM10 20h2v10h-2z"
        />
        <path
          class="fill-gray-900"
          d="m16.78 17.875l-1.906-2.384l-1.442-3.605A2.986 2.986 0 0 0 10.646 10H5c-1.654 0-3 1.346-3 3v7c0 1.103.897 2 2 2h1v8h2V20H4v-7a1 1 0 0 1 1-1h5.646c.411 0 .776.247.928.629l1.645 3.996l2 2.5zM4 5c0-2.206 1.794-4 4-4s4 1.794 4 4s-1.794 4-4 4s-4-1.794-4-4m2 0c0 1.103.897 2 2 2s2-.897 2-2s-.897-2-2-2s-2 .897-2 2"
        />
      </svg>

      <h2 class="text-2xl xl:text-3xl font-extrabold text-gray-800 mb-6 flex flex-col items-center">
        Podaci za dostavu
      </h2>

      <div class="flex flex-col items-center">
        <button
          class="w-full max-w-xs font-bold shadow-sm hover:bg-red-400 rounded-lg py-3 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
          type="button"
        >
          <div class="bg-white p-2 rounded-full">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-6 text-red-600">
              <path
                fill="currentColor"
                d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
              />
            </svg>
          </div>
          <span class="ml-4"> Ispunite glasovno pomoću AI </span>
        </button>
        <small class="pt-2 w-full max-w-xs text-xs">
          Pritisnite gumb i popunite obrazac glasom npr. "Zovem se Ivan Horvat. Moja email adresa je
          ..."
        </small>
      </div>

      <div class="my-8 border-b text-center">
        <div
          class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
        >
          ili unesite podatke ručno
        </div>
      </div>

      <form class="space-y-5" @submit.prevent>
        <div class="flex gap-4">
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Ime</label>
            <input
              v-model="forma.ime"
              type="text"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Prezime</label>
            <input
              v-model="forma.prezime"
              type="text"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
        </div>

        <div>
          <label class="block mb-1 text-sm text-gray-600">Email</label>
          <input
            v-model="forma.email"
            type="email"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>

        <div>
          <label class="block mb-1 text-sm text-gray-600">Broj telefona</label>
          <input
            v-model="forma.telefon"
            type="text"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>

        <div>
          <label class="block mb-1 text-sm text-gray-600">Adresa</label>
          <input
            v-model="forma.adresa"
            type="text"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>

        <div>
          <label class="block mb-1 text-sm text-gray-600">Država</label>
          <input
            v-model="forma.drzava"
            type="text"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>

        <div>
          <label class="block mb-1 text-sm text-gray-600">Županija</label>
          <input
            v-model="forma.zupanija"
            type="text"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
          />
        </div>

        <div class="flex gap-4">
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Grad</label>
            <input
              v-model="forma.grad"
              type="text"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
          <div class="w-1/2">
            <label class="block mb-1 text-sm text-gray-600">Poštanski broj</label>
            <input
              v-model="forma.postanski_broj"
              type="text"
              class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            />
          </div>
        </div>
      </form>

      <div class="mt-4 border-b text-center">
        <div
          class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
        >
          ili učitajte podatke s vašeg profila
        </div>
      </div>
      <button
        type="button"
        class="flex items-center border p-2 mt-4 rounded-lg mx-auto border-gray-200 shadow-md hover:text-teal-500 hover:border-teal-500"
        @click="ucitajIzProfila"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24">
          <defs>
            <mask id="letsIconsLoadCircleDuotoneLine0">
              <g fill="none">
                <circle
                  cx="5"
                  cy="5"
                  r="5"
                  fill="#fff"
                  fill-opacity=".25"
                  transform="matrix(0 -1 -1 0 17 20)"
                />
                <circle
                  cx="5"
                  cy="5"
                  r="5.3"
                  stroke="silver"
                  stroke-opacity=".25"
                  stroke-width=".6"
                  transform="matrix(0 -1 -1 0 17 20)"
                />
                <path stroke="#fff" stroke-width="1.2" d="M5.239 14.812a7 7 0 0 0 13.523 0" />
                <path
                  fill="#fff"
                  d="m12 13l-.375.469l.375.3l.375-.3zm.6-9a.6.6 0 1 0-1.2 0zM6.625 9.469l5 4l.75-.937l-5-4zm5.75 4l5-4l-.75-.938l-5 4zM12.6 13V4h-1.2v9z"
                />
              </g>
            </mask>
          </defs>
          <path
            fill="currentColor"
            d="M0 0h24v24H0z"
            mask="url(#letsIconsLoadCircleDuotoneLine0)"
          />
        </svg>
        Učitaj podatke
      </button>
    </div>

    <div class="bg-gray-50 p-8 border-l border-gray-200">
      <h3 class="text-xl font-semibold text-gray-700 mb-2">Naručit ćete</h3>

      <div class="mb-1 text-orange-400 border-b border-orange-200 mb-2">Proizvodi</div>
      <ul class="space-y-4 mb-4">
        <li v-for="p in proizvodi" :key="p.kljuc" class="flex items-center gap-4">
          <img :src="p.slika || defaultProizvod" alt="" class="size-20 rounded-sm object-cover" />
          <div>
            <h3 class="text-lg text-gray-900">{{ p.naziv }}</h3>
            <dl class="mt-0.5 space-y-px text-sm text-gray-600">
              <div>
                <dt class="inline">Cijena:</dt>
                <dd class="inline ml-1 font-bold">{{ formatCijena(p.cijena) }}</dd>
              </div>
              <div>
                <dt class="inline">Količina:</dt>
                <dd class="inline ml-1 font-bold">{{ p.kolicina }} / {{ p.mjerna_jedinica }}</dd>
              </div>
            </dl>
          </div>
        </li>
        <li v-if="!proizvodi.length" class="text-sm text-gray-400">Nema proizvoda.</li>
      </ul>

      <div class="text-orange-400 border-b border-orange-200 mb-2">Usluge</div>
      <ul class="space-y-4 mb-4">
        <li v-for="u in usluge" :key="u.kljuc" class="flex items-center gap-4">
          <img :src="u.slika || defaultUsluga" alt="" class="size-20 rounded-sm object-cover" />
          <div>
            <h3 class="text-lg text-gray-900">{{ u.naziv }}</h3>
            <dl class="mt-0.5 space-y-px text-sm text-gray-600">
              <div class="text-xs">
                <dt class="inline">Cijena:</dt>
                <dd class="inline ml-1 font-bold">{{ formatCijena(u.cijena) }}</dd>
              </div>
              <div class="text-xs">
                <dt class="inline">Količina:</dt>
                <dd class="inline ml-1 font-bold">{{ u.kolicina }} / {{ u.mjerna_jedinica }}</dd>
              </div>
              <div class="text-xs" v-if="u.termin_od && u.termin_do">
                <dt class="inline">Termin:</dt>
                <dd class="inline ml-1 font-bold">
                  {{ fmtHR(u.termin_od) }} → {{ fmtHR(u.termin_do) }}
                </dd>
              </div>
            </dl>
          </div>
        </li>
        <li v-if="!usluge.length" class="text-sm text-gray-400">Nema usluga.</li>
      </ul>

      <h3 class="text-xl font-semibold text-gray-700 mb-6 mt-10 border-t pt-6">
        Odaberite način plaćanja
      </h3>
      <div class="space-y-4">
        <button
          type="button"
          class="flex items-center w-full text-left p-4 bg-white rounded-lg shadow-sm border border-gray-300 hover:shadow-md transition"
          :class="nacinPlacanja === 'pouzece' ? 'ring-2 ring-teal-500' : ''"
          @click="nacinPlacanja = 'pouzece'"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            viewBox="0 0 48 48"
            class="mr-4"
          >
            <path
              fill="#78909C"
              d="M40 41H8c-2.2 0-4-1.8-4-4V16.1c0-1.3.6-2.5 1.7-3.3L24 0l18.3 12.8c1.1.7 1.7 2 1.7 3.3V37c0 2.2-1.8 4-4 4z"
            />
            <path fill="#AED581" d="M14 1h20v31H14z" />
            <g fill="#558B2F">
              <path d="M13 0v33h22V0H13zm20 31H15V2h18v29z" />
              <path
                d="M34 3c0 1.7-.3 3-2 3s-3-1.3-3-3s1.3-2 3-2s2 .3 2 2zM16 1c1.7 0 3 .3 3 2s-1.3 3-3 3s-2-1.3-2-3s.3-2 2-2z"
              />
              <circle cx="24" cy="8" r="2" />
              <circle cx="24" cy="20" r="6" />
            </g>
            <path fill="#CFD8DC" d="M40 41H8c-2.2 0-4-1.8-4-4V17l20 13l20-13v20c0 2.2-1.8 4-4 4z" />
          </svg>
          <p class="text-gray-700 font-medium">Pouzećem</p>
        </button>
      </div>

      <h3 class="text-xl font-semibold text-gray-700 mb-6 mt-10 border-t pt-6">
        Odaberite način dostave
      </h3>
      <div class="space-y-4">
        <div
          class="flex items-center p-4 bg-white rounded-lg shadow-sm border border-gray-300 hover:shadow-md transition"
        >
          <input
            id="dostava-da"
            name="nacin-dostave"
            type="radio"
            class="mr-2"
            value="dostava"
            v-model="nacinDostave"
          />
          <label for="dostava-da" class="w-full py-1 ms-2 text-sm font-medium text-gray-900"
            >Dostava na adresu (5€)</label
          >

          <input
            id="dostava-ne"
            name="nacin-dostave"
            type="radio"
            class="ml-4 mr-2"
            value="osobno"
            v-model="nacinDostave"
          />
          <label for="dostava-ne" class="w-full py-1 ms-2 text-sm font-medium text-gray-900"
            >Osobno preuzimanje (Besplatno)</label
          >
        </div>
      </div>

      <div class="mt-10 border-t pt-6">
        <h4 class="text-gray-700 font-semibold mb-2">Za platiti</h4>
        <div class="flex justify-between text-gray-600">
          <span>Ukupan iznos bez PDV-a</span>
          <span>{{ formatCijena(iznosBezPDVa) }}</span>
        </div>
        <div class="flex justify-between text-gray-600 mt-1">
          <span>PDV (25%)</span>
          <span>{{ formatCijena(pdv) }}</span>
        </div>
        <div class="flex justify-between text-gray-600 mt-1">
          <span>Dostava</span>
          <span>
            <template v-if="nacinDostave === 'dostava'">{{ formatCijena(iznosDostave) }}</template>
            <template v-else>Besplatna (osobno preuzimanje)</template>
          </span>
        </div>
        <div class="flex justify-between text-lg font-bold text-gray-800 mt-4">
          <span>Ukupan iznos s PDV-om</span>
          <span>{{ formatCijena(ukupnoBruto) }}</span>
        </div>
      </div>

      <button
        class="w-full mt-4 bg-teal-600 hover:bg-teal-900 text-gray-100 text-lg py-3 rounded-lg transition disabled:opacity-50"
        :disabled="narudzbe.loading || !mozeNaruciti"
        @click="naruci"
      >
        {{ narudzbe.loading ? "Slanje…" : "Naruči" }}
      </button>
    </div>
  </div>
</template>
<script setup>
import { computed, reactive, ref } from "vue"
import { useRouter } from "vue-router"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import { useKosaricaStore } from "@/stores/kosarica"
import { useNarudzbaStore } from "@/stores/narudzba"

const router = useRouter()
const autentifikacija = useAutentifikacijskiStore()
const kosarica = useKosaricaStore()
const narudzbe = useNarudzbaStore()

const defaultProizvod = "https://placehold.co/160x160?text=Proizvod"
const defaultUsluga = "https://placehold.co/160x160?text=Usluga"

const forma = reactive({
  ime: "",
  prezime: "",
  email: "",
  telefon: "",
  adresa: "",
  drzava: "",
  zupanija: "",
  grad: "",
  postanski_broj: "",
})

const nacinPlacanja = ref("pouzece")
const nacinDostave = ref("osobno")
const iznosDostave = computed(() => (nacinDostave.value === "dostava" ? 5 : 0))

const proizvodi = computed(() =>
  kosarica.stavke
    .filter((s) => s.tip === "proizvod" || (!!s.proizvod_id && !s.termin_od))
    .map((s) => ({
      kljuc: `p-${s.proizvod_id || s.id}`,
      naziv: s.naziv,
      kolicina: s.kolicina,
      mjerna_jedinica: s.mjerna_jedinica,
      cijena: Number(s.cijena || 0),
      slika: s.slika,
    })),
)

const usluge = computed(() =>
  kosarica.stavke
    .filter((s) => s.tip === "usluga" || (!!s.usluga_id && !!s.termin_od))
    .map((s) => ({
      kljuc: `u-${s.usluga_id || s.id}-${s.termin_od || "x"}`,
      naziv: s.naziv,
      kolicina: s.kolicina,
      mjerna_jedinica: s.mjerna_jedinica,
      cijena: Number(s.cijena || 0),
      slika: s.slika,
      termin_od: s.termin_od,
      termin_do: s.termin_do,
    })),
)

function pad(n) {
  return String(n).padStart(2, "0")
}
function fmtHR(iso) {
  const d = new Date(iso)
  if (isNaN(d)) return iso
  const dd = pad(d.getDate())
  const mm = pad(d.getMonth() + 1)
  const yyyy = d.getFullYear()
  const hh = pad(d.getHours())
  const mi = pad(d.getMinutes())
  return `${dd}-${mm}-${yyyy} ${hh}:${mi}`
}

function bruto(x) {
  return Number(x || 0)
}
function neto(x) {
  return bruto(x) / 1.25
}

function zaokruziDva(x) {
  return Math.round((Number(x || 0) + Number.EPSILON) * 100) / 100
}

const iznosBezPDVa = computed(() => {
  const ukupnoP = proizvodi.value.reduce((a, x) => a + neto(x.cijena) * (x.kolicina || 0), 0)
  const ukupnoU = usluge.value.reduce((a, x) => a + neto(x.cijena) * (x.kolicina || 0), 0)
  return zaokruziDva(ukupnoP + ukupnoU)
})

const pdv = computed(() => zaokruziDva(iznosBezPDVa.value * 0.25))

const ukupnoBrutoBezDostave = computed(() => {
  const ukupnoP = proizvodi.value.reduce((a, x) => a + bruto(x.cijena) * (x.kolicina || 0), 0)
  const ukupnoU = usluge.value.reduce((a, x) => a + bruto(x.cijena) * (x.kolicina || 0), 0)
  return zaokruziDva(ukupnoP + ukupnoU)
})

const ukupnoBruto = computed(() => zaokruziDva(ukupnoBrutoBezDostave.value + iznosDostave.value))

const mozeNaruciti = computed(() => {
  const imaStavki = kosarica.stavke?.length > 0
  const ispunjeno =
    forma.ime &&
    forma.prezime &&
    forma.email &&
    forma.telefon &&
    forma.adresa &&
    forma.grad &&
    forma.postanski_broj &&
    forma.zupanija &&
    forma.drzava
  return autentifikacija.korisnikAutentificiran && imaStavki && !!ispunjeno
})

function formatCijena(v) {
  const n = Number(v || 0)
  return `${n.toFixed(2)} €`
}

async function ucitajIzProfila() {
  if (!autentifikacija.korisnicki_profil && autentifikacija.korisnikAutentificiran) {
    try {
      await autentifikacija.dohvatiProfil()
    } catch {}
  }
  const p = autentifikacija.korisnicki_profil
  if (!p) return

  const k = p.korisnik || p
  const prof = p.korisnicki_profil || p

  forma.ime = k.ime || forma.ime
  forma.prezime = k.prezime || forma.prezime
  forma.email = k.email || forma.email
  forma.telefon = k.broj_telefona || forma.telefon
  forma.adresa = prof.adresa || forma.adresa
  forma.grad = prof.grad || forma.grad
  forma.postanski_broj = prof.postanski_broj || forma.postanski_broj
  forma.zupanija = prof.zupanija || forma.zupanija
  forma.drzava = prof.drzava || forma.drzava
}

async function naruci() {
  if (!mozeNaruciti.value) return

  const stavkePayload = [
    ...proizvodi.value.map((p) => ({
      tip: "proizvod",
      naziv: p.naziv,
      kolicina: p.kolicina,
      mjerna_jedinica: p.mjerna_jedinica,
      cijena: p.cijena,
      slika: p.slika || null,
      termin_od: null,
      termin_do: null,
    })),
    ...usluge.value.map((u) => ({
      tip: "usluga",
      naziv: u.naziv,
      kolicina: u.kolicina,
      mjerna_jedinica: u.mjerna_jedinica,
      cijena: u.cijena,
      slika: u.slika || null,
      termin_od: u.termin_od || null,
      termin_do: u.termin_do || null,
    })),
  ]

  const payload = {
    ime: forma.ime,
    prezime: forma.prezime,
    email: forma.email,
    telefon: forma.telefon,
    adresa: forma.adresa,
    grad: forma.grad,
    postanski_broj: forma.postanski_broj,
    zupanija: forma.zupanija,
    drzava: forma.drzava,
    nacin_placanja: "pouzece",
    nacin_dostave: nacinDostave.value,
    stavke: stavkePayload,
  }

  const nar = await narudzbe.kreirajNarudzbu(payload)

  kosarica.reset()

  router.push({ name: "potvrdaNarudzbe" })
}
</script>
