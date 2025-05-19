<script setup lang="ts">
import { inject } from 'vue'

import ViewHeader from '@/components/ViewHeader.vue'
import AlbumItem from '@/components/elements/AlbumItem.vue'
import type { Album } from '@/components/classes/Album'
import SongItem from '@/components/elements/SongItem.vue'
import type { Song } from '@/components/classes/Song'
import { useI18n } from 'vue-i18n'

const { locale, t } = useI18n()
const latestAlbums = inject<Album[]>('latestAlbums')
const latestSongs = inject<Song[]>('latestSongs')
</script>

<template>
  <ViewHeader>{{ $t('artists-page.title') }}</ViewHeader>

  <section v-if="latestAlbums">
    <h2 class="display-5 mt-3">{{ $t('artists-page.tag2') }}</h2>
    <div class="mix-grid d-flex flex-wrap gap-3 justify-content-center">
      <AlbumItem v-for="(album, index) in latestAlbums" :key="index" :album="album" />
    </div>
  </section>
  <p v-else>Loading....</p>

  <section v-if="latestSongs">
    <h2 class="display-5 mt-3">{{ $t('songs-page.tag1') }}</h2>
    <div class="mix-grid d-flex flex-wrap gap-3 justify-content-center">
      <SongItem v-for="(song, index) in latestSongs" :key="index" :song="song" />
    </div>
  </section>
  <p v-else>Loading...</p>
</template>

<style scoped>
.mix-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: flex-start;
}
</style>
