<script setup lang="ts">
const props = defineProps(['image', 'name', 'isRounded'])

const imgClass = props.isRounded ? 'img-fluid rounded-circle' : 'img-fluid'
</script>

<template>
  <div class="row pb-3">
    <div class="col-3">
      <img :src="image" :alt="name + ' image'" :class="imgClass" />
    </div>
    <div class="col d-flex flex-column justify-content-center">
      <h1 class="display-5 fw-bold">{{ name }}</h1>
      <p class="text-muted h5"><slot></slot></p>
    </div>
  </div>
</template>
