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

  async function login(loginData: LoginData): Promise<any> {
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

  async function signup(signupData: SignupData): Promise<any> {
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

  async function recoverUser(token: string): Promise<any> {
    const url = API_URL + 'accounts/recover/'
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: `{ "token": "${token}" }`,
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
    const url = API_URL + 'importer/'
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


  return { getData, login, signup, recoverUser, userLogout, importArtist }
}
