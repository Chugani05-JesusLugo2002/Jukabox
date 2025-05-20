<script setup lang="ts">
const { comment } = defineProps(['comment'])
</script>

<template>
  <div class="row py-1">
    <div class="col-1">
      <img
        :src="comment.author.avatar"
        :alt="comment.author.name + ' picture'"
        class="img-fluid rounded-circle"
      />
    </div>
    <div class="col d-flex flex-column">
      <h5>{{ comment.author.username }}</h5>
      <p>{{ comment.comment }}</p>
    </div>
    <div class="col">
      <p class="text-secondary text-end">{{ comment.created_at }}</p>
    </div>
  </div>
</template>
