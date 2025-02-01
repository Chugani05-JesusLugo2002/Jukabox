import type { Artist, Album } from './Artist'

export interface Genre {
  id: number
  name: string
  color: string
}

export interface Song {
  id: number
  title: string
  artists: Artist[]
  released_at: number
  album: Album|string
  cover: string
  genre: Genre[]
  added_at: string
}
