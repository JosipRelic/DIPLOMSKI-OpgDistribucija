<template>
  <div
    class="mx-auto max-w-screen-lg my-12 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden"
  >
    <div class="hidden md:block w-full md:w-1/2">
      <img
        :src="slikePotvrdaNarudzbe"
        class="h-full w-full object-cover"
        alt="slika potvrda narudžbe"
      />
    </div>

    <div class="w-full md:w-1/2 p-8 space-y-6" v-if="nar">
      <h2 class="text-sm font-medium text-green-600">Narudžba uspješno poslana</h2>

      <div>
        <h1 class="text-3xl font-bold text-gray-900">Hvala na narudžbi!</h1>
        <span class="text-sm text-gray-400 my-0">
          Datum i vrijeme narudžbe: {{ formatDatumVrijeme(nar.datum_izrade) }}
        </span>
      </div>

      <p class="text-gray-600">
        Zahvaljujemo na Vašoj narudžbi. Trenutno je obrađujemo i uskoro ćemo Vam poslati potvrdu
        putem e-maila.
      </p>

      <div>
        <p class="text-sm font-medium text-gray-700">Broj narudžbe:</p>
        <span class="text-orange-600 font-semibold">{{ nar.broj_narudzbe }}</span>
      </div>

      <div>
        <div :class="{ hidden: !proizvodi.length }">
          <div class="text-orange-400 border-b border-orange-200 mb-2">Proizvodi</div>
          <ul>
            <li
              v-for="(s, idx) in proizvodi"
              :key="`p-${idx}`"
              class="flex py-1 items-center space-x-4"
            >
              <img :src="s.slika || defaultProizvod" class="w-16 h-16 object-cover rounded" />
              <div class="flex-1">
                <p class="text-sm font-semibold text-gray-900">{{ s.naziv }}</p>
                <p class="text-sm text-gray-500">
                  Količina: {{ s.kolicina }} / {{ s.mjerna_jedinica }}
                </p>
              </div>
              <p class="text-sm text-gray-900">{{ formatCijena(s.cijena) }}</p>
            </li>
          </ul>
        </div>

        <div class="mt-4" :class="{ hidden: !usluge.length }">
          <div class="text-orange-400 border-b border-orange-200 mb-2">Usluge</div>
          <ul>
            <li
              v-for="(s, idx) in usluge"
              :key="`u-${idx}`"
              class="flex py-1 items-center space-x-4"
            >
              <img :src="s.slika || defaultUsluga" class="w-16 h-16 object-cover rounded" />
              <div class="flex-1">
                <p class="text-sm font-semibold text-gray-900">{{ s.naziv }}</p>
                <p class="text-xs text-gray-500">
                  Količina: {{ s.kolicina }} / {{ s.mjerna_jedinica }}
                </p>
                <p class="text-xs text-gray-500" v-if="s.termin_od && s.termin_do">
                  Termin: {{ fmtHR(s.termin_od) }} → {{ fmtHR(s.termin_do) }}
                </p>
              </div>
              <p class="text-sm text-gray-900">{{ formatCijena(s.cijena) }}</p>
            </li>
            <li v-if="!usluge.length" class="text-sm text-gray-400 py-1">Nema usluga.</li>
          </ul>
        </div>
      </div>

      <div class="space-y-2 pt-2">
        <div class="flex justify-between text-sm">
          <span>Ukupan iznos bez PDV-a</span><span>{{ formatCijena(nar.iznos_bez_pdva) }}</span>
        </div>
        <div class="flex justify-between text-sm">
          <span>PDV (25%)</span><span>{{ formatCijena(nar.pdv) }}</span>
        </div>
        <div class="flex justify-between text-sm">
          <span>Dostava</span>
          <span>
            <template v-if="nar.dostava > 0">{{ formatCijena(nar.dostava) }}</template>
            <template v-else>Besplatna (osobno preuzimanje)</template>
          </span>
        </div>
        <div class="flex justify-between font-semibold text-lg border-t pt-2">
          <span>Ukupno</span><span>{{ formatCijena(nar.ukupno) }}</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm text-gray-700 pt-6">
        <div>
          <p class="font-medium">Podaci dostave</p>
          <p>
            {{ nar.ime }} {{ nar.prezime }}<br />
            {{ nar.email }}<br />
            {{ nar.telefon }}<br />
            {{ nar.adresa }}, {{ nar.grad }} {{ nar.postanski_broj }}<br />
            {{ nar.zupanija }}, {{ nar.drzava }}
          </p>
        </div>
        <div>
          <p class="font-medium">Način plaćanja</p>
          <p>
            {{ nar.nacin_placanja === "pouzece" ? "Pouzećem" : nar.nacin_placanja }}
          </p>
        </div>
        <div>
          <p class="font-medium">Način dostave</p>
          <p>
            {{ nar.nacin_dostave === "osobno" ? "Osobno preuzimanje" : "Dostava na adresu" }}
          </p>
        </div>
      </div>

      <div>
        <router-link :to="{ name: 'pocetna' }" class="text-orange-600 font-medium hover:underline">
          Nastavi kupovinu →
        </router-link>
      </div>
    </div>

    <div v-else class="w-full md:w-1/2 p-8">
      <h2 class="text-xl font-semibold text-gray-800 mb-4">Nema aktivne narudžbe</h2>
      <router-link :to="{ name: 'pocetna' }" class="text-orange-600 hover:underline"
        >Vrati se na početnu</router-link
      >
    </div>
  </div>
</template>
<script setup>
import { computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import { useNarudzbaStore } from "@/stores/narudzba"
import slikePotvrdaNarudzbe from "@/assets/slike/potvrda-narudzbe.png"

const router = useRouter()
const narudzbe = useNarudzbaStore()
const nar = computed(() => narudzbe.aktivna)

const defaultProizvod = "https://placehold.co/160x160?text=Proizvod"
const defaultUsluga = "https://placehold.co/160x160?text=Usluga"

const proizvodi = computed(() => (nar.value?.stavke || []).filter((s) => s.tip === "proizvod"))
const usluge = computed(() => (nar.value?.stavke || []).filter((s) => s.tip === "usluga"))

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
  const dd = pad(d.getDate())
  const mm = pad(d.getMonth() + 1)
  const yyyy = d.getFullYear()
  const hh = pad(d.getHours())
  const mi = pad(d.getMinutes())
  return `${dd}-${mm}-${yyyy} ${hh}:${mi}`
}

function formatDatumVrijeme(iso) {
  try {
    const d = new Date(iso)
    const datum = d.toLocaleDateString("hr-HR")
    const vrijeme = d.toLocaleTimeString("hr-HR", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    })
    return `${datum} ${vrijeme}`
  } catch {
    return iso
  }
}

onMounted(() => {
  if (!nar.value) {
    router.replace({ name: "pocetna" })
  }
})
</script>
