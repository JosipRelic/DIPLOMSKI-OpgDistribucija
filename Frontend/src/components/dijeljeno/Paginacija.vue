<template>
  <div class="flex justify-center mt-4">
    <ol
      v-if="ukupnoStranica > 1"
      class="flex border border-gray-200 shadow-md rounded-md items-center justify-center max-w-full"
    >
      <li>
        <button
          :disabled="stranica <= 1"
          @click="$emit('idi-na', stranica - 1)"
          class="text-black border-r border-gray-200 font-semibold px-4 py-2 cursor-pointer"
        >
          Prethodna stranica
        </button>
      </li>

      <li v-for="n in ukupnoStranica" :key="n">
        <button
          @click="$emit('idi-na', n)"
          class="flex space-x-2 px-4 py-2 cursor-pointer border"
          :class="
            n === stranica
              ? 'border-gray-300 bg-orange-500 text-white shadow-3xl shadow-orange-500'
              : 'border-gray-100'
          "
        >
          {{ n }}
        </button>
      </li>

      <li>
        <button
          :disabled="stranica >= ukupnoStranica"
          @click="$emit('idi-na', stranica + 1)"
          class="text-black border-l border-gray-200 font-semibold px-4 py-2 cursor-pointer"
        >
          Sljedeća stranica
        </button>
      </li>
    </ol>
  </div>
</template>

<script setup>
defineProps({
  stranica: { type: Number, default: 1 },
  ukupnoStranica: { type: Number, default: 1 },
})
defineEmits(["idi-na"])
</script>
