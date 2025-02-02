<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="d-flex">
    <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
    <RouterLink class="btn btn-outline-primary" to="/signup">Signup</RouterLink>
  </div>
</template>
