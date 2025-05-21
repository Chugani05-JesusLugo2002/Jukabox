<script setup lang="ts">
const { album } = defineProps(['album'])
</script>

<template>
  <RouterLink :to="`/albums/${album.id}`" class="col-lg-3 col-xl-2 col-5 fw-bold text-decoration-none">
    <div class="card border-0">
      <img :src="album.cover" :alt="album.title + ' cover'" class="img-fluid rounded-5 shadow"/>
      <div class="card-body">
        <h5 class="text-center">{{ album.title }}</h5>
      </div>
    </div>
  </RouterLink>
</template>
