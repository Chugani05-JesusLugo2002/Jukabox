<script setup lang="ts">
const props = defineProps(['url'])
</script>

<template>
  <a :href="url" target="_blank">
    {{ url }}
  </a>
</template>
