<script setup lang="ts">
const { song } = defineProps(['song'])
</script>

<template>
  <RouterLink :to="`/songs/${song.id}`" class="col-lg-3 col-xl-2 col-5 fw-bold text-decoration-none">
    <div class="card border-0">
      <img :src="song.cover" :alt="song.title + ' cover'" class="img-fluid rounded-5 shadow"/>
      <div class="card-body">
        <h5>{{ song.title }}</h5>
        <p class="text-muted">by {{ song.artists[0].name }}</p>
      </div>
    </div>
  </RouterLink>
</template>
