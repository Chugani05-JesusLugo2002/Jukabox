<script setup lang="ts">
import { useI18n } from "vue-i18n";
const { locale, t } = useI18n();

const changeLanguage = (lang: string) => {
  locale.value = lang;
};

function changeTheme(mode: string) {

}
</script>

<template>
    <footer class="bg-light container-fluid border-top">
      <div class="container d-flex justify-content-between py-3">
        <p class="text-muted">© Jukabox, 2025</p>
        <div class="d-flex">
          <div class="btn-group text-success px-2" role="group">
            <button type="button" class="btn btn-outline-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
              <i class="bi bi-moon-stars-fill"></i>
            </button>
            <ul class="dropdown-menu">
              <li class="dropdown-item" @click="changeTheme('auto')"><i class="bi bi-circle-half"></i> Auto</li>
              <li class="dropdown-item" @click="changeTheme('light')"><i class="bi bi-brightness-high-fill"></i> {{ $t("footer.light") }}</li>
              <li class="dropdown-item" @click="changeTheme('dark')"><i class="bi bi-moon-stars-fill"></i> {{ $t("footer.dark") }}</li>
            </ul>
          </div>

          <div class="btn-group text-success" role="group">
            <button type="button" class="btn btn-outline-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
              <i class="bi bi-globe2"></i>
            </button>
            <ul class="dropdown-menu">
              <li class="dropdown-item" @click="changeLanguage('en')">🇬🇧 {{ $t("footer.english") }}</li>
              <li class="dropdown-item" @click="changeLanguage('es')">🇪🇸 {{ $t("footer.spanish") }}</li>
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



