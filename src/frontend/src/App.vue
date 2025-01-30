<script setup lang="ts">
import { RouterView } from 'vue-router'

import Navbar from './components/Navbar.vue'
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
