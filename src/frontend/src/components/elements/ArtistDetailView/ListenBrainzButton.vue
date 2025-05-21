<script setup lang="ts">
const { lbzUrl } = defineProps(['lbzUrl'])
console.log(lbzUrl)
</script>

<template>
    <a :href="lbzUrl" class="btn btn-light w-25 py-3 border fw-bold" target="_blank">
      <img src="/imgs/listenbrainz-logo.svg" alt="ListenBrainz logo" class="img-fluid col-2 px-2" />
      Play in ListenBrainz
    </a>
</template>