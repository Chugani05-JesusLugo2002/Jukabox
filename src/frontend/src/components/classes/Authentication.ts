export interface User {
  id: number
  token: string
  slug: string
  username: string
  first_name: string
  last_name: string
  email: string
  bio: string
  avatar: string
  liked_songs_count: number
  liked_albums_count: number
  liked_artists_count: number
  reviews_count: number
}

export interface SignupData {
  username: string
  first_name: string
  last_name: string
  email: string
  password: string
}

export interface LoginData {
  username: string
  password: string
}
