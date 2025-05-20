import type { Song } from './Song'
import type { Artist } from './Artist'

export interface Album {
  id: number
  title: string
  artists: Artist[]
  songs: Song[]
  likes: number
  released_at: number
  cover: string
  added_at: string
  lbz_url: string
}
