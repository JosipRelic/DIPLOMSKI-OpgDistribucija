<template>
  <div class="text-slate-100 p-8">
    <div
      role="alert"
      class="rounded-xl border-s-4 border-blue-200 bg-blue-50 p-4 max-w-3xl mb-3 mx-auto"
    >
      <div class="flex items-center gap-2 text-blue-600">
        <svg xmlns="http://www.w3.org/2000/svg" class="size-5" viewBox="0 0 48 48">
          <circle cx="24" cy="24" r="21" fill="#2196F3" />
          <path fill="#fff" d="M22 22h4v11h-4z" />
          <circle cx="24" cy="16.5" r="2.5" fill="#fff" />
        </svg>

        <strong class="font-medium">
          Dodajte datume i vremenske periode u kojima ste slobodni za obavljanje svih vaših usluga
        </strong>
      </div>

      <p class="mt-2 text-sm text-blue-400">
        Ukoliko ne navedete datum, dogovor oko obavljanja vaših usluga ćete obavljati sami izravno
        nakon narudžbe s kupcem vaših usluga. Usluge bez definiranog datuma će se prikazivati s
        oznakom "Datum po dogovoru".
      </p>
    </div>

    <div class="mx-auto max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-8">
      <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-semibold text-orange-600">{{ oznakaMjeseca }}</h2>
          <div class="flex items-center gap-2">
            <button
              class="px-3 py-1.5 rounded-xl text-orange-600 hover:text-gray-900"
              @click="idiDanas"
            >
              Danas
            </button>
            <button
              class="p-2 rounded-xl text-orange-600 hover:text-gray-900"
              @click="pomakniMjesec(-1)"
              aria-label="Prethodni mjesec"
            >
              <
            </button>
            <button
              class="p-2 rounded-xl text-orange-600 hover:text-gray-900"
              @click="pomakniMjesec(1)"
              aria-label="Sljedeći mjesec"
            >
              >
            </button>
          </div>
        </div>

        <div class="grid grid-cols-7 text-center text-sm text-orange-600 mb-2 select-none">
          <div v-for="(d, i) in daniUTjednuKratko" :key="i" class="py-2">{{ d }}</div>
        </div>

        <div class="grid grid-cols-7 gap-2">
          <button
            v-for="dan in mrezaDana"
            :key="dan.kljuc"
            class="relative aspect-square rounded-2xl transition-colors flex items-center justify-center"
            :class="[
              dan.uMjesecu
                ? 'text-gray-600 hover:text-white hover:bg-[#223c2f] shadow-sm'
                : 'bg-white text-gray-300',
              jeIstiDatum(dan.datum, odabraniDatum) && 'shadow-lg bg-[#223c2f] text-white',
              jeProsliDan(dan.datum) && 'opacity-30 cursor-not-allowed',
            ]"
            @click="klikNaDan(dan.datum)"
            :disabled="!dan.uMjesecu || jeProsliDan(dan.datum)"
          >
            <span class="text-base font-medium">
              {{ dan.datum.getDate().toString().padStart(2, "0") }}
            </span>

            <span
              v-if="imaDostupnostiZaDatum(dan.datum)"
              class="absolute bottom-2 left-1/2 -translate-x-1/2 h-2 w-2 rounded-full bg-green-600"
            />
          </button>
        </div>
      </div>

      <div class="rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5">
        <div
          class="flex flex-row max-sm:flex-col md:flex-row lg:flex-col xl:flex-row items-center justify-between mb-6"
        >
          <div>
            <h2 class="text-3xl text-orange-600 font-semibold">Raspored</h2>
            <p class="text-gray-400 max-sm:mb-2">{{ oznakaMjeseca }}</p>
          </div>
          <div class="flex gap-2">
            <button
              class="px-3 py-2 rounded-xl bg-orange-600 hover:bg-orange-900 shadow-md"
              @click="otvoriTjedniObrazac"
            >
              <span class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  class="me-1"
                >
                  <path
                    fill="#ffffff"
                    d="M18 20v-3h-3v-2h3v-3h2v3h3v2h-3v3h-2ZM3 21q-.825 0-1.413-.588T1 19V5q0-.825.588-1.413T3 3h14q.825 0 1.413.588T19 5v5h-2V8H3v11h13v2H3Z"
                  />
                </svg>
                Tjedni raspored
              </span>
            </button>
            <button
              class="px-3 py-2 rounded-xl bg-orange-600 hover:bg-orange-900 shadow-md"
              @click="otvoriDnevniObrazac"
            >
              <span class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  class="me-1"
                >
                  <path
                    fill="#ffffff"
                    d="M18 20v-3h-3v-2h3v-3h2v3h3v2h-3v3h-2ZM3 21q-.825 0-1.413-.588T1 19V5q0-.825.588-1.413T3 3h14q.825 0 1.413.588T19 5v5h-2V8H3v11h13v2H3Z"
                  />
                </svg>
                Dnevni raspored
              </span>
            </button>
          </div>
        </div>

        <div
          v-if="rezim === 'tjedno'"
          class="rounded-2xl bg-white text-gray-600 shadow shadow-lg p-4"
        >
          <div class="flex items-center justify-between mb-3">
            <h3 class="text-lg font-semibold">Ovaj tjedan ({{ oznakaRasponaTjedna }})</h3>
            <div class="flex gap-2">
              <button
                class="px-3 py-1.5 rounded-xl bg-teal-500 hover:bg-teal-800 shadow-lg text-white"
                @click="spremiTjedniRaspored"
              >
                Spremi
              </button>
              <button
                class="px-3 py-1.5 rounded-xl bg-red-700 hover:bg-red-900 shadow-lg text-white"
                @click="ponistiObrasce"
              >
                Odustani
              </button>
            </div>
          </div>

          <div class="mt-4 text-sm text-gray-500 flex items-center gap-2">
            <span v-if="!urediNaslov" class="italic">Naslov: {{ tekstNaslova }}</span>
            <input
              v-else
              type="text"
              v-model="tekstNaslova"
              class="px-3 py-1.5 rounded-xl bg-gray-100 shadow-sm text-gray-900 border border-gray-200 mb-2 w-full max-w-md"
            />
            <button
              class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
              @click="prebaciUrediNaslov"
              :title="urediNaslov ? 'Spremi naslov' : 'Uredi naslov'"
            >
              <span v-if="urediNaslov"> SPREMI </span>
              <span v-else>✏️</span>
            </button>
          </div>

          <div class="divide-y divide-orange-200">
            <div
              v-for="red in redoviTjedna"
              :key="red.kljuc"
              class="flex items-center gap-4 py-3 max-sm:gap-2 lg:gap-2 xl:gap-4"
            >
              <label class="flex items-center gap-2 w-28 max-sm:w-12 lg:w-14 xl:w-28">
                <input type="checkbox" v-model="red.ukljuceno" class="accent-sky-500 h-4 w-4" />
                <span class="w-16">{{ red.naziv }}</span>
              </label>
              <input
                type="time"
                v-model="red.od"
                class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
              />
              <input
                type="time"
                v-model="red.do"
                class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
              />
            </div>
          </div>
        </div>

        <div
          v-if="rezim === 'dnevno'"
          class="rounded-2xl shadow-lg text-gray-600 bg-white shadow-lg p-4"
        >
          <div v-if="!naCekanjuDatum">
            <p>Odaberite željeni datum u kalendaru.</p>
          </div>
          <div v-else>
            <div class="flex items-center justify-between mb-3">
              <h3 class="text-lg font-semibold">Datum: {{ formatirajPun(naCekanjuDatum) }}</h3>
              <div class="flex gap-2">
                <button
                  class="px-3 py-1.5 rounded-xl bg-teal-500 hover:bg-teal-800 shadow-lg text-white"
                  @click="spremiJedanDatum"
                >
                  Spremi
                </button>
                <button
                  class="px-3 py-1.5 rounded-xl bg-red-700 hover:bg-red-900 shadow-lg text-white"
                  @click="ponistiObrasce"
                >
                  Odustani
                </button>
              </div>
            </div>

            <div class="mt-4 text-sm text-gray-500 flex items-center gap-2">
              <span v-if="!urediNaslov" class="italic">Naslov: {{ tekstNaslova }}</span>
              <input
                v-else
                type="text"
                v-model="tekstNaslova"
                class="px-3 py-1.5 rounded-xl bg-gray-100 shadow-sm text-gray-900 border border-gray-200 mb-2 w-full max-w-md"
              />
              <button
                class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                @click="prebaciUrediNaslov"
                :title="urediNaslov ? 'Spremi naslov' : 'Uredi naslov'"
              >
                <span v-if="urediNaslov"> SPREMI </span>
                <span v-else>✏️</span>
              </button>
            </div>

            <div class="flex items-center gap-4">
              <input
                type="time"
                v-model="jedan.od"
                class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
              />
              <input
                type="time"
                v-model="jedan.do"
                class="w-32 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow-lg"
              />
            </div>
          </div>
        </div>

        <div class="space-y-4 mt-6">
          <div
            v-for="stavka in paginiraniDogadjaji"
            :key="stavka.id"
            class="flex gap-4 items-stretch"
          >
            <div class="w-20 shrink-0 rounded-2xl bg-white shadow-lg text-center py-3">
              <div class="text-3xl font-bold text-[#223c2f] leading-none">
                {{ brojDana(stavka.datum) }}
              </div>
              <div class="text-orange-600">{{ kraciMjesec(stavka.datum) }}</div>
            </div>

            <div class="flex-1 rounded-2xl shadow-lg bg-white px-5 py-4">
              <div class="flex items-center gap-2 mb-1">
                <span
                  class="inline-block h-3 w-3 rounded-full"
                  :style="{ background: stavka.tockaBoja }"
                />
                <h3 class="text-lg font-medium text-gray-600 flex-1">
                  <template v-if="urediStanje.id !== stavka.id">
                    {{ stavka.naslov || "Termin" }}
                  </template>
                  <template v-else>
                    <input
                      type="text"
                      v-model="urediStanje.naslov"
                      class="px-3 py-1.5 rounded-xl bg-gray-100 shadow-sm text-gray-900 border border-gray-200 w-full max-w-sm"
                      placeholder="Naslov (opcionalno)"
                    />
                  </template>
                </h3>

                <template v-if="urediStanje.id !== stavka.id">
                  <button
                    @click="zapocniUredivanje(stavka)"
                    class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                    title="Uredi termin"
                  >
                    ✏️
                  </button>
                  <button
                    @click="obrisiTermin(stavka.id)"
                    class="p-2 rounded-lg bg-white/5 hover:bg-white/10"
                    title="Obriši termin"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="20"
                      height="20"
                      viewBox="0 0 2048 2048"
                      class="text-red-500"
                    >
                      <path
                        fill="currentColor"
                        d="M1664 128h384v1792H0V128h384V0h128v128h1024V0h128v128zM384 256H128v256h1792V256h-256v128h-128V256H512v128H384V256zM128 1792h1792V640H128v1152zm1171-941l90 90l-274 275l274 275l-90 90l-275-275l-275 275l-90-90l274-275l-274-275l90-90l275 275l275-275z"
                      />
                    </svg>
                  </button>
                </template>

                <template v-else>
                  <button
                    @click="spremiUredivanje"
                    class="px-3 py-1.5 rounded-xl bg-teal-500 hover:bg-teal-800 shadow-lg text-white"
                  >
                    Spremi
                  </button>
                  <button
                    @click="odustaniOdUredivanja"
                    class="px-3 py-1.5 rounded-xl bg-red-700 hover:bg-red-900 shadow-lg text-white"
                  >
                    Odustani
                  </button>
                </template>
              </div>

              <div v-if="urediStanje.id !== stavka.id" class="text-gray-400">
                {{ rasponVremena(stavka) }}, {{ puniDanUTjednu(stavka.datum) }},
                {{ formatirajDatum(stavka.datum) }}
              </div>

              <div v-else class="flex flex-wrap items-center gap-3 text-gray-600">
                <div class="flex items-center gap-2 mt-2">
                  <span class="text-gray-400">Vrijeme:</span>
                  <input
                    type="time"
                    v-model="urediStanje.od"
                    class="w-28 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow"
                  />
                  <span>–</span>
                  <input
                    type="time"
                    v-model="urediStanje.do"
                    class="w-28 px-3 py-2 rounded-xl bg-white border border-gray-200 shadow"
                  />
                </div>

                <div class="flex items-center gap-2">
                  <span class="text-gray-400">Datum:</span>
                  <input
                    type="date"
                    :value="isoDatum(stavka.datum)"
                    @input="
                      (e) => {
                        urediStanje.datum = new Date(e.target.value + 'T00:00:00')
                      }
                    "
                    class="px-3 py-2 rounded-xl bg-white border border-gray-200 shadow"
                  />
                </div>
              </div>
            </div>
          </div>

          <p v-if="!mjesecniDogadjaji.length" class="text-slate-400">
            Nema događaja u ovom mjesecu.
          </p>

          <div v-else-if="totalPages > 1" class="flex items-center justify-between pt-2">
            <div class="text-sm text-gray-500">
              Prikazano
              <strong>{{ prikazOd }}–{{ prikazDo }}</strong>
              od <strong>{{ totalItems }}</strong>
            </div>

            <div class="flex gap-2">
              <button
                class="px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 text-orange-600 disabled:opacity-40 disabled:cursor-not-allowed"
                :disabled="!hasPrev"
                @click="prethodnaStranica"
              >
                ◀︎ Prethodna
              </button>
              <button
                class="px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 text-orange-600 disabled:opacity-40 disabled:cursor-not-allowed"
                :disabled="!hasNext"
                @click="sljedecaStranica"
              >
                Sljedeća ▶︎
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="mx-auto max-w-6xl grid grid-cols-1gap-8 mt-5 rounded-2xl bg-white p-6 shadow-xl ring-1 ring-white/5"
    >
      <div>
        <div class="flex mb-6">
          <h2 class="text-3xl text-orange-600 font-semibold">Zadnje rezervacije</h2>
          <router-link
            :to="{ name: 'profilOpgPrimljeneRezervacije' }"
            class="text-white flex items-center bg-orange-600 px-3 py-2 ms-4 rounded-xl hover:bg-orange-900 shadow-md"
          >
            <span>Pogledaj sve</span>
            <span>
              <svg
                class="ms-2"
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 2048 2048"
              >
                <path
                  fill="currentColor"
                  d="M0 1408v-384h384v384H0zm128-256v128h128v-128H128zM0 896V512h384v384H0zm128-256v128h128V640H128zM0 384V0h384v384H0zm128-256v128h128V128H128zm512 640V640h1152v128H640zm896 384v128H640v-128h896zM640 128h1408v128H640V128zM0 1920v-384h384v384H0zm128-256v128h128v-128H128zm512 128v-128h1152v128H640z"
                />
              </svg>
            </span>
          </router-link>
        </div>

        <ol class="items-center sm:flex p-6 w-full">
          <li class="relative mb-6 sm:mb-0 sm:flex-1">
            <div class="flex items-center mb-5">
              <div
                class="z-10 flex items-center justify-center w-6 h-6 bg-orange-600 rounded-full ring-0 ring-orange-600 sm:ring-8 shrink-0"
              >
                <svg
                  class="w-4 h-4 text-white"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
                  />
                </svg>
              </div>
              <div class="hidden sm:flex w-full bg-orange-500 h-0.5"></div>
            </div>
            <div class="mt-3 sm:pe-8 h-full">
              <div class="flex items-start gap-3">
                <img
                  class="w-20 h-20 rounded-xl shrink-0"
                  src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?q=80&w=1548&auto=format&fit=crop"
                  alt="Oranje"
                />
                <div class="flex flex-col justify-between">
                  <h3 class="text-lg font-semibold text-gray-900 mb-1">
                    <span class="inline-block h-3 w-3 rounded-full bg-red-600 me-2" />Oranje | 1
                    hektar
                  </h3>
                  <time class="block mb-1 text-sm font-bold leading-none text-teal-500"
                    >26. siječnja 2025. 12:00-13:00</time
                  >
                  <p class="text-sm font-normal text-gray-500">
                    Broj narudžbe:
                    <router-link :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe' }">
                      <span class="text-orange-600 font-semibold hover:underline cursor-pointer"
                        >#2196F3</span
                      >
                    </router-link>
                  </p>
                </div>
              </div>
            </div>
          </li>

          <li class="relative mb-6 sm:mb-0 sm:flex-1">
            <div class="flex items-center mb-5">
              <div
                class="z-10 flex items-center justify-center w-6 h-6 bg-orange-600 rounded-full ring-0 ring-orange-600 sm:ring-8 shrink-0"
              >
                <svg
                  class="w-4 h-4 text-white"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
                  />
                </svg>
              </div>
              <div class="hidden sm:flex w-full bg-orange-500 h-0.5"></div>
            </div>
            <div class="mt-3 sm:pe-8 h-full">
              <div class="flex items-start gap-3">
                <img
                  class="w-20 h-20 rounded-xl shrink-0"
                  src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?q=80&w=1548&auto=format&fit=crop"
                  alt="Oranje"
                />
                <div class="flex flex-col justify-between">
                  <h3 class="text-lg font-semibold text-gray-900 mb-1">
                    <span class="inline-block h-3 w-3 rounded-full bg-red-600 me-2" />Špricanje | 1
                    hektar
                  </h3>
                  <time class="block mb-1 text-sm font-bold leading-none text-teal-500"
                    >25. siječnja 2025. 12:00-17:00</time
                  >
                  <p class="text-sm font-normal text-gray-500">
                    Broj narudžbe:
                    <router-link :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe' }">
                      <span class="text-orange-600 font-semibold hover:underline cursor-pointer"
                        >#2196F3</span
                      >
                    </router-link>
                  </p>
                </div>
              </div>
            </div>
          </li>

          <li class="relative mb-6 sm:mb-0 sm:flex-1">
            <div class="flex items-center mb-5">
              <div
                class="z-10 flex items-center justify-center w-6 h-6 bg-orange-600 rounded-full ring-0 ring-orange-600 sm:ring-8 shrink-0"
              >
                <svg
                  class="w-4 h-4 text-white"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
                  />
                </svg>
              </div>
              <div class="hidden sm:flex w-full bg-orange-500 h-0.5"></div>
            </div>
            <div class="mt-3 sm:pe-8 h-full">
              <div class="flex items-start gap-3">
                <img
                  class="w-20 h-20 rounded-xl shrink-0"
                  src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?q=80&w=1548&auto=format&fit=crop"
                  alt="Oranje"
                />
                <div class="flex flex-col justify-between">
                  <h3 class="text-lg font-semibold text-gray-900 mb-1">
                    <span class="inline-block h-3 w-3 rounded-full bg-red-600 me-2" />Tanjuranje | 1
                    hektar
                  </h3>
                  <time class="block mb-1 text-sm font-bold leading-none text-teal-500"
                    >24. siječnja 2025. 12:00-13:00</time
                  >
                  <p class="text-sm font-normal text-gray-500">
                    Broj narudžbe:
                    <router-link :to="{ name: 'profilOpgPrimljeneNarudzbeDetaljiNarudzbe' }">
                      <span class="text-orange-600 font-semibold hover:underline cursor-pointer"
                        >#2196F3</span
                      >
                    </router-link>
                  </p>
                </div>
              </div>
            </div>
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, reactive, ref, watch, onMounted } from "vue"
import { useRaspolozivostOpgStore } from "@/stores/raspolozivostOpg"
import { useUiStore } from "@/stores/ui"

