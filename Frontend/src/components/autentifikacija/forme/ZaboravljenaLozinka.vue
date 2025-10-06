<template>
  <div id="content" role="main" class="w-full max-w-md mx-auto p-6">
    <div class="mt-7 bg-white rounded-xl shadow">
      <div class="p-4 sm:p-7">
        <div class="text-center">
          <h1 class="block text-2xl font-bold text-gray-900">Zaboravili ste lozinku?</h1>
          <p class="mt-2 text-sm text-gray-900">
            Sjetili ste se lozinke?
            <router-link
              :to="{ name: 'prijava' }"
              class="text-teal-700 decoration-2 hover:underline font-medium"
            >
              Prijavite se ovdje
            </router-link>
          </p>
        </div>

        <div class="mt-5">
          <form @submit.prevent="posaljiZahtjev">
            <div class="grid gap-y-2">
              <div>
                <div class="mx-auto max-w-xs">
                  <input
                    v-model.trim="email"
                    class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white"
                    type="email"
                    placeholder="Unesite email adresu"
                    :disabled="loading || poslanZahtjev"
                    required
                  />

                  <p v-if="greska" class="mt-2 text-sm text-red-600">{{ greska }}</p>
                  <p v-if="poslanZahtjev" class="mt-2 text-sm text-teal-700">
                    Ako postoji račun s tom adresom, poslali smo vam link za oporavak.
                  </p>

                  <button
                    type="submit"
                    class="mt-5 tracking-wide font-semibold bg-teal-600 hover:bg-teal-900 text-gray-100 w-full py-4 rounded-lg transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none disabled:opacity-60"
                    :disabled="loading || !emailValidan || poslanZahtjev"
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
                    Zatraži link za oporavak
                  </button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed } from "vue"
import { useUiStore } from "@/stores/ui"
import { useAutentifikacijskiStore } from "@/stores/autentifikacija"

const ui = useUiStore()
const auth = useAutentifikacijskiStore()

const email = ref("")
const loading = ref(false)
const greska = ref("")
const poslanZahtjev = ref(false)

const emailValidan = computed(() => /\S+@\S+\.\S+/.test(email.value))

async function posaljiZahtjev() {
  greska.value = ""
  if (!emailValidan.value) {
    greska.value = "Unesite ispravnu e-mail adresu."
    return
  }
  loading.value = true
  const { ok } = await auth.zatraziLinkZaOporavak(email.value)
  loading.value = false

  poslanZahtjev.value = true
  ui.obavijest({
    tekst: "Ako e-mail postoji, poslan je link za oporavak.",
    tip_obavijesti: ok ? "uspjeh" : "informacija",
  })
}
</script>
