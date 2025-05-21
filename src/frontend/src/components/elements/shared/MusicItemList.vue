<script setup lang="ts">
import LikesCounter from '@/components/gui/LikesCounter.vue'
import ReviewsCounter from '@/components/gui/ReviewsCounter.vue'

const { id, title, likes, reviews, type } = defineProps<{
  id: number
  title: string
  type: 'songs' | 'albums' | 'artists'
  likes: number
  reviews?: number
}>()


</script>

<template>
  <RouterLink
    :class="`row text-reset py-2 text-decoration-none d-flex align-items-center ${type == 'songs' ? 'border' : 'lead'}`"
    :to="`/${type}/${id}`"
  >
    <p class="col m-0">{{ title }}</p>
    <p class="col m-0"><slot></slot></p>
    <div class="col-2 d-flex justify-content-end align-items-center">
      <LikesCounter :likes="likes" />
      <ReviewsCounter :reviews="reviews ? reviews : 0" />
    </div>
  </RouterLink>
</template>

<style scoped lang="scss">
.row {
  transition: 0.3s;
  &:hover {
    background-color: rgb(226, 220, 207);
  }
}
</style>
