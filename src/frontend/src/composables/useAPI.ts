import type { LoginData, SignupData, User } from '@/components/classes/Authentication'
import type { JSONResponse } from '@/components/classes/JSONResponse'
import { useAuthStore } from '@/stores/useAuth'
import { useToast } from 'vue-toast-notification'

export const useAPI = () => {
  const API_URL = 'http://localhost:8000/api/v1/'
  const authStore = useAuthStore()
  const toast = useToast()

  async function getData(path: string): Promise<object|undefined> {
    const url = API_URL + path
    try {
      const response = await fetch(url)
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  async function userLogin(loginData: LoginData): Promise<User|undefined> {
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

  async function userSignup(signupData: SignupData): Promise<User|undefined> {
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

  async function getLikedItems(userId: string, itemType: string): Promise<any> {
    const url = API_URL + `users/${userId}/liked_${itemType}s/`
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
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

  async function importArtist(artist_mbid: string): Promise<JSONResponse|undefined> {
    const url = API_URL + 'import/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${authStore.user?.token}`
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

  async function like(id: number, type: string, token: string): Promise<any> {
    const url = API_URL + `${type}s/${id}/like/`
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: `{ "${type}_id": "${id}" }`,
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

  async function addReview(songId: number, comment: string, token: string): Promise<any> {
    const url = API_URL + `songs/${songId}/add-review/`
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: `{ "comment": "${comment}" }`,
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

  async function getExplorerResult(query: string, type: string): Promise<any> {
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

  async function userLogout(): Promise<any> {
    const url = API_URL + 'accounts/logout/'
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
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

  return {
    getData,
    userLogin,
    userSignup,
    userLogout,
    importArtist,
    getExplorerResult,
    like,
    addReview,
    getLikedItems,
  }
}
