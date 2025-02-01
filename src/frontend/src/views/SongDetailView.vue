<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { Song } from '@/components/classes/Song'
import ViewHeader from '@/components/ViewHeader.vue'
import { useAPI } from '@/composables/useAPI'

const { getData } = useAPI()
const route = useRoute()
const song = ref<null | Song>(null)

onMounted(async () => {
  const song_pk = route.params['song_pk']
  song.value = await getData(`songs/${song_pk}/`)
})
</script>

<template>
  <div v-if="song">
    <!-- Este es el título -->
    <ViewHeader :title="song.title" /> 

    <!-- Aqui va toda la mondá relacionada con la canción -->

    
  </div>

  <p v-else>Loading song</p>
</template>
