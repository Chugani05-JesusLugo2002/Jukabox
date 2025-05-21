import type { User } from '@/components/classes/Authentication'
import type { Song } from '@/components/classes/Song';
import type { Album } from '@/components/classes/Album';
import type { Artist } from '@/components/classes/Artist';
import type { JSONResponse } from '@/components/classes/JSONResponse'

import { useAuthStore } from '@/stores/useAuth'
import { useToast } from 'vue-toast-notification'

export const useSocial = () => {
  const API_URL = 'http://localhost:8000/api/v1/'
  const authStore = useAuthStore()
  const toast = useToast()

  async function getMyProfile(token: string): Promise<User | undefined> {
    const url = API_URL + 'users/my-profile/'
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
      })
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      return await response.json()
    } catch (error) {
      console.error(error)
    }
  }

  async function likeItem(id: number, type: string): Promise<JSONResponse|undefined> {
    const url = API_URL + `${type}s/${id}/like/`
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authStore.user?.token}`,
        },
        body: `{ "${type}_id": "${id}" }`,
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

  async function getLikedItems(userId: string, itemType: string): Promise<Song[]|Artist[]|Album[]|undefined> {
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
      return await response.json()
    } catch (error) {
      console.error(error)
    }
  }

  return { getMyProfile, likeItem, getLikedItems }
}
