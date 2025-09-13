<template>
  <section v-if="kategorije_s.aktivna">
    <KategorijeProizvodaProizvodiNaslovna
      :naziv_kategorije="kategorije_s.aktivna.naziv"
      :opis="kategorije_s.aktivna.opis"
      :slika="kategorije_s.aktivna.slika_kategorije"
    />
  </section>

  <section>
    <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
      <div
        v-if="proizvodi_s.loading"
        class="py-8 text-center text-gray-500 col-span-full mx-auto text-lg font-semibold"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="80"
          height="80"
          viewBox="0 0 24 24"
          fill="#000000"
          class="mx-auto"
        >
          <g fill="#000000">
            <path
              d="M8.55 10.55a1 1 0 1 1-2 0a1 1 0 0 1 2 0Zm2 1a1 1 0 1 0 0-2a1 1 0 0 0 0 2Zm3 0a1 1 0 1 0 0-2a1 1 0 0 0 0 2Z"
            />
            <path
              fill-rule="evenodd"
              d="M16.207 4.893a8.001 8.001 0 0 1 .662 10.565c.016.013.03.027.045.042l4.243 4.243a1 1 0 0 1-1.414 1.414L15.5 16.914a.933.933 0 0 1-.042-.045A8.001 8.001 0 0 1 4.893 4.893a8 8 0 0 1 11.314 0Zm-9.9 9.9a6 6 0 1 0 8.486-8.485a6 6 0 0 0-8.485 8.485Z"
              clip-rule="evenodd"
            />
          </g>
        </svg>
        Učitavanje…
      </div>

      <div
        v-else
        class="mt-4 lg:mt-8 grid grid-cols-1 gap-8"
        :class="!proizvodi_s.kategorijaPrazna ? 'lg:grid-cols-4' : 'lg:grid-cols-1'"
      >
        <KategorijeProizvodaProizvodiFilteri v-if="!proizvodi_s.kategorijaPrazna" />

        <div class="lg:col-span-3">
          <div
            class="grid grid-cols-1 max-sm:grid-cols-2 sm:grid-cols-2 md:grid-cols-3 gap-6 px-4 py-8 mb-14"
          >
            <div
              v-if="proizvodi_s.kategorijaPrazna"
              class="col-span-full rounded-lg border border-dashed border-gray-300 p-10 mt-4 text-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="200"
                height="200"
                viewBox="0 0 24 24"
                fill="currentColor"
                class="mx-auto"
              >
                <g fill="none" fill-rule="evenodd">
                  <path
                    d="m12.594 23.258l-.012.002l-.071.035l-.02.004l-.014-.004l-.071-.036q-.016-.004-.024.006l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.016-.018m.264-.113l-.014.002l-.184.093l-.01.01l-.003.011l.018.43l.005.012l.008.008l.201.092q.019.005.029-.008l.004-.014l-.034-.614q-.005-.019-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.003-.011l.018-.43l-.003-.012l-.01-.01z"
                  />
                  <path
                    fill="currentColor"
                    d="M11.084 3.244a3 3 0 0 1 1.607-.063l.225.063L19.45 5.34c.19.063.361.181.486.346l.07.105l2.75 4.747a1 1 0 0 1-.44 1.407l-.12.047l-2.051.658v4.33a2 2 0 0 1-1.237 1.848l-.152.056l-5.84 1.872a3 3 0 0 1-1.607.063l-.225-.062l-5.84-1.873a2 2 0 0 1-1.382-1.743l-.007-.162V12.65l-2.051-.658a1 1 0 0 1-.617-1.338l.057-.116l2.75-4.747a1 1 0 0 1 .445-.406l.11-.045zM13 12.305v6.324l5.145-1.65v-3.687l-3.09.991a1 1 0 0 1-1.106-.353l-.064-.098zm-2 0l-.885 1.527a1 1 0 0 1-1.17.451l-3.09-.991v3.687L11 18.63zM5.32 7.49l-1.723 2.977l5.191 1.666l1.725-2.977zm13.36 0l-5.193 1.666l1.724 2.977l5.192-1.666zm-6.375-2.342a1 1 0 0 0-.49-.03l-.12.03L8.13 6.292L12 7.533l3.87-1.241z"
                  />
                </g>
              </svg>
              <h3 class="text-lg font-semibold text-gray-900 mb-2">
                Trenutno nemamo proizvoda u ovoj kategoriji...
              </h3>
              <p class="text-gray-600">Istražite neku drugu kategoriju ili se vratite kasnije.</p>
            </div>

            <div
              v-else-if="proizvodi_s.nemaRezultata"
              class="col-span-full rounded-lg border border-dashed border-gray-300 p-10 mt-4 text-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="80"
                height="80"
                class="mx-auto"
                viewBox="0 0 512 512"
              >
                <path
                  fill="#000000"
                  fill-rule="evenodd"
                  d="m310.109 279.878l142.31 142.309l-30.17 30.17l-139.292-139.293l-5.623 6.874v149.334h-42.667V319.938h-.448L42.667 85.272L64 85.27l25.752-25.75zM175.841 85.271h293.493l-132.072 161.42l-30.312-30.312l72.357-88.44l-160.798-.001z"
                />
              </svg>
              <h3 class="text-lg font-semibold text-gray-900 mb-2">
                Nema rezultata za zadane kriterije.
              </h3>
              <p class="text-gray-600">Promijenite pretragu ili filtere.</p>
            </div>

            <KarticaProizvoda
              v-else
              v-for="proizvod in proizvodi_s.proizvodi"
              :key="proizvod.id"
              :proizvod="proizvod"
              :kat-slug="route.params.slug"
            />
          </div>

          <PaginacijaETrznica
            v-if="proizvodi_s.imaProizvoda && proizvodi_s.ukupnoStranica > 1"
            :stranica="proizvodi_s.stranica"
            :ukupno-stranica="proizvodi_s.ukupnoStranica"
            @idi-na="proizvodi_s.promijeniStranicu"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, watch, computed } from "vue"
import { useRoute } from "vue-router"
import { useEtrznicaKategorijeStore } from "@/stores/eTrznicaKategorije"
import { useEtrznicaProizvodiStore } from "@/stores/eTrznicaProizvodi"

import KategorijeProizvodaProizvodiNaslovna from "@/components/etrznica/kategorije-proizvoda/KategorijeProizvodaProizvodiNaslovna.vue"
import KategorijeProizvodaProizvodiFilteri from "@/components/etrznica/kategorije-proizvoda/KategorijeProizvodaProizvodiFilteri.vue"
import KarticaProizvoda from "@/components/dijeljeno/KarticaProizvoda.vue"
import PaginacijaETrznica from "@/components/etrznica/PaginacijaETrznica.vue"

const route = useRoute()
const kategorije_s = useEtrznicaKategorijeStore()
const proizvodi_s = useEtrznicaProizvodiStore()

async function ucitajProizvode() {
  const slug = route.params.slug
  await kategorije_s.ucitajPojedinuKategoriju(slug)
  proizvodi_s.postaviKategoriju(slug)
  proizvodi_s.resetirajStranice()
  await Promise.all([proizvodi_s.ucitajFiltere(), proizvodi_s.ucitajProizvode()])
}

onMounted(ucitajProizvode)
watch(() => route.params.slug, ucitajProizvode)
</script>
