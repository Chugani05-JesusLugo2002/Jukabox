<script setup lang="ts">
const { comment } = defineProps(['comment'])

function formatDateTime(input: string): string {
  const date = new Date(input)
  const datePart = date.toISOString().split('T')[0]
  const timePart = date.toTimeString().split(' ')[0].slice(0, 5)
  return `${datePart}, ${timePart}`
}
</script>

<template>
  <div class="row py-1" v-if="comment">
    <RouterLink class="col-1" :to="`/profiles/${comment.author.slug}`">
      <img
        :src="comment.author.avatar"
        :alt="comment.author.name + ' picture'"
        class="img-fluid rounded-circle"
      />
    </RouterLink>
    <div class="col d-flex flex-column">
      <RouterLink class="text-decoration-none" :to="`/profiles/${comment.author.slug}`">
        <h5 class="profile-username text-black">{{ comment.author.username }}</h5>
      </RouterLink>
      <p><slot></slot></p>
    </div>
    <div class="col">
      <p class="text-secondary text-end">{{ formatDateTime(comment.created_at) }}</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.profile-username {
  text-decoration: none;
  &:hover {
    text-decoration: underline;
  }
}
</style>
