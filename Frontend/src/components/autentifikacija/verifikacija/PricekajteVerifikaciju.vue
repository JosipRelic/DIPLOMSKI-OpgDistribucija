<template>
  <div class="bg-white max-w-lg my-30 mx-auto shadow-lg p-10 text-center rounded-lg">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="100"
      height="100"
      viewBox="0 0 24 24"
      class="mx-auto text-green-600 mb-2"
    >
      <g
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="1.5"
        color="currentColor"
      >
        <path
          d="M16.177 18.456c.3.144.673.517.854.818c.06.42.36-1.203 1.828-2.165m2.641.892a4 4 0 1 1-8 0a4 4 0 0 1 8 0"
        />
        <circle cx="11.008" cy="12.001" r="2" />
        <path
          d="M7.508 18.001c.95-.9 1.75-1.4 3.525-1.5m8.475-5c0-.8.025-3.25-.1-4.25c-.075-.825-.3-1.95-1.325-2.6c-.625-.325-1.225-.625-4.1-.65m-6.025 0c-2.15 0-3.825.175-4.65 1.2c-.7.957-.659 2.05-.725 2.4c-.15 1.875-.05 8.425-.05 9.525c0 1.15-.075 3.487 1.5 4.275c1.35.675 2.75.575 7.5.6m-.675-20c-.6 0-1.1 0-1.6.525c-.425.4-.36.753-.525 1.375c-.234.875-.35 1.337-.025 1.7c.298.39.799.392 1.242.393h.008c.425.03 1.853.016 2.275 0c.452-.018.817-.043 1.125-.443c.275-.357.112-.952-.05-1.575c-.16-.614-.1-.925-.525-1.45c-.6-.6-1.325-.525-1.925-.525"
        />
      </g>
    </svg>
    <h1 class="font-bold text-2xl mb-4">Vaš OPG čeka na verifikaciju</h1>
    <p class="text-left">
      Kako biste mogli pristupiti vašem OPG računu i koristiti sve funkcionalnosti aplikacije,
      potrebno je pričekati da vaš OPG bude verificiran od strane našeg administratora. Nakon
      uspješne verifikacije, bit ćete obaviješteni putem e-maila i moći ćete se prijaviti u sustav.
    </p>
    <p class="mt-3 font-semibold">Hvala na strpljenju!</p>
    <p class="text-gray-400">OPG Distribucija</p>
    <small class="flex justify-center mt-4 text-gray-400 mb-2"
      >Dok čekate na verifikaciju pogledajte ponudu ostalih OPG-ova:</small
    >
    <div class="flex justify-center space-x-3">
      <router-link :to="{ name: 'e-trznica' }" class="bg-orange-500 text-white p-2 rounded-md"
        >E-Tržnica (OPG-ovi i proizvodi)</router-link
      >
      <router-link :to="{ name: 'farmaPlus' }" class="bg-orange-500 text-white p-2 rounded-md"
        >Farma+ (Usluge)</router-link
      >
    </div>
  </div>
</template>
