<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { Genre, Song } from '@/components/classes/Song'
import { useAPI } from '@/composables/useAPI'

const { getData } = useAPI()
const route = useRoute()

const genre = ref<Genre | null>(null)
const songs = ref<Song[]>([])

onMounted(async () => {
  const genre_slug = route.params['genre_slug']
  genre.value = await getData(`genres/${genre_slug}/`)
  songs.value = await getData(`genres/${genre_slug}/songs/`)
})
</script>

<template>
  <h1 v-if="genre">{{ genre.name }}</h1>
  <ul>
    <li v-for="song in songs">{{ song.title }}</li>
  </ul>
</template>
