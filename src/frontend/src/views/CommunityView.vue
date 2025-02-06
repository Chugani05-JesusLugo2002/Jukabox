<script setup lang="ts">
import ViewHeader from '@/components/ViewHeader.vue'
import { useI18n } from "vue-i18n";

const { locale, t } = useI18n();
</script>

<template>
  <ViewHeader>{{ $t("community-page.title") }}</ViewHeader>
</template>
