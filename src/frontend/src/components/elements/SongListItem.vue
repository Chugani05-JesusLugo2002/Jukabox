<script setup lang="ts">
const { song } = defineProps(['song'])

const songDetailUrl = {
  name: 'song-detail',
  params: {
    song_pk: song.id,
  },
}
</script>

<template>
  <RouterLink :to="songDetailUrl" class="list-group-item list-group-item-action">
    {{ song.title }}
  </RouterLink>
</template>