const ui = useUiStore()
const raspolozivost = useRaspolozivostOpgStore()

const isoDatum = (d) => {
  const y = d.getFullYear()
  const m = String(d.getMonth() + 1).padStart(2, "0")
  const day = String(d.getDate()).padStart(2, "0")
  return `${y}-${m}-${day}`
}
const pocetakMjeseca = (d) => new Date(d.getFullYear(), d.getMonth(), 1)
const krajMjeseca = (d) => new Date(d.getFullYear(), d.getMonth() + 1, 0)
const dodajMjesece = (d, n) => new Date(d.getFullYear(), d.getMonth() + n, 1)
const jeIstiDatum = (a, b) =>
  a &&
  b &&
  a.getFullYear() === b.getFullYear() &&
  a.getMonth() === b.getMonth() &&
  a.getDate() === b.getDate()
const dohvatiPonedjeljak = (d) => {
  const dd = new Date(d)
  const day = (dd.getDay() + 6) % 7
  dd.setDate(dd.getDate() - day)
  dd.setHours(0, 0, 0, 0)
  return dd
}
const dodajDane = (d, n) => {
  const x = new Date(d)
  x.setDate(x.getDate() + n)
  return x
}
const spojiDatumVrijeme = (date, hhmm) => {
  const [h, m] = (hhmm || "00:00").split(":").map(Number)
  const d = new Date(date)
  d.setHours(h ?? 0, m ?? 0, 0, 0)
  return d
}
const jeUProslosti = (date, hhmm) => spojiDatumVrijeme(date, hhmm) < new Date()

