<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import ItemHeader from '@/components/elements/ItemHeader.vue'
import SongListItem from '@/components/elements/SongListItem.vue'
import type { Artist } from '@/components/classes/Artist'
import { useAPI } from '@/composables/useAPI'

const { getData } = useAPI()
const route = useRoute()

const artist = ref<Artist | null>(null)

onMounted(async () => {
  const artist_pk = route.params['artist_pk']
  artist.value = await getData(`artists/${artist_pk}/`)
})
</script>

<template>
  <div v-if="artist">
    <ItemHeader :image="artist.avatar" :name="artist.name" :isRounded="true" />
  </div>

  <p v-else>Loading artist</p>
</template>
