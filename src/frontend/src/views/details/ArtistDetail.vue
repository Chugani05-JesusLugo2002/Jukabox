<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import ItemHeader from '@/components/elements/ItemHeader.vue'
import type { Artist } from '@/components/classes/Artist'
import { useAPI } from '@/composables/useAPI'
import type { Album } from '@/components/classes/Album'
import AlbumItem from '@/components/elements/AlbumItem.vue'

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
    <ItemHeader :name="artist.name" :isRounded="true" :itemId="artist.id" :itemType="'artist'"/>

    <div v-if="albums">
      <h5>Albums</h5>
      <div class="d-flex flex-wrap gap-3 justify-content-center">
        <AlbumItem v-for="album in albums" :title="album.title" :image="album.cover" :url="`/albums/${album.id}/`"></AlbumItem>
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