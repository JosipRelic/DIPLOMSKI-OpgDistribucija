<template>
  <div class="flex justify-center items-center p-5">
    <div class="w-full max-w-7xl rounded-lg overflow-x-auto bg-white shadow-md">
      <div class="p-4 min-w-full">
        <div class="flex justify-between items-center">
          <div class="ps-4">
            <p class="text-3xl font-bold">Sve narudžbe</p>
            <small class="text-gray-500">Sve što je naručeno od vas</small>
          </div>
        </div>
      </div>

      <div class="max-w-sm ps-8 pb-5">
        <label for="pretragaBrojNarudzbe">
          <div class="relative">
            <input
              type="text"
              id="pretragaBrojNarudzbe"
              v-model="pretraga"
              placeholder="Pretraži po broju narudžbe"
              class="mt-0.5 w-full rounded border-gray-300 pe-10 shadow-sm sm:text-sm p-3 h-10"
            />
            <span class="absolute inset-y-0 right-2 grid w-8 place-content-center">
              <button
                type="button"
                aria-label="Submit"
                class="rounded-full p-1.5 text-gray-700 transition-colors hover:bg-gray-100"
                @click="primijeniPretragu"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="size-4"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
                  />
                </svg>
              </button>
            </span>
          </div>
        </label>
      </div>

      <table class="w-full text-left">
        <thead>
          <tr>
            <th class="px-8 py-3 border-b border-gray-300 w-[20%]">Naručitelj</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[20%]">Broj narudžbe</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[15%]">Ukupan iznos</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[25%]">Datum i vrijeme narudžbe</th>
            <th class="px-8 py-3 border-b border-gray-300 w-[10%]">
              <div class="flex">
                Status
                <span @click="urediStatus" class="ms-1 cursor-pointer"
                  ><span v-if="uredivanjeUTijeku" title="Završi uređivanje">✅</span>
                  <span v-else title="Uredi statuse">✏️</span></span
                >
              </div>
            </th>
            <th class="px-8 py-3 border-b border-gray-300 w-[10%]"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="primljene_narudzbe.loading">
            <td colspan="6" class="px-8 py-5 text-center text-gray-500">Učitavanje…</td>
          </tr>
          <tr v-else-if="!primljene_narudzbe.narudzbe.length">
            <td colspan="6" class="px-8 py-5 text-center text-gray-500">Nema narudžbi.</td>
          </tr>
          <tr v-else v-for="n in primljene_narudzbe.narudzbe" :key="n.id">
            <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
              <router-link
                v-if="n.kupac_slug"
                :to="{ name: 'profilOpgDetaljiKupca', params: { kupacSlug: n.kupac_slug } }"
                class="text-orange-600 hover:text-orange-900 hover:underline"
              >
                {{ n.narucitelj || "Kupac" }}
                <span class="text-gray-400">- ({{ n.narucitelj_tip }})</span>
              </router-link>

              <router-link
                v-else-if="n.opg_slug"
                :to="{ name: 'ETrznicaDetaljiOPGa', params: { opgSlug: n.opg_slug } }"
                class="text-orange-600 hover:text-orange-900 hover:underline"
              >
                {{ n.narucitelj || "OPG" }}
                <span class="text-gray-400">- ({{ n.narucitelj_tip }})</span>
              </router-link>

              <span v-else>{{ n.narucitelj }} (Profil izbrisan)</span>
            </td>
            <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
              <p class="text-gray-500">{{ n.broj_narudzbe }}</p>
            </td>
            <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">
              {{ formatCijena(n.ukupno) }}
            </td>
            <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[25%]">
              {{ formatHR(n.datum_izrade) }}
            </td>
            <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
              <div class="flex items-center gap-2">
                <span
                  :class="klasaOznaka(n.status)"
                  class="inline-flex items-center justify-center rounded-full px-2.5 py-0.5"
                >
                  <p class="text-sm whitespace-nowrap capitalize">{{ statusOznaka(n.status) }}</p>
                </span>
                <select
                  v-if="uredivanjeUTijeku"
                  class="text-sm border border-gray-300 shadow-sm text-gray-900 rounded px-1 py-0.5"
                  v-model="status[n.id]"
                  @change="promijeniStatus(n.id)"
                >
                  <option value="u_tijeku">U tijeku</option>
                  <option value="isporuceno">Isporučeno</option>
                  <option value="otkazano">Otkazano</option>
                </select>
              </div>
            </td>
            <td
              class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
            >
              <router-link
                :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe', params: { id: n.id } }"
                >Detalji</router-link
              >
            </td>
          </tr>
        </tbody>
      </table>

      <div
        v-if="primljene_narudzbe.ukupnoStranica > 1"
        class="flex items-center p-5 justify-center min-w-full"
      >
        <div class="flex border border-gray-200 shadow rounded-md">
          <button
            class="text-black border-r border-gray-200 font-semibold px-4 py-2 cursor-pointer"
            :disabled="primljene_narudzbe.stranica === 1"
            @click="idiNa(primljene_narudzbe.stranica - 1)"
          >
            Prethodna
          </button>
          <div class="flex space-x-2">
            <button
              v-for="s in stranice"
              :key="s"
              class="px-4 py-2"
              :class="s === primljene_narudzbe.stranica ? 'bg-orange-500 text-white' : ''"
              @click="idiNa(s)"
            >
              {{ s }}
            </button>
          </div>
          <button
            class="text-black border-l border-gray-200 font-semibold px-4 py-2 cursor-pointer"
            :disabled="primljene_narudzbe.stranica === primljene_narudzbe.ukupnoStranica"
            @click="idiNa(primljene_narudzbe.stranica + 1)"
          >
            Sljedeća
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, watch } from "vue"
import { usePrimljeneNarudzbeOpgStore } from "@/stores/primljeneNarudzbeOpg"

