<script setup lang="ts">
import { ref } from 'vue';

import ViewHeader from '@/components/layout/ViewHeader.vue'
import SearchBar from '@/components/elements/ExploreView/SearchBar.vue';
import ResultList from '@/components/elements/ExploreView/ResultList.vue';
import AlertComp from '@/components/gui/AlertComp.vue';

const result = ref()
</script>

<template>
  <ViewHeader>{{ $t('explore-page.title') }}</ViewHeader>

  <SearchBar @search-results="(r) => result = r"/>
  <ResultList v-if="result" :result="result"/>
  <AlertComp v-else :style="'info mt-2'">No search yet! Try with your favourite song! <i class="bi bi-search"></i></AlertComp>
</template>
