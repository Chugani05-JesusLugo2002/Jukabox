<script setup lang="ts">
import { ref, inject, onMounted } from 'vue' 
import SongElement from '@/components/SongElement.vue';

const songs = ref<null|undefined>(null)

onMounted(async () => {
  songs.value = await inject('songs')
})
</script>

<template>
  <h1>All Songs</h1>
  <hr />
  <h2 v-if="!songs">Loading songs...</h2>
  <ul>
    <SongElement v-for="song in songs" :song="song"/>
  </ul>
</template>
