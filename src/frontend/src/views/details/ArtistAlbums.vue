<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { useAPI } from '@/composables/useAPI'
import MusicItemList from '@/components/elements/shared/MusicItemList.vue'

const route = useRoute()
const { getData } = useAPI()

const artist = ref()
const albums = ref()

onMounted(async () => {
  const artist_pk = route.params['artist_pk']
  artist.value = await getData(`artists/${artist_pk}/`)
  albums.value = await getData(`artists/${artist_pk}/albums/`)
})
</script>

<template>
  <div v-if="artist">
    <h1 class="mb-5">
      <RouterLink :to="`/artists/${artist.id}`" class="text-black">{{ artist.name }}</RouterLink> -
      Albums
    </h1>
    <div class="row display-6 my-3">
      <div class="col-sm-5 col">Album</div>
      <div class="col-sm-5 col text-end text-sm-start">Year</div>
      <div class="col-sm-2 text-end d-sm-inline d-none">Stats</div>
    </div>
    <MusicItemList
      v-for="album in albums"
      :key="album.id"
      :title="album.title"
      :type="'albums'"
      :id="album.id"
      :likes="album.likes"
    >
      {{ album.released_at.slice(0, 4) }}
    </MusicItemList>
  </div>
  <div v-else>Loading artist albums...</div>
</template>
