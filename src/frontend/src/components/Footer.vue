<script setup lang="ts">
import { useI18n } from "vue-i18n";
const { locale, t } = useI18n();
const changeLanguage = (lang) => {
  locale.value = lang;
};
</script>

<template>
    <div class="btn-group text-success" role="group">
        <button type="button" class="btn btn-outline-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
          <i class="bi bi-translate icon-medium"></i>
        </button>
        <ul class="dropdown-menu">
          <li class="dropdown-item"><a @click="changeLanguage('en')">English</a></li>
          <li class="dropdown-item"><a  @click="changeLanguage('es')">Español</a></li>
        </ul>
    </div>
</template>