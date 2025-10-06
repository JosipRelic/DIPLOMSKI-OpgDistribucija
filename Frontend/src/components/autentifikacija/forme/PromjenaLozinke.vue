<template>
  <div id="content" role="main" class="w-full max-w-md mx-auto p-6">
    <div class="mt-7 bg-white rounded-xl shadow">
      <div class="p-4 sm:p-7">
        <div class="text-center">
          <h1 class="block text-2xl font-bold text-gray-900">Promjena lozinke</h1>
          <p class="mt-2 text-sm text-gray-900">Postavite novu lozinku za svoj korisnički račun.</p>
        </div>

        <div class="mt-5" v-if="imaToken">
          <form @submit.prevent="promijeniLozinku">
            <div class="grid gap-y-2">
              <div class="mx-auto max-w-xs">
                <input
                  v-model.trim="lozinka"
                  class="w-full px-8 py-4 my-1 rounded-lg font-medium bg-white border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
                  type="password"
                  placeholder="Nova lozinka (min 8 znakova)"
                  :disabled="loading"
                  required
                  minlength="8"
                />
                <input
                  v-model.trim="potvrda"
                  class="w-full px-8 py-4 my-1 rounded-lg font-medium bg-white border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600"
                  type="password"
                  placeholder="Potvrdite novu lozinku"
                  :disabled="loading"
                  required
                  minlength="8"
                />

                <p v-if="greska" class="mt-2 text-sm text-red-600">{{ greska }}</p>

                <button
                  type="submit"
                  class="mt-5 tracking-wide font-semibold bg-teal-600 hover:bg-teal-900 text-gray-100 w-full py-4 rounded-lg transition-all duration-300 ease-in-out flex items-center justify-center disabled:opacity-60"
                  :disabled="loading || !mozeSubmit"
                >
                  <svg
                    v-if="loading"
                    class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      class="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      stroke-width="4"
                    />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z" />
                  </svg>
                  Promijenite lozinku
                </button>
              </div>
            </div>
          </form>
        </div>

        <div v-else class="mt-5 text-center text-red-600">
          Neispravan pristup — nedostaje token.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useUiStore } from "@/stores/ui"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"

const ui = useUiStore()
const auth = useAutentifikacijskiStore()
const route = useRoute()
const router = useRouter()

const token = route.query.token?.toString() || ""
const imaToken = computed(() => !!token)

const lozinka = ref("")
const potvrda = ref("")
const loading = ref(false)
const greska = ref("")

const mozeSubmit = computed(() => lozinka.value.length >= 8 && lozinka.value === potvrda.value)

async function promijeniLozinku() {
  greska.value = ""
  if (!mozeSubmit.value) {
    greska.value = "Lozinke moraju imati min. 8 znakova i biti iste."
    return
  }
  loading.value = true
  const { ok, error } = await auth.promijeniLozinkuToken({
    token,
    nova_lozinka: lozinka.value,
    potvrda_lozinke: potvrda.value,
  })
  loading.value = false

  if (ok) {
    ui.obavijest({ tekst: "Lozinka uspješno promijenjena.", tip_obavijesti: "uspjeh" })
    router.push({ name: "prijava" })
  } else {
    greska.value = error
    ui.obavijest({ tekst: error, tip_obavijesti: "upozorenje" })
  }
}
</script>
