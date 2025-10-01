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
              href="#"
            >
              Prijavite se ovdje
            </router-link>
          </p>
        </div>

        <div class="mt-5">
          <form>
            <div class="grid gap-y-2">
              <div>
                <div class="mx-auto max-w-xs">
                  <input
                    class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 focus:bg-white"
                    type="email"
                    placeholder="Unesite email adresu"
                  />
                  <button
                    type="submit"
                    class="mt-5 tracking-wide font-semibold bg-teal-600 hover:bg-teal-900 text-gray-100 w-full py-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none"
                  >
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
