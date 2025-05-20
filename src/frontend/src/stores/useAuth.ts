import { defineStore } from 'pinia'
import { ref } from 'vue'
import { useAPI } from '@/composables/useAPI'
import { useRouter } from 'vue-router'

import type { User } from '@/components/classes/Authentication'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()
  const isAuthenticated = ref(false)
  const user = ref<User | null>(null)

  function authenticate(userData: User) {
    isAuthenticated.value = true
    user.value = userData
    localStorage.setItem('token', userData.token)
  }

  async function logout() {
    const { userLogout } = useAPI()
    await userLogout()
    isAuthenticated.value = false
    user.value = null
    localStorage.removeItem('token')
    router.push('/home')
  }

  return { isAuthenticated, user, authenticate, logout }
})
