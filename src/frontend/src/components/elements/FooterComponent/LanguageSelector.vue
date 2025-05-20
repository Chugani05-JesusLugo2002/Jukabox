<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

function changeLanguage(lang: string) {
  locale.value = lang
}
</script>

<template>
    <div class="btn-group text-success">
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
</template>

<style scoped lang="scss">
.dropdown-item {
  cursor: pointer;
}</style>