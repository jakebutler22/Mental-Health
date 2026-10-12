<script setup>
defineProps({ decorative: { type: Boolean, default: true } });
</script>
<template>
  <svg class="guac-mark" viewBox="0 0 64 76" :aria-hidden="decorative" role="img" :aria-label="decorative ? undefined : 'Guac avocado'">
    <path d="M32 3C19 3 23 18 12 32C-3 51 8 71 31 73C57 75 70 52 52 31C42 19 44 3 32 3Z" fill="#243D25"/>
    <path d="M32 10C24 10 27 23 17 37C6 51 14 65 32 66C49 67 59 53 47 38C37 25 40 10 32 10Z" fill="#DCE8AD"/>
    <circle cx="32" cy="49" r="13" fill="#8B563B"/>
    <path d="M26 41C28 38 34 38 37 41" fill="none" stroke="#BC8C65" stroke-width="3" stroke-linecap="round"/>
    <path d="M27 18C26 25 23 30 21 33" fill="none" stroke="#FAF8EF" stroke-width="3" stroke-linecap="round"/>
  </svg>
</template>
