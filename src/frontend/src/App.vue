<script setup lang="ts">
import { RouterView } from 'vue-router'

import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <header>
    <Navbar />
  </header>
  <main class="container my-3">
    <RouterView />
  </main>
  <Footer />
</template>
