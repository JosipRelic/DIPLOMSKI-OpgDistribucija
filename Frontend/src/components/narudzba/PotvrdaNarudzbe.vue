<template>
  <div
    class="mx-auto max-w-screen-lg my-12 bg-white flex flex-col md:flex-row rounded-2xl shadow-lg overflow-hidden"
  >
    <div class="hidden md:block w-full md:w-1/2">
      <img
        src="https://images.unsplash.com/photo-1582803824122-f25becf36ad8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODN8fHNob3BwaW5nJTIwYmFnfGVufDB8fDB8fHwy"
        class="h-full w-full object-cover"
      />
    </div>

    <div class="w-full md:w-1/2 p-8 space-y-6">
      <h2 class="text-sm font-medium text-green-600">Narudžba uspješno poslana</h2>
      <h1 class="text-3xl font-bold text-gray-900">Hvala na narudžbi!</h1>
      <p class="text-gray-600">
        Zahvaljujemo na Vašoj narudžbi. Trenutno je obrađujemo i uskoro ćemo Vam poslati potvrdu
        putem e-maila.
      </p>

      <div>
        <p class="text-sm font-medium text-gray-700">Broj narudžbe:</p>
        <a href="#" class="text-orange-600 font-semibold hover:underline">5154787875554584512</a>
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
      </div>

      <div>
        <router-link :to="{ name: 'pocetna' }" class="text-orange-600 font-medium hover:underline"
          >Nastavi kupovinu →</router-link
        >
      </div>
    </div>
  </div>
</template>
