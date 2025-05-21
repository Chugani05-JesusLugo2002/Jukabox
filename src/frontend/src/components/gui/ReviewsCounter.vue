<script setup lang="ts">
const { reviews } = defineProps(['reviews'])
</script>

<template>
  <h5 class="px-2"><i class="bi bi-chat-left-text"></i> {{ reviews }}</h5>
</template>
