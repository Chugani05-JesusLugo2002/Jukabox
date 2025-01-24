<script setup lang="ts">
const props = defineProps(['song'])
</script>

<template>
  <li class="list-group-item">
    {{ song.name }}
  </li>
</template>
