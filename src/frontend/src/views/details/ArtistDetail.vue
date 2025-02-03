<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import type { Artist } from '@/components/classes/Artist';
import { useAPI } from '@/composables/useAPI';

const { getData } = useAPI()
const route = useRoute()

const artist = ref<Artist|null>(null)

onMounted(async () => {
    const artist_pk = route.params['artist_pk']
    artist.value = await getData(`artists/${artist_pk}/`)
})
</script>

<template>
    <h1 v-if="artist">{{ artist.name }}</h1>
</template>