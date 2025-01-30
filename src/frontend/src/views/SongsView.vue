<script setup lang="ts">
import ViewHeader from '@/components/ViewHeader.vue'

import { ref, onMounted } from 'vue'
import { useAPI } from '@/composables/useAPI'

const { getData } = useAPI()
const songs = ref(null)

onMounted(async () => {
  songs.value = await getData('songs/')
  console.log(songs.value)
})
</script>

<template>
  <ViewHeader title="Songs" />

  <ul v-if="songs">
    <li v-for="(song, index) in songs" :key="index">{{ song }}</li>
  </ul>
  <p v-else>Loading</p>
</template>
