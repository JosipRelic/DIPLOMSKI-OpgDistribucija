<template>
  <section>
    <div class="mx-auto max-w-7xl px-5 py-10 md:px-10 md:py-12">
      <div class="grid grid-cols-1 items-center gap-8 sm:gap-14 lg:gap-20 md:grid-cols-2">
        <img
          :src="detalji_opga_s.opg?.slika_profila || defaultSlika"
          :alt="detalji_opga_s.opg?.naziv"
          class="inline-block aspect-4/3 w-full rounded-lg object-cover"
        />

        <div class="sm:max-w-sm md:max-w-md lg:max-w-lg">
          <div class="flex items-center mb-4">
            <p class="inline-block font-bold text-2xl mr-5">{{ detalji_opga_s.opg?.naziv }}</p>
            <div class="boder-none sm:border-l-2 border-black sm:pl-8">
              <div class="flex justify-center sm:justify-start">
                <h3 class="text-2xl font-semibold mr-2">
                  {{ (detalji_opga_s.opg?.prosjecna_ocjena ?? 0).toFixed(2) }}
                </h3>
                <div class="flex">
                  <svg
                    v-for="i in 5"
                    :key="i"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 36 36"
                    class="w-5 me-1"
                    :class="i <= zaokruzeno ? 'fill-orange-600' : 'fill-orange-200'"
                  >
                    <path
                      d="M27.287 34.627c-.404 0-.806-.124-1.152-.371L18 28.422l-8.135 5.834a1.97 1.97 0 0 1-2.312-.008a1.971 1.971 0 0 1-.721-2.194l3.034-9.792l-8.062-5.681a1.98 1.98 0 0 1-.708-2.203a1.978 1.978 0 0 1 1.866-1.363L12.947 13l3.179-9.549a1.976 1.976 0 0 1 3.749 0L23 13l10.036.015a1.975 1.975 0 0 1 1.159 3.566l-8.062 5.681l3.034 9.792a1.97 1.97 0 0 1-.72 2.194a1.957 1.957 0 0 1-1.16.379z"
                    />
                  </svg>
                </div>
              </div>
              <div class="text-sm text-gray-700">
                <template class="max-sm:hidden" v-if="detalji_opga_s.opg?.broj_recenzija > 0"
                  >Ocijenjeni od strane
                  <strong>{{ detalji_opga_s.opg.broj_recenzija }}</strong> korisnika.
                </template>
                <template v-else> Još nema recenzija. </template>
              </div>
            </div>
          </div>

          <p class="mb-6 max-w-md text-gray-500 md:mb-10 lg:mb-12">
            {{ detalji_opga_s.opg?.opis }}
          </p>
          <div class="flow-root">
            <dl class="-my-3 divide-y divide-gray-200 text-sm">
              <div class="grid grid-cols-1 gap-1 py-3 sm:grid-cols-3 sm:gap-4">
                <dt class="font-medium text-gray-900">Vlasnik</dt>

                <dd class="text-gray-700 sm:col-span-2">
                  {{ detalji_opga_s.opg?.ime }} {{ detalji_opga_s.opg?.prezime }}
                </dd>
              </div>
              <div class="grid grid-cols-1 gap-1 py-3 sm:grid-cols-3 sm:gap-4">
                <dt class="font-medium text-gray-900">Adresa</dt>

                <dd class="text-gray-700 sm:col-span-2">{{ punaAdresa }}</dd>
              </div>

              <div class="grid grid-cols-1 gap-1 py-3 sm:grid-cols-3 sm:gap-4">
                <dt class="font-medium text-gray-900">Email</dt>

                <dd class="text-teal-500 sm:col-span-2">
                  <a
                    class="hover:underline hover:text-teal-900"
                    :href="`mailto:${detalji_opga_s.opg?.email}`"
                    >{{ detalji_opga_s.opg?.email }}</a
                  >
                </dd>
              </div>

              <div class="grid grid-cols-1 gap-1 py-3 sm:grid-cols-3 sm:gap-4">
                <dt class="font-medium text-gray-900">Broj telefona</dt>

                <dd class="text-teal-500 sm:col-span-2">
                  <a
                    class="hover:underline hover:text-teal-900"
                    :href="`tel:${detalji_opga_s.opg?.broj_telefona}`"
                    >{{ detalji_opga_s.opg?.broj_telefona }}</a
                  >
                </dd>
              </div>
            </dl>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="mx-auto max-w-7xl px-10 pb-4">
      <span class="flex items-center mt-6">
        <span class="shrink-0 pe-4 text-orange-600 text-2xl font-extrabold">PONUDA</span>

        <span class="h-px flex-1 bg-orange-300"></span>
      </span>
      <div class="text-sm font-medium text-center text-gray-600 mt-3">
        <ul class="flex flex-wrap -mb-px">
          <li class="me-2">
            <button
              @click="prikaziTab('proizvodi')"
              :class="[
                'inline-block p-4 rounded-t-lg border-b-2 cursor-pointer text-lg text-gray-900 font-medium',
                aktivniTab === 'proizvodi'
                  ? 'text-orange-600 border-orange-600'
                  : 'hover:text-orange-900 hover:border-orange-900 border-transparent',
              ]"
            >
              <div class="flex itmes-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="mr-3"
                  width="30"
                  height="30"
                  viewBox="0 0 48 48"
                >
                  <g fill="currentColor">
                    <path d="M22.5 28a1.5 1.5 0 1 1 0-3a1.5 1.5 0 0 1 0 3Z" />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="1.5"
                      fill-rule="evenodd"
                      d="M9.429 20c.194 0 .385-.016.571-.048V28H7.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h33a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5H38v-8.048c.186.032.377.048.571.048C40.473 20 42 18.448 42 16.551v-2.39a2.73 2.73 0 0 0-.163-.93l-2.18-6.01A1.85 1.85 0 0 0 37.917 6H10.082a1.85 1.85 0 0 0-1.738 1.222l-2.18 6.009a2.728 2.728 0 0 0-.164.93v2.39C6 18.448 7.527 20 9.429 20Zm-1.385-6.087L10.189 8H37.81l2.145 5.913c.03.08.044.163.044.248v2.39A1.44 1.44 0 0 1 38.57 18c-.78 0-1.428-.64-1.428-1.449a1 1 0 0 0-2 0A1.44 1.44 0 0 1 33.713 18c-.78 0-1.428-.64-1.428-1.448a1 1 0 0 0-2 0c0 .808-.648 1.448-1.429 1.448s-1.428-.64-1.428-1.449a1 1 0 1 0-2 0A1.439 1.439 0 0 1 24 18a1.44 1.44 0 0 1-1.429-1.448a1 1 0 0 0-2 0c0 .808-.647 1.448-1.428 1.448c-.781 0-1.429-.64-1.429-1.449a1 1 0 1 0-2 0c0 .808-.647 1.449-1.428 1.449c-.781 0-1.429-.64-1.429-1.449a1 1 0 1 0-2 0c0 .808-.647 1.449-1.428 1.449C8.647 18 8 17.36 8 16.551v-2.39a.72.72 0 0 1 .044-.248ZM36 19.122a3.401 3.401 0 0 1-2.286.878a3.404 3.404 0 0 1-2.428-1.014A3.404 3.404 0 0 1 28.857 20a3.404 3.404 0 0 1-2.428-1.014A3.404 3.404 0 0 1 24 20a3.404 3.404 0 0 1-2.429-1.014A3.404 3.404 0 0 1 19.143 20c-.951 0-1.81-.389-2.429-1.014A3.404 3.404 0 0 1 14.286 20c-.88 0-1.68-.333-2.286-.878V28h2.5a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v.5h1.5a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5H36v-8.878ZM8 33a1 1 0 0 1 1-1h30a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-8Zm2 7v-6h28v6H10Z"
                      clip-rule="evenodd"
                    />
                  </g>
                </svg>
                E-Tržnica
              </div>
            </button>
          </li>

          <li class="me-2">
            <button
              @click="prikaziTab('usluge')"
              :class="[
                'inline-block p-4 rounded-t-lg border-b-2 cursor-pointer text-lg text-gray-900 font-medium',
                aktivniTab === 'usluge'
                  ? 'text-orange-600 border-orange-600'
                  : 'hover:text-orange-900 hover:border-orange-900 border-transparent',
              ]"
            >
              <div class="flex items-center">
                <svg
                  class="mr-3 stroke-gray-900"
                  xmlns="http://www.w3.org/2000/svg"
                  width="30"
                  height="30"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1.5"
                    d="M8 14V4.5a2.5 2.5 0 0 0-5 0V14m5-6l6-5l8 6m-2-5v10m-8-4h4v4h-4zM2 14h20M2 22l5-8m0 8l5-8m10 8H12l5-8m-2 4h7"
                  />
                </svg>
                Farma+
              </div>
            </button>
          </li>
        </ul>
        <ul class="flex ms-4 mb-3 flex-wrap -mb-px">
          <li>
            <div v-if="aktivniTab === 'proizvodi'" class="mt-4 flex flex-wrap gap-2">
              <button
                @click="klikKategorijaProizvoda(null)"
                :class="[
                  'px-3 py-1.5 rounded-full border text-sm shadow-md text-[#223c2f]',
                  detalji_opga_s.aktivnaKatProizvoda === null
                    ? 'bg-[#223c2f] text-white border-[#223c2f] shadow-[#223c2f]'
                    : 'border-gray-200 hover:bg-[#223c2f] hover:text-white hover:border-[#223c2f]',
                ]"
              >
                Sve
                <span v-if="detalji_opga_s.proizvodi.ukupno_proizvoda" class="opacity-70"
                  >({{ detalji_opga_s.proizvodi.ukupno_proizvoda }})</span
                >
              </button>

              <button
                v-for="k in detalji_opga_s.katProizvodi"
                :key="k.slug"
                @click="klikKategorijaProizvoda(k.slug)"
                :class="[
                  'px-3 py-1.5 rounded-full border shadow-md text-sm',
                  detalji_opga_s.aktivnaKatProizvoda === k.slug
                    ? 'bg-[#223c2f] text-white border-[#223c2f] shadow-[#223c2f]'
                    : 'border-gray-200 hover:bg-[#223c2f] hover:text-white hover:border-[#223c2f]',
                ]"
              >
                {{ k.naziv }} <span class="opacity-70">({{ k.broj }})</span>
              </button>
            </div>
          </li>

          <li>
            <div v-if="aktivniTab === 'usluge'" class="mt-4 flex flex-wrap gap-2">
              <button
                @click="klikKategorijaUsluge(null)"
                :class="[
                  'px-3 py-1.5 rounded-full border shadow-md text-sm',
                  detalji_opga_s.aktivnaKatUsluge === null
                    ? 'bg-[#223c2f] text-white border-[#223c2f] shadow-[#223c2f]'
                    : 'border-gray-200 hover:bg-[#223c2f] hover:text-white hover:border-[#223c2f]',
                ]"
              >
                Sve
                <span v-if="detalji_opga_s.usluge.ukupno_usluga" class="opacity-70"
                  >({{ detalji_opga_s.usluge.ukupno_usluga }})</span
                >
              </button>

              <button
                v-for="k in detalji_opga_s.katUsluge"
                :key="k.slug"
                @click="klikKategorijaUsluge(k.slug)"
                :class="[
                  'px-3 py-1.5 rounded-full border shadow-md text-sm',
                  detalji_opga_s.aktivnaKatUsluge === k.slug
                    ? 'bg-[#223c2f] text-white border-[#223c2f] shadow-[#223c2f]'
                    : 'border-gray-200 hover:bg-[#223c2f] hover:text-white hover:border-[#223c2f]',
                ]"
              >
                {{ k.naziv }} <span class="opacity-70">({{ k.broj }})</span>
              </button>
            </div>
          </li>
        </ul>
      </div>

      <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4 py-6">
        <template v-if="aktivniTab === 'proizvodi'">
          <div
            v-if="detalji_opga_s.proizvodi.loading"
            class="col-span-full text-center text-gray-500 py-10"
          >
            Učitavanje…
          </div>
          <div
            v-else-if="detalji_opga_s.proizvodi.lista_proizvoda.length === 0"
            class="col-span-full text-center text-gray-500 py-10"
          >
            Nema proizvoda.
          </div>
          <KarticaProizvoda
            v-else
            v-for="p in detalji_opga_s.proizvodi.lista_proizvoda"
            :key="p.id"
            :proizvod="p"
            :kat-slug="detalji_opga_s.aktivnaKatProizvoda || p.kategorija_slug"
            :prikazi-link-prema-opgu="false"
          />
        </template>

        <template v-else>
          <div
            v-if="detalji_opga_s.usluge.loading"
            class="col-span-full text-center text-gray-500 py-10"
          >
            Učitavanje…
          </div>
          <div
            v-else-if="detalji_opga_s.usluge.lista_usluga.length === 0"
            class="col-span-full text-center text-gray-500 py-10"
          >
            Nema usluga.
          </div>
          <KarticaUsluge
            v-else
            v-for="u in detalji_opga_s.usluge.lista_usluga"
            :key="u.id"
            :usluga="u"
            :prikazi-ponudaca-usluge="false"
            :override-ima-termina="opgImaTermina"
          />
        </template>
      </div>
      <span class="flex items-center">
        <span class="h-px mt-6 mb-4 flex-1 bg-orange-300"></span>
      </span>
    </div>
  </section>

  <RecenzijeOPG />
