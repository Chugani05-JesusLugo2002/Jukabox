<script setup lang="ts">
import { ref, inject, onMounted } from 'vue'
import SongItem from '@/components/SongItem.vue'

const songs = ref<null | undefined>(null)

onMounted(async () => {
  songs.value = await inject('songs')
})
</script>

<template>
  <h1>All Songs</h1>
  <hr />
  <h2 v-if="!songs">Loading songs...</h2>
  <ul class="list-group list-group-flush">
    <SongItem v-for="song in songs" :song="song" />
  </ul>
</template>
