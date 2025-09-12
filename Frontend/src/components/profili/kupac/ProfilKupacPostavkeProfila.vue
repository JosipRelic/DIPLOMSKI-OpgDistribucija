<template>
  <div
    class="mx-auto max-w-screen-md my-6 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden p-12"
  >
    <form @submit.prevent="azurirajPodatkeKupca" class="w-full">
      <div class="space-y-8">
        <div class="border-b border-gray-900/10 pb-6">
          <div class="flex items-center gap-x-4">
            <div class="relative w-20 h-20 group cursor-pointer">
              <input
                ref="odabranaSlika"
                type="file"
                accept="image/*"
                class="hidden"
                @change.prevent="promjenaSlike"
              />

              <img
                :src="slika"
                alt="Slika profila"
                class="w-full h-full object-cover rounded-full transition duration-300"
                @click.prevent="odabirSlike"
              />

              <div
                class="absolute inset-0 flex items-center justify-center rounded-full bg-black/30 opacity-0 group-hover:opacity-100 transition duration-300"
                @click.prevent="odabirSlike"
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
                  id="ime"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.ime"
                  placeholder="Upišite ime..."
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="prezime" class="block text-sm/6 font-medium text-gray-900">Prezime</label>
              <div class="mt-2">
                <input
                  type="text"
                  id="prezime"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.prezime"
                  placeholder="Unesite prezime..."
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="brojTelefona" class="block text-sm/6 font-medium text-gray-900"
                >Broj telefona</label
              >
              <div class="mt-2">
                <input
                  type="text"
                  id="brojTelefona"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.broj_telefona"
                  placeholder="Unesite broj telefona..."
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="drzava" class="block text-sm/6 font-medium text-gray-900">Država</label>
              <div class="mt-2 grid grid-cols-1">
                <input
                  type="text"
                  id="drzava"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.drzava"
                  placeholder="Unesite drzavu..."
                />
              </div>
            </div>

            <div class="col-span-full">
              <label for="adresa" class="block text-sm/6 font-medium text-gray-900">Adresa</label>
              <div class="mt-2">
                <input
                  type="text"
                  id="adresa"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.adresa"
                  placeholder="Unesite adresu..."
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
                  id="zupanija"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.zupanija"
                  placeholder="Unesite županiju..."
                />
              </div>
            </div>
            <div class="sm:col-span-3">
              <label for="grad" class="block text-sm/6 font-medium text-gray-900">Grad</label>
              <div class="mt-2">
                <input
                  type="text"
                  id="grad"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.grad"
                  placeholder="Unesite grad..."
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
                  id="postanskiBroj"
                  class="block w-full rounded-md bg-white px-3 py-2 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                  v-model.trim="forma.postanski_broj"
                  placeholder="Unesite poštanski broj..."
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div
        v-if="obavijest"
        :class="
          obavijest.tip_obavijesti === 'Uspjeh'
            ? 'bg-green-100 text-green-700'
            : 'bg-red-100 text-red-700'
        "
        class="p-3 rounded-md mt-4"
      >
        {{ obavijest.poruka }}
        <button
          @click="obavijest = null"
          class="ml-4 text-xl leading-none float-end text-gray-600 hover:text-gray-600"
        >
          &times;
        </button>
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
  <div
    class="mx-auto max-w-screen-md my-6 bg-red-400 flex flex-col md:flex-row rounded-2xl shadow-lg shadow-red-400 overflow-hidden p-4"
  >
    <div class="flex items-center gap-4">
      <svg
        class="text-white"
        xmlns="http://www.w3.org/2000/svg"
        width="100"
        height="100"
        viewBox="0 0 24 24"
        fill="currentColor"
      >
        <path
          fill="currentColor"
          d="M18 19a3 3 0 0 1-3 3H8a3 3 0 0 1-3-3V7H4V4h4.5l1-1h4l1 1H19v3h-1v12M6 7v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2-2V7H6m12-1V5h-4l-1-1h-3L9 5H5v1h13M8 9h1v10H8V9m6 0h1v10h-1V9Z"
        />
      </svg>

      <div class="flex-1">
        <strong class="font-medium text-white"> Brisanje profila </strong>

        <p class="mt-0.5 text-sm text-white">
          Brisanjem profila trajno se uklanjaju svi vaši podaci. Ova radnja je nepovratna.
        </p>

        <div class="mt-3 flex items-center gap-2">
          <button
            type="button"
            @click.prevent="obrisiProfil"
            :disabled="autentifikacija.loading"
            class="rounded border border-gray-300 px-3 py-1.5 text-sm font-medium text-white shadow-sm transition-colors hover:bg-white hover:text-red-500"
          >
            Obriši profil
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, computed, watchEffect, reactive } from "vue"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"
import { useRouter } from "vue-router"