const jeProsliDan = (d) => {
  const danas = new Date()
  const x = new Date(d.getFullYear(), d.getMonth(), d.getDate())
  const n = new Date(danas.getFullYear(), danas.getMonth(), danas.getDate())
  return x < n
}

const hrFmt = new Intl.DateTimeFormat("hr-HR", { month: "long", year: "numeric" })
const hrMjesecKratko = new Intl.DateTimeFormat("hr-HR", { month: "short" })
const hrDanUTjednuPuni = new Intl.DateTimeFormat("hr-HR", { weekday: "long" })

const daniUTjednuKratko = ["Pon", "Uto", "Sri", "Čet", "Pet", "Sub", "Ned"]

const danas = new Date()
const prikazMjeseca = ref(pocetakMjeseca(danas))
const odabraniDatum = ref(danas)

const urediNaslov = ref(false)
const tekstNaslova = ref("Slobodni za obavljanje usluga")
const prebaciUrediNaslov = () => (urediNaslov.value = !urediNaslov.value)

const rezim = ref("none")
const naCekanjuDatum = ref(null)
const jedan = reactive({ od: "00:00", do: "00:00" })

const redoviTjedna = reactive([
  { kljuc: "mon", naziv: "Pon", offset: 0, ukljuceno: false, od: "00:00", do: "00:00" },
  { kljuc: "tue", naziv: "Uto", offset: 1, ukljuceno: false, od: "00:00", do: "00:00" },
  { kljuc: "wed", naziv: "Sri", offset: 2, ukljuceno: false, od: "00:00", do: "00:00" },
  { kljuc: "thu", naziv: "Čet", offset: 3, ukljuceno: false, od: "00:00", do: "00:00" },
  { kljuc: "fri", naziv: "Pet", offset: 4, ukljuceno: false, od: "00:00", do: "00:00" },
  { kljuc: "sat", naziv: "Sub", offset: 5, ukljuceno: false, od: "00:00", do: "00:00" },
  { kljuc: "sun", naziv: "Ned", offset: 6, ukljuceno: false, od: "00:00", do: "00:00" },
])

