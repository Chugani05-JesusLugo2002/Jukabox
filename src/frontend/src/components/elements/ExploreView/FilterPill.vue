<script setup lang="ts">
const { selected } = defineProps(['selected'])
</script>

<template>
  <button :class="`btn rounded-pill mx-1 my-2 fw-bold btn-${!selected ? 'outline-' : ''}primary`">
    <slot></slot>
  </button>
</template>
