<script setup lang="ts">
const { id, type } = defineProps<{
    id: number;
    type: 'albums'|'songs'
}>()
</script>

<template>
   <div class="d-flex justify-content-between">
        <p class="display-6">Featured {{ type }}</p>
        <RouterLink :to="`/artists/${id}/${type}`" class="display-6 text-black">
        All {{ type }}
        </RouterLink>
    </div> 
</template>