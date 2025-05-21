<script setup lang="ts">
import LikesCounter from '@/components/gui/LikesCounter.vue'
import ReviewsCounter from '@/components/gui/ReviewsCounter.vue'

const { likes, reviews } = defineProps(['likes', 'reviews'])
</script>

<template>
  <div class="my-3">
    <slot>
      <p class="h4">Status</p>
      <LikesCounter :likes="likes" />
      <ReviewsCounter :reviews="reviews ? reviews : 0" />
    </slot>
  </div>
</template>
