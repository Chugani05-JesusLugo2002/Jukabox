<script setup lang="ts">
import { provide, ref } from 'vue'
import { RouterView } from 'vue-router'
import { getJsonData } from './components/classes/APIManager'

import Navbar from './components/Navbar.vue'

const songs = getJsonData('songs.json')

provide('songs', songs)
</script>

<template>
  <header>
    <Navbar />
  </header>
  <main class="container my-3">
    <RouterView />
  </main>
  <footer></footer>
</template>