async function ucitajDatumeZaMjesec() {
  const g = prikazMjeseca.value.getFullYear()
  const m = prikazMjeseca.value.getMonth() + 1
  await raspolozivost.dohvatiMjesecneDatume({ godina: g, mjesec: m })
}

const oznakaMjeseca = computed(() =>
  hrFmt.format(prikazMjeseca.value).replace(/^./, (c) => c.toUpperCase()),
)

const mrezaDana = computed(() => {
  const start = pocetakMjeseca(prikazMjeseca.value)
  const end = krajMjeseca(prikazMjeseca.value)

  const startWeekdayMonFirst = (start.getDay() + 6) % 7
  const dani = []

  for (let i = startWeekdayMonFirst; i > 0; i--) {
    const d = new Date(start)
    d.setDate(d.getDate() - i)
    dani.push({ kljuc: "p" + i + d.getTime(), datum: d, uMjesecu: false })
  }

  for (let i = 1; i <= end.getDate(); i++) {
    const d = new Date(start)
    d.setDate(i)
    dani.push({ kljuc: "m" + i, datum: d, uMjesecu: true })
  }

  while (dani.length % 7 !== 0 || dani.length < 42) {
    const last = dani[dani.length - 1].datum
    const d = new Date(last)
    d.setDate(d.getDate() + 1)
    dani.push({ kljuc: "n" + d.getTime(), datum: d, uMjesecu: false })
  }

  return dani
})

