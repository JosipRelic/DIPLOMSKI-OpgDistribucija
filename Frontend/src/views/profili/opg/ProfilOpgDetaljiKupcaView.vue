<template>
  <section>
    <div
      class="mx-auto w-full bg-white rounded-xl max-w-7xl px-5 py-12 md:px-10 md:py-20"
      v-if="kupac"
    >
      <h2 class="text-center text-3xl font-bold md:text-5xl">
        {{ kupac.ime }} {{ kupac.prezime }}
      </h2>
      <span class="flex justify-center items-center">
        <img
          class="my-5 w-30 h-30 object-cover rounded-full"
          :src="kupac.slika_profila || defaultSlika"
          alt="kupac"
        />
      </span>

      <div
        class="mx-auto rounded-xl flex w-full max-w-3xl flex-col flex-wrap justify-between gap-5 bg-gray-100 px-16 py-8 sm:flex-row md:gap-6"
      >
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
          <div class="flex flex-col items-start">
            <p class="text-sm uppercase">Naručeno kod nas</p>
            <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">
              Proizvoda: {{ statistika.broj_proizvoda }}
            </h4>
            <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">
              Usluga: {{ statistika.broj_usluga }}
            </h4>
          </div>

          <div class="flex flex-col items-start">
            <p class="text-sm uppercase">Zadnja narudžba napravljena</p>
            <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">
              {{
                statistika.zadnja_narudzba ? formatDatumVrijeme(statistika.zadnja_narudzba) : "—"
              }}
            </h4>
          </div>

          <div class="flex flex-col items-start">
            <p class="text-sm uppercase">Najčešće kupljeno</p>
            <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">
              {{ statistika.najcesce_kupljeno || "—" }}
            </h4>
          </div>

          <div class="flex flex-col items-start">
            <p class="text-sm uppercase">Vrijednost svih narudžbi</p>
            <h4 class="text-xl font-bold sm:text-2xl md:text-3xl">
              {{ formatCijena(statistika.ukupna_vrijednost) }}
            </h4>
          </div>
        </div>

        <div class="flow-root mt-8 w-full">
          <dl class="divide-y divide-gray-200 text-sm *:even:bg-gray-50">
            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Email</dt>
              <dd class="text-gray-700 sm:col-span-2">{{ kupac.email || "—" }}</dd>
            </div>
            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Broj telefona</dt>
              <dd class="text-gray-700 sm:col-span-2">{{ kupac.broj_telefona || "—" }}</dd>
            </div>
            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Adresa</dt>
              <dd class="text-gray-700 sm:col-span-2">{{ kupac.adresa || "—" }}</dd>
            </div>
            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Županija</dt>
              <dd class="text-gray-700 sm:col-span-2">{{ kupac.zupanija || "—" }}</dd>
            </div>
            <div class="grid grid-cols-1 gap-1 p-3 sm:grid-cols-3 sm:gap-4">
              <dt class="font-medium text-gray-900">Grad</dt>
              <dd class="text-gray-700 sm:col-span-2">{{ gradIPB }}</dd>
            </div>
          </dl>
        </div>
      </div>

      <div class="max-w-sm ps-0 md:ps-0 lg:ps-0 pb-0 mt-10">
        <label for="pretragaBrojNarudzbe">
          <div class="relative">
            <input
              type="text"
              id="pretragaBrojNarudzbe"
              placeholder="Pretraži po broju narudžbe"
              v-model.trim="pretraga"
              @keydown.enter.prevent="ucitaj(1)"
              class="mt-0.5 w-full rounded border-gray-300 pe-10 shadow-sm sm:text-sm p-3 h-10"
            />
            <span class="absolute inset-y-0 right-2 grid w-8 place-content-center">
              <button
                type="button"
                aria-label="Submit"
                @click="ucitaj(1)"
                class="rounded-full p-1.5 text-gray-700 transition-colors hover:bg-gray-100"
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

      <div class="w-full overflow-x-auto mt-6">
        <table class="able-auto border-collapse w-full">
          <thead>
            <tr>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[20%]">Broj narudžbe</th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[15%]">Ukupan iznos</th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[45%]">
                Datum i vrijeme narudžbe
              </th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[10%]">Status</th>
              <th class="px-8 py-3 text-left border-b border-gray-300 w-[10%]"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="n in narudzbe.stavke" :key="n.id">
              <td class="px-8 py-5 border-b border-gray-200 w-[20%]">
                <p class="text-gray-500">#{{ n.broj_narudzbe }}</p>
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[15%]">
                {{ formatCijena(n.ukupno) }}
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[45%]">
                {{ formatDatumVrijeme(n.datum_izrade) }}
              </td>
              <td class="px-8 py-5 text-gray-500 border-b border-gray-200 w-[10%]">
                <span
                  class="inline-flex items-center justify-center rounded-full px-2.5 py-0.5"
                  :class="statusKlasa(n.status)"
                >
                  <svg
                    v-if="n.status === 'otkazano'"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="-ms-1 me-1.5 size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z"
                    />
                  </svg>
                  <svg
                    v-else-if="n.status === 'u_tijeku'"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    class="-ms-1 me-1.5 size-3"
                  >
                    <path
                      fill="none"
                      stroke="currentColor"
                      stroke-width="1.5"
                      d="M1 1h22M10 4.5h4V6c0 1-2 2-2 2s-2-1-2-2V4.5ZM5 1v5c0 3 5 3.235 5 6s-5 3-5 6v5M19 1v5c0 3-5 3.235-5 6s5 3 5 6v5M1 23h22M8 21c0-2 4-4 4-4s4 2 4 4v2H8v-2Z"
                    />
                  </svg>
                  <svg
                    v-else
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="-ms-1 me-1.5 size-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>

                  <p class="text-sm whitespace-nowrap">
                    {{ mapStatus(n.status) }}
                  </p>
                </span>
              </td>
              <td
                class="px-8 py-5 border-b border-gray-200 text-orange-600 hover:text-orange-900 hover:underline w-[10%]"
              >
                <router-link
                  :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe', params: { id: n.id } }"
                >
                  Detalji
                </router-link>
              </td>
            </tr>

            <tr v-if="!narudzbe.stavke.length">
              <td colspan="5" class="px-8 py-6 text-center text-gray-500">Nema narudžbi.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="flex items-center p-5 justify-center min-w-full" v-if="ukupnoStranica > 1">
        <div class="flex border border-gray-200 shadow rounded-md">
          <button
            class="text-black border-r border-gray-200 font-semibold px-4 py-2 cursor-pointer disabled:opacity-50"
            :disabled="stranica === 1"
            @click="ucitaj(stranica - 1)"
          >
            Prethodna
          </button>
          <div class="flex space-x-2">
            <button
              v-for="str in straniceZaPrikaz"
              :key="str"
              class="px-4 py-2"
              :class="str === stranica ? 'bg-orange-500 text-white' : ''"
              @click="ucitaj(str)"
            >
              {{ str }}
            </button>
          </div>
          <button
            class="text-black border-l border-gray-200 font-semibold px-4 py-2 cursor-pointer disabled:opacity-50"
            :disabled="stranica === ukupnoStranica"
            @click="ucitaj(stranica + 1)"
          >
            Sljedeća
          </button>
        </div>
      </div>
    </div>

    <div v-else class="mx-auto w-full bg-white rounded-xl max-w-7xl px-5 py-12 md:px-10 md:py-20">
      <p class="text-gray-600">Učitavanje…</p>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { useRoute } from "vue-router"
