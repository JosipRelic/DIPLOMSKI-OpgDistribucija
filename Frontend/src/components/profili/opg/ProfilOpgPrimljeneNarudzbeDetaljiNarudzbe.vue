<template>
  <div
    class="mx-auto max-w-screen-lg my-6 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden"
    v-if="detalji"
  >
    <div class="w-full p-8 space-y-6">
      <h1 class="text-3xl font-bold text-gray-900">Detalji narudžbe</h1>

      <div>
        <p class="text-sm font-medium text-gray-700 mb-1">Status narudžbe</p>
        <div class="flex items-center">
          <h2
            class="text-lg font-medium inline-flex items-center justify-center rounded-full px-2.5 py-0.5"
            :class="klasaOznaka(detalji.status)"
          >
            {{ prikazStatus() }}
          </h2>
          <button
            type="button"
            class="ms-1 cursor-pointer"
            title="Promijeni status"
            @click="urediStatus"
          >
            <span v-if="uredivanjeUTijeku" title="Završi uređivanje">✅</span>
            <span v-else title="Uredi status">✏️</span>
          </button>
          <select
            v-if="uredivanjeUTijeku"
            class="ms-2 text-sm border border-gray-300 shadow-sm text-gray-900 rounded px-2 py-1"
            v-model="status"
            @change="promijeniStatus"
            :disabled="mijenjamStatus"
          >
            <option value="u_tijeku">U tijeku</option>
            <option value="isporuceno">Isporučeno</option>
            <option value="otkazano">Otkazano</option>
          </select>
        </div>
      </div>

      <div>
        <p class="text-sm font-medium text-gray-700">Broj narudžbe</p>
        <p class="text-orange-600 font-semibold">#{{ detalji.broj_narudzbe }}</p>
      </div>

      <div v-if="detalji.proizvodi?.length">
        <div class="text-orange-400 border-b border-orange-200 mb-1 px-1">Proizvodi</div>
        <div
          v-for="s in detalji.proizvodi"
          :key="`p-${s.id}`"
          class="flex py-4 items-center space-x-4"
        >
          <img :src="s.slika || defaultProizvod" class="w-16 h-16 object-cover rounded" />
          <div class="flex-1">
            <p class="text-sm font-semibold text-gray-900">{{ s.naziv }}</p>
            <p class="text-sm text-gray-500">Količina: {{ s.kolicina }} {{ s.mjerna_jedinica }}</p>
          </div>
          <p class="text-sm text-gray-900">{{ formatCijena(s.cijena) }}</p>
        </div>
      </div>

      <div v-if="detalji.usluge?.length">
        <div class="text-orange-400 border-b border-orange-200 mb-2 px-1">Usluge</div>
        <div
          v-for="s in detalji.usluge"
          :key="`u-${s.id}`"
          class="flex py-4 items-center space-x-4"
        >
          <img :src="s.slika || defaultUsluga" class="w-16 h-16 object-cover rounded" />
          <div class="flex-1">
            <p class="text-sm font-semibold text-gray-900">{{ s.naziv }}</p>
            <p class="text-xs text-gray-500">Količina: {{ s.kolicina }} {{ s.mjerna_jedinica }}</p>
            <p v-if="s.termin_od && s.termin_do" class="text-xs text-gray-500">
              Termin:
              <span class="text-teal-500">{{ fmtHR(s.termin_od) }} → {{ fmtHR(s.termin_do) }}</span>
            </p>
          </div>
          <p class="text-sm text-gray-900">{{ formatCijena(s.cijena) }}</p>
        </div>
      </div>

      <div class="space-y-2 border-t border-orange-200 pt-3">
        <div class="flex justify-between text-sm">
          <span>Ukupan iznos bez PDV-a</span><span>{{ formatCijena(detalji.iznos_bez_pdva) }}</span>
        </div>
        <div class="flex justify-between text-sm">
          <span>PDV (25%)</span><span>{{ formatCijena(detalji.pdv) }}</span>
        </div>
        <div class="flex justify-between text-sm pb-2">
          <span>Dostava</span>
          <span v-if="detalji.dostava > 0">{{ formatCijena(detalji.dostava) }}</span>
          <span v-else>Besplatna (osobno preuzimanje)</span>
        </div>
        <div class="flex justify-between font-semibold text-lg border-t pt-2">
          <span>Ukupno</span><span>{{ formatCijena(detalji.ukupno) }}</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm text-gray-700 pt-6">
        <div>
          <p class="font-medium">Podaci o naručitelju</p>
          <p>
            {{ detalji.narucitelj }}<br />
            {{ detalji.kupac_email }}<br />
            {{ detalji.kupac_telefon }}<br />
            {{ detalji.adresa }}<br />
            {{ detalji.zupanija }}, Hrvatska
          </p>
        </div>
        <div class="space-y-4">
          <div>
            <p class="font-medium">Način plaćanja</p>
            <p class="inline">
              {{ detalji.nacin_placanja === "pouzece" ? "Pouzećem" : detalji.nacin_placanja }}
            </p>
          </div>
          <div>
            <p class="font-medium">Način dostave</p>
            <p class="inline">
              {{ detalji.nacin_dostave === "osobno" ? "Osobno preuzimanje" : "Dostava na adresu" }}
            </p>
          </div>
        </div>
      </div>

      <div class="w-full mt-6">
        <button
          @click="otvoriFormuNarudzbe"
          class="bg-orange-500 text-gray-100 px-4 py-2 rounded-xl shadow hover:bg-orange-900 transition"
        >
          {{ formaOtvorena ? "Sakrij formu" : "Pošalji email vezan uz narudžbu" }}
        </button>

        <form
          v-if="formaOtvorena"
          class="mt-4 p-6 border border-gray-200 rounded-xl shadow bg-white space-y-4"
        >
          <div>
            <label class="block text-sm font-medium">Broj Narudžbe </label>
            <span class="text-xs text-gray-400"
              >Automatski se dodaje kao dio predmeta prilikom slanja e-maila</span
            >
            <input
              type="text"
              class="mt-1 w-full rounded-md bg-white text-base text-gray-500 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              :value="'#' + detalji.broj_narudzbe"
              disabled
            />
          </div>
          <div>
            <label class="block text-sm font-medium">Email</label>

            <input
              type="email"
              class="mt-1 w-full rounded-md bg-white text-base text-gray-500 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              :value="detalji.kupac_email"
              disabled
            />
          </div>
          <div class="flex flex-col items-center">
            <button
              class="w-full max-w-xs max-sm:p-2 font-bold shadow-sm hover:bg-red-400 rounded-lg py-2 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
            >
              <div class="bg-white p-2 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  class="w-6 text-red-600"
                >
                  <path
                    fill="currentColor"
                    d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
                  />
                </svg>
              </div>
              <span class="ml-4 max-sm:text-sm"> Ispunite glasovno pomoću AI </span>
            </button>
            <small class="pt-2 w-full max-w-xs text-xs"
              >Pritisnite gumb i popunite obrazac glasom npr. "Nemamo proizvod na stanju. Nažalost
              proizvod koji ste tražili nemamo na stanju itd..."</small
            >
          </div>
          <div class="border-b text-center">
            <div
              class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
            >
              ili unesite podatke ručno
            </div>
          </div>
          <div>
            <label class="block text-sm font-medium">Predmet</label>
            <input
              type="text"
              class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              placeholder="Upiši predmet..."
              v-model="predmet"
            />
          </div>
          <div>
            <label class="block text-sm font-medium">Poruka</label>
            <textarea
              rows="5"
              class="mt-1 w-full rounded-md bg-white px-4 py-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              placeholder="Upiši poruku..."
              v-model="poruka"
            ></textarea>
          </div>

          <button
            type="submit"
            class="bg-teal-600 text-gray-100 px-4 py-2 rounded-xl hover:bg-teal-900 transition disabled:bg-gray-500"
            :disabled="slanjeMaila"
            @click.prevent="posaljiMail"
          >
            {{ slanjeMaila ? "Slanje u tijeku..." : "Pošalji" }}
          </button>
        </form>
      </div>
    </div>
  </div>
  <div v-else class="p-8 text-center text-gray-500">Učitavanje…</div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue"
