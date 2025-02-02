<script setup lang="ts">
import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth'
import { ref } from 'vue'
import type { User } from '@/components/classes/Authentication'

const api = useAPI()
const authStore = useAuthStore()

const username = ref('')
const first_name = ref('')
const last_name = ref('')
const email = ref('')
const password = ref('')

async function signup() {
  const signupData = {
    username: username.value,
    first_name: first_name.value,
    last_name: last_name.value,
    email: email.value,
    password: password.value,
  }
  const user: User | null = await api.signup(signupData)
  if (user) {
    authStore.authenticate(user)
  }
}
</script>

<template>
  <form @submit.prevent="signup">
    <input type="text" name="username" id="username" v-model="username" placeholder="Username" />
    <input
      type="text"
      name="first_name"
      id="first_name"
      v-model="first_name"
      placeholder="first_name"
    />
    <input
      type="text"
      name="last_name"
      id="last_name"
      v-model="last_name"
      placeholder="last_name"
    />
    <input type="email" name="email" id="email" v-model="email" placeholder="email" />
    <input
      type="password"
      name="password"
      id="password"
      v-model="password"
      placeholder="Password"
    />
    <input type="submit" value="Signup" />
  </form>
</template>