function imaDostupnostiZaDatum(d) {
  const iso = isoDatum(d)
  return (raspolozivost.datumi || []).some((x) => x.datum === iso)
}

const localDateFromISO = (s) => {
  const [yy, mm, dd] = (s || "1970-01-01").split("-").map(Number)
  return new Date(yy, (mm || 1) - 1, dd || 1)
}

const mjesecniDogadjaji = computed(() => {
  const y = prikazMjeseca.value.getFullYear()
  const m = prikazMjeseca.value.getMonth()

  const lista = (raspolozivost.datumi || [])
    .map((e) => ({
      id: e.id,
      datum: localDateFromISO(e.datum),
      naslov: e.naslov,
      od: e.pocetno_vrijeme,
      do: e.zavrsno_vrijeme,
      tockaBoja: "#22c55e",
    }))
    .filter((e) => e.datum.getFullYear() === y && e.datum.getMonth() === m)
    .sort((a, b) => a.datum - b.datum || (a.od || "").localeCompare(b.od || ""))

  return lista
})

function odaberiDatum(d) {
  odabraniDatum.value = d
}
function pomakniMjesec(n) {
  prikazMjeseca.value = dodajMjesece(prikazMjeseca.value, n)
}
function idiDanas() {
  prikazMjeseca.value = pocetakMjeseca(danas)
  odabraniDatum.value = danas
}

