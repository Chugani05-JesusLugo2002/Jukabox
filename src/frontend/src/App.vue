<script setup lang="ts">
import { onBeforeMount, provide, ref } from 'vue'
import { RouterView } from 'vue-router'

import type { Song } from './components/classes/Song'
import type { Album } from './components/classes/Album'
import HeaderComponent from './components/layout/HeaderComponent.vue'
import FooterComponent from './components/layout/FooterComponent.vue'
import { useAPI } from './composables/useAPI'
import { useSocial } from './composables/useSocial'
import { useAuthStore } from './stores/useAuth'

const { getData } = useAPI()
const { getMyProfile } = useSocial()
const { authenticate } = useAuthStore()

const latestSongs = ref<Song[]>([])
const latestAlbums = ref<Album[]>([])

onBeforeMount(async () => {
  const token = localStorage.getItem('token')
  if (token) {
    const user = await getMyProfile(token)
    if (user) {
      authenticate(user)
    }
  }

  latestSongs.value = await getData('songs/latest/')
  latestAlbums.value = await getData('albums/latest/')
})

provide('latestSongs', latestSongs)
provide('latestAlbums', latestAlbums)
</script>

<template>
  <HeaderComponent />
  <main class="container mt-3 mb-5 pb-5">
    <RouterView />
  </main>
  <FooterComponent />
</template>
