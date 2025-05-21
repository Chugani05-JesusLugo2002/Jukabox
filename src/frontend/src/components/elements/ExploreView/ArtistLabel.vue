<script setup lang="ts">
const { artist } = defineProps(['artist'])
</script>

<template>
    <RouterLink :to="`/artists/${artist.id}`" class="text-black">
        {{ artist.name }}
    </RouterLink>
</template>