const autentifikacija = useAutentifikacijskiStore()
const router = useRouter()

const obavijest = ref(null)

const odabranaSlika = ref(null)
const novaSlika = ref(null)
const lokalniPretpregledSlike = ref(null)

const slika = computed(
  () =>
    lokalniPretpregledSlike.value ||
    autentifikacija.korisnicki_profil?.slika_profila ||
    "https://placehold.co/80x80?text=SlikaProfila",
)

const odabirSlike = () => {
  odabranaSlika.value?.click()
}

const promjenaSlike = async (event) => {
  const slika = event.target.files?.[0]
  if (!slika) {
    return
  }

  if (lokalniPretpregledSlike.value) URL.revokeObjectURL(lokalniPretpregledSlike.value)

  novaSlika.value = slika
  lokalniPretpregledSlike.value = URL.createObjectURL(slika)
}

const forma = reactive({
  ime: "",
  prezime: "",
  broj_telefona: "",
  drzava: "",
  zupanija: "",
  grad: "",
  postanski_broj: "",
  adresa: "",
  slug: "",
})

onMounted(async () => {
  await autentifikacija.dohvatiProfil()
})

watchEffect(() => {
  const kp = autentifikacija.korisnicki_profil || {}
  forma.ime = kp.ime || ""
  forma.prezime = kp.prezime || ""
  forma.broj_telefona = kp.broj_telefona || ""
  forma.drzava = kp.drzava || ""
  forma.zupanija = kp.zupanija || ""
  forma.grad = kp.grad || ""
  forma.postanski_broj = kp.postanski_broj || ""
  forma.adresa = kp.adresa || ""
  forma.slug = kp.slug || ""
})

const azurirajPodatkeKupca = async (e) => {
  e.preventDefault()
  try {
    await autentifikacija.azurirajProfil({
      ...forma,
    })

    if (novaSlika.value) {
      const ok = await autentifikacija.ucitajSlikuProfila(novaSlika.value)
      if (!ok) throw new Error("Neuspješan upload slike")
      novaSlika.value = null
      if (odabranaSlika.value) odabranaSlika.value.value = ""
      if (lokalniPretpregledSlike.value) {
        URL.revokeObjectURL(lokalniPretpregledSlike.value)
        lokalniPretpregledSlike.value = null
      }
    }

    obavijest.value = { tip_obavijesti: "Uspjeh", poruka: "Podaci su uspješno ažurirani." }
    if (obavijest.value) {
      setTimeout(() => {
        obavijest.value = null
      }, 4000)
    }
  } catch (err) {
    obavijest.value = { tip_obavijesti: "Greška", poruka: "Greška pri ažuriranju podataka." }
    if (obavijest.value) {
      setTimeout(() => {
        obavijest.value = null
      }, 4000)
    }
  }
}

const obrisiProfil = async () => {
  if (confirm("Jeste li sigurni da želite obrisati profil? Ova radnja je nepovratna.")) {
    const ok = await autentifikacija.obrisiProfil()
    if (ok) {
      router.push({ name: "pocetna" })
    }
  }
}
</script>
