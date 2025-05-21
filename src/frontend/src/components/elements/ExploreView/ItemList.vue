<script lang="ts" setup>
import PlayButton from './PlayButton.vue';

const { id, img, type } = defineProps<{
  id: number,
  img: string,
  type: 'artist'|'album'|'song',
  lbzUrl?: string
}>()
</script>

<template>
  <div class="row py-1">
    <RouterLink :to="`/${type}s/${id}/`" class="col-1">
      <img :src="img" :alt="id + ' image'" :class="`img-fluid ${type=='artist' ? 'rounded-circle' : 'rounded-3'}`" />
    </RouterLink>
    <div class="col-8">
      <h5>
        <RouterLink :to="`/${type}s/${id}/`" class="text-black"><slot></slot></RouterLink>
        <slot name="credits"></slot>
      </h5>
      <p class="fw-bold text-body-secondary">
        {{ type.charAt(0).toUpperCase() + type.slice(1) }}
      </p>
    </div>
    <div class="col d-flex align-items-center"><slot name="stats"></slot></div>
    <PlayButton :lbzUrl="lbzUrl" :type="type" :id="id"/>
  </div>
</template>

