<script setup lang="ts">
const props = defineProps(['itemType', 'links', 'lbz_link'])
</script>

<template>
  <div class="mb-3">
    <a v-if="lbz_link" :href="lbz_link" class="btn btn-light w-100 py-3 border fw-bold" target="_blank">
      <img src="/imgs/listenbrainz-logo.svg" alt="ListenBrainz logo" class="img-fluid col-2 px-2">
      Listen on ListenBrainz
    </a>

    <div class="d-flex flex-column mt-3" v-if="links">
      <h4>External links</h4>
      
      <a v-for="url in links['result'][0]" :href="url['url']">
        <div class="h5" v-if="url['url'].includes('spotify')"><i class="bi bi-spotify"></i> View album in Spotify</div>
        <div class="h5" v-else-if="url['url'].includes('youtube')"><i class="bi bi-youtube"></i> View album in Youtube</div>
        <div class="h5" v-else-if="url['url'].includes('deezer')"><i class="bi bi-music-note"></i> View album in Deezer</div>
      </a>
    </div>
  </div>
</template>

<style scoped lang="scss">
a {
  color: black;
  span {
    font-style: italic;
  }
}
</style>
