<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/useAuth'
import isAuth from './elements/Navbar/isAuth.vue'
import noAuth from './elements/Navbar/noAuth.vue'

const authStore = useAuthStore()
</script>

<template>
  <header class="bg-light mb-2 border-bottom">
    <nav class="navbar navbar-expand container d-flex flex-wrap justify-content-between">
      <div class="navbar-brand">
        <RouterLink to="/" class="fs-3 fw-bold nav-link">Jukabox</RouterLink>
      </div>

      <ul class="navbar-nav">
        <li class="nav-item">
          <RouterLink class="nav-link" to="/home">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/songs">Songs</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/artists">Artists</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/community">Community</RouterLink>
        </li>
      </ul>

      <isAuth v-if="authStore.isAuthenticated" />
      <noAuth v-else />
    </nav>
  </header>
</template>

<style scoped lang="scss">
@import '@/scss/colors';

.navbar-nav {
  .router-link-active {
    background-color: $primary-color;
    border-radius: 5px;
    font-weight: bold;
  }
}
</style>
