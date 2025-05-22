<script setup lang="ts">
import AuthDisplay from '../elements/NavbarComponent/AuthDisplay.vue'
</script>

<template>
  <nav class="navbar navbar-expand-sm container justify-content-between px-sm-0 px-5">
    <div class="navbar-brand col-sm-2 col-4">
      <RouterLink to="/home"
        ><img src="/imgs/logo.png" alt="jukabox logo" class="img-fluid"
      /></RouterLink>
    </div>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mx-auto my-2 mb-sm-0">
        <li class="nav-item">
          <RouterLink class="nav-link px-3" to="/explore">{{ $t('navbar.explore') }}</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link px-3" to="/music">{{ $t('navbar.music') }}</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link px-3" to="/importer">Importer</RouterLink>
        </li>
      </ul>
      <AuthDisplay />
    </div>
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
