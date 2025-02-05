<script setup lang="ts">
import type { Artist } from '../classes/Artist'
import { ref } from 'vue'

interface FixedArtist {
  name: string
  url: string
}

const props = defineProps(['artists'])
const artistsCount = ref(props.artists.length)

const fixedArtists: FixedArtist[] = []
props.artists.forEach((artist: Artist) => {
  fixedArtists.push({
    name: artist.name,
    url: `/artists/${artist.id}`,
  })
})

const firstArtist: FixedArtist = fixedArtists[0]
const lastArtist: FixedArtist = fixedArtists.slice(-1)[0]
</script>

<template>
  <p>
    By <RouterLink :to="firstArtist.url" class="text-muted">{{ firstArtist.name }}</RouterLink>
    <span v-if="artistsCount > 1">
      <span v-if="artistsCount > 2" v-for="artist in fixedArtists.slice(1, -1)"
        >, <RouterLink :to="artist.url" class="text-muted">{{ artist.name }}</RouterLink></span
      >
      and <RouterLink :to="lastArtist.url" class="text-muted">{{ lastArtist.name }}</RouterLink>
    </span>
  </p>
</template>
