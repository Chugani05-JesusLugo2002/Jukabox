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
  released_at: number
  cover: string
  added_at: string
}
