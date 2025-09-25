<template>
  <div class="relative overflow-x-auto m-4 shadow-md rounded-lg">
    <ProfilOpgPonudaFarmaPlusKalendar />
    <div class="bg-white pt-2 px-4 flex flex-items justify-center border-t border-gray-100 pt-5">
      <p class="text-green-600 pe-2">(Dostupno usluga)</p>
      <p class="text-red-400 pe-2">(Nema dostupnih usluga)</p>
      <p class="text-yellow-500 pe-2">(Usluga postoji, ali je javno nedostupna)</p>
    </div>
    <div class="flex items-center justify-center p-20 py-4 md:py-8 flex-wrap bg-white shadow-md">
      <button
        type="button"
        class="border border-gray-200 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
        :class="
          !aktivnaKategorijaId
            ? 'bg-[#223c2f] text-white'
            : 'text-gray-600 hover:bg-[#223c2f] hover:text-white'
        "
        @click="filtrirajPoKategoriji(null)"
      >
        Prikaži sve
        <span :class="ukupnoDostupno > 0 ? 'text-green-600' : 'text-red-400'"
          >({{ ukupnoDostupno }})</span
        >
        <span v-if="ukupnoNedostupno > 0" class="text-yellow-500 ms-1"
          >({{ ukupnoNedostupno }})</span
        >
      </button>
      <button
        v-for="k in ponudaFarmaPlus.kategorije"
        :key="k.id"
        type="button"
        class="border border-gray-200 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
        :class="
          aktivnaKategorijaId === k.id
            ? 'bg-[#223c2f] text-white'
            : 'text-gray-600 hover:bg-[#223c2f] hover:text-white'
        "
        @click="filtrirajPoKategoriji(k.id)"
      >
        {{ k.naziv }}
        <span
          :class="(k.dostupni ?? k.ukupno - k.nedostupni) > 0 ? 'text-green-600' : 'text-red-400'"
          >({{ k.dostupni ?? k.ukupno - k.nedostupni }})</span
        >
        <span v-if="k.nedostupni > 0" class="text-yellow-500 ms-1">({{ k.nedostupni }})</span>
      </button>
    </div>

    <div
      class="relative overflow-x-auto m-4 shadow-md rounded-lg bg-white p-4 flex items-center gap-2 cursor-pointer hover:bg-gray-100"
      @click="otvoriFormuZaDodavanjeUsluge"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 32 32">
        <g fill="none">
          <path
            fill="url(#fluentColorAddCircle320)"
            d="M30 16c0 7.732-6.268 14-14 14S2 23.732 2 16S8.268 2 16 2s14 6.268 14 14"
          />
          <path
            fill="url(#fluentColorAddCircle321)"
            d="M15 10a1 1 0 1 1 2 0v5h5a1 1 0 1 1 0 2h-5v5a1 1 0 1 1-2 0v-5h-5a1 1 0 1 1 0-2h5z"
          />
          <defs>
            <linearGradient
              id="fluentColorAddCircle320"
              x1="3"
              x2="22.323"
              y1="7.25"
              y2="27.326"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#52D17C" />
              <stop offset="1" stop-color="#22918B" />
            </linearGradient>
            <linearGradient
              id="fluentColorAddCircle321"
              x1="11.625"
              x2="15.921"
              y1="10.428"
              y2="25.592"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#fff" />
              <stop offset="1" stop-color="#E3FFD9" />
            </linearGradient>
          </defs>
        </g>
      </svg>
      <p class="text-gray-900 rounded-full text-base font-medium">
        {{ formaZaDodavanjeUslugeOtvorena ? "Dodaj informacije o usluzi" : "Dodaj novu uslugu" }}
      </p>
    </div>
    <form
      v-if="formaZaDodavanjeUslugeOtvorena"
      class="p-4 rounded-lg shadow-md bg-white space-y-4 m-4"
      @submit.prevent="dodajUslugu"
    >
      <div class="flex items-center gap-x-4 justify-center py-2">
        <div class="relative w-20 h-20 group cursor-pointer">
          <input
            ref="odabirSlike"
            type="file"
            accept="image/*"
            class="hidden"
            @change="odaberiSlikuUsluge"
          />

          <img
            :src="lokalniPretpregled || 'https://placehold.co/80x80?text=SlikaUsluge'"
            alt="Slika usluge"
            class="w-full h-full object-cover rounded-lg transition duration-300"
            @click="odabirSlike?.click()"
          />

          <div
            class="absolute inset-0 flex items-center justify-center rounded-lg bg-black/30 opacity-0 group-hover:opacity-100 transition duration-300"
            @click="odabirSlike?.click()"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-10 w-10 text-white"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M15.232 5.232l3.536 3.536M9 13l6.768-6.768a2 2 0 112.828 2.828L11.828 16H9v-2.828z"
              />
            </svg>
          </div>
        </div>

        <p class="block text-sm font-medium">Dodajte sliku usluge</p>
      </div>

      <div class="flex flex-col items-center mt-2">
        <button
          class="w-full max-w-xs font-bold shadow-sm hover:bg-red-400 rounded-lg py-2 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
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
        <small class="pt-2 w-full max-w-xs text-xs"
          >Pritisnite gumb i popunite obrazac glasom npr. "Priprema tla pomoću oranja po cijeni od
          70 eura po metru kvadratnom..."</small
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
        <label class="block mb-1 text-sm font-medium text-gray-900"
          >Odaberi kategoriju usluge</label
        >
        <select
          v-model="forma.kategorija_id"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
        >
          <option :value="null">Odaberi...</option>
          <option v-for="k in ponudaFarmaPlus.kategorije" :key="k.id" :value="k.id">
            {{ k.naziv }}
          </option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium">Usluga</label>
        <input
          type="text"
          v-model.trim="forma.naziv"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          placeholder="Upiši naziv usluge..."
        />
      </div>
      <div>
        <label class="block mb-1 text-sm font-medium text-gray-900"
          >Odaberi mjernu jedinicu usluge</label
        >
        <select
          v-model="forma.mjerna_jedinica"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
        >
          <option>sat</option>
          <option>hektar</option>
          <option>m</option>
          <option>m2</option>
          <option>ral (jutro)</option>
          <option>kom</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-900">Trajanje po mjernoj jedinici</label>
        <div class="flex items-center gap-2">
          <input
            type="number"
            min="0"
            v-model.number="trajanje_s"
            class="mt-1 w-20 rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          />
          sat/i
          <input
            type="number"
            min="0"
            max="59"
            v-model.number="trajanje_m"
            class="w-20 mt-1 rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          />
          minuta
        </div>
        <small class="text-gray-500"
          >Unesite koliko vam vremena treba za 1 {{ forma.mjerna_jedinica }}</small
        >
      </div>
      <div>
        <label class="block text-sm font-medium">Cijena</label>
        <div class="flex items-center">
          <input
            type="number"
            v-model.number="forma.cijena"
            step="0.01"
            min="0"
            class="mt-1 w-xs rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
            placeholder="Upiši cijenu usluge npr. 23.99"
          />
          <p class="ms-2 text-xl">€</p>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <input id="dostupno" type="checkbox" v-model="forma.usluga_dostupna" />
        <label for="dostupno">Dostupan</label>
      </div>

      <div>
        <label class="block text-sm font-medium">Opis</label>
        <textarea
          rows="5"
          v-model.trim="forma.opis"
          class="mt-1 w-full rounded-md bg-white px-4 py-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          placeholder="Upiši opis usluge..."
        ></textarea>
      </div>

      <button
        type="submit"
        class="bg-teal-600 text-gray-100 px-4 py-2 rounded-xl hover:bg-teal-900 transition"
      >
        Dodaj uslugu
      </button>
    </form>

    <div
      v-if="ponudaFarmaPlus.usluge.length === 0"
      class="p-4 rounded-lg shadow-md bg-white space-y-4 m-4 text-center text-2xl text-gray-400"
    >
      Nemate usluga u ovoj kategoriji...
    </div>

    <table v-else class="w-full text-sm text-left rtl:text-right text-gray-500">
      <thead class="text-xs uppercase bg-gray-200 text-gray-700">
        <tr>
          <th scope="col" class="px-16 py-3"></th>
          <th scope="col" class="pe-6 py-3">Usluga</th>
          <th scope="col" class="px-6 py-3">Opis</th>
          <th scope="col" class="px-4 py-3">Dostupno</th>
          <th scope="col" class="px-6 py-3">Cijena</th>
          <th scope="col" class="px-6 py-3">Mjerna jedinica</th>
          <th scope="col" class="px-6 py-3">Trajanje / jedinica</th>
          <th scope="col" class="px-6 py-3"></th>
          <th scope="col" class="px-6 py-3"></th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="p in ponudaFarmaPlus.usluge"
          :key="p.id"
          class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]"
        >
          <td class="p-4">
            <div v-if="uredivanjeId === p.id" class="relative w-16 h-16 group">
              <input
                type="file"
                accept="image/*"
                class="hidden"
                :ref="'ucitajSliku' + p.id"
                @change="promijeniSliku(p, $event)"
              />
              <img
                :src="
                  p._lokalniUrl || p.slika_usluge || 'https://placehold.co/64x64?text=SlikaUsluge'
                "
                class="w-16 h-16 rounded-lg cursor-pointer"
                :alt="p.naziv"
                @click="$refs['ucitajSliku' + p.id][0].click()"
              />
              <div
                class="absolute inset-0 flex items-center justify-center bg-black/40 rounded-lg opacity-0 group-hover:opacity-100 cursor-pointer"
                @click="$refs['ucitajSliku' + p.id][0].click()"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15.232 5.232l3.536 3.536M9 13l6.768-6.768a2 2 0 112.828 2.828L11.828 16H9v-2.828z"
                  />
                </svg>
              </div>
            </div>

            <img
              v-else
              :src="p.slika_usluge || 'https://placehold.co/64x64?text=SlikaUsluge'"
              class="w-16 h-16 rounded-lg"
              :alt="p.naziv"
            />
          </td>

          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <template v-if="uredivanjeId === p.id">
              <input
                v-model.trim="urediFormu.naziv"
                class="w-40 rounded border border-yellow-500 px-2 py-1"
              />
            </template>
            <template v-else>{{ p.naziv }}</template>
          </td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <template v-if="uredivanjeId === p.id">
              <textarea
                v-model.trim="urediFormu.opis"
                rows="2"
                class="h-full w-50 rounded border border-yellow-500 px-2 py-1"
              ></textarea>
            </template>
            <template v-else>{{ p.opis }}</template>
          </td>
          <td class="px-4 py-4">
            <template v-if="uredivanjeId === p.id">
              <input type="checkbox" class="scale-150" v-model="urediFormu.usluga_dostupna" />
            </template>
            <template v-else>
              <input type="checkbox" class="scale-150" :checked="p.usluga_dostupna" disabled />
            </template>
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <template v-if="uredivanjeId === p.id">
              <input
                v-model.number="urediFormu.cijena"
                type="number"
                step="0.01"
                class="w-24 rounded border px-2 py1 border-yellow-500"
              />
            </template>
            <template v-else>{{ Number(p.cijena).toFixed(2) }} €</template>
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <template v-if="uredivanjeId === p.id">
              <select
                v-model="urediFormu.mjerna_jedinica"
                class="rounded border group-hover:text.gray-100 px-2 py-1 border-yellow-500"
              >
                <option class="text-gray-600">sat</option>
                <option class="text-gray-600">hektar</option>
                <option class="text-gray-600">m</option>
                <option class="text-gray-600">m2</option>
                <option class="text-gray-600">ral (jutro)</option>
                <option class="text-gray-600">kom</option>
              </select>
            </template>
            <template v-else>{{ p.mjerna_jedinica }}</template>
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <template v-if="uredivanjeId === p.id">
              <input
                type="time"
                step="60"
                v-model="urediFormu._trajanje_hhmm"
                class="w-28 rounded border px-2 py-1 border-yellow-500"
              />
            </template>
            <template v-else>
              {{
                p.trajanje_po_mjernoj_jedinici != null
                  ? String(Math.floor(p.trajanje_po_mjernoj_jedinici / 60)).padStart(2, "0") +
                    ":" +
                    String(p.trajanje_po_mjernoj_jedinici % 60).padStart(2, "0")
                  : "—"
              }}
            </template>
          </td>
          <template v-if="uredivanjeId === p.id">
            <td class="px-6 py-4">
              <button
                class="font-medium text-yellow-500 hover:underline"
                @click.prevent="spremiUredeno(p)"
              >
                Spremi
              </button>
            </td>
            <td class="px-6 py-4">
              <button
                class="font-medium text-gray-600 hover:underline group-hover:text-gray-100"
                @click.prevent="prekiniUredivanje"
              >
                Odustani
              </button>
            </td>
          </template>
          <template v-else>
            <td class="px-6 py-4">
              <button
                class="font-medium text-teal-500 hover:underline"
                @click.prevent="zapocniUredivanje(p)"
              >
                Uredi
              </button>
            </td>
            <td class="px-6 py-4">
              <button
                class="font-medium text-red-500 hover:underline"
                @click.prevent="obrisiUslugu(p)"
              >
                Obriši
              </button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup>
