<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { useAPI } from '@/composables/useAPI'
import ListenBrainzButton from '../ArtistDetailView/ListenBrainzButton.vue'
import UrlComp from './UrlComp.vue'

const { getData } = useAPI()
const { id, type, lbzUrl } = defineProps<{
  id: number
  lbzUrl: string
  type: 'artists' | 'albums' | 'songs'
}>()

const links = ref()

onMounted(async () => {
  const response = await getData(`${type}/${id}/links/`)
  if (response) {
    links.value = response
  }
})
</script>

<template>
  <div class="mb-3" v-if="links">
    <ListenBrainzButton :lbz-url="lbzUrl" :as-button="true" />

    <div class="d-flex flex-column mt-3" v-if="links.length > 0">
      <h4>External links</h4>
      <UrlComp v-for="(link, index) in links" :key="index" :link="link">
        View album in {{ link.url_type.charAt(0).toUpperCase() + link.url_type.slice(1) }}
      </UrlComp>
    </div>
  </div>
</template>

<style scoped lang="scss">
a {
  color: black;
}
</style>
