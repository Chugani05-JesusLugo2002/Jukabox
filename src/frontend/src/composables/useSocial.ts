import type { User } from '@/components/classes/Authentication'

export const useSocial = () => {
  const API_URL = 'http://localhost:8000/api/v1/'

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

  return { getMyProfile }
}
