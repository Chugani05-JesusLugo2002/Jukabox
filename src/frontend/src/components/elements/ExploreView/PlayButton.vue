<script setup lang="ts">
import { Tooltip } from 'bootstrap'

const { lbzUrl, type, id } = defineProps(['lbzUrl', 'type', 'id'])

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const tooltipList = [...tooltipTriggerList].map((tooltipTriggerEl) => new Tooltip(tooltipTriggerEl))
</script>

<template>
  <a
    :href="lbzUrl"
    class="col-md-1 d-none rounded d-lg-flex justify-content-center play-button text-decoration-none flex-column"
    target="_blank"
    data-bs-toggle="tooltip"
    data-bs-title="Play in ListenBrainz"
  >
    <img
      src="/imgs/listenbrainz-logo.svg"
      :alt="`ListenBrainz to ${type} ${id}`"
      class="img-fluid w-100"
    />
    <p class="fst-italic text-secondary text-center">Listen</p>
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
