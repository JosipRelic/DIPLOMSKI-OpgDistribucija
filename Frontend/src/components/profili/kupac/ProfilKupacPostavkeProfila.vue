<template>
  <div
    class="mx-auto max-w-screen-md my-6 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden p-12"
  >
    <form class="w-full">
      <div class="space-y-12">
        <div class="border-b border-gray-900/10 pb-6">
          <h2 class="text-2xl font-bold">Postavke profila</h2>
          <p class="mt-1 text-sm/6 text-gray-600">
            Ovdje možete dodati i izmijeniti svoje podatke. Podaci se koriste za informacije o
            dostavi.
          </p>
        </div>

        <div class="border-b border-gray-900/10 pb-12">
          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div class="col-span-full">
              <label for="slikaProfila" class="block text-sm/6 font-medium text-gray-900"
                >Slika profila</label
              >
              <div class="mt-2 flex items-center gap-x-3">
                <img
                  class="mr-1 w-20 h-20 object-cover rounded-full"
                  src="https://images.unsplash.com/photo-1660412230160-9bc219efcb00?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bWFsZSUyMHNob3BwZXJ8ZW58MHx8MHx8fDI%3D"
                  alt=""
                />
                <button
                  type="button"
                  class="rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-xs ring-1 ring-gray-300 ring-inset hover:bg-gray-50"
                >
                  Promjeni
                </button>
              </div>
            </div>
          </div>

          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
            <div class="sm:col-span-3">
              <label for="ime" class="block text-sm/6 font-medium text-gray-900">Ime</label>
              <div class="mt-2">
                <input
                  type="text"
                  name="ime"
                  id="ime"
                  value="Ivan"
                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
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
                  value="Horvat"
                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
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
                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="drzava" class="block text-sm/6 font-medium text-gray-900">Država</label>
              <div class="mt-2 grid grid-cols-1">
                <select
                  id="drzava"
                  name="drzava"
                  class="col-start-1 row-start-1 w-full appearance-none rounded-md bg-white py-1.5 pr-8 pl-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
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
                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
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
                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
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
                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
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
                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-teal-600 sm:text-sm/6"
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
