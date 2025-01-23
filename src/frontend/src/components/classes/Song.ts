export class Song {
  id: number
  name: string
  artist: string
  album: string
  genre: string[]
  year: number

  constructor(
    id: number,
    name: string,
    artist: string,
    album: string,
    genre: string[],
    year: number,
  ) {
    this.id = id
    this.name = name
    this.artist = artist
    this.album = album
    this.genre = genre
    this.year = year
  }
}
