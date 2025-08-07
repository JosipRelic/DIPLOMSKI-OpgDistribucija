<template>
  <div
    class="mx-auto max-w-screen-md my-6 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden p-12"
  >
    <form class="w-full">
      <div class="space-y-8">
        <div class="border-b border-gray-900/10 pb-6">
          <div class="flex items-center gap-x-4">
            <div class="relative w-20 h-20 group cursor-pointer">
              <input
                ref="odabranaSlika"
                type="file"
                accept="image/*"
                class="hidden"
                @change="promjenaSlike"
              />

              <img
                :src="slikaProfilaOpg"
                alt="Slika profila"
                class="w-full h-full object-cover rounded-full transition duration-300"
                @click="odabirSlike"
              />

              <div
                class="absolute inset-0 flex items-center justify-center rounded-full bg-black/30 opacity-0 group-hover:opacity-100 transition duration-300"
                @click="odabirSlike"
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

            <div>
              <h2 class="text-2xl font-bold">Postavke profila</h2>
              <p class="mt-1 text-sm text-gray-600">Ovdje možete izmijeniti svoje podatke.</p>
            </div>
          </div>
        </div>

        <div class="border-b border-gray-900/10 pb-12">
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
              >Pritisnite gumb i izmijenite podatke u obrascu glasom npr. "Moja adresa više nije
              Preradovićeva 99, nego Zagrebačka 23..."</small
            >
          </div>
          <div class="border-b text-center">
            <div
              class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2"
            >
              ili unesite podatke ručno
            </div>
          </div>

          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-4 sm:grid-cols-6">
            <div class="sm:col-span-3">
              <label for="ime" class="block text-sm/6 font-medium text-gray-900">Ime</label>
              <div class="mt-2">
                <input
                  type="text"
                  name="ime"
                  id="ime"
                  value="Hrvoje"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="prezime" class="block text-sm/6 font-medium text-gray-900">Prezime</label>
              <div class="mt-2">
                <input
                  type="text"
                  name="prezime"
                  id="prezime"
                  value="Babić"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="nazivOPG" class="block text-sm/6 font-medium text-gray-900"
                >Naziv OPG-a</label
              >
              <div class="mt-2">
                <input
                  type="text"
                  name="nazivOPG"
                  id="NazivOPG"
                  value="OPG Babić"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="prezime" class="block text-sm/6 font-medium text-gray-900"
                >Identifikacijski broj PG-a (MIBPG)</label
              >
              <div class="mt-2">
                <input
                  type="number"
                  name="mibpg"
                  id="mibpg"
                  value="241234"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="brojTelefona" class="block text-sm/6 font-medium text-gray-900"
                >Broj telefona</label
              >
              <div class="mt-2">
                <input
                  id="brojTelefona"
                  name="brojTelefona"
                  type="text"
                  value="0998765432"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="drzava" class="block text-sm/6 font-medium text-gray-900">Država</label>
              <div class="mt-2 grid grid-cols-1">
                <select
                  id="drzava"
                  name="drzava"
                  class="col-start-1 row-start-1 w-full appearance-none rounded-md bg-white py-2 pr-8 pl-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                >
                  <option>Hrvatska</option>
                </select>
              </div>
            </div>

            <div class="col-span-full">
              <label for="adresa" class="block text-sm/6 font-medium text-gray-900">Adresa</label>
              <div class="mt-2">
                <input
                  type="text"
                  name="adresa"
                  id="adresa"
                  value="Preradovićeva 99"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>
            <div class="sm:col-span-full">
              <label for="zupanija" class="block text-sm/6 font-medium text-gray-900"
                >Županija</label
              >
              <div class="mt-2">
                <input
                  type="text"
                  name="zupanija"
                  id="zupanija"
                  value="Sisačko-Moslavačka"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>
            <div class="sm:col-span-3">
              <label for="grad" class="block text-sm/6 font-medium text-gray-900">Grad</label>
              <div class="mt-2">
                <input
                  type="grad"
                  name="grad"
                  id="grad"
                  value="Sisak"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="postanskiBroj" class="block text-sm/6 font-medium text-gray-900"
                >Poštanski broj</label
              >
              <div class="mt-2">
                <input
                  type="text"
                  name="postanskiBroj"
                  id="postanskiBroj"
                  value="44000"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mt-6 flex items-center justify-start gap-x-6">
        <button
          type="submit"
          class="rounded-md bg-teal-600 hover:bg-teal-900 text-gray-100 px-3 py-2 text-sm font-semibold shadow-xs focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-600"
        >
          Ažuriraj podatke
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue"

const slikaProfilaOpg = ref(
  "https://images.unsplash.com/photo-1660412230160-9bc219efcb00?w=700&auto=format&fit=crop&q=60",
)

const odabranaSlika = ref(null)

const odabirSlike = () => {
  odabranaSlika.value?.click()
}

const promjenaSlike = (event) => {
  const slika = event.target.files[0]
  if (slika) {
    const ucitavanjeSlike = new FileReader()
    ucitavanjeSlike.onload = (e) => {
      slikaProfilaOpg.value = e.target.result
    }
    ucitavanjeSlike.readAsDataURL(slika)
  }
}
</script>
