<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { useAPI } from '@/composables/useAPI'
import MusicItemList from '@/components/elements/shared/MusicItemList.vue'

const route = useRoute()
const { getData } = useAPI()

const artist = ref()
const songs = ref()

onMounted(async () => {
  const artist_pk = route.params['artist_pk']
  artist.value = await getData(`artists/${artist_pk}/`)
  songs.value = await getData(`artists/${artist_pk}/songs/`)
})
</script>

<template>
  <div v-if="artist">
    <h1 class="mb-5">
      <RouterLink :to="`/artists/${artist.id}`" class="text-black">{{ artist.name }}</RouterLink> -
      Songs
    </h1>
    <div class="row display-6 my-3">
      <div class="col-sm-5 col">Song</div>
      <div class="col-sm-5 col text-end text-sm-start">Album</div>
      <div class="col-2 text-end d-none d-sm-inline">Stats</div>
    </div>
    <MusicItemList
      v-for="song in songs"
      :key="song.id"
      :title="song.title"
      :type="'songs'"
      :id="song.id"
      :likes="song.likes"
      :reviews="song.reviews"
    >
      <span v-if="song.albums.length > 0">{{ song.albums[0].title }}</span>
    </MusicItemList>
  </div>
  <div v-else>Loading artist songs...</div>
</template>
