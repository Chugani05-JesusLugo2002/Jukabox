import { defineStore } from 'pinia'

export const useSongsStore = defineStore('songs', () => {
  const example = 'Hello world!'

  return { example }
})
