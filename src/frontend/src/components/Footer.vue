<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
const { locale, t } = useI18n()

const changeLanguage = (lang: string) => {
  locale.value = lang
}

const themeIconClass = ref('')
const theme = ref('')

function changeTheme(mode: string) {
  document.documentElement.setAttribute('data-bs-theme', mode)
  localStorage.setItem('theme', mode)
  theme.value = mode
  themeIconClass.value = mode == 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-brightness-high-fill'
}

const footerClass = ref('container-fluid border-top bg-')

onMounted(() => {
  const previousTheme = localStorage.getItem('theme')
  if (previousTheme) {
    changeTheme(previousTheme)
    theme.value = previousTheme
    themeIconClass.value = previousTheme == 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-brightness-high-fill'
  }
})
</script>

<template>
  <footer :class="footerClass + theme">
    <div class="container d-flex justify-content-between py-3">
      <p class="text-muted">© Jukabox, 2025</p>
      <div class="d-flex">
        <div class="btn-group text-success px-2" role="group">
          <button
            type="button"
            class="btn btn-outline-primary dropdown-toggle"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <i :class="themeIconClass"></i>
          </button>
          <ul class="dropdown-menu">
            <li class="dropdown-item" @click="changeTheme('light')">
              <i class="bi bi-brightness-high-fill"></i> {{ $t('footer.light') }}
            </li>
            <li class="dropdown-item" @click="changeTheme('dark')">
              <i class="bi bi-moon-stars-fill"></i> {{ $t('footer.dark') }}
            </li>
          </ul>
        </div>

        <div class="btn-group text-success" role="group">
          <button
            type="button"
            class="btn btn-outline-primary dropdown-toggle"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <i class="bi bi-globe2"></i>
          </button>
          <ul class="dropdown-menu">
            <li class="dropdown-item" @click="changeLanguage('en')">
              🇬🇧 {{ $t('footer.english') }}
            </li>
            <li class="dropdown-item" @click="changeLanguage('es')">
              🇪🇸 {{ $t('footer.spanish') }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped lang="scss">
footer {
  bottom: 0;
  position: fixed;
}

.dropdown-item {
  cursor: pointer;
}
</style>
