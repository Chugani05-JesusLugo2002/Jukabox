<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { useAPI } from '@/composables/useAPI'

import ItemHeader from '@/components/elements/shared/ItemHeader.vue'
import ArtistsLabel from '@/components/elements/includes/ArtistsLabel.vue'
import UrlsContainer from '@/components/elements/shared/UrlsContainer.vue'
import StatsContainer from '@/components/elements/shared/StatsContainer.vue'
import MusicItemList from '@/components/elements/shared/MusicItemList.vue'

const { getData } = useAPI()
const route = useRoute()

const album = ref()
const songs = ref()

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
      <div class="col order-lg-1 order-2">
          <MusicItemList v-for="song in songs" :key="song.id" :id="song.id" :title="song.title" :likes="song.likes" :reviews="song.reviews" :type="'songs'"/>
      </div>
      <div class="col-lg-3 col-12 order-1">
        <UrlsContainer :type="'albums'" :id="album.id" :lbzUrl="album.lbz_url" />
        <StatsContainer :likes="album.likes"></StatsContainer>
      </div>
    </div>
  </div>

  <p v-else>Loading album</p>
</template>
