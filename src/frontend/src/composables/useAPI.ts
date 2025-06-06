import type { LoginData, SignupData, User } from '@/components/classes/Authentication'
import type { JSONResponse } from '@/components/classes/JSONResponse'
import { useAuthStore } from '@/stores/useAuth'
import { useToast } from 'vue-toast-notification'

export const useAPI = () => {
  const API_URL = 'http://localhost:8000/api/v1/'
  const authStore = useAuthStore()
  const toast = useToast()

  async function getData(path: string): Promise<object | undefined> {
    const url = API_URL + path
    try {
      const response = await fetch(url)
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  async function userLogin(loginData: LoginData): Promise<User | undefined> {
    const url = API_URL + 'accounts/login/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData),
      })
      if (!response.ok) {
        const data = await response.json()
        toast.error(data.error)
        throw new Error(data.error)
      }
      return await response.json()
    } catch (error) {
      console.error(error)
    }
  }

  async function userSignup(signupData: SignupData): Promise<User | undefined> {
    const url = API_URL + 'accounts/signup/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(signupData),
      })
      if (!response.ok) {
        const data = await response.json()
        toast.error(data.error)
        throw new Error(data.error)
      }
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  async function updateProfile(bio: string): Promise<JSONResponse | undefined> {
    const url = API_URL + 'users/change-profile/'
    try {
      const formData = new FormData()
      formData.append('bio', bio)
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${authStore.user?.token}`,
        },
        body: formData,
      })
      if (!response.ok) {
        const data = await response.json()
        toast.error(data.error)
        throw new Error(data.error)
      }
      return await response.json()
    } catch (error) {
      console.error(error)
    }
  }

  async function deleteProfile(): Promise<JSONResponse | undefined> {
    const url = API_URL + 'users/leave/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${authStore.user?.token}`,
        }
      })
      if (!response.ok) {
        const data = await response.json()
        toast.error(data.error)
        throw new Error(data.error)
      }
      return await response.json()
    } catch (error) {
      console.error(error)
    }
  }

  async function importArtist(artist_mbid: string): Promise<JSONResponse | undefined> {
    const url = API_URL + 'import/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authStore.user?.token}`,
        },
        body: `{ "artist_mbid": "${artist_mbid}" }`,
      })
      if (!response.ok) {
        const data = await response.json()
        toast.error(data.error)
        throw new Error(data.error)
      }
      return await response.json()
    } catch (error) {
      console.error(error)
    }
  }

  async function getExplorerResult(query: string, type: string): Promise<object[] | undefined> {
    const url = API_URL + 'explore/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: `{ "query": "${query}", "type": "${type}" }`,
      })
      if (!response.ok) {
        const data = await response.json()
        toast.error(data.error)
        throw new Error(data.error)
      }
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  async function userLogout(): Promise<JSONResponse | undefined> {
    const url = API_URL + 'accounts/logout/'
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      const data = await response.json()
      if (!response.ok) {
        toast.error(data.error)
        throw new Error(data.error)
      }
      toast.info(data.message)
      return data
    } catch (error) {
      console.error(error)
    }
  }

  return {
    getData,
    userLogin,
    userSignup,
    userLogout,
    importArtist,
    getExplorerResult,
    updateProfile,
    deleteProfile
  }
}
