<script setup lang="ts">
const { genre } = defineProps(['genre'])
const style = `width: 15rem; height: 15rem; background-color: ${genre.color};`

const genreDetailUrl = {
  name: 'genre-songs',
  params: {
    genre_slug: genre.slug,
  },
}
</script>

<template>
  <RouterLink :to="genreDetailUrl" class="fw-bold text-decoration-none">
    <div
      class="d-flex justify-content-center align-items-center text-dark border border-2 rounded"
      :style="style"
    >
      <h5 class="bg-light p-3 rounded">{{ genre.name }}</h5>
    </div>
  </RouterLink>
</template>
