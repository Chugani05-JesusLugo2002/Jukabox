<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import ExplorerFilterPill from './ExplorerFilterPill.vue'

const { locale, t } = useI18n()
const query = ref('')
</script>

<template>
  <div class="input-group input-group-lg">
    <span class="input-group-text"><i class="bi bi-search"></i></span>
    <input
      type="text"
      name="query"
      id="query"
      v-model="query"
      class="form-control input-lg"
      :placeholder="$t('explore-page.placeholder')"
    />
  </div>

  <div class="d-flex justify-content-center align-items-center">
    <ExplorerFilterPill>{{ $t('explore-page.pill1') }}</ExplorerFilterPill>
    <ExplorerFilterPill>{{ $t('explore-page.pill2') }}</ExplorerFilterPill>
    <ExplorerFilterPill>{{ $t('explore-page.pill3') }}</ExplorerFilterPill>
    <ExplorerFilterPill>Albums</ExplorerFilterPill>
    <ExplorerFilterPill>Playlists</ExplorerFilterPill>
    <ExplorerFilterPill>{{ $t('explore-page.pill6') }}</ExplorerFilterPill>
  </div>
</template>
