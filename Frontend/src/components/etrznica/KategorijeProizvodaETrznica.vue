<template>
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-10 mb-12">
    <div class="flex items-center justify-between mb-2">
      <h2 class="text-2xl font-bold text-gray-900">
        Odaberite kategoriju kako biste pregledali njezine proizvode.
      </h2>
    </div>
    <p class="mb-8 max-w-3xl text-gray-500">
      Na našoj E-Tržnici pronaći ćete pažljivo odabrane proizvode domaćih OPG-ova. Od svježeg voća i
      povrća do raznih delicija i prirodnih proizvoda. Svaki proizvod dolazi izravno s hrvatskih
      farmi, s naglaskom na kvalitetu, svježinu i lokalnu proizvodnju. Pregledajte ponudu i
      pronađite sve što vam treba, brzo i jednostavno.
    </p>
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-4"
    >
      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaDomaceVoce' }">
          <img
            :src="slikeETrznicaKategorijeVoce"
            alt="Domaće voće"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">Domaće voće</div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaSezonskoPovrce' }">
          <img
            :src="slikeETrznicaKategorijePovrce"
            alt="Sezonsko povrće"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">Sezonsko povrće</div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaJajaiMlijecniProizvodi' }">
          <img
            :src="slikeETrznicaKategorijeMlijecniProizvodi"
            alt="Jaja i mliječni proizvodi"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">
            Jaja i mliječni proizvodi
          </div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaIzKosnice' }">
          <img
            :src="slikeETrznicaKategorijeIzKosnice"
            alt="Iz košnice"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">Iz košnice</div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaPicaiRakije' }">
          <img
            :src="slikeETrznicaKategorijePica"
            alt="Domaća pića i rakije"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">
            Domaća pića i rakije
          </div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaUljaizPrirode' }">
          <img
            :src="slikeETrznicaKategorijeUlja"
            alt="Ulja iz prirode"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">Ulja iz prirode</div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaCajeviZacinskoBilje' }">
          <img
            :src="slikeETrznicaKategorijeCajeviZacini"
            alt="Čajevi i začinsko bilje"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">
            Čajevi i začinsko bilje
          </div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaSuhomesnato' }">
          <img
            :src="slikeETrznicaKategorijeSuhomesnato"
            alt="Suhomesnati proizvodi"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">
            Suhomesnati proizvodi
          </div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaPrirodnaKozmetika' }">
          <img
            :src="slikeETrznicaKategorijeKozmetika"
            alt="Prirodna kozmetika"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">Prirodna kozmetika</div>
        </router-link>
      </div>

      <div
        class="rounded-xl overflow-hidden shadow-sm hover:shadow-md transition bg-white cursor-pointer"
      >
        <router-link :to="{ name: 'ETrznicaKategorijaIzSumeiDvorista' }">
          <img
            :src="slikeETrznicaKategorijeSumaDvoriste"
            alt="Iz šume i dvorišta"
            class="w-full h-52 object-cover bg-gray-100"
          />
          <div class="p-4 text-center text-lg font-semibold text-gray-800">Iz šume i dvorišta</div>
        </router-link>
      </div>
    </div>
  </section>
</template>
<script setup>
import slikeETrznicaKategorijeVoce from "@/assets/slike/etrznica-kategorije-voce.jpg"
import slikeETrznicaKategorijePovrce from "@/assets/slike/etrznica-kategorije-povrce.jpg"
import slikeETrznicaKategorijeMlijecniProizvodi from "@/assets/slike/etrznica-kategorije-mlijecniproizvodi.jpg"
import slikeETrznicaKategorijeIzKosnice from "@/assets/slike/etrznica-kategorije-izkosnice.jpg"
import slikeETrznicaKategorijePica from "@/assets/slike/etrznica-kategorije-pica.jpg"
import slikeETrznicaKategorijeUlja from "@/assets/slike/etrznica-kategorije-ulja.jpg"
import slikeETrznicaKategorijeCajeviZacini from "@/assets/slike/etrznica-kategorije-cajevi-zacini.jpg"
import slikeETrznicaKategorijeSuhomesnato from "@/assets/slike/etrznica-kategorije-suhomesnato.jpg"
import slikeETrznicaKategorijeKozmetika from "@/assets/slike/etrznica-kategorije-kozmetika.jpg"
import slikeETrznicaKategorijeSumaDvoriste from "@/assets/slike/etrznica-kategorije-sumaidvoriste.jpg"
</script>
