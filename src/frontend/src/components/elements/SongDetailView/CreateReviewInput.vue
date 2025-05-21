<script setup lang="ts">
import { ref } from 'vue'

import { useSocial } from '@/composables/useSocial'

const { songId } = defineProps<{
  songId: number
}>()
const emit = defineEmits(['sentReview'])
const social = useSocial()

const review = ref('')

async function sendReview(songId: number) {
  if (review.value) {
    const response = await social.sendReview(songId, review.value)
    if (response) {
      review.value = ''
      emit('sentReview', response)
    }
  }
}
</script>

<template>
  <form id="comment-input" class="mb-3" @submit.prevent="sendReview(songId)">
    <div class="form-floating">
      <input type="text" name="comment" id="comment" class="form-control mb-2" v-model="review" />
      <label for="comment">Your review...</label>
    </div>
    <input class="btn btn-primary" type="submit" value="Send" />
  </form>
</template>
