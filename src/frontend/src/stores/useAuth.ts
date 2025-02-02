import { defineStore } from 'pinia'
import { ref } from 'vue'

import type { User } from '@/components/classes/Authentication'

export const useAuthStore = defineStore('auth', () => {
  const isAuthenticated = ref(false)
  const user = ref<User | null>(null)

  function authenticate(userData: User) {
    isAuthenticated.value = true
    user.value = userData
  }

  function logout() {
    isAuthenticated.value = false
    user.value = null
  }

  return { isAuthenticated, user, authenticate, logout }
})