import { usePrimljeneNarudzbeOpgStore } from "@/stores/primljeneNarudzbeOpg"

const route = useRoute()
const kupacSlug = computed(() => route.params.kupacSlug)
const primljene_narudzbe = usePrimljeneNarudzbeOpgStore()

const kupac = computed(() => primljene_narudzbe.kupac)
const statistika = computed(
  () =>
    primljene_narudzbe.kupacStatistika || {
      broj_proizvoda: 0,
      broj_usluga: 0,
      zadnja_narudzba: null,
      najcesce_kupljeno: null,
      ukupna_vrijednost: 0,
    },
)

const narudzbe = computed(() => primljene_narudzbe.kupacNarudzbe)
const stranica = computed(() => narudzbe.value.stranica)
const velicina = computed(() => narudzbe.value.velicina)
const ukupno = computed(() => narudzbe.value.ukupno)
const ukupnoStranica = computed(() => Math.max(1, Math.ceil(ukupno.value / velicina.value)))

const pretraga = computed({
  get: () => primljene_narudzbe.kupacP,
  set: (v) => primljene_narudzbe.postaviKupacP(v),
})

const defaultSlika = "https://placehold.co/160x160?text=Kupac"

const gradIPB = computed(() => {
  if (!kupac.value) return "—"
  const g = kupac.value.grad || ""
  const pb = kupac.value.postanski_broj || ""
  return [g, pb].filter(Boolean).join(" ")
})

function formatCijena(v) {
  const n = Number(v || 0)
  return `${n.toFixed(2)} €`
}

function formatDatumVrijeme(iso) {
  if (!iso) return "—"
  const d = new Date(iso)
  if (isNaN(d)) return iso
  const datum = d.toLocaleDateString("hr-HR")
  const vrijeme = d.toLocaleTimeString("hr-HR", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  })
  return `${datum} ${vrijeme}`
}

function mapStatus(s) {
  if (s === "otkazano") return "Otkazano"
  if (s === "isporuceno") return "Isporučeno"
  return "U tijeku"
}
function statusKlasa(s) {
  if (s === "otkazano") return "bg-red-600 text-red-100"
  if (s === "isporuceno") return "bg-emerald-100 text-emerald-700"
  return "bg-amber-500 text-amber-100"
}

async function ucitaj(str = 1) {
  await primljene_narudzbe.ucitajKupca(kupacSlug.value, {
    stranica: str,
    velicina: velicina.value,
    p: pretraga.value,
  })
}

onMounted(() => {
  ucitaj(1)
})
</script>
