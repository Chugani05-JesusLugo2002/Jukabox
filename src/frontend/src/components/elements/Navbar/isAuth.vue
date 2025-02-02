<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/useAuth'
import { ref } from 'vue'

const logoutIcon = ref('bi bi-door-closed')
const authStore = useAuthStore()
</script>

<template>
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
        <RouterLink to="/profile" class="dropdown-item"
          ><i class="bi bi-person-circle"></i> My profile</RouterLink
        >
      </li>
      <li>
        <a class="dropdown-item" href="#"><i class="bi bi-moon"></i> Change theme</a>
      </li>
      <li>
        <a class="dropdown-item" href="#"><i class="bi bi-gear" id="settings-icon"></i> Settings</a>
      </li>
      <li>
        <button
          class="dropdown-item"
          @mouseover="logoutIcon = 'bi bi-door-open'"
          @mouseleave="logoutIcon = 'bi bi-door-closed'"
          @click="authStore.logout"
        >
          <i :class="logoutIcon"></i> Logout
        </button>
      </li>
    </ul>
  </div>
</template>
