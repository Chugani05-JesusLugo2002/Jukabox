import type { Song } from "./Song"

export interface Playlist {
    id: number
    title: string
    songs: Song[]
    user: string
    created_at: string
}