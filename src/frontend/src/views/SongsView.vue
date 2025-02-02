<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { useAPI } from '@/composables/useAPI'
import type { Song } from '@/components/classes/Song'
import ViewHeader from '@/components/ViewHeader.vue'
import SongItem from '@/components/elements/SongItem.vue'

const { getData } = useAPI()
const latestSongs = ref<Song[]>([])

onMounted(async () => {
  latestSongs.value = await getData('songs/latest/')
})
</script>

<template>
  <ViewHeader title="Songs" />

  <h2 class="display-5 mt-3">Latest songs</h2>
  <ol>
    <SongItem v-for="(song, index) in latestSongs" :key="index" :song_id="song.id">
      {{ song.title }}
    </SongItem>
  </ol>

  <h2 class="display-5 mt-3">Trending genres</h2>

  <h2 class="display-5 mt-3">Most liked playlists</h2>
</template>
