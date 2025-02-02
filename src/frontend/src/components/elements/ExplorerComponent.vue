<script setup lang="ts">
import { ref } from 'vue' 

import ExplorerFilterPill from './ExplorerFilterPill.vue';
const filters = ['All', 'Songs', 'Artists', 'Albums', 'Playlists', 'Genres']

const query = ref('')
</script>

<template>
    <div class="input-group input-group-lg">
        <span class="input-group-text"><i class="bi bi-search"></i></span>
        <input type="text" name="query" id="query" v-model="query" class="form-control input-lg" placeholder="Let your heart guide you! <3">
    </div>
    
    <div class="d-flex justify-content-center align-items-center">
        <ExplorerFilterPill v-for="filter in filters">{{ filter }}</ExplorerFilterPill>
    </div>
</template>