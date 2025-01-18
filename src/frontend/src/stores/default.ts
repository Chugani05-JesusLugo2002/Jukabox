import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const example = 'Hello world!'

  return { example }
})
