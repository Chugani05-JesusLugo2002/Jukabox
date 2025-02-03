import type { Song } from "./Song"

export interface Artist {
  id: number
  name: string
  bio: string
  avatar: string
  added_at: string
}

export interface Album {
  id: number
  title: string
  artists: Artist[]
  songs: Song[]
  released_at: number
  cover: string
  added_at: string
}
