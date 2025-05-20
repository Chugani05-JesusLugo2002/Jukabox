<script setup lang="ts">
import { useAPI } from '@/composables/useAPI';
import { onMounted, ref } from 'vue';

const { getData } = useAPI()
const props = defineProps(['item_type', 'item_id', 'lbz_link'])
const fixedLinks = ref<any[]>([])

onMounted(async() => {
  const api_url = `${props.item_type}s/${props.item_id}/links/`
  const response = await getData(api_url)
  response.forEach((link: any) => {
  fixedLinks.value.push({
    target: link.url,
    urlType: link.url_type.charAt(0).toUpperCase() + link.url_type.slice(1) 
  })
})})
</script>

<template>
  <div class="mb-3">
    <a v-if="lbz_link" :href="lbz_link" class="btn btn-light w-100 py-3 border fw-bold" target="_blank">
      <img src="/imgs/listenbrainz-logo.svg" alt="ListenBrainz logo" class="img-fluid col-2 px-2">
      Listen on ListenBrainz
    </a>

    <div class="d-flex flex-column mt-3" v-if="fixedLinks.length > 0">
      <h4>External links</h4>
      
      <div v-for="url in fixedLinks">
        <a :href="url.target" class="btn btn-light py-2 my-1 w-100 fw-bold border d-flex justify-content-center align-items-center" target="_blank">
          <i v-if="url.urlType == 'Spotify'" class="bi bi-spotify h4 px-2 m-0 text-success"></i>
          <i v-else-if="url.urlType == 'Youtube'" class="bi bi-youtube h3 m-0 px-2 text-danger"></i>      
          <img v-else-if="url.urlType == 'Deezer'" src="/imgs/deezer-logo.svg" style="height: 32px;" class="mx-2">     
          <img v-else-if="url.urlType == 'Bandcamp'" src="/imgs/bandcamp-logo.png" style="height: 32px;" class="mx-2"> 
          <i v-else class="bi bi-music-note h3 px-2 m-0 h4"></i>      
          <span>View album in {{ url.urlType }}</span>
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
a {
  color: black;
}
</style>
