<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/useAuth'
import isAuth from './elements/Navbar/isAuth.vue'
import noAuth from './elements/Navbar/noAuth.vue'
import { useI18n } from "vue-i18n";

const { locale, t } = useI18n();
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
          <RouterLink class="nav-link" to="/explore">{{ $t("navbar.explore") }}</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/songs">{{ $t("navbar.songs") }}</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/artists">{{ $t("navbar.artists") }}</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/community">{{ $t("navbar.community") }}</RouterLink>
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
