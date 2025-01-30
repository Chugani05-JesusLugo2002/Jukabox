<script setup lang="ts">
import ViewHeader from '@/components/ViewHeader.vue';
import { useAPI } from '@/composables/useAPI';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import type { Song } from '@/components/classes/Song';

const { getData } = useAPI()
const route = useRoute()
const song = ref<null|Song>(null)

onMounted(async() => {
    const song_pk = route.params['song_pk']
    song.value = await getData(`songs/${song_pk}/`)
})
</script>

<template>
    <div v-if="song">
        <ViewHeader :title="song.title"/>
    </div>
    <p v-else>Loading song</p>
</template>