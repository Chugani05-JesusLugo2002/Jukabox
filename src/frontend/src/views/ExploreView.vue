<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import ViewHeader from '@/components/ViewHeader.vue'
import ExplorerComponent from '@/components/elements/ExplorerComponent.vue'

const { locale, t } = useI18n()
</script>

<template>
  <ViewHeader>{{ $t('explore-page.title') }}</ViewHeader>

  <ExplorerComponent />
</template>
