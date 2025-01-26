<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

const logoutIcon = ref('bi bi-door-closed')
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
      </ul>

      <div class="dropdown">
        <a
          class="dropdown-toggle text-body-emphasis"
          type="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          <img
            src="https://github.com/mdo.png"
            alt="My profile avatar"
            class="rounded-circle"
            width="32"
            height="32"
          />
        </a>
        <ul class="dropdown-menu">
          <li>
            <a class="dropdown-item" href="#"><i class="bi bi-person-circle"></i> My profile</a>
          </li>
          <li>
            <a class="dropdown-item" href="#"><i class="bi bi-moon"></i> Change theme</a>
          </li>
          <li>
            <a class="dropdown-item" href="#"
              ><i class="bi bi-gear" id="settings-icon"></i> Settings</a
            >
          </li>
          <li>
            <a
              class="dropdown-item"
              href="#"
              @mouseover="logoutIcon = 'bi bi-door-open'"
              @mouseleave="logoutIcon = 'bi bi-door-closed'"
            >
              <i :class="logoutIcon"></i> Logout
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<style scoped>
.navbar-nav .router-link-active {
  background-color: rgb(199, 199, 252);
  border-radius: 5px;
  font-weight: bold;
}
</style>