import { useRoute } from "vue-router"
import { usePrimljeneNarudzbeOpgStore } from "@/stores/primljeneNarudzbeOpg"
import { useUiStore } from "@/stores/ui"

const route = useRoute()
const primljene_narudzbe = usePrimljeneNarudzbeOpgStore()
const detalji = computed(() => primljene_narudzbe.detalji)

const slanjeMaila = ref(false)
const predmet = ref("")
const poruka = ref("")
const mijenjamStatus = ref(false)
const ui = useUiStore()

const defaultProizvod = "https://placehold.co/160x160?text=Proizvod"
const defaultUsluga = "https://placehold.co/160x160?text=Usluga"

const status = ref(null)

function formatCijena(v) {
  const n = Number(v || 0)
  return `${n.toFixed(2)} €`
}
function pad(n) {
  return String(n).padStart(2, "0")
}
function fmtHR(iso) {
  const d = new Date(iso)
  if (isNaN(d)) return iso
  return `${pad(d.getDate())}.${pad(d.getMonth() + 1)}.${d.getFullYear()}. ${pad(d.getHours())}:${pad(d.getMinutes())}`
}
function statusOznaka(s) {
  return s === "u_tijeku" ? "U tijeku" : s === "isporuceno" ? "Isporučeno" : "Otkazano"
}

