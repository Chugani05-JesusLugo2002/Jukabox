<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="d-flex">
    <RouterLink class="btn btn-outline-primary mx-2" to="/signup">Signup</RouterLink>
    <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
  </div>
</template>
