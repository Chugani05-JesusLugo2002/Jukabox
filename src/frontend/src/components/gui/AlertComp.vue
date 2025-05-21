<script setup lang="ts">
const { style } = defineProps(['style'])
</script>

<template>
  <div :class="`alert alert-${style} text-center fw-bold`" role="alert">
    <slot></slot>
  </div>
</template>