import { ref, reactive, onMounted, computed } from "vue"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import { usePonudaFarmaPlusStore } from "@/stores/ponudaFarmaPlus"
import { useUiStore } from "@/stores/ui"
import ProfilOpgPonudaFarmaPlusKalendar from "@/components/profili/opg/ProfilOpgPonudaFarmaPlusKalendar.vue"

const autentifikacija = useAutentifikacijskiStore()
const ponudaFarmaPlus = usePonudaFarmaPlusStore()

const ui = useUiStore()

const formaZaDodavanjeUslugeOtvorena = ref(false)

const trajanje_s = ref(0)
const trajanje_m = ref(0)

const otvoriFormuZaDodavanjeUsluge = () => {
  formaZaDodavanjeUslugeOtvorena.value = !formaZaDodavanjeUslugeOtvorena.value
}

const odabirSlike = ref(null)
const novaSlika = ref(null)
const lokalniPretpregled = ref(null)

const forma = reactive({
  naziv: "",
  opis: "",
  cijena: null,
  mjerna_jedinica: "hektar",
  usluga_dostupna: true,
  kategorija_id: null,
})

const aktivnaKategorijaId = computed(() => ponudaFarmaPlus.aktivnaKategorijaId)

const ukupnoDostupno = computed(() =>
  (ponudaFarmaPlus.kategorije || []).reduce(
    (sum, k) => sum + (k.dostupni ?? (k.ukupno || 0) - (k.nedostupni || 0)),
    0,
  ),
)

