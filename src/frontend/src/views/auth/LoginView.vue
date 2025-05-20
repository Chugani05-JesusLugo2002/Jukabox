<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { Toast } from 'bootstrap'

import type { User } from '@/components/classes/Authentication'

import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth'

import ViewHeader from '@/components/ViewHeader.vue'
import ToastElement from '@/components/elements/Toast/ToastElement.vue'

const { userLogin } = useAPI()
const authStore = useAuthStore()
const router = useRouter()
const username = ref('')
const password = ref('')

async function login() {
  const loginData = {
    username: username.value,
    password: password.value,
  }
  const user: User|undefined = await userLogin(loginData)
  if (user) {
    authStore.authenticate(user)
    router.push(`/profiles/${user.slug}`)
  } else {
    const userNotFoundToast = document.getElementById('userNotFoundToast')
    if (userNotFoundToast) {
      Toast.getOrCreateInstance(userNotFoundToast).show()
    }
  }
}
</script>

<template>
  <ToastElement :id="'userNotFoundToast'" :title="'Error!'" :type="'danger'">User not found!</ToastElement>

  <ViewHeader>{{ $t('login.title') }}</ViewHeader>
  <form
    @submit.prevent="login"
    class="container mt-5 p-4 border rounded bg-light"
    style="max-width: 400px"
  >
    <div class="mb-3 h5">
      <label for="username" class="form-label">{{ $t('login.username') }}</label>
      <input
        type="text"
        name="username"
        id="username"
        v-model="username"
        class="form-control"
        :placeholder="$t('login.placeholder1')"
        required
      />
    </div>
    <div class="mb-3 h5">
      <label for="password" class="form-label">{{ $t('login.password') }}</label>
      <input
        type="password"
        name="password"
        id="password"
        v-model="password"
        class="form-control"
        :placeholder="$t('login.placeholder2')"
        required
      />
    </div>
    <button type="submit" class="btn btn-primary w-100"><i class="bi bi-box-arrow-in-right"></i> {{ $t('login.button') }}</button>
    <p class="text-center mt-3">No account? <RouterLink to="/signup">Sign up!</RouterLink></p>
  </form>
</template>
