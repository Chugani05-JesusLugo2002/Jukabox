<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import ItemHeader from '@/components/elements/ItemHeader.vue'
import type { Artist } from '@/components/classes/Artist'
import { useAPI } from '@/composables/useAPI'
import type { Album } from '@/components/classes/Album'
import AlbumItem from '@/components/elements/MusicView/AlbumItem.vue'
import UrlsContainer from '@/components/elements/includes/UrlsContainer.vue'

const { getData } = useAPI()
const route = useRoute()

const artist = ref<Artist | null>(null)
const albums = ref<Album[]>()

onMounted(async () => {
  const artist_pk = route.params['artist_pk']
  artist.value = await getData(`artists/${artist_pk}/`)
  albums.value = await getData(`artists/${artist_pk}/albums/`)
})
</script>

<template>
  <div v-if="artist">
    <ItemHeader :name="artist.name" :isRounded="true" :itemId="artist.id" :itemType="'artist'" />

    <UrlsContainer :lbz_link="artist.lbz_url" :artist_links="artist.links" />

    <div v-if="albums">
      <h5>Albums</h5>
      <div class="album-grid d-flex flex-wrap gap-3 justify-content-center">
        <AlbumItem v-for="album in albums" :album="album"></AlbumItem>
      </div>
    </div>
  </div>

  <p v-else>Loading artist</p>
</template>

<style scoped>
.album-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: flex-start;
}
</style>
