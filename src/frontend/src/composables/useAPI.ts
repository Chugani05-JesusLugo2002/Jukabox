import type { LoginData, SignupData } from '@/components/classes/Authentication'

export const useAPI = () => {
  const API_URL = 'http://localhost:8000/api/v1/'

  async function getData(path: string): Promise<any> {
    const url = API_URL + path
    try {
      const response = await fetch(url)
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  async function userLogin(loginData: LoginData): Promise<any> {
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
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  async function userSignup(signupData: SignupData): Promise<any> {
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
        throw new Error(`HTTP error! status: ${response.status}`)
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
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  async function importArtist(artist_mbid: string): Promise<any> {
    const url = API_URL + 'import/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: `{ "artist_mbid": "${artist_mbid}" }`,
      })
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      const data = await response.json()
      return data
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
        throw new Error(`HTTP error! status: ${response.status}`)
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
        throw new Error(`HTTP error! status: ${response.status}`)
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
        throw new Error(`HTTP error! status: ${response.status}`)
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
        throw new Error(`HTTP error! status: ${response.status}`)
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
