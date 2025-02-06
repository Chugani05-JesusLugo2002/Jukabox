<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { useAPI } from '@/composables/useAPI'
import type { Song, Genre } from '@/components/classes/Song'
import ViewHeader from '@/components/ViewHeader.vue'
import SongItem from '@/components/elements/SongItem.vue'
import GenreItem from '@/components/elements/GenreItem.vue'
import { useI18n } from "vue-i18n";

const { locale, t } = useI18n();
const { getData } = useAPI()
const latestSongs = ref<Song[]>([])
const latestGenres = ref<Genre[]>([])

onMounted(async () => {
  latestSongs.value = await getData('songs/latest/')
  latestGenres.value = await getData('genres/')
})
</script>

<template>
  <ViewHeader>{{ $t("songs-page.title") }}</ViewHeader>

  <h2 class="display-5 mt-3">{{ $t("songs-page.tag1") }}</h2>
  <div class="songs-grid d-flex flex-wrap gap-3 justify-content-center">
    <SongItem v-for="(song, index) in latestSongs" :key="index" :song="song" />
  </div>

  <h2 class="display-5 mt-3">{{ $t("songs-page.tag2") }}</h2>
  <div class="songs-grid d-flex flex-wrap gap-3 justify-content-center">
    <GenreItem v-for="(genre, index) in latestGenres.slice(0, 5)" :key="index" :genre="genre" />
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
