<template>
  <!--Naslovna sekcija-->
  <section
    class="overflow-hidden bg-cover bg-center bg-no-repeat"
    :style="`background-image: url(${slikeCoverPocetna})`"
  >
    <NaslovnaPocetna />
  </section>

  <!--Najprodavaniji proizvodi-->
  <section>
    <span class="flex items-center py-8">
      <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>

      <span class="shrink-0 px-4 text-gray-900 text-3xl">Najprodavaniji proizvodi</span>

      <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
    </span>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-20 py-8">
      <KarticaProizvoda />
    </div>
  </section>

  <!--Najbolje ocijenjeni opg-ovi-->

  <section>
    <span class="flex items-center py-6">
      <span class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></span>

      <span class="shrink-0 px-4 text-gray-900 text-3xl">Najbolje ocijenjeni OPG-ovi</span>

      <span class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></span>
    </span>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-20 py-8 mb-14">
      <KarticaOPGa />
    </div>
  </section>

  <section>
    <div class="flex items-center justify-center space-x-4 text-3xl my-8">
      <div class="h-px flex-1 bg-gradient-to-r from-transparent to-gray-300"></div>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="100"
        height="100"
        viewBox="0 0 24 24"
        class="text-[#223c2f]"
      >
        <g
          fill="none"
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="1.5"
          color="currentColor"
        >
          <circle cx="6.5" cy="16.5" r="4.5" />
          <circle cx="19" cy="18" r="3" />
          <path
            d="M2 10.5a7.5 7.5 0 0 1 11.995 6.287c-.023.604-.034.907.113 1.06s.42.153.965.153H16m-3-9l3.106.582c2.34.44 3.511.659 4.202 1.492c.692.833.692 2.03.692 4.426M20 12h-1"
          />
          <path
            d="M13 12.5V9.587q0-.587-.169-1.15L11.5 3M4 9V3M3 3h10m5 6.5V8a2 2 0 0 1 2-2M7 9V3"
          />
        </g>
      </svg>

      <div class="w-10 h-px bg-gray-300"></div>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="100"
        height="100"
        viewBox="0 0 24 24"
        class="text-[#223c2f]"
      >
        <path
          fill="currentColor"
          d="M11 12H8.82c.8.5 1.53 1.07 2.18 1.68V12m-4-1c.27-5.12 2.37-9 5-9c2.66 0 4.77 3.94 5 9.12c1.5-.69 3.17-1.12 5-1.12c-5.75 2.57-3.75 12-10 12c-6 0-4.07-9.43-10-12c1.82 0 3.5.4 5 1m4 0V9H8.24l-.21 2H11m0-3V6H9.05c-.25.6-.45 1.27-.62 2H11m0-3V3.3c-.55.33-1.05.92-1.5 1.7H11m1-2v2h1v1h-1v2h2v1h-2v2h3v1h-3v2h2v1h-1.77c1.19 1.45 1.92 3 2.09 4.23c.99-1.67 1.64-4.39 1.68-7.47C15.94 7 14.13 3 12 3Z"
        />
      </svg>
      <div class="w-10 h-px bg-gray-300"></div>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="100"
        height="100"
        viewBox="0 0 512 512"
        class="text-[#223c2f]"
      >
        <path
          fill="currentColor"
          d="M468.958 108.958c-27.507 2.08-48.997 7.94-71.375 22.572c-5.333-2.214-12.62-17.738-16-16c-11.82 6.08-14.892 19.555-4.916 32.817l-59.084 9.916c-24.776 3.341-49.567 4.838-74.187 5.334c1.326 3.832 2.96 7.636 4.812 10.05c5.219 6.802 20.323 6.21 21.07 14.75c1.935 22.098-24.876 47.415-47.056 47.057c-15.401-.248-17.017-28.762-31.604-33.713c-19.097-6.482-41.62 18.77-59.699 9.832c-15.267-7.547-24.992-39.8-27.836-50.41c-10.213-.127-20.327-.142-30.316.035c-12.564.366-22.902 5.645-29.408 14.239c-8.676 11.458-11.652 26.658-13.254 42.925c-1.78 18.057 6.147 53.007 5.517 70.282c-.504 13.85-7.493 11.87-11.912 18.888c-13.52 21.47 8.894 20.83 17.014 5.56c12.482-23.473 4.253-63.11 7.195-92.974c1.855-35.76 10.597-23.937 15.664-24.588c-4.2 13.065-6.21 30.962-7 51.334c6.895-2.342 36.498-11.6 42.73-.174c6.872 12.598-27.802 22.016-23.878 35.819c2.464 8.666 22.95 2.378 24.582 11.238c3.322 18.035-32.13 38.713-42.236 44.209c.812 23.329 1.564 45.567 1.238 65.086H88.91c-4.234-16.543-12.038-49.944-4.06-55.084c21.425-18.091 29.836-37.484 42.732-56.428c8.755 2.556 16.92 4.787 24.782 6.672c3.553.972 7.244 1.771 10.984 2.44c24.859 4.967 61.553 5.678 90.783-.172c3.76 34.12 7.263 68.452 4.602 102.572h28.957c-12.375-26.902-4.263-65.044 13.892-86.27l44.934-33.462c24.881-16.384 42.93-37.996 55.982-63.38c30.402 3.413 57.086 3.29 77.192-.786l12.84-19.55c-24.257-17.857-43.3-36.585-62.948-58.13c10.063-14.533 25.027-22.765 39.375-32.506zm-39.375 54.572a8 8 0 1 1 0 16a8 8 0 0 1 0-16zM366.2 183.481c5.029 9.822-26.17 10.808-24.933 21.772c.998 8.847 22.204 3.839 23.53 12.643c3.818 25.373-28.44 53.805-54.08 54.78c-14.262.544-34.902-14.06-32.308-28.093c2.605-14.092 34.551-1.657 40.383-14.748c4.724-10.603-18.352-22.01-12.992-32.307c6.264-12.032 30.364-22.553 41.934-22.646c11.57-.093 15.606 3.347 18.466 8.6zm-26.585 126.346l-34.707 23.96l6.464 69.255h34.414c-11.783-22.454-15.58-55.506-6.171-93.215zm-204.561 1.41c-6.047 12.184-14.147 21.97-22.174 31.242c5.97 3.235 11.648 5.414 17.154 6.614c11.218 2.443 21.636.333 29.948-4.408c10.056-5.737 17.521-14.452 24.115-23.368c-14.615-.869-32.96-2.962-49.043-10.08zm24.252 52c-8.737 2.585-17.452 3.7-25.566 2.96c5.167 12.624 10.45 24.152 15.824 36.845h28.306c-10.393-18.48-16.148-29.285-18.564-39.805z"
        />
      </svg>
      <div class="h-px flex-1 bg-gradient-to-l from-transparent to-gray-300"></div>
    </div>

    <FarmaPlusSekcija />
  </section>
</template>

<script setup>
import slikeCoverPocetna from "@/assets/slike/cover-pocetna.jpg"
import NaslovnaPocetna from "@/components/pocetna/NaslovnaPocetna.vue"
import KarticaProizvoda from "@/components/dijeljeno/KarticaProizvoda.vue"
import KarticaOPGa from "@/components/dijeljeno/KarticaOPGa.vue"
import FarmaPlusSekcija from "@/components/pocetna/FarmaPlusSekcija.vue"
</script>
