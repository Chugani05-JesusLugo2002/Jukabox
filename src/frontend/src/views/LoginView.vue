<script setup lang="ts">
import type { User } from '@/components/classes/Authentication'
import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth'
import { ref } from 'vue'

const api = useAPI()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')

async function login() {
  const loginData = {
    username: username.value,
    password: password.value,
  }
  const user: User | null = await api.login(loginData)
  if (user) {
    authStore.authenticate(user)
  }
}
</script>

<template>
  <form @submit.prevent="login">
    <input type="text" name="username" id="username" v-model="username" placeholder="Username" />
    <input
      type="password"
      name="password"
      id="password"
      v-model="password"
      placeholder="Password"
    />
    <input type="submit" value="Login" />
  </form>
</template>
