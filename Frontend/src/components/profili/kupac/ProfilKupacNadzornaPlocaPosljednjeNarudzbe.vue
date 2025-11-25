<template>
  <section
    class="relative isolate py-16 sm:py-24 bg-white rounded-md shadow-lg max-w-7xl mx-auto mb-6"
  >
    <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-4xl sm:text-5xl font-extrabold tracking-tight text-gray-700 pb-5">
          Posljednje naručeno
        </h2>

        <router-link :to="{ name: 'profilKupacMojeNarudzbe' }">
          <button
            class="bg-orange-500 text-white shadow-sm px-8 py-3 rounded-md hover:bg-orange-900 cursor-pointer"
          >
            Pogledaj sve narudžbe
          </button>
        </router-link>
      </div>

      <p class="mt-14 text-xl text-gray-600 font-semibold">Proizvodi</p>
      <div class="mt-2 grid gap-6 sm:gap-8 md:grid-cols-2 lg:grid-cols-3">
        <router-link
          v-for="p in proizvodi"
          :key="`p-${p.stavka_id}`"
          :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe', params: { id: p.narudzba_id } }"
        >
          <article
            class="group relative overflow-hidden rounded-2xl bg-orange-500 shadow-2xl ring-1 ring-white/10 hover:ring-white/20"
          >
            <div class="relative aspect-[4/3]">
              <img
                :src="p.slika || defaultProizvod"
                :alt="p.naziv"
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
              />
              <div
                class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-900/10 to-transparent"
              ></div>
            </div>

            <div class="pointer-events-none absolute inset-x-0 bottom-0 p-5 sm:p-6">
              <div class="flex items-center gap-3 text-sm text-slate-300/90">
                <time :datetime="p.datum_izrade" class="font-medium">{{
                  fmtDatum(p.datum_izrade)
                }}</time>
                <span aria-hidden="true">•</span>
                <div class="flex items-center gap-2">
                  <img
                    :src="p.opg_slika || defaultOpg"
                    :alt="p.opg_naziv"
                    class="h-6 w-6 rounded-full object-cover ring-1 ring-white/20"
                  />
                  <span class="font-medium">{{ p.opg_naziv }}</span>
                </div>
              </div>

              <h3 class="mt-3 text-lg font-semibold leading-snug text-white">
                <p class="pointer-events-auto underline-offset-4 hover:underline">
                  {{ p.naziv }} - {{ p.kolicina }} {{ p.mjerna_jedinica }} - {{ fmtEUR(p.cijena) }}
                </p>
              </h3>
            </div>
          </article>
        </router-link>

        <div
          v-if="!loading && !proizvodi.length"
          class="col-span-full text-center text-gray-500 py-8"
        >
          Nema nedavnih proizvoda.
        </div>
      </div>

      <p class="mt-14 text-xl text-gray-600 font-semibold">Usluge</p>
      <div class="mt-2 grid gap-6 sm:gap-8 md:grid-cols-2 lg:grid-cols-3">
        <router-link
          v-for="u in usluge"
          :key="`u-${u.stavka_id}`"
          :to="{ name: 'profilKupacMojeNarudzbeDetaljiNarudzbe', params: { id: u.narudzba_id } }"
        >
          <article
            class="group relative overflow-hidden rounded-2xl bg-orange-500 shadow-2xl ring-1 ring-white/10 hover:ring-white/20"
          >
            <div class="relative aspect-[4/3]">
              <img
                :src="u.slika || defaultUsluga"
                :alt="u.naziv"
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
              />
              <div
                class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-900/10 to-transparent"
              ></div>
            </div>

            <div class="pointer-events-none absolute inset-x-0 bottom-0 p-5 sm:p-6">
              <div class="flex items-center gap-3 text-sm text-slate-300/90">
                <time :datetime="u.datum_izrade" class="font-medium">{{
                  fmtDatum(u.datum_izrade)
                }}</time>
                <span aria-hidden="true">•</span>
                <div class="flex items-center gap-2">
                  <img
                    :src="u.opg_slika || defaultOpg"
                    :alt="u.opg_naziv"
                    class="h-6 w-6 rounded-full object-cover ring-1 ring-white/20"
                  />
                  <span class="font-medium">{{ u.opg_naziv }}</span>
                </div>
              </div>

              <h3 class="mt-3 text-lg font-semibold leading-snug text-white">
                <p class="pointer-events-auto underline-offset-4 hover:underline">
                  {{ u.naziv }} - {{ u.kolicina }} {{ u.mjerna_jedinica }} - {{ fmtEUR(u.cijena) }}
                </p>
              </h3>
            </div>
          </article>
        </router-link>

        <div v-if="!loading && !usluge.length" class="col-span-full text-center text-gray-500 py-8">
          Nema nedavnih usluga.
        </div>
      </div>

      <div v-if="loading" class="text-center text-gray-500 py-10">Učitavanje…</div>
    </div>
  </section>
</template>

<script setup>
import { useNadzornaPlocaKupacStore } from "@/stores/nadzornaPlocaKupac"
import { onMounted, computed } from "vue"

const nadzorna = useNadzornaPlocaKupacStore()

onMounted(() => nadzorna.ucitaj())

const loading = computed(() => nadzorna.loading)
const proizvodi = computed(() => nadzorna.posljednje?.proizvodi ?? [])
const usluge = computed(() => nadzorna.posljednje?.usluge ?? [])

const defaultOpg = "https://placehold.co/80x80?text=OPG"
const defaultProizvod = "https://placehold.co/800x600?text=Proizvod"
const defaultUsluga = "https://placehold.co/800x600?text=Usluga"

function fmtEUR(v) {
  return `${Number(v || 0).toFixed(2)} €`
}
function fmtDatum(iso) {
  if (!iso) return ""
  const d = new Date(iso)
  return isNaN(d)
    ? ""
    : d.toLocaleDateString("hr-HR", { day: "2-digit", month: "short", year: "numeric" })
}
</script>
