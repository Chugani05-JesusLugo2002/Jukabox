<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <header class="d-flex justify-content-center py-3">
    <ul class="nav nav-pills">
      <li class="nav-item"><RouterLink to="/" class="btn btn-primary mx-1">Home</RouterLink></li>
      <li class="nav-item">
        <RouterLink to="/songs" class="btn btn-primary mx-1">Songs</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink to="/artists" class="btn btn-primary mx-1">Artists</RouterLink>
      </li>
    </ul>
  </header>
</template>