function klikNaDan(d) {
  odaberiDatum(d)
  if (rezim.value === "dnevno") {
    if (jeProsliDan(d)) {
      ui.obavijest({ tekst: "Prošli dan nije moguće odabrati.", tip_obavijesti: "greska" })
      return
    }
    naCekanjuDatum.value = d
  }
}

function otvoriTjedniObrazac() {
  rezim.value = "tjedno"
  naCekanjuDatum.value = null
}
function otvoriDnevniObrazac() {
  rezim.value = "dnevno"
  naCekanjuDatum.value = null
}
function ponistiObrasce() {
  rezim.value = "none"
  naCekanjuDatum.value = null
  urediNaslov.value = false
}

const oznakaRasponaTjedna = computed(() => {
  const base = dohvatiPonedjeljak(odabraniDatum.value || danas)
  const sun = dodajDane(base, 6)
  const fmt = (d) => d.toLocaleDateString("hr-HR", { day: "2-digit", month: "2-digit" })
  return `${fmt(base)} – ${fmt(sun)}`
})

async function spremiTjedniRaspored() {
  const greske = redoviTjedna.filter((r) => r.ukljuceno && r.od >= r.do).map((r) => r.naziv)
  if (greske.length) {
    ui.obavijest({
      tekst: `Završno vrijeme mora biti veće od početnog za: ${greske.join(", ")}`,
      tip_obavijesti: "greska",
    })
    return
  }

  const pon = dohvatiPonedjeljak(odabraniDatum.value || danas)
  const kreiranja = []

  for (const r of redoviTjedna) {
    if (!r.ukljuceno) continue
    const datum = dodajDane(pon, r.offset)
    if (jeProsliDan(datum)) continue
    if (jeUProslosti(datum, r.od)) continue
    kreiranja.push(
      raspolozivost.dodajDatum({
        datum: isoDatum(datum),
        pocetno_vrijeme: r.od || "00:00",
        zavrsno_vrijeme: r.do || "00:00",
        naslov: tekstNaslova.value || null,
      }),
    )
  }

  if (!kreiranja.length) {
    ui.obavijest({ tekst: "Nema ništa za spremiti u ovom tjednu.", tip_obavijesti: "informacija" })
    return
  }

  try {
    await Promise.all(kreiranja)
    await ucitajDatumeZaMjesec()
    ui.obavijest({ tekst: "Raspored za ovaj tjedan je spremljen.", tip_obavijesti: "uspjeh" })
  } catch (e) {
    ui.obavijest({ tekst: "Greška pri spremanju rasporeda.", tip_obavijesti: "greska" })
  } finally {
    ponistiObrasce()
  }
}

