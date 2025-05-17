<script setup lang="ts">
const props = defineProps(['likes', 'comments'])
</script>

<template>
  <h4><slot></slot></h4>
  <h5 class="px-2"><i class="bi bi-heart-fill"></i> {{ likes }}</h5>
  <h5 class="px-2" v-if="comments"><i class="bi bi-chat-left-text-fill"></i> {{ comments }}</h5>
</template>
