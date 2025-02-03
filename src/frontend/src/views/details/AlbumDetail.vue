<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import type { Song } from '@/components/classes/Song';
import type { Album } from '@/components/classes/Artist';
import { useAPI } from '@/composables/useAPI';

const { getData } = useAPI()
const route = useRoute()

const album = ref<Album|null>(null)
const songs = ref<Song[]>([])

onMounted(async () => {
    const album_pk = route.params['album_pk']
    album.value = await getData(`albums/${album_pk}/`)
    songs.value = await getData(`albums/${album_pk}/songs/`)
})
</script>

<template>
    <div v-if="album">
        <h1>{{ album.title }}</h1>
        <h2>Artists</h2>
        <ul>
            <li v-for="artist in album.artists">{{ artist.name }}</li>
        </ul>
        <h2>Songs</h2>
        <ol>
            <li v-for="song in songs">{{ song.title }}</li>
        </ol>
    </div>
</template>