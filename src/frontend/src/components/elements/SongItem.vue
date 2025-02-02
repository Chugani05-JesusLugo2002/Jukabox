<script setup lang="ts">
const { song } = defineProps(['song'])

const songDetailUrl = {
  name: 'song-detail',
  params: {
    song_pk: song.id,
  },
}
</script>

<template>
    <RouterLink :to="songDetailUrl" class="fw-bold text-decoration-none">
        <div class="card border-0" style="width: 15rem;">
            <img :src="song.cover" :alt="song.title + ' cover'" />
            <div class="card-body">
                <h5>{{ song.title }}</h5>
                <p class="text-muted ">by {{ song.artists[0].name }}</p>
            </div>
        </div>
    </RouterLink>
</template>

