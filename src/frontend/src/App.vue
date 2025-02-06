<script setup lang="ts">
import { RouterView } from 'vue-router'

import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import { onMounted, provide, ref } from 'vue'
import type { Song, Genre } from './components/classes/Song'
import type { Artist, Album } from './components/classes/Artist'
import { useAPI } from './composables/useAPI'

const { getData } = useAPI()

const latestSongs = ref<Song[]>([])
const trendingGenres = ref<Genre[]>([])
const latestArtists = ref<Artist[]>([])
const latestAlbums = ref<Album[]>([])

onMounted(async () => {
  latestSongs.value = await getData('songs/latest/')
  trendingGenres.value = await getData('genres/')
  latestArtists.value = await getData('artists/latest/')
  latestAlbums.value = await getData('albums/latest/')
})

provide('latestSongs', latestSongs)
provide('trendingGenres', trendingGenres)
provide('latestArtists', latestArtists)
provide('latestAlbums', latestAlbums)
</script>

<template>
  <header>
    <Navbar />
  </header>
  <main class="container mt-3 mb-5 pb-5">
    <RouterView />
  </main>
  <Footer />
</template>
