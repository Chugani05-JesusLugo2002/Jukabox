<script setup lang="ts">
import SongItem from '@/components/elements/SongItem.vue'
import ViewHeader from '@/components/ViewHeader.vue'
import { useAPI } from '@/composables/useAPI'
import { onMounted } from 'vue'
import { ref } from 'vue'

const { getData } = useAPI()
const songs = ref(null)

onMounted(async () => {
  songs.value = await getData('songs')
})
</script>

<template>
  <ViewHeader title="Explore" />

  <ul v-if="songs">
    <SongItem v-for="(song, index) in songs" :key="index" :song="song" />
  </ul>
  <p v-else>Loading</p>
</template>
