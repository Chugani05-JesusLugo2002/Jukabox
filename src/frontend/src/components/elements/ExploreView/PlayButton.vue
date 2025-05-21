<script setup lang="ts">
import { Tooltip } from 'bootstrap'

const { lbzUrl, type, id } = defineProps(['lbzUrl', 'type', 'id'])

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new Tooltip(tooltipTriggerEl))
</script>

<template>
    <a :href="lbzUrl" class="col-1 rounded d-flex justify-content-center play-button" target="_blank" data-bs-toggle="tooltip" data-bs-title="Play in ListenBrainz">
      <img src="/imgs/listenbrainz-logo.svg" :alt="`ListenBrainz to ${type} ${id}`" class="img-fluid w-50">
    </a>
</template>


<style scoped lang="scss">
.play-button {
  transition: 0.3s;
  &:hover {
    background-color: rgb(209, 207, 207);
  }
}
</style>