<template>
  <div class="relative overflow-x-auto m-4 shadow-md rounded-lg">
    <div class="bg-white pt-2 px-4 flex flex-items justify-center pt-5">
      <p class="text-green-600 pe-2">(Dostupno proizvoda)</p>
      <p class="text-red-400 pe-2">(Nema dostupnih proizvoda)</p>
      <p class="text-yellow-500 pe-2">(Proizvod postoji, ali je javno nedostupan)</p>
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
        v-for="k in ponudaEtrznica.kategorije"
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
      @click="otvoriFormuZaDodavanjeProizvoda"
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
        {{
          formaZaDodavanjeProizvodaOtvorena
            ? "Dodaj informacije o proizvodu"
            : "Dodaj novi proizvod"
        }}
      </p>
    </div>
    <form
      v-if="formaZaDodavanjeProizvodaOtvorena"
      class="p-4 rounded-lg shadow-md bg-white space-y-4 m-4"
      @submit.prevent="dodajProizvod"
    >
      <div class="flex items-center gap-x-4 justify-center py-2">
        <div class="relative w-20 h-20 group cursor-pointer">
          <input
            type="file"
            accept="image/*"
            class="hidden"
            ref="odabirSlike"
            @change="odaberiSlikuProizvoda"
          />

          <img
            :src="lokalniPretpregled || 'https://placehold.co/80x80?text=SlikaProizvoda'"
            alt="Slika proizvoda"
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

        <p class="block text-sm font-medium">Dodajte sliku proizvoda</p>
      </div>

      <div class="flex flex-col items-center mt-2">
        <GumbZaGlasovnoPopunjavanje strukturaUpita="novi_proizvod" @popuni="popuniFormuPomocuAI" />
        <small class="pt-2 w-full max-w-xs text-xs"
          >Pritisnite gumb i popunite obrazac glasom npr. "Svježi krastavci s naših polja po cijeni
          od 2 eura po kg..."</small
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
        <label class="block mb-2 text-sm font-medium text-gray-900"
          >Odaberi kategoriju proizvoda</label
        >
        <select
          v-model="forma.kategorija_id"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
        >
          <option :value="null">Odaberi...</option>
          <option v-for="k in ponudaEtrznica.kategorije" :key="k.id" :value="k.id">
            {{ k.naziv }}
          </option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium">Proizvod</label>
        <input
          type="text"
          v-model.trim="forma.naziv"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          placeholder="Upiši naziv proizvoda..."
        />
      </div>
      <div>
        <label class="block mb-2 text-sm font-medium text-gray-900"
          >Odaberi mjernu jedinicu proizvoda</label
        >
        <select
          v-model="forma.mjerna_jedinica"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
        >
          <option>kom</option>
          <option>kg</option>
          <option>g</option>
          <option>ml</option>
          <option>l</option>
        </select>
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
            placeholder="Upiši cijenu proizvoda npr. 3.99"
          />
          <p class="ms-2 text-xl">€</p>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <input id="dostupno" type="checkbox" v-model="forma.proizvod_dostupan" />
        <label for="dostupno">Dostupan</label>
      </div>

      <div>
        <label class="block text-sm font-medium">Opis</label>
        <textarea
          rows="5"
          v-model.trim="forma.opis"
          class="mt-1 w-full rounded-md bg-white px-4 py-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          placeholder="Upiši opis proizvoda..."
        ></textarea>
      </div>

      <button
        type="submit"
        class="bg-teal-600 text-gray-100 px-4 py-2 rounded-xl hover:bg-teal-900 transition"
      >
        Dodaj proizvod
      </button>
    </form>

    <div
      v-if="ponudaEtrznica.proizvodi.length === 0"
      class="p-4 rounded-lg shadow-md bg-white space-y-4 m-4 text-center text-2xl text-gray-400"
    >
      Nemate proizvoda u ovoj kategoriji...
    </div>

    <table v-else class="w-full text-sm text-center rtl:text-right text-gray-500">
      <thead class="text-xs uppercase bg-gray-200 text-gray-700">
        <tr>
          <th scope="col" class="px-16 py-3"></th>
          <th scope="col" class="pe-6 py-3">Proizvod</th>
          <th scope="col" class="px-6 py-3">Opis</th>
          <th scope="col" class="px-4 py-3">Dostupno</th>
          <th scope="col" class="px-6 py-3">Cijena</th>
          <th scope="col" class="px-6 py-3">Mjerna jedinica</th>
          <th scope="col" class="px-6 py-3"></th>
          <th scope="col" class="px-6 py-3"></th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="p in ponudaEtrznica.proizvodi"
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
                  p._lokalniUrl ||
                  p.slika_proizvoda ||
                  'https://placehold.co/64x64?text=SlikaProizvoda'
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
              :src="p.slika_proizvoda || 'https://placehold.co/64x64?text=SlikaProizvoda'"
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
              <input type="checkbox" class="scale-150" v-model="urediFormu.proizvod_dostupan" />
            </template>
            <template v-else>
              <input type="checkbox" class="scale-150" :checked="p.proizvod_dostupan" disabled />
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
          <td class="px-6 py-4 font-semibold group-hover:text-gray-100">
            <template v-if="uredivanjeId === p.id">
              <select
                v-model="urediFormu.mjerna_jedinica"
                class="rounded border group-hover:text.gray-100 px-2 py-1 border-yellow-500"
              >
                <option class="text-gray-600">kom</option>
                <option class="text-gray-600">kg</option>
                <option class="text-gray-600">g</option>
                <option class="text-gray-600">ml</option>
                <option class="text-gray-600">l</option>
              </select>
            </template>
            <template v-else>{{ p.mjerna_jedinica }}</template>
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
                @click.prevent="obrisiProizvod(p)"
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
import { usePonudaEtrznicaStore } from "@/stores/ponudaEtrznica"
import { useUiStore } from "@/stores/ui"
import GumbZaGlasovnoPopunjavanje from "@/components/ai/GumbZaGlasovnoPopunjavanje.vue"
import { primijeniPodatkeOdAIuFormu } from "@/ai/primijeniPodatkeOdAIuFormu"

const autentifikacija = useAutentifikacijskiStore()
const ponudaEtrznica = usePonudaEtrznicaStore()
const ui = useUiStore()

const formaZaDodavanjeProizvodaOtvorena = ref(false)

const otvoriFormuZaDodavanjeProizvoda = () => {
  formaZaDodavanjeProizvodaOtvorena.value = !formaZaDodavanjeProizvodaOtvorena.value
}

const odabirSlike = ref(null)
const novaSlika = ref(null)
const lokalniPretpregled = ref(null)

const forma = reactive({
  naziv: "",
  opis: "",
  cijena: null,
  mjerna_jedinica: "kg",
  proizvod_dostupan: true,
  kategorija_id: null,
})

const aktivnaKategorijaId = computed(() => ponudaEtrznica.aktivnaKategorijaId)

const ukupnoDostupno = computed(() =>
  (ponudaEtrznica.kategorije || []).reduce(
    (sum, k) => sum + (k.dostupni ?? (k.ukupno || 0) - (k.nedostupni || 0)),
    0,
  ),
)

const ukupnoNedostupno = computed(() =>
  (ponudaEtrznica.kategorije || []).reduce((sum, k) => sum + (k.nedostupni || 0), 0),
)

onMounted(async () => {
  await ponudaEtrznica.ucitajKategorije()
  await ponudaEtrznica.ucitajProizvode()
})

function odaberiSlikuProizvoda(e) {
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

async function dodajProizvod() {
  if (!forma.kategorija_id) return
  const kreirano = await ponudaEtrznica.dodajProizvod({
    ...forma,
    opg_id: autentifikacija.korisnicki_profil?.opg_id || autentifikacija.korisnicki_profil?.id,
  })
  if (novaSlika.value) {
    await ponudaEtrznica.ucitajSlikuProizvoda(kreirano.id, novaSlika.value)
  }

  Object.assign(forma, {
    naziv: "",
    opis: "",
    cijena: null,
    mjerna_jedinica: "kg",
    proizvod_dostupan: true,
    kategorija_id: null,
  })
  novaSlika.value = null
  lokalniPretpregled.value = null
  formaZaDodavanjeProizvodaOtvorena.value = false
  ui.obavijest({ tekst: "Proizvod je dodan.", tip_obavijesti: "uspjeh" })
}

async function filtrirajPoKategoriji(kid) {
  await ponudaEtrznica.ucitajProizvode(kid || null)
}

const uredivanjeId = ref(null)
const urediFormu = reactive({
  naziv: "",
  opis: "",
  cijena: null,
  mjerna_jedinica: "",
  proizvod_dostupan: true,
  kategorija_id: null,
})

function zapocniUredivanje(p) {
  uredivanjeId.value = p.id
  Object.assign(urediFormu, {
    naziv: p.naziv,
    opis: p.opis,
    cijena: p.cijena,
    mjerna_jedinica: p.mjerna_jedinica,
    proizvod_dostupan: p.proizvod_dostupan,
    kategorija_id: p.kategorija_id,
  })
}

function prekiniUredivanje() {
  const p = ponudaEtrznica.proizvodi.find((x) => x.id === uredivanjeId.value)
  if (p?._lokalniUrl) {
    URL.revokeObjectURL(p._lokalniUrl)
    delete p._lokalniUrl
  }
  if (p?._novaSlika) {
    delete p._novaSlika
  }
  uredivanjeId.value = null
  ui.obavijest({ tekst: "Odustali ste od ažuriranja proizvoda.", tip_obavijesti: "informacija" })
}

async function spremiUredeno(p) {
  await ponudaEtrznica.urediProizvod(p.id, { ...urediFormu })
  if (p._novaSlika) {
    const res = await ponudaEtrznica.ucitajSlikuProizvoda(p.id, p._novaSlika)
    if (res?.slika_proizvoda) p.slika_proizvoda = res.slika_proizvoda
    if (p._lokalniUrl) URL.revokeObjectURL(p._lokalniUrl)
    delete p._lokalniUrl
    delete p._novaSlika
  }
  uredivanjeId.value = null
  ui.obavijest({ tekst: "Proizvod je ažuriran.", tip_obavijesti: "uspjeh" })
}

async function obrisiProizvod(p) {
  const potvrda = await ui.obavijestSaPotvrdom({
    naslov: "Obrisati proizvod?",
    poruka: `Proizvod "${p.naziv}" bit će trajno uklonjen.`,
    tip_obavijesti: "upozorenje",
    potvrdiRadnju: "Obriši",
    odustaniOdRadnje: "Odustani",
  })
  if (!potvrda) return
  await ponudaEtrznica.obrisiProizvod(p.id)
  ui.obavijest({ tekst: "Proizvod je obrisan.", tip_obavijesti: "uspjeh" })
}

function normalizirajMjernuJedinicuProizvoda(mj) {
  const s = String(mj || "").toLowerCase()
  if (["kom", "komad", "komada"].includes(s)) return "kom"
  if (["kg", "kilogram", "kilograma"].includes(s)) return "kg"
  if (["g", "gram", "grama"].includes(s)) return "g"
  if (["l", "litar", "litra", "litara"].includes(s)) return "l"
  if (["ml", "mililitar", "mililitra", "mililitara"].includes(s)) return "ml"
  return forma.mjerna_jedinica
}

function popuniFormuPomocuAI({ podaci }) {
  const sp = { ...(podaci || {}) }

  if (sp.kategorija && !sp.kategorija_id) {
    const kat = (ponudaEtrznica.kategorije || []).find(
      (k) => k.naziv?.toLowerCase() === String(sp.kategorija).toLowerCase(),
    )
    if (kat) sp.kategorija_id = kat.id
  }
  if (sp.mjerna_jedinica)
    sp.mjerna_jedinica = normalizirajMjernuJedinicuProizvoda(sp.mjerna_jedinica)

  const formaAI = { ...forma }
  primijeniPodatkeOdAIuFormu(formaAI, sp)
  Object.assign(forma, formaAI)
}
</script>
