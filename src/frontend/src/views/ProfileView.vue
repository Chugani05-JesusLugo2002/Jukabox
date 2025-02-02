<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuth'
import ViewHeader from '@/components/ViewHeader.vue'

const { isAuthenticated, user } = useAuthStore()
</script>

<template>
  <ViewHeader v-if="user">{{ user.username }}</ViewHeader>
  <ViewHeader v-else>No deberias estar aqui :c</ViewHeader>
</template>
