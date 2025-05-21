<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth.ts'

import ItemHeader from '@/components/elements/shared/ItemHeader.vue'
import UrlsContainer from '@/components/elements/shared/UrlsContainer.vue'
import StatsContainer from '@/components/elements/shared/StatsContainer.vue'
import ArtistsLabel from '@/components/elements/includes/ArtistsLabel.vue'
import CreateReviewInput from '@/components/elements/SongDetailView/CreateReviewInput.vue'
import AlertComp from '@/components/gui/AlertComp.vue'
import ReviewItem from '@/components/elements/SongDetailView/ReviewItem.vue'

const { getData } = useAPI()
const authStore = useAuthStore()
const route = useRoute()

const song = ref()
const comments = ref()

async function updateComments(songId: number) {
  if (song.value) {
    comments.value = await getData(`songs/${songId}/reviews/`)
  }
}

onMounted(async () => {
  const song_pk = route.params['song_pk']
  song.value = await getData(`songs/${song_pk}/`)
  if (song.value) {
    await updateComments(song.value.id)
  }
})
</script>

<template>
  <div v-if="song">
    <ItemHeader :img="song.cover" :title="song.title" :id="song.id" :type="'song'">
      <ArtistsLabel :artists="song.artists" />
    </ItemHeader>

    <div class="row">
      <div class="col-9">
        <h4>Reviews</h4>
        <CreateReviewInput
          :songId="song.id"
          v-if="authStore.isAuthenticated"
          @sentReview="updateComments(song.id)"
        />
        <div v-if="comments">
          <div v-if="comments.length > 0">
            <ReviewItem v-for="(review, index) in comments" :key="index" :comment="review">
              {{ review.comment }}
            </ReviewItem>
          </div>
          <AlertComp :style="'info'" v-else>No comments yet. Write the first one! :)</AlertComp>
        </div>
      </div>
      <div class="col-3">
        <UrlsContainer :type="'songs'" :id="song.id" :lbzUrl="song.lbz_url" />
        <StatsContainer :likes="song.likes" :reviews="song.reviews"></StatsContainer>
      </div>
    </div>
  </div>

  <p v-else>Loading song</p>
</template>
