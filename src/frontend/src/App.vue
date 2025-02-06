<script setup lang="ts">
import { RouterView } from 'vue-router'

import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <header>
    <Navbar />
  </header>
  <main class="container mt-3 mb-5 pb-5">
    <RouterView />
  </main>
  <Footer />
</template>