async function spremiJedanDatum() {
  if (!naCekanjuDatum.value) return

  const danas00 = new Date()
  danas00.setHours(0, 0, 0, 0)
  const datum00 = new Date(naCekanjuDatum.value)
  datum00.setHours(0, 0, 0, 0)
  if (datum00 < danas00) {
    ui.obavijest({ tekst: "Odabrani datum je u prošlosti.", tip_obavijesti: "greska" })
    return
  }
  if (jedan.od >= jedan.do) {
    ui.obavijest({ tekst: "Završno vrijeme mora biti veće od početnog.", tip_obavijesti: "greska" })
    return
  }

  if (jeUProslosti(naCekanjuDatum.value, jedan.od)) {
    ui.obavijest({ tekst: "Početno vrijeme je u prošlosti.", tip_obavijesti: "greska" })
    return
  }
  if (jeUProslosti(naCekanjuDatum.value, jedan.do)) {
    ui.obavijest({ tekst: "Završno vrijeme je u prošlosti.", tip_obavijesti: "greska" })
    return
  }

  try {
    await raspolozivost.dodajDatum({
      datum: isoDatum(naCekanjuDatum.value),
      pocetno_vrijeme: jedan.od,
      zavrsno_vrijeme: jedan.do,
      naslov: tekstNaslova.value || null,
    })
    await ucitajDatumeZaMjesec()
    ui.obavijest({ tekst: "Termin dodan.", tip_obavijesti: "uspjeh" })
  } catch (e) {
    const status = e?.response?.status
    const detail = e?.response?.data?.detail
    if (status === 409) {
      ui.obavijest({ tekst: "Termin se preklapa s postojećim terminom.", tip_obavijesti: "greska" })
    } else {
      ui.obavijest({
        tekst: detail || "Greška pri dodavanju termina.",
        tip_obavijesti: "greska",
      })
    }
  } finally {
    ponistiObrasce()
  }
}

async function obrisiTermin(id) {
  const potvrda = await ui.obavijestSaPotvrdom({
    naslov: "Obrisati termin?",
    poruka: `Termin će biti trajno uklonjen.`,
    tip_obavijesti: "upozorenje",
    potvrdiRadnju: "Obriši",
    odustaniOdRadnje: "Odustani",
  })
  if (!potvrda) return
  await raspolozivost.obrisiDatum(id)
}

