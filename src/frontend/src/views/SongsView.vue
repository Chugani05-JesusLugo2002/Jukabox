<script setup lang="ts">
import ViewHeader from '@/components/ViewHeader.vue'
import { useAPI } from '@/composables/useAPI'
import { onMounted, ref } from 'vue'

const { getData } = useAPI()
const latestSongs = ref(null)

onMounted(async () => {
  latestSongs.value = await getData('songs/')
})
</script>

<template>
  <ViewHeader title="Songs" />

  <h2 class="display-5 mt-3">Latest songs</h2>
  <ul>
    <li v-for="song in latestSongs">{{ song }}</li>
  </ul>

  <h2 class="display-5 mt-3">Trending genres</h2>

  <h2 class="display-5 mt-3">Most liked playlists</h2>
</template>
