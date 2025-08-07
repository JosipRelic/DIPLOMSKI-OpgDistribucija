<template>
  <div class="flex justify-center items-center p-4 w-full">
    <div class="w-full px-2 sm:w-[90%] md:w-[80%] lg:w-[60%]">
      <div class="grid grid-cols-1 xl:grid-cols-3 gap-4">
        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start lg:border-b-0 items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Ukupno zaprimljenih narudžbi</span>
          </div>
          <router-link
            :to="{ name: 'profilOpgPrimljeneNarudzbe' }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
            >32</router-link
          >
        </div>
        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start lg:border-b-0 items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Zarada ovaj mjesec</span>
          </div>
          <p class="text-2xl font-bold text-green-600" href="#">253.99 €</p>
        </div>
        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start lg:border-b-0 items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Ukupna zarada</span>
          </div>
          <p class="text-2xl font-bold text-green-600" href="#">1833.99 €</p>
        </div>
        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start lg:border-b-0 items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Najprodavaniji proizvod</span>
          </div>
          <router-link
            :to="{ name: 'profilOpgPonudaETrznica' }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
            >Rajčica</router-link
          >
        </div>
        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start lg:border-b-0 items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Najvjerniji kupac</span>
          </div>
          <router-link
            :to="{ name: 'profilOpgDetaljiKupca' }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
            >Ivan Horvat</router-link
          >
        </div>
        <div
          class="p-8 bg-white rounded-md shadow-lg flex flex-col lg:items-start lg:border-b-0 items-center justify-center"
        >
          <div class="flex justify-between w-full mb-8">
            <span class="text-gray-500 font-bold">Najtraženija usluga</span>
          </div>
          <router-link
            :to="{ name: 'profilOpgPonudaFarmaPlus' }"
            class="text-2xl font-bold text-orange-600 hover:text-orange-900"
            >Oranje</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>
