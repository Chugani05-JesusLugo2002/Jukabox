<script setup lang="ts">
import { ref, watch } from 'vue'
import { useAPI } from '@/composables/useAPI'
import { useI18n } from 'vue-i18n'

import FilterPill from './FilterPill.vue'

const { getExplorerResult } = useAPI()
const { t } = useI18n()
const emit = defineEmits(['searchResults'])

const POSSIBLE_FILTERS = [
  { id: 'All', name: t('explore-page.pill1') },
  { id: 'Artists', name: t('explore-page.pill2') },
  { id: 'Songs', name: t('explore-page.pill3') },
  { id: 'Albums', name: t('explore-page.pill4') },
]
const query = ref('')
const type = ref('All')

async function searchInAPI() {
  const result = query.value ? await getExplorerResult(query.value, type.value) : ''
  emit('searchResults', result)
}

watch(query, searchInAPI)
watch(type, searchInAPI)
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
    <FilterPill
      v-for="(filter, index) in POSSIBLE_FILTERS"
      :key="index"
      @click="type = filter.id"
      :selected="filter.id == type"
    >
      {{ filter.name }}
    </FilterPill>
  </div>
</template>
