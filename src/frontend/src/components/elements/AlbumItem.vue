<script setup lang="ts">
const { album } = defineProps(['album'])

const albumDetailUrl = {
  name: 'album-detail',
  params: {
    album_pk: album.id
  }
}
</script>

<template>
  <RouterLink :to="albumDetailUrl" class="fw-bold text-decoration-none">
    <div class="card border-0" style="width: 15rem">
      <img :src="album.cover" :alt="album.title + ' cover'" />
      <div class="card-body">
        <h5 class="text-center">{{ album.title }}</h5>
      </div>
    </div>
  </RouterLink>
</template>
