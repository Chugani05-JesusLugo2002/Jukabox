<script setup lang="ts">
const props = defineProps(['song'])
</script>

<template>
  <li>{{ song.name }}</li>
</template>
