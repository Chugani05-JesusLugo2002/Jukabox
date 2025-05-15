import type { Artist, Album } from './Artist'

export interface Song {
  id: number
  title: string
  artists: Artist[]
  released_at: number
  album: Album | string
  cover: string
  added_at: string
  hearts: number
}
