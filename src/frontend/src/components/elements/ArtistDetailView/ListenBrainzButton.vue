<script setup lang="ts">
const { lbzUrl, asButton } = defineProps(['lbzUrl', 'asButton'])
</script>

<template>
  <div :class="asButton ? 'btn btn-light w-100 text-decoration-none fw-bold border' : ''">
    <img src="/imgs/listenbrainz-logo.svg" alt="ListenBrainz logo" class="img-fluid col-2" />
    <a :href="lbzUrl" class="col py-3 mx-3 my-1 text-black" target="_blank">Play in ListenBrainz</a>
  </div>
</template>

<style scoped lang="scss">
img {
  width: 32px;
}
</style>