const primljene_narudzbe = usePrimljeneNarudzbeOpgStore()
const pretraga = ref(primljene_narudzbe.p)
const status = ref({})

function formatCijena(v) {
  const n = Number(v || 0)
  return `${n.toFixed(2)} €`
}
function formatHR(iso) {
  try {
    const d = new Date(iso)
    return d.toLocaleString("hr-HR")
  } catch {
    return iso
  }
}
function statusOznaka(s) {
  return s === "u_tijeku" ? "U tijeku" : s === "isporuceno" ? "Isporučeno" : "Otkazano"
}
function klasaOznaka(s) {
  if (s === "otkazano") return "bg-red-600 text-red-100"
  if (s === "isporuceno") return "bg-emerald-100 text-emerald-700"
  return "bg-amber-500 text-amber-100"
}

const stranice = computed(() => {
  const str = []
  for (let i = 1; i <= primljene_narudzbe.ukupnoStranica; i++) str.push(i)
  return str
})

function idiNa(p) {
  if (p < 1 || p > primljene_narudzbe.ukupnoStranica) return
  primljene_narudzbe.idiNa(p)
}
function primijeniPretragu() {
  primljene_narudzbe.postaviP(pretraga.value)
}

async function promijeniStatus(id) {
  const v = status.value[id]
  if (!v) return
  await primljene_narudzbe.promijeniStatusNarudzbe(id, v)
}

watch(
  () => primljene_narudzbe.narudzbe,
  (narudzba) => {
    const tmp = {}
    narudzba.forEach((n) => (tmp[n.id] = n.status))
    status.value = tmp
  },
  { immediate: true },
)

let t = null
watch(
  pretraga,
  (v) => {
    clearTimeout(t)
    t = setTimeout(() => {
      primljene_narudzbe.postaviP(v || "")
    }, 300)
  },
  { immediate: true },
)

const uredivanjeUTijeku = ref(false)
const urediStatus = () => {
  uredivanjeUTijeku.value = !uredivanjeUTijeku.value
}

onMounted(() => primljene_narudzbe.ucitajNarudzbe())
</script>
