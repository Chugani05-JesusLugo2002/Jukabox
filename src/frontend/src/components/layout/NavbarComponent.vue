<script setup lang="ts">
import AuthDisplay from '../elements/NavbarComponent/AuthDisplay.vue'
</script>

<template>
  <nav class="navbar navbar-expand container d-flex flex-wrap justify-content-between">
    <div class="navbar-brand col-2">
      <RouterLink to="/home"
        ><img src="/imgs/logo.png" alt="jukabox logo" class="img-fluid"
      /></RouterLink>
    </div>

    <ul class="navbar-nav">
      <li class="nav-item">
        <RouterLink class="nav-link" to="/explore">{{ $t('navbar.explore') }}</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink class="nav-link" to="/music">{{ $t('navbar.music') }}</RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink class="nav-link" to="/importer">Importer</RouterLink>
      </li>
    </ul>

    <AuthDisplay />
  </nav>
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
