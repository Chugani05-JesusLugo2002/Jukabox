<script lang="ts" setup>
const props = defineProps(['title', 'url', 'image', 'type'])
</script>

<template>
  <RouterLink class="row py-1 text-reset text-decoration-none" :to="url">
    <img :src="image" :alt="title + ' image'" class="col-1 img-fluid" />
    <div class="col">
      <h5>{{ title }}</h5>
      <p class="fw-bold text-body-secondary" v-if="type">{{ type }}</p>
    </div>
  </RouterLink>
</template>
