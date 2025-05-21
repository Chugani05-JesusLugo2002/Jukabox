<script setup lang="ts">
const { artist } = defineProps(['artist'])
</script>

<template>
  <RouterLink :to="`/artists/${artist.id}`" class="text-secondary artist-label">
    {{ artist.name }}
  </RouterLink>
</template>

<style scoped lang="scss">
.artist-label {
  text-decoration: none;
  &:hover {
    text-decoration: underline;
  }
}
</style>
