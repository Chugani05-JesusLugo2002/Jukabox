<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

import { useAuthStore } from '@/stores/useAuth'

import LogoElement from './LogoElement.vue'

const authStore = useAuthStore()
const logoutIcon = ref('bi bi-door-closed')
</script>

<template>
  <div class="dropdown" v-if="authStore.isAuthenticated && authStore.user">
    <LogoElement :user="authStore.user" />
    <ul class="dropdown-menu">
      <li>
        <RouterLink :to="'/profiles/' + authStore.user.slug" class="dropdown-item"
          ><i class="bi bi-person-circle"></i> My profile</RouterLink
        >
      </li>
      <li>
        <RouterLink :to="'/settings/'" class="dropdown-item"><i class="bi bi-gear" id="settings-icon"></i> Settings</RouterLink>
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

  <div class="d-flex" v-else>
    <RouterLink class="btn btn-outline-primary mx-2" to="/signup">{{
      $t('noauth.register')
    }}</RouterLink>
    <RouterLink class="btn btn-primary" to="/login">{{ $t('noauth.login') }}</RouterLink>
  </div>
</template>
