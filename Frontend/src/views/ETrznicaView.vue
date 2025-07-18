<template>
  <section>
    <NaslovnaEtrznica />
  </section>

  <section class="bg-[#f5ebdc] py-12 my-4">
    <div class="max-w-screen-xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-10 text-center">
        <div class="flex flex-col items-center">
          <div class="bg-[#223c2f] p-4 rounded-full mb-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-8 h-8 text-orange-50"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
              />
            </svg>
          </div>
          <h3 class="text-lg font-semibold text-gray-900 mb-1">Pronađite lokalni OPG</h3>
          <p class="text-gray-600 text-sm">Pretražujte proizvođače u vašoj blizini</p>
        </div>

        <div class="flex flex-col items-center">
          <div class="bg-[#223c2f] p-4 rounded-full mb-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-8 h-8 text-orange-50"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
              />
            </svg>
          </div>
          <h3 class="text-lg font-semibold text-gray-900 mb-1">Kupujte direktno</h3>
          <p class="text-gray-600 text-sm">Naručite proizvode izravno od OPG-ova</p>
        </div>

        <div class="flex flex-col items-center">
          <div class="bg-[#223c2f] p-4 rounded-full mb-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-8 h-8 text-orange-50"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15.182 15.182a4.5 4.5 0 0 1-6.364 0M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Z"
              />
            </svg>
          </div>
          <h3 class="text-lg font-semibold text-gray-900 mb-1">Uživajte u svježim proizvodima</h3>
          <p class="text-gray-600 text-sm">Nabavite sezonske i domaće proizvode</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <ProizvodiETrznica />
  </section>

  <section>
    <div class="bg-[#f5ebdc] py-10 sm:py-20">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <dl class="grid grid-cols-1 gap-x-8 gap-y-16 text-center lg:grid-cols-3">
          <div
            v-for="podatak in dummy_podaci"
            :key="podatak.id"
            class="mx-auto flex max-w-xs flex-col gap-y-4"
          >
            <dt class="text-base/7 text-gray-900">{{ podatak.name }}</dt>
            <dd
              class="order-first text-3xl font-semibold tracking-tight text-[#223c2f] sm:text-5xl"
            >
              {{ podatak.value }}
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </section>

  <section>
    <OpgoviETrznica />
  </section>
</template>
<script setup>
import NaslovnaEtrznica from "@/components/etrznica/NaslovnaETrznica.vue"
import ProizvodiETrznica from "@/components/etrznica/ProizvodiETrznica.vue"
import OpgoviETrznica from "@/components/etrznica/OpgoviETrznica.vue"

const dummy_podaci = [
  { id: 1, name: "Registriranih OPG-ova", value: "120" },
  { id: 2, name: "Proizvoda u ponudi", value: "5000+" },
  { id: 3, name: "Narudžbi", value: "200+" },
]
</script>
