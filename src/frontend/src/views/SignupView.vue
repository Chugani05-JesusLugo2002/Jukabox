<script setup lang="ts">
import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth'
import { ref } from 'vue'
import type { User } from '@/components/classes/Authentication'
import ViewHeader from '@/components/ViewHeader.vue'

const api = useAPI()
const authStore = useAuthStore()

const username = ref('')
const first_name = ref('')
const last_name = ref('')
const email = ref('')
const password = ref('')
const repeat_password = ref('')

async function signup() {
  const signupData = {
    username: username.value,
    first_name: first_name.value,
    last_name: last_name.value,
    email: email.value,
    password: password.value,
    repeat_password: repeat_password.value,
  }
  const user: User | null = await api.signup(signupData)
  if (user) {
    authStore.authenticate(user)
  }
}
</script>

<template>
  <ViewHeader>Signup</ViewHeader>
  <form @submit.prevent="signup" class="container mt-5 p-4 border rounded bg-light" style="max-width: 800px;">
    <div class="row mb-3 h3">
      <div class="col-6">
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
      <div class="col-6">
        <label for="first_name" class="form-label">First Name</label>
        <input
          type="text"
          name="first_name"
          id="first_name"
          v-model="first_name"
          class="form-control"
          placeholder="Enter your first name"
          required
        />
      </div>
    </div>
    <div class="row mb-3 h3">
      <div class="col-6">
        <label for="last_name" class="form-label">Last Name</label>
        <input
          type="text"
          name="last_name"
          id="last_name"
          v-model="last_name"
          class="form-control"
          placeholder="Enter your last name"
          required
        />
      </div>
      <div class="col-6">
        <label for="email" class="form-label">Email</label>
        <input
          type="email"
          name="email"
          id="email"
          v-model="email"
          class="form-control"
          placeholder="Enter your email"
          required
        />
      </div>
    </div>
    <div class="row mb-3 h3">
      <div class="col-6">
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
      <div class="col-6">
        <label for="repeat_password" class="form-label">Repeat Password</label>
        <input
          type="password"
          name="repeat_password"
          id="repeat_password"
          v-model="repeat_password"
          class="form-control"
          placeholder="Repeat your password"
          required
        />
      </div>
    </div>
    <button type="submit" class="btn btn-primary w-100">Signup</button>
  </form>
</template>

