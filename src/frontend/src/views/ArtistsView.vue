<script setup lang="ts">
import ViewHeader from '@/components/ViewHeader.vue'

import { useAPI } from '@/composables/useAPI'
import { onMounted, ref } from 'vue'

const { getData } = useAPI()
const artists = ref(null)

onMounted(async () => {
  artists.value = await getData('artists/')
})
</script>

<template>
  <ViewHeader title="Artists" />

  <ul v-if="artists">
    <li v-for="(artist, index) in artists" :key="index">{{ artist }}</li>
  </ul>
  <p v-else>Loading artists</p>
</template>