</template>
<script setup>
import { onMounted, computed, ref } from "vue"
import { useRoute } from "vue-router"
import { useEtrznicaOpgDetaljiStore } from "@/stores/eTrznicaOpgDetalji"
import KarticaProizvoda from "@/components/dijeljeno/KarticaProizvoda.vue"
import KarticaUsluge from "@/components/dijeljeno/KarticaUsluge.vue"
import RecenzijeOPG from "@/components/etrznica/opgovi/RecenzijeOPG.vue"
import api from "@/services/api"

const route = useRoute()
const slug = computed(() => route.params.opgSlug)

const detalji_opga_s = useEtrznicaOpgDetaljiStore()
const aktivniTab = ref("proizvodi")

const opgImaTermina = ref(null)

async function provjeriOpgTermine(opgId, horizon = 3) {
  if (!opgId) {
    opgImaTermina.value = false
    return
  }
  const now = new Date()
  let found = false
  for (let i = 0; i < horizon; i++) {
    const d = new Date(now.getFullYear(), now.getMonth() + i, 1)
    try {
      const { data } = await api.get("/opg/raspolozivost/kalendar", {
        params: { opg_id: opgId, godina: d.getFullYear(), mjesec: d.getMonth() + 1 },
      })
      if (data?.slotovi && Object.keys(data.slotovi).length > 0) {
        found = true
        break
      }
    } catch (_) {}
  }
  opgImaTermina.value = found
}