const ukupnoNedostupno = computed(() =>
  (ponudaFarmaPlus.kategorije || []).reduce((sum, k) => sum + (k.nedostupni || 0), 0),
)

onMounted(async () => {
  await ponudaFarmaPlus.ucitajKategorije()
  await ponudaFarmaPlus.ucitajUsluge()
})

function odaberiSlikuUsluge(e) {
  const f = e.target.files?.[0]
  if (!f) return
  if (lokalniPretpregled.value) URL.revokeObjectURL(lokalniPretpregled.value)
  novaSlika.value = f
  lokalniPretpregled.value = URL.createObjectURL(f)
}

async function promijeniSliku(p, e) {
  const f = e.target.files?.[0]
  if (!f) return
  if (p._lokalniUrl) URL.revokeObjectURL(p._lokalniUrl)
  p._novaSlika = f
  p._lokalniUrl = URL.createObjectURL(f)
}

async function dodajUslugu() {
  if (!forma.kategorija_id) return
  const kreirano = await ponudaFarmaPlus.dodajUslugu({
    ...forma,
    trajanje_po_mjernoj_jedinici: Math.max(
      0,
      (trajanje_s.value || 0) * 60 + (trajanje_m.value || 0),
    ),
    opg_id: autentifikacija.korisnicki_profil?.opg_id || autentifikacija.korisnicki_profil?.id,
  })
  if (novaSlika.value) {
    await ponudaFarmaPlus.ucitajSlikuUsluge(kreirano.id, novaSlika.value)
  }

  Object.assign(forma, {
    naziv: "",
    opis: "",
    cijena: null,
    mjerna_jedinica: "kg",
    usluga_dostupna: true,
    kategorija_id: null,
  })
  novaSlika.value = null
  lokalniPretpregled.value = null
  trajanje_s.value = 0
  trajanje_m = 0
  formaZaDodavanjeUslugeOtvorena.value = false
  ui.obavijest({ tekst: "Usluga je dodana.", tip_obavijesti: "uspjeh" })
}

