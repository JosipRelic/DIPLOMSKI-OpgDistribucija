<template>
  <div
    class="mx-auto max-w-screen-lg my-6 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden"
  >
    <div class="w-full p-8 space-y-6">
      <h1 class="text-3xl font-bold text-gray-900">Detalji narudžbe</h1>
      <div class="flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="-ms-1 me-1.5 size-4">
          <path
            fill="none"
            class="stroke-amber-600"
            stroke-width="2"
            d="M1 1h22M10 4.5h4V6c0 1-2 2-2 2s-2-1-2-2V4.5ZM5 1v5c0 3 5 3.235 5 6s-5 3-5 6v5M19 1v5c0 3-5 3.235-5 6s5 3 5 6v5M1 23h22M8 21c0-2 4-4 4-4s4 2 4 4v2H8v-2Z"
          />
        </svg>
        <h2 class="text-lg font-medium text-amber-600">U tijeku</h2>
        <button type="button" class="ms-2 cursor-pointer" title="Promijeni status">✏️</button>
      </div>
      <div>
        <p class="text-sm font-medium text-gray-700">Broj narudžbe:</p>
        <p class="text-orange-600 font-semibold">#234521</p>
      </div>

      <div class="divide-y divide-gray-200 border-t border-b">
        <div class="flex py-4 items-center space-x-4">
          <img
            src="https://images.unsplash.com/photo-1611048661702-7b55eed346b4?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            class="w-16 h-16 object-cover rounded"
          />
          <div class="flex-1">
            <p class="text-sm font-semibold text-gray-900">Krastavci</p>
            <p class="text-sm text-gray-500">Količina: 1 KG</p>
          </div>
          <p class="text-sm text-gray-900">2.99 €</p>
        </div>
        <div class="flex py-4 items-center space-x-4">
          <img
            src="https://images.unsplash.com/photo-1518977956812-cd3dbadaaf31?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            class="w-16 h-16 object-cover rounded"
            alt="Artwork Tee"
          />
          <div class="flex-1">
            <p class="text-sm font-semibold text-gray-900">Luk</p>
            <p class="text-sm text-gray-500">Količina: 1 KG</p>
          </div>
          <p class="text-sm text-gray-900">0.99 €</p>
        </div>
        <div class="flex py-4 items-center space-x-4">
          <img
            src="https://images.unsplash.com/photo-1669863347362-1630fe821708?q=80&w=1548&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            class="w-16 h-16 object-cover rounded"
            alt="Artwork Tee"
          />
          <div class="flex-1">
            <p class="text-sm font-semibold text-gray-900">Paprika</p>
            <p class="text-sm text-gray-500">Količina: 1 KG</p>
          </div>
          <p class="text-sm text-gray-900">1.59 €</p>
        </div>
      </div>

      <div class="space-y-2">
        <div class="flex justify-between text-sm">
          <span>Ukupan iznos bez PDV-a</span><span>4.18 €</span>
        </div>
        <div class="flex justify-between text-sm"><span>PDV (25%)</span><span>1.39 €</span></div>
        <div class="flex justify-between text-sm">
          <span>Dostava</span><span>Besplatna (osobno preuzimanje)</span>
        </div>
        <div class="flex justify-between font-semibold text-lg border-t pt-2">
          <span>Ukupno</span><span>5.57 €</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm text-gray-700 border-t pt-6">
        <div>
          <p class="font-medium">Podaci dostave</p>
          <p>
            Ivan Horvat<br />ihorvat@gmail.com<br />0998765432<br />Preradovićeva 99, Sisak 44000<br />
            Sisačko-Moslavačka, Hrvatska
          </p>
        </div>
        <div>
          <p class="font-medium">Način plaćanja</p>
          <p class="inline">Pouzećem</p>
        </div>
        <div>
          <p class="font-medium">Način dostave</p>
          <p class="inline">Osobno preuzimanje</p>
        </div>
      </div>

      <div class="w-full mt-6">
        <button
          @click="otvoriFormuNarudzbe"
          class="bg-orange-500 text-gray-100 px-4 py-2 rounded-xl shadow hover:bg-orange-900 transition"
        >
          {{ formaOtvorena ? "Sakrij formu" : "Pošalji email vezan uz narudžbu" }}
        </button>

        <form
          v-if="formaOtvorena"
          class="mt-4 p-6 border border-gray-200 rounded-xl shadow bg-white space-y-4"
        >
          <div>
            <label class="block text-sm font-medium">Broj Narudžbe </label>
            <span class="text-xs text-gray-400"
              >Automatski se dodaje kao dio predmeta prilikom slanja e-maila</span
            >
            <input
              type="email"
              class="mt-1 w-full rounded-md bg-white text-base text-gray-500 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              value="#234521"
              disabled
            />
          </div>
          <div>
            <label class="block text-sm font-medium">Email</label>

            <input
              type="email"
              class="mt-1 w-full rounded-md bg-white text-base text-gray-500 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              value="ihorvat@gmail.com"
              disabled
            />
          </div>
          <div class="flex flex-col items-center">
            <button
              class="w-full max-w-xs font-bold shadow-sm hover:bg-red-400 rounded-lg py-2 bg-red-300 text-gray-900 flex items-center justify-center transition-all duration-300 ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline"
            >
              <div class="bg-white p-2 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  class="w-6 text-red-600"
                >
                  <path
                    fill="currentColor"
                    d="m20.713 7.128l-.246.566a.506.506 0 0 1-.934 0l-.246-.566a4.36 4.36 0 0 0-2.22-2.25l-.759-.339a.53.53 0 0 1 0-.963l.717-.319A4.37 4.37 0 0 0 19.276.931L19.53.32a.506.506 0 0 1 .942 0l.253.61a4.37 4.37 0 0 0 2.25 2.327l.718.32a.53.53 0 0 1 0 .962l-.76.338a4.36 4.36 0 0 0-2.219 2.251M8.5 6h-2v12h2zM4 10H2v4h2zm9-8h-2v20h2zm4.5 6h-2v10h2zm4.5 2h-2v4h2z"
                  />
                </svg>
              </div>
              <span class="ml-4"> Ispunite glasovno pomoću AI </span>
            </button>
            <small class="pt-2 w-full max-w-xs text-xs"
              >Pritisnite gumb i popunite obrazac glasom npr. "Nemamo proizvod na stanju. Nažalost
              proizvod koji ste tražili nemamo na stanju itd..."</small
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
            <label class="block text-sm font-medium">Predmet</label>
            <input
              type="text"
              class="mt-1 w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              placeholder="Upiši predmet..."
            />
          </div>
          <div>
            <label class="block text-sm font-medium">Poruka</label>
            <textarea
              rows="5"
              class="mt-1 w-full rounded-md bg-white px-4 py-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
              placeholder="Upiši poruku..."
            ></textarea>
          </div>

          <button
            type="submit"
            class="bg-teal-600 text-gray-100 px-4 py-2 rounded-xl hover:bg-teal-900 transition"
          >
            Pošalji
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
const formaOtvorena = ref(false)
const otvoriFormuNarudzbe = () => {
  formaOtvorena.value = !formaOtvorena.value
}
</script>
