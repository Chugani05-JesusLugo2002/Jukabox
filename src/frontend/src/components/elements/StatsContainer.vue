<script setup lang="ts">
const { hearts } = defineProps(['hearts'])
</script>

<template>
  <h4><slot></slot></h4>
  <h5 class="px-2"><i class="bi bi-heart-fill"></i> {{ hearts }}</h5>
  <h5 class="px-2"><i class="bi bi-chat-left-text-fill"></i> 100</h5>
  <h5 class="px-2"><i class="bi bi-star-fill"></i> 4.5</h5>
</template>