async function filtrirajPoKategoriji(kid) {
  await ponudaFarmaPlus.ucitajUsluge(kid || null)
}

const uredivanjeId = ref(null)
const urediFormu = reactive({
  naziv: "",
  opis: "",
  cijena: null,
  mjerna_jedinica: "",
  usluga_dostupna: true,
  kategorija_id: null,
})

function zapocniUredivanje(p) {
  uredivanjeId.value = p.id
  Object.assign(urediFormu, {
    naziv: p.naziv,
    opis: p.opis,
    cijena: p.cijena,
    mjerna_jedinica: p.mjerna_jedinica,
    _trajanje_hhmm:
      p.trajanje_po_mjernoj_jedinici != null
        ? `${String(Math.floor(p.trajanje_po_mjernoj_jedinici / 60)).padStart(2, "0")}:${String(p.trajanje_po_mjernoj_jedinici % 60).padStart(2, "0")}`
        : "00:00",
    usluga_dostupna: p.usluga_dostupna,
    kategorija_id: p.kategorija_id,
  })
}

function prekiniUredivanje() {
  const p = ponudaFarmaPlus.usluge.find((x) => x.id === uredivanjeId.value)
  if (p?._lokalniUrl) {
    URL.revokeObjectURL(p._lokalniUrl)
    delete p._lokalniUrl
  }
  if (p?._novaSlika) {
    delete p._novaSlika
  }
  uredivanjeId.value = null
  ui.obavijest({ tekst: "Odustali ste od ažuriranja usluge.", tip_obavijesti: "informacija" })
}
async function spremiUredeno(p) {
  const [hh, mm] = (urediFormu._trajanje_hhmm || "00:00").split(":").map(Number)
  await ponudaFarmaPlus.urediUslugu(p.id, {
    naziv: urediFormu.naziv,
    opis: urediFormu.opis,
    cijena: urediFormu.cijena,
    mjerna_jedinica: urediFormu.mjerna_jedinica,
    usluga_dostupna: urediFormu.usluga_dostupna,
    kategorija_id: urediFormu.kategorija_id,
    trajanje_po_mjernoj_jedinici: (hh || 0) * 60 + (mm || 0),
  })
  if (p._novaSlika) {
    const res = await ponudaFarmaPlus.ucitajSlikuUsluge(p.id, p._novaSlika)
    if (res?.slika_usluge) p.slika_usluge = res.slika_usluge
    if (p._lokalniUrl) URL.revokeObjectURL(p._lokalniUrl)
    delete p._lokalniUrl
    delete p._novaSlika
  }
  uredivanjeId.value = null
  ui.obavijest({ tekst: "Usluga je ažurirana.", tip_obavijesti: "uspjeh" })
}

async function obrisiUslugu(p) {
  const potvrda = await ui.obavijestSaPotvrdom({
    naslov: "Obrisati uslugu?",
    poruka: `Usluga "${p.naziv}" bit će trajno uklonjena.`,
    tip_obavijesti: "upozorenje",
    potvrdiRadnju: "Obriši",
    odustaniOdRadnje: "Odustani",
  })
  if (!potvrda) return

  await ponudaFarmaPlus.obrisiUslugu(p.id)
  ui.obavijest({ tekst: "Usluga je obrisana.", tip_obavijesti: "uspjeh" })
}
</script>
