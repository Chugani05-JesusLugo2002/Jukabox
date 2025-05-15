<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { Song } from '@/components/classes/Song'
import type { Album } from '@/components/classes/Album'
import { useAPI } from '@/composables/useAPI'
import ItemHeader from '@/components/elements/ItemHeader.vue'
import SongListItem from '@/components/elements/SongListItem.vue'
import ArtistsLabel from '@/components/elements/includes/ArtistsLabel.vue'

const { getData } = useAPI()
const route = useRoute()

const album = ref<Album | null>(null)
const songs = ref<Song[]>([])

onMounted(async () => {
  const album_pk = route.params['album_pk']
  album.value = await getData(`albums/${album_pk}/`)
  songs.value = await getData(`albums/${album_pk}/songs/`)
})
</script>

<template>
  <div v-if="album">
    <ItemHeader :image="album.cover" :name="album.title">
      <ArtistsLabel :artists="album.artists" />
    </ItemHeader>

    <ul class="list-group">
      <SongListItem v-for="song in songs" :song="song"></SongListItem>
    </ul>
  </div>

  <p v-else>Loading album</p>
</template>
