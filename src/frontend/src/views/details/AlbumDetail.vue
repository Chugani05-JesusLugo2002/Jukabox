<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { Song } from '@/components/classes/Song'
import type { Album } from '@/components/classes/Album'
import { useAPI } from '@/composables/useAPI'
import ItemHeader from '@/components/elements/ItemHeader.vue'
import SongListItem from '@/components/elements/SongListItem.vue'
import ArtistsLabel from '@/components/elements/includes/ArtistsLabel.vue'
import UrlsContainer from '@/components/elements/includes/UrlsContainer.vue'
import StatsContainer from '@/components/elements/includes/StatsContainer.vue'

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
    <ItemHeader :img="album.cover" :title="album.title" :id="album.id" :type="'album'">
      <ArtistsLabel :artists="album.artists" />
    </ItemHeader>

    <div class="row">
      <div class="col">
        <ul class="list-group">
          <SongListItem v-for="song in songs" :key="song.id" :song="song"></SongListItem>
        </ul>
      </div>
      <div class="col-3">
        <UrlsContainer :item_type="'album'" :item_id="album.id" :lbz_link="album.lbz_url" />
        <StatsContainer :likes="album.likes">Stats</StatsContainer>
      </div>
    </div>
  </div>

  <p v-else>Loading album</p>
</template>
