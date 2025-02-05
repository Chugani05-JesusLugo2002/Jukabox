<script setup lang="ts">
const { artist } = defineProps(['artist'])

const artistDetailUrl = {
  name: 'artist-detail',
  params: {
    artist_pk: artist.id,
  },
}
</script>

<template>
  <RouterLink :to="artistDetailUrl" class="fw-bold text-decoration-none">
    <div class="card border-0" style="width: 15rem">
      <img
        :src="artist.avatar"
        :alt="artist.name + ' profile pic'"
        class="img-fluid rounded-circle"
      />
      <div class="card-body">
        <h5 class="text-center">{{ artist.name }}</h5>
      </div>
    </div>
  </RouterLink>
</template>

<style scoped lang="scss">
img {
  width: 100%;
  height: 250px;
}
</style>
