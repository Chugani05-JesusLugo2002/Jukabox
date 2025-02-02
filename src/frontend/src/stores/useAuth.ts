import { defineStore } from 'pinia'
import { onMounted, ref } from 'vue'
import { useAPI } from '@/composables/useAPI'

import type { User } from '@/components/classes/Authentication'

export const useAuthStore = defineStore('auth', () => {
  const isAuthenticated = ref(false)
  const user = ref<User | null>(null)

  function authenticate(userData: User) {
    isAuthenticated.value = true
    user.value = userData
    localStorage.setItem('token', userData.token)
  }

  function logout() {
    isAuthenticated.value = false
    user.value = null
    localStorage.removeItem('token')
  }

  onMounted(async () => {
    const token = localStorage.getItem('token')
    if (token) {
      const { recoverUser } = useAPI()
      const { authenticate, logout } = useAuthStore()
      const user = await recoverUser(token)
      if (user) {
        authenticate(user)
      } else {
        logout()
      }
    }
  })

  return { isAuthenticated, user, authenticate, logout }
})
