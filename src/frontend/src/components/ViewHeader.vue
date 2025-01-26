<script lang="ts" setup>
const { title } = defineProps(['title'])
</script>

<template>
  <h1 class="display-1">{{ title }}</h1>
  <hr />
</template>
