<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { Song } from '@/components/classes/Song'
import ItemHeader from '@/components/elements/ItemHeader.vue'
import UrlsContainer from '@/components/elements/UrlsContainer.vue'
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
    <ItemHeader :image="song.cover" :name="song.title" :isRounded="false">
      by <span v-for="artist in song.artists">{{ artist.name }}</span>
    </ItemHeader>

    <div class="row">
      <div class="col-9">
        <p class="h4">Reviews</p>
        <input class="btn btn-primary" type="submit" value="Submit">
      </div>
      <div class="col-3">
        <UrlsContainer>Where to listen</UrlsContainer>
        <h4>Stats</h4>
        <h4>About</h4>
      </div>
    </div>
  </div>

  <p v-else>Loading song</p>
</template>
