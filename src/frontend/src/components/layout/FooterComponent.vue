<script setup lang="ts">
import { ref, onMounted } from 'vue'
import ThemeSelector from '../elements/FooterComponent/ThemeSelector.vue'
import LanguageSelector from '../elements/FooterComponent/LanguageSelector.vue'

const footerClass = ref('container-fluid border-top bg-')

const themeIconClass = ref('')
const theme = ref('')

function changeTheme(mode: string) {
  document.documentElement.setAttribute('data-bs-theme', mode)
  localStorage.setItem('theme', mode)
  theme.value = mode
  themeIconClass.value = mode == 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-brightness-high-fill'
}

onMounted(() => {
  const previousTheme = localStorage.getItem('theme')
  if (previousTheme) {
    changeTheme(previousTheme)
    theme.value = previousTheme
    themeIconClass.value =
      previousTheme == 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-brightness-high-fill'
  }
})
</script>

<template>
  <footer :class="footerClass + theme">
    <div class="container d-flex justify-content-between py-3">
      <p class="text-muted">© Jukabox, 2025</p>
      <div class="d-flex">
        <ThemeSelector @change-theme="changeTheme" :theme-icon-class="themeIconClass" />
        <LanguageSelector />
      </div>
    </div>
  </footer>
</template>

<style scoped lang="scss">
footer {
  bottom: 0;
  position: fixed;
}
</style>
