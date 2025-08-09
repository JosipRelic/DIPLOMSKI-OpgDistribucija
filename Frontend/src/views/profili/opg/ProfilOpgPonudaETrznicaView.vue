<template>
  <div class="relative overflow-x-auto m-4 shadow-md rounded-lg">
    <div class="flex items-center justify-center p-20 py-4 md:py-8 flex-wrap bg-white">
      <button
        type="button"
        class="border border-gray-200 bg-[#223c2f] text-white shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Domaće voće <span class="text-green-600">(4)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Sezonsko povrće <span class="text-green-600">(2)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Jaja i mliječni proizvodi <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Iz košnice <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Domaća pića i rakije <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Ulja iz prirode <span class="text-green-600">(4)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Čajevi i začinsko bilje <span class="text-green-600">(2)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Suhomesnati proizvodi <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Prirodna kozmetika <span class="text-red-400">(0)</span>
      </button>
      <button
        type="button"
        class="border border-gray-200 hover:text-white hover:bg-[#223c2f] text-gray-600 shadow-md rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3"
      >
        Iz šume i dvorišta <span class="text-red-400">(0)</span>
      </button>
    </div>

    <div
      class="relative overflow-x-auto m-4 shadow-md rounded-lg bg-white p-4 flex items-center gap-2 cursor-pointer hover:bg-gray-100"
      @click="otvoriFormuZaDodavanjeProizvoda"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 32 32">
        <g fill="none">
          <path
            fill="url(#fluentColorAddCircle320)"
            d="M30 16c0 7.732-6.268 14-14 14S2 23.732 2 16S8.268 2 16 2s14 6.268 14 14"
          />
          <path
            fill="url(#fluentColorAddCircle321)"
            d="M15 10a1 1 0 1 1 2 0v5h5a1 1 0 1 1 0 2h-5v5a1 1 0 1 1-2 0v-5h-5a1 1 0 1 1 0-2h5z"
          />
          <defs>
            <linearGradient
              id="fluentColorAddCircle320"
              x1="3"
              x2="22.323"
              y1="7.25"
              y2="27.326"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#52D17C" />
              <stop offset="1" stop-color="#22918B" />
            </linearGradient>
            <linearGradient
              id="fluentColorAddCircle321"
              x1="11.625"
              x2="15.921"
              y1="10.428"
              y2="25.592"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#fff" />
              <stop offset="1" stop-color="#E3FFD9" />
            </linearGradient>
          </defs>
        </g>
      </svg>
      <p class="text-gray-900 rounded-full text-base font-medium">
        {{
          formaZaDodavanjeProizvodaOtvorena
            ? "Dodaj informacije o proizvodu"
            : "Dodaj novi proizovod"
        }}
      </p>
    </div>
    <form
      v-if="formaZaDodavanjeProizvodaOtvorena"
      class="p-4 rounded-lg shadow-md bg-white space-y-4 m-4"
    >
      <div class="flex items-center gap-x-4 justify-center py-2">
        <div class="relative w-20 h-20 group cursor-pointer">
          <input
            ref="odabranaSlikaProizvoda"
            type="file"
            accept="image/*"
            class="hidden"
            @change="promjenaSlike"
          />

          <img
            :src="slikaProizvoda"
            alt="Slika proizvoda"
            class="w-full h-full object-cover rounded-lg transition duration-300"
            @click="odabirSlikeproizvoda"
          />

          <div
            class="absolute inset-0 flex items-center justify-center rounded-lg bg-black/30 opacity-0 group-hover:opacity-100 transition duration-300"
            @click="odabirSlikeproizvoda"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-10 w-10 text-white"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M15.232 5.232l3.536 3.536M9 13l6.768-6.768a2 2 0 112.828 2.828L11.828 16H9v-2.828z"
              />
            </svg>
          </div>
        </div>

        <p class="block text-sm font-medium">Dodajte sliku proizvoda</p>
      </div>

      <div class="flex flex-col items-center mt-2">
        <button
          class="w-full max-w-xs font-bold shadow-sm hover:bg-red-400 rounded-lg py-2 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
        >
          <div class="bg-white p-2 rounded-full">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-6 text-red-600">
              <path
                fill="currentColor"
                d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
              />
            </svg>
          </div>
          <span class="ml-4"> Ispunite glasovno pomoću AI </span>
        </button>
        <small class="pt-2 w-full max-w-xs text-xs"
          >Pritisnite gumb i popunite obrazac glasom npr. "Svježi krastavci s naših polja po cijeni
          od 2 eura po kg..."</small
        >
      </div>
      <div class="border-b text-center">
        <div
          class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
        >
          ili unesite podatke ručno
        </div>
      </div>
      <div>
        <label for="kategorijeProizvoda" class="block mb-2 text-sm font-medium text-gray-900"
          >Odaberi kategoriju proizvoda</label
        >
        <select
          id="countries"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
        >
          <option>Domaće voće</option>
          <option>Sezonsko povrće</option>
          <option>Jaja i mliječni proizvodi</option>
          <option>Iz košnice</option>
          <option>Domaća pića i rakije</option>
          <option>Ulja iz prirode</option>
          <option>Čajevi i začinsko bilje</option>
          <option>Suhomesnati proizvodi</option>
          <option>Prirodna kozmetika</option>
          <option>Iz šume i dvorišta</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium">Proizvod</label>
        <input
          type="text"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          placeholder="Upiši naziv proizvoda..."
        />
      </div>
      <div>
        <label for="kategorijeProizvoda" class="block mb-2 text-sm font-medium text-gray-900"
          >Odaberi mjernu jedinicu proizvoda</label
        >
        <select
          id="countries"
          class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
        >
          <option>kom</option>
          <option>kg</option>
          <option>g</option>
          <option>ml</option>
          <option>l</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium">Cijena</label>
        <div class="flex items-center">
          <input
            type="number"
            class="mt-1 w-xs rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
            placeholder="Upiši cijenu proizvoda npr. 3.99"
          />
          <p class="ms-2 text-xl">€</p>
        </div>
      </div>
      <div>
        <label class="block text-sm font-medium">Opis</label>
        <textarea
          rows="5"
          class="mt-1 w-full rounded-md bg-white px-4 py-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
          placeholder="Upiši opis proizvoda..."
        ></textarea>
      </div>

      <button
        type="submit"
        class="bg-teal-600 text-gray-100 px-4 py-2 rounded-xl hover:bg-teal-900 transition"
      >
        Dodaj proizvod
      </button>
    </form>
    <table class="w-full text-sm text-left rtl:text-right text-gray-500">
      <thead class="text-xs uppercase bg-gray-200 text-gray-700">
        <tr>
          <th scope="col" class="px-16 py-3"></th>
          <th scope="col" class="pe-6 py-3">Proizvod</th>
          <th scope="col" class="px-6 py-3">Opis</th>
          <th scope="col" class="px-4 py-3">Dostupno</th>
          <th scope="col" class="px-6 py-3">Cijena</th>
          <th scope="col" class="px-6 py-3">Mjerna jedinica</th>
          <th scope="col" class="px-6 py-3"></th>
          <th scope="col" class="px-6 py-3"></th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              checked
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
        <tr class="bg-white border-b border-gray-200 group hover:bg-[#223c2f]">
          <td class="p-4">
            <img
              src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              class="w-16 h-16 rounded-lg"
              alt="Krastavci"
            />
          </td>
          <td class="pe-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">Krastavci</td>

          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">
            <!-- <textarea
              class="w-full resize-none rounded-lg border-gray-200 text-center focus:outline-[#223c2f] shadow-sm sm:text-sm p-2"
            >
Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola, puni prirodne svježine i blagih nota koje pristaju svakom jelu."
            </textarea> -->
            Hrskavi, sočni i osvježavajući. Krastavci su nezaobilazni dio ljetnih salata i zdravih
            obroka. Uzgojeni bez pesticida, naši krastavci dolaze izravno s polja do vašeg stola,
            puni prirodne svježine i blagih nota koje pristaju svakom jelu.
          </td>
          <td class="px-4 py-4">
            <input
              type="checkbox"
              class="size-5 rounded-lg border-gray-300 shadow-sm ms-6"
              id="Option1"
              disabled
            />
          </td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">2.99 €</td>
          <td class="px-6 py-4 font-semibold text-gray-600 group-hover:text-gray-100">kg</td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-teal-500 hover:underline">Uredi</a>
          </td>
          <td class="px-6 py-4">
            <a href="#" class="font-medium text-red-500 hover:underline">Obriši</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script setup>
import { ref } from "vue"
const formaZaDodavanjeProizvodaOtvorena = ref(false)
const otvoriFormuZaDodavanjeProizvoda = () => {
  formaZaDodavanjeProizvodaOtvorena.value = !formaZaDodavanjeProizvodaOtvorena.value
}

const slikaProizvoda = ref(
  "https://images.unsplash.com/photo-1675162113465-a3609eedc50d?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTB8fG5vJTIwaW1hZ2V8ZW58MHx8MHx8fDI%3D",
)

const odabranaSlikaProizvoda = ref(null)

const odabirSlikeproizvoda = () => {
  odabranaSlikaProizvoda.value?.click()
}

const promjenaSlike = (event) => {
  const slika = event.target.files[0]
  if (slika) {
    const ucitavanjeSlike = new FileReader()
    ucitavanjeSlike.onload = (e) => {
      slikaProizvoda.value = e.target.result
    }
    ucitavanjeSlike.readAsDataURL(slika)
  }
}
</script>
