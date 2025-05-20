<script setup lang="ts">
const { user } = defineProps(['user'])
</script>

<template>
  <a
    class="dropdown-toggle text-body-emphasis"
    type="button"
    data-bs-toggle="dropdown"
    aria-expanded="false"
  >
    <img
      v-if="user"
      :src="user.avatar"
      alt="My profile avatar"
      class="rounded-circle"
      width="32"
      height="32"
    />
  </a>
</template>
