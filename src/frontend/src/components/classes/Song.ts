import type { Artist } from './Artist'

export interface Song {
  id: number,
  title: string,
  artists: Artist[],
}