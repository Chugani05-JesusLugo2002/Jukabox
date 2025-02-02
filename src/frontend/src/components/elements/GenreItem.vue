<script setup lang="ts">
const { genre } = defineProps(['genre'])
const style = `width: 15rem; height: 15rem; background-color: ${genre.color};`
</script>

<template>
    <a class="fw-bold text-decoration-none">
        <div class="d-flex justify-content-center align-items-center text-dark border border-2 rounded" :style="style">
            <h5 class="bg-light p-3 rounded">{{ genre.name }}</h5>
        </div>
    </a>
</template>