onMounted(async () => {
  await detalji_opga_s.ucitajDetaljeOpga(slug.value)
  if (detalji_opga_s.nijePronadeno) return

  await provjeriOpgTermine(detalji_opga_s.opg?.id)
  await Promise.all([
    detalji_opga_s.ucitajKategorijeProizvoda(slug.value),
    detalji_opga_s.ucitajKategorijeUsluga(slug.value),
    detalji_opga_s.ucitajRecenzije(slug.value),
  ])

  await detalji_opga_s.ucitajProizvode(slug.value)
})

function klikKategorijaProizvoda(katSlug) {
  detalji_opga_s.postaviAktivnuKatProizvoda(katSlug, slug.value)
}

function klikKategorijaUsluge(katSlug) {
  detalji_opga_s.postaviAktivnuKatUsluge(katSlug, slug.value)
}

function prikaziTab(tab) {
  aktivniTab.value = tab
  if (tab === "proizvodi" && detalji_opga_s.proizvodi.lista_proizvoda.length === 0) {
    detalji_opga_s.ucitajProizvode(slug.value)
  }
  if (tab === "usluge" && detalji_opga_s.usluge.lista_usluga.length === 0) {
    detalji_opga_s.ucitajUsluge(slug.value)
  }
}

const zaokruzeno = computed(() => Math.round(detalji_opga_s.opg?.prosjecna_ocjena ?? 0))
const punaAdresa = computed(() => {
  if (!detalji_opga_s.opg) return ""
  const adresa = [
    detalji_opga_s.opg.adresa,
    [detalji_opga_s.opg.postanski_broj, detalji_opga_s.opg.grad].filter(Boolean).join(" "),
  ].filter(Boolean)
  return adresa.join(", ")
})

const defaultSlika = "https://placehold.co/800x600?text=OPG"
</script>