const brojDana = (d) => String(d.getDate()).padStart(2, "0")
const kraciMjesec = (d) => hrMjesecKratko.format(d)
const puniDanUTjednu = (d) => hrDanUTjednuPuni.format(d)
const formatirajDatum = (d) => d.toLocaleDateString("hr-HR", { day: "2-digit", month: "long" })
const formatirajPun = (d) =>
  d.toLocaleDateString("hr-HR", { day: "2-digit", month: "long", year: "numeric" })
const rasponVremena = (e) => `${e.od} - ${e["do"]}`

watch(prikazMjeseca, () => {
  ucitajDatumeZaMjesec()
})

onMounted(async () => {
  await ucitajDatumeZaMjesec()
})

const PAGE_SIZE = 4
const page = ref(1)

const totalItems = computed(() => mjesecniDogadjaji.value.length)
const totalPages = computed(() => Math.max(1, Math.ceil(totalItems.value / PAGE_SIZE)))

const paginiraniDogadjaji = computed(() => {
  const start = (page.value - 1) * PAGE_SIZE
  return mjesecniDogadjaji.value.slice(start, start + PAGE_SIZE)
})

const hasPrev = computed(() => page.value > 1)
const hasNext = computed(() => page.value < totalPages.value)

function prethodnaStranica() {
  if (hasPrev.value) page.value -= 1
}
function sljedecaStranica() {
  if (hasNext.value) page.value += 1
}

const prikazOd = computed(() => (totalItems.value === 0 ? 0 : (page.value - 1) * PAGE_SIZE + 1))
const prikazDo = computed(() => Math.min(page.value * PAGE_SIZE, totalItems.value))

watch([prikazMjeseca, mjesecniDogadjaji], () => {
  page.value = 1
})

watch(totalPages, () => {
  if (page.value > totalPages.value) page.value = totalPages.value
})

const urediStanje = reactive({
  id: null,
  datum: null,
  od: "00:00",
  do: "00:00",
  naslov: "",
})

function zapocniUredivanje(stavka) {
  urediStanje.id = stavka.id
  urediStanje.datum = new Date(stavka.datum)
  urediStanje.od = stavka.od || "00:00"
  urediStanje.do = stavka.do || "00:00"
  urediStanje.naslov = stavka.naslov || ""
}

function odustaniOdUredivanja() {
  urediStanje.id = null
  urediStanje.datum = null
  urediStanje.od = "00:00"
  urediStanje.do = "00:00"
  urediStanje.naslov = ""
}

async function spremiUredivanje() {
  if (!urediStanje.id || !urediStanje.datum) return

  const danas00 = new Date()
  danas00.setHours(0, 0, 0, 0)
  const datum00 = new Date(urediStanje.datum)
  datum00.setHours(0, 0, 0, 0)

  if (datum00 < danas00) {
    ui.obavijest({ tekst: "Odabrani datum je u prošlosti.", tip_obavijesti: "greska" })
    return
  }
  if ((urediStanje.od || "") >= (urediStanje.do || "")) {
    ui.obavijest({ tekst: "Završno vrijeme mora biti veće od početnog.", tip_obavijesti: "greska" })
    return
  }

  if (jeUProslosti(urediStanje.datum, urediStanje.od)) {
    ui.obavijest({ tekst: "Početno vrijeme je u prošlosti.", tip_obavijesti: "greska" })
    return
  }
  if (jeUProslosti(urediStanje.datum, urediStanje.do)) {
    ui.obavijest({ tekst: "Završno vrijeme je u prošlosti.", tip_obavijesti: "greska" })
    return
  }

  try {
    await raspolozivost.urediDatum(urediStanje.id, {
      datum: isoDatum(urediStanje.datum),
      pocetno_vrijeme: urediStanje.od,
      zavrsno_vrijeme: urediStanje.do,
      naslov: urediStanje.naslov || null,
    })
    await ucitajDatumeZaMjesec()
    ui.obavijest({ tekst: "Termin ažuriran.", tip_obavijesti: "uspjeh" })
    odustaniOdUredivanja()
  } catch (e) {
    const status = e?.response?.status
    const detail = e?.response?.data?.detail
    if (status === 409) {
      ui.obavijest({ tekst: "Termin se preklapa s postojećim terminom.", tip_obavijesti: "greska" })
    } else {
      ui.obavijest({ tekst: detail || "Greška pri ažuriranju termina.", tip_obavijesti: "greska" })
    }
  }
}
</script>

<style scoped>
button:focus-visible {
  outline: 2px solid rgba(56, 189, 248, 0.6);
  outline-offset: 2px;
}
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
