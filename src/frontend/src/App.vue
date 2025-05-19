<script setup lang="ts">
import { RouterView } from 'vue-router'

import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import { onMounted, provide, ref } from 'vue'
import type { Song } from './components/classes/Song'
import type { Album } from './components/classes/Album'
import { useAPI } from './composables/useAPI'
import { useAuthStore } from './stores/useAuth'

const { getMyProfile, getData } = useAPI()
const { authenticate, logout } = useAuthStore()

const latestSongs = ref<Song[]>([])
const latestAlbums = ref<Album[]>([])

onMounted(async () => {
  const token = localStorage.getItem('token')
  console.log(token)
  if (token) {
    const user = await getMyProfile(token)
    if (user) {
      authenticate(user)
    } else {
      console.log(user)
    }
  }

  latestSongs.value = await getData('songs/latest/')
  latestAlbums.value = await getData('albums/latest/')
})

provide('latestSongs', latestSongs)
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