function prikazStatus() {
  return mijenjamStatus.value ? "Mijenjam..." : statusOznaka(detalji.value?.status)
}

function klasaOznaka(s) {
  if (mijenjamStatus.value) return "bg-gray-500 text-white"
  if (s === "otkazano") return "bg-red-600 text-red-100"
  if (s === "isporuceno") return "bg-emerald-100 text-emerald-700"
  return "bg-amber-500 text-amber-100"
}

async function promijeniStatus() {
  if (!detalji.value) return
  mijenjamStatus.value = true
  try {
    const r = await primljene_narudzbe.promijeniStatusNarudzbe(detalji.value.id, status.value)
    if (r.ok) {
      ui.obavijest({
        tekst: `Status ažuriran na ${statusOznaka(status.value)}.`,
        tip_obavijesti: "uspjeh",
      })
    } else {
      ui.obavijest({ tekst: r.error || "Greška pri promjeni statusa.", tip_obavijesti: "greska" })
      status.value = primljene_narudzbe.detalji?.status || status.value
    }
  } finally {
    mijenjamStatus.value = false
  }
}

async function posaljiMail() {
  if (!detalji.value?.id) return
  if (!predmet.value.trim() || !poruka.value.trim()) {
    ui.obavijest({ tekst: "Unesite predmet i poruku.", tip_obavijesti: "upozorenje" })
    return
  }

  slanjeMaila.value = true
  try {
    const r = await primljene_narudzbe.posaljiMailKupcu(
      detalji.value.id,
      predmet.value.trim(),
      poruka.value.trim(),
    )
    if (r.ok) {
      ui.obavijest({ tekst: "E-mail poslan kupcu.", tip_obavijesti: "uspjeh" })
      formaOtvorena.value = false
      predmet.value = ""
      poruka.value = ""
    } else {
      ui.obavijest({ tekst: r.error || "Greška pri slanju e-maila.", tip_obavijesti: "greska" })
    }
  } finally {
    slanjeMaila.value = false
  }
}

onMounted(async () => {
  const id = Number(route.params.id)
  await primljene_narudzbe.ucitajDetaljeNarudzbe(id)
  status.value = primljene_narudzbe.detalji?.status || "u_tijeku"
})

const uredivanjeUTijeku = ref(false)
const urediStatus = () => {
  uredivanjeUTijeku.value = !uredivanjeUTijeku.value
}

const formaOtvorena = ref(false)
const otvoriFormuNarudzbe = () => {
  formaOtvorena.value = !formaOtvorena.value
}
</script>
