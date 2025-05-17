import type { Artist } from './Artist'
import type { Album } from './Album'

export interface Song {
  id: number
  title: string
  artists: Artist[]
  released_at: number
  album: Album | string
  cover: string
  added_at: string
  likes: number
}
