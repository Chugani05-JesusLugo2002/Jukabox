<script setup lang="ts">
const { title } = defineProps(['title'])
</script>

<template>
  <section>
    <h2 class="display-5 my-3">{{ title }}</h2>
    <div class="row justify-content-center">
      <slot></slot>
    </div>
  </section>
</template>

<style scoped>
.mix-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: flex-start;
}
</style>
