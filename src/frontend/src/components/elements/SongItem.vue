<script setup lang="ts">
const { song_id } = defineProps(['song_id'])

const songDetailUrl = {
    name: 'song-detail',
    params: {
        song_pk: song_id
    }
}
</script>

<template>
    <li>
        <RouterLink :to="songDetailUrl" class="fw-bold">
            <slot></slot>
        </RouterLink>
    </li>
</template>