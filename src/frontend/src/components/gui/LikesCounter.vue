<script setup lang="ts">
const { likes } = defineProps(['likes'])
</script>

<template>
  <h5 class="px-2"><i class="bi bi-heart-fill"></i> {{ likes }}</h5>
</template>
