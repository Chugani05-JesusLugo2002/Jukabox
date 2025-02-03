<script setup lang="ts">
import type { User } from '@/components/classes/Authentication'
import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth'
import { ref } from 'vue'
import ViewHeader from '@/components/ViewHeader.vue'
import { useRouter } from 'vue-router'

const api = useAPI()
const authStore = useAuthStore()
const router = useRouter()

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
    router.push(`/profile`)
  }
}
</script>

<template>
  <ViewHeader>Login</ViewHeader>
  <form
    @submit.prevent="login"
    class="container mt-5 p-4 border rounded bg-light"
    style="max-width: 400px"
  >
    <div class="mb-3 h3">
      <label for="username" class="form-label">Username</label>
      <input
        type="text"
        name="username"
        id="username"
        v-model="username"
        class="form-control"
        placeholder="Enter your username"
        required
      />
    </div>
    <div class="mb-3 h3">
      <label for="password" class="form-label">Password</label>
      <input
        type="password"
        name="password"
        id="password"
        v-model="password"
        class="form-control"
        placeholder="Enter your password"
        required
      />
    </div>
    <button type="submit" class="btn btn-primary w-100">Login</button>
  </form>
</template>
