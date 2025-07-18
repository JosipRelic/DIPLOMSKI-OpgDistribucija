<template>
  <section class="flex h-screen">
    <RouterLink
      :to="{ name: 'registracijaKupac' }"
      class="group relative w-1/2 overflow-hidden transition-all duration-500 hover:w-[55%]"
    >
      <img
        src="https://plus.unsplash.com/premium_photo-1686156705991-a7e289071bda?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTU3fHxmYXJtZXJ8ZW58MHwxfDB8fHww"
        alt="Registracija kupca"
        class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
      />
      <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
        <h2 class="text-gray-100 text-3xl font-semibold group-hover:scale-105 p-10 transition">
          Kupac
        </h2>
      </div>
    </RouterLink>

    <RouterLink
      :to="{ name: 'registracijaOPG' }"
      class="group relative w-1/2 overflow-hidden transition-all duration-500 hover:w-[55%]"
    >
      <img
        src="https://images.unsplash.com/photo-1551649001-7a2482d98d05?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fEZhcm1lcnxlbnwwfHwwfHx8MA%3D%3D"
        alt="Registracija OPG-a"
        class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
      />
      <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
        <h2 class="text-white text-3xl font-semibold group-hover:scale-105 p-10 transition">OPG</h2>
      </div>
    </RouterLink>
  </section>
</template>
