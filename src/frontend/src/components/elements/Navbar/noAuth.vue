<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useI18n } from "vue-i18n";

const { locale, t } = useI18n();
</script>

<template>
  <div class="d-flex">
    <RouterLink class="btn btn-outline-primary mx-2" to="/signup">{{ $t("noauth.register") }}</RouterLink>
    <RouterLink class="btn btn-primary" to="/login">{{ $t("noauth.login") }}</RouterLink>
  </div>
</template>
