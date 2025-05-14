<script setup lang="ts">
import { ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import ExplorerFilterPill from './ExplorerFilterPill.vue'
import ItemList from './ItemList.vue'
import { useAPI } from '@/composables/useAPI'

const { locale, t } = useI18n()
const { getExplorerResult } = useAPI()
const query = ref('')
const type = ref('')
const result = ref()

async function searchInAPI() {
  if (query.value) {
    try {
      result.value = await getExplorerResult(query.value, type.value)
    } catch (e) {
      console.error(e)
    }
  }
  else {
    result.value = ''
  }
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
    <ExplorerFilterPill @click="type = ''">{{ $t('explore-page.pill1') }}</ExplorerFilterPill>
    <ExplorerFilterPill @click="type = 'Artists'">{{ $t('explore-page.pill2') }}</ExplorerFilterPill>
    <ExplorerFilterPill @click="type = 'Songs'">{{ $t('explore-page.pill3') }}</ExplorerFilterPill>
    <ExplorerFilterPill @click="type = 'Albums'">{{ $t('explore-page.pill4') }}</ExplorerFilterPill>
  </div>

  <div v-if="result">
    <ul class="list-group">
      <ItemList v-for="artist in result.result.artists" :title="artist.name" :url="`/artists/${artist.id}/`" :image="artist.avatar" type="Artist"></ItemList>
      <ItemList v-for="album in result.result.albums" :title="album.title" :url="`/albums/${album.id}/`" :image="album.cover" type="Album"></ItemList>
      <ItemList v-for="song in result.result.songs" :title="song.title" :url="`/songs/${song.id}/`" :image="song.cover" type="Song"></ItemList>
    </ul>
  </div>
</template>
