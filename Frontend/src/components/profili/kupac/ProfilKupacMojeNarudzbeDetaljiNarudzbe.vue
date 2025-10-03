<template>
  <div
    class="mx-auto max-w-screen-lg my-6 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden"
    v-if="detalji"
  >
    <div class="w-full p-8 space-y-6">
      <h1 class="text-3xl font-bold text-gray-900">Detalji narudžbe</h1>

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
            <p class="text-sm font-semibold text-gray-900 flex items-center gap-2">
              {{ s.naziv }}
              <span
                class="inline-flex items-center justify-center rounded-full px-2.5 py-0.5 text-xs"
                :class="klasaOznaka(s.status)"
              >
                {{ statusOznaka(s.status) }}
              </span>
            </p>
            <p class="text-xs text-gray-500">
              Naručeno od:
              <router-link
                :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: s.opg_slug } }"
                class="text-orange-600 font-bold hover:underline"
              >
                {{ s.opg_naziv }}
              </router-link>
            </p>
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
            <p class="text-sm font-semibold text-gray-900 flex items-center gap-2">
              {{ s.naziv }}
              <span
                class="inline-flex items-center justify-center rounded-full px-2.5 py-0.5 text-xs"
                :class="klasaOznaka(s.status)"
              >
                {{ statusOznaka(s.status) }}
              </span>
            </p>
            <p class="text-xs text-gray-500">
              Naručeno od:
              <router-link
                :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: s.opg_slug } }"
                class="text-orange-600 font-bold hover:underline"
              >
                {{ s.opg_naziv }}
              </router-link>
            </p>
            <p class="text-xs text-gray-500">Količina: {{ s.kolicina }} {{ s.mjerna_jedinica }}</p>
            <p v-if="s.termin_od && s.termin_do" class="text-xs text-gray-500">
              Termin:
              <span class="text-teal-500 font-bold"
                >{{ fmtHR(s.termin_od) }} → {{ fmtHR(s.termin_do) }}</span
              >
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
          <span v-if="(detalji.dostava || 0) > 0">{{ formatCijena(detalji.dostava) }}</span>
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
  </div>

  <div v-else class="p-8 text-center text-gray-500">Učitavanje…</div>
</template>

<script setup>
import { useMojeNarudzbeKupacStore } from "@/stores/mojeNarudzbeKupac"
import { onMounted, computed } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()
const moje_narudzbe = useMojeNarudzbeKupacStore()

const detalji = computed(() => moje_narudzbe.detalji)

const defaultProizvod = "https://placehold.co/160x160?text=Proizvod"
const defaultUsluga = "https://placehold.co/160x160?text=Usluga"

function formatCijena(v) {
  return `${Number(v || 0).toFixed(2)} €`
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
function klasaOznaka(s) {
  if (s === "otkazano") return "bg-red-600 text-red-100"
  if (s === "isporuceno") return "bg-emerald-100 text-emerald-700"
  return "bg-amber-500 text-amber-100"
}

onMounted(async () => {
  const id = Number(route.params.id)
  await moje_narudzbe.ucitajDetaljeNarudzbe(id)
})
</script>
