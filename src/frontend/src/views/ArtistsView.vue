<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { useAPI } from '@/composables/useAPI'
import ViewHeader from '@/components/ViewHeader.vue'
import ArtistItem from '@/components/elements/ArtistItem.vue'
import AlbumItem from '@/components/elements/AlbumItem.vue'
import type { Artist, Album } from '@/components/classes/Artist'

const { getData } = useAPI()
const latestArtists = ref<Artist[]>([])
const latestAlbums = ref<Album[]>([])

onMounted(async () => {
  latestArtists.value = await getData('artists/latest/')
  latestAlbums.value = await getData('albums/latest/')
})
</script>

<template>
  <ViewHeader>Artists</ViewHeader>

  <h2 class="display-5 mt-3">Most loved</h2>
  <div class="artist-grid d-flex flex-wrap gap-3 justify-content-center">
    <ArtistItem v-for="(artist, index) in latestArtists" :key="index" :artist="artist" />
  </div>

  <h2 class="display-5 mt-3">Best albums</h2>
  <div class="artist-grid d-flex flex-wrap gap-3 justify-content-center">
    <AlbumItem v-for="(album, index) in latestAlbums" :key="index" :album="album" />
  </div>

  <h2 class="display-5 mt-3">Around the world!</h2>
</template>

<style scoped>
.songs-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: flex-start;
}
</style>
