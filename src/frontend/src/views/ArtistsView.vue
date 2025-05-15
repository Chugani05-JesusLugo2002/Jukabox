<script setup lang="ts">
import { inject } from 'vue'

import ViewHeader from '@/components/ViewHeader.vue'
import ArtistItem from '@/components/elements/ArtistItem.vue'
import AlbumItem from '@/components/elements/AlbumItem.vue'
import type { Artist } from '@/components/classes/Artist'
import type { Album } from '@/components/classes/Album'
import { useI18n } from 'vue-i18n'

const { locale, t } = useI18n()
const latestArtists = inject<Artist[]>('latestArtists')
const latestAlbums = inject<Album[]>('latestAlbums')
</script>

<template>
  <ViewHeader>{{ $t('artists-page.title') }}</ViewHeader>

  <h2 class="display-5 mt-3">{{ $t('artists-page.tag1') }}</h2>
  <div class="artist-grid d-flex flex-wrap gap-3 justify-content-center">
    <ArtistItem v-for="(artist, index) in latestArtists" :key="index" :artist="artist" />
  </div>

  <h2 class="display-5 mt-3">{{ $t('artists-page.tag2') }}</h2>
  <div class="artist-grid d-flex flex-wrap gap-3 justify-content-center">
    <AlbumItem v-for="(album, index) in latestAlbums" :key="index" :album="album" />
  </div>
</template>

<style scoped>
.songs-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: flex-start;
}
</style>
