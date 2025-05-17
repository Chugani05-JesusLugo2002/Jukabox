import type { Song } from "./Song"
import type { Album } from "./Album"
import type { Artist } from "./Artist"

export interface User {
  id: number
  token: string
  username: string
  first_name: string
  last_name: string
  email: string
  bio: string
  avatar: string
  liked_songs: Song[]
  liked_albums: Album[]
  liked_artists: Artist[]
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
