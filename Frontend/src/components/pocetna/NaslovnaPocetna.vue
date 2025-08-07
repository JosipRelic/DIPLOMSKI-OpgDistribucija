<template>
  <div class="bg-black/50 p-8 md:p-12 lg:px-16 lg:py-40">
    <div class="text-center ltr:sm:text-left rtl:sm:text-right">
      <h2 class="text-2xl font-bold text-gray-100 sm:text-3xl md:text-5xl">Svježe s naših polja</h2>

      <p class="hidden max-w-xl text-gray-100 md:mt-6 sm:block md:text-lg md:leading-relaxed">
        Istražite ponudu OPG-ova i njihovih proizvoda na našoj E-Tržnici.
      </p>

      <div class="mt-4 sm:mt-8">
        <RouterLink
          :to="{ name: 'e-trznica' }"
          class="inline-block rounded-full bg-orange-700 px-12 py-3 text-sm font-medium text-gray-100 transition hover:bg-orange-900 focus:ring-3 focus:ring-yellow-400 focus:outline-hidden"
        >
          Posjetite E-Tržnicu
        </RouterLink>
      </div>
    </div>
  </div>
</template>
