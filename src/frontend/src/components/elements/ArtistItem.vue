<script setup lang="ts">
const { artist } = defineProps(['artist'])
</script>

<template>
    <a class="fw-bold text-decoration-none">
        <div class="card border-0" style="width: 15rem;">
            <img :src="artist.avatar" :alt="artist.name + ' profile pic'" class="img-fluid rounded-circle" />
            <div class="card-body">
                <h5 class="text-center">{{ artist.name }}</h5>
            </div>
        </div>
    </a>
</template>