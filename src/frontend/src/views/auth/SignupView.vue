<script setup lang="ts">
import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth'
import { ref } from 'vue'
import type { User } from '@/components/classes/Authentication'
import ViewHeader from '@/components/ViewHeader.vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

const { locale, t } = useI18n()
const api = useAPI()
const authStore = useAuthStore()
const router = useRouter()

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
    router.push(`/profile`)
  }
}
</script>

<template>
  <ViewHeader>{{ $t('register.title') }}</ViewHeader>
  <form
    @submit.prevent="signup"
    class="container mt-5 p-4 border rounded bg-light"
    style="max-width: 800px"
  >
    <div class="row mb-3 h3">
      <div class="col-6">
        <label for="username" class="form-label">{{ $t('register.username') }}</label>
        <input
          type="text"
          name="username"
          id="username"
          v-model="username"
          class="form-control"
          :placeholder="$t('register.placeholder1')"
          required
        />
      </div>
      <div class="col-6">
        <label for="first_name" class="form-label">{{ $t('register.firstname') }}</label>
        <input
          type="text"
          name="first_name"
          id="first_name"
          v-model="first_name"
          class="form-control"
          :placeholder="$t('register.placeholder3')"
          required
        />
      </div>
    </div>
    <div class="row mb-3 h3">
      <div class="col-6">
        <label for="last_name" class="form-label">{{ $t('register.lastname') }}</label>
        <input
          type="text"
          name="last_name"
          id="last_name"
          v-model="last_name"
          class="form-control"
          :placeholder="$t('register.placeholder4')"
          required
        />
      </div>
      <div class="col-6">
        <label for="email" class="form-label">{{ $t('register.email') }}</label>
        <input
          type="email"
          name="email"
          id="email"
          v-model="email"
          class="form-control"
          :placeholder="$t('register.placeholder5')"
          required
        />
      </div>
    </div>
    <div class="row mb-3 h3">
      <div class="col-6">
        <label for="password" class="form-label">{{ $t('register.password') }}</label>
        <input
          type="password"
          name="password"
          id="password"
          v-model="password"
          class="form-control"
          :placeholder="$t('register.placeholder2')"
          required
        />
      </div>
      <div class="col-6">
        <label for="repeat_password" class="form-label">{{ $t('register.repeatpassword') }}</label>
        <input
          type="password"
          name="repeat_password"
          id="repeat_password"
          v-model="repeat_password"
          class="form-control"
          :placeholder="$t('register.placeholder6')"
          required
        />
      </div>
    </div>
    <button type="submit" class="btn btn-primary w-100">{{ $t('register.button') }}</button>
  </form>
</template>
