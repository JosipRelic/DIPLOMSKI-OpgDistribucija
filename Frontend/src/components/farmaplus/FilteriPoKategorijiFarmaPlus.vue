<template>
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
    <span class="flex items-center mb-6">
      <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="40"
        height="40"
        viewBox="0 0 24 24"
        class="text-orange-600"
      >
        <path
          fill="currentColor"
          d="m12 19.164l6.207-6.207l-1.414-1.414L12 16.336l-4.793-4.793l-1.414 1.414L12 19.164Zm0-5.65l6.207-6.207l-1.414-1.414L12 10.686L7.207 5.893L5.793 7.307L12 13.514Z"
        />
      </svg>
      <span class="shrink-0 px-4 text-gray-900 text-3xl">Priprema tla</span>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="40"
        height="40"
        viewBox="0 0 24 24"
        class="text-orange-600"
      >
        <path
          fill="currentColor"
          d="m12 19.164l6.207-6.207l-1.414-1.414L12 16.336l-4.793-4.793l-1.414 1.414L12 19.164Zm0-5.65l6.207-6.207l-1.414-1.414L12 10.686L7.207 5.893L5.793 7.307L12 13.514Z"
        />
      </svg>
      <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
    </span>
    <div class="grid grid-cols-1 lg:grid-cols-[300px_1fr] gap-8">
      <div class="px-2 md:px-6">
        <div
          class="mb-6 py-4 flex flex-col items-start md:flex-row md:justify-between border-b border-gray-200"
        >
          <p class="text-xl font-bold">Filteri</p>
          <button class="text-sm text-gray-600">Očisti</button>
        </div>

        <div class="pb-6 border-b border-gray-100 mb-6">
          <p class="font-bold mb-4">Usluge</p>
          <div class="flex flex-wrap gap-2">
            <button
              class="p-2 flex items-center gap-2 text-sm bg-orange-600 text-gray-100 hover:bg-orange-900 hover:text-white font-bold rounded-md"
            >
              Oranje
            </button>
            <button
              class="p-2 flex items-center gap-2 text-sm bg-gray-100 hover:bg-orange-900 hover:text-white font-bold rounded-md"
            >
              Tanjuranje
            </button>
            <button
              class="p-2 flex items-center gap-2 text-sm bg-gray-100 hover:bg-orange-900 hover:text-white font-bold rounded-md"
            >
              Frezanje
            </button>
            <button
              class="p-2 flex items-center gap-2 text-sm bg-gray-100 hover:bg-orange-900 hover:text-white font-bold rounded-md"
            >
              Rahljenje (gruber, podrivač)
            </button>
            <button
              class="p-2 flex items-center gap-2 text-sm bg-gray-100 hover:bg-orange-900 hover:text-white font-bold rounded-md"
            >
              Valjanje tla
            </button>
            <button
              class="p-2 flex items-center gap-2 text-sm bg-gray-100 hover:bg-orange-900 hover:text-white font-bold rounded-md"
            >
              Nivelacija zemljišta
            </button>
            <button
              class="p-2 flex items-center gap-2 text-sm bg-gray-100 hover:bg-orange-900 hover:text-white font-bold rounded-md"
            >
              Kultiviranje
            </button>
          </div>
        </div>

        <div class="pb-6 border-b border-gray-100 mb-6">
          <div class="flex justify-between items-center mb-4">
            <p class="font-bold">Županija</p>
            <button class="text-sm text-gray-600">Očisti</button>
          </div>
          <div class="space-y-2">
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Sisačko-Moslavačka</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Krapinsko-Zagorska</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Brodsko-Posavska</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" />
              Koprivničko-Križevačka</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Zagrebačka</label
            >
          </div>
        </div>

        <div class="pb-6 border-b border-gray-100 mb-6">
          <div class="flex justify-between items-center mb-4">
            <p class="font-bold">Grad</p>
            <button class="text-sm text-gray-600">Očisti</button>
          </div>
          <div class="space-y-2">
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Novska</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Koprivnica</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Slavonski Brod</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Krapina</label
            >
            <label class="flex items-center"
              ><input type="checkbox" class="form-checkbox mr-2 size-4" /> Zagreb</label
            >
          </div>
        </div>
      </div>

      <div class="p-2 md:p-6 rounded-md flex items-center justify-center">
        <div
          class="lg:col-span-3 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-2 gap-6 px-20 py-8 mb-14"
        >
          <!-- <KarticaUsluge /> -->

          <Paginacija />
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import KarticaUsluge from "@/components/dijeljeno/KarticaUsluge.vue"
import Paginacija from "@/components/dijeljeno/Paginacija.vue"
</script>
