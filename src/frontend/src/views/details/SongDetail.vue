<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { Song } from '@/components/classes/Song'
import ItemHeader from '@/components/elements/ItemHeader.vue'
import UrlsContainer from '@/components/elements/includes/UrlsContainer.vue'
import StatsContainer from '@/components/elements/includes/StatsContainer.vue'
import ArtistsLabel from '@/components/elements/includes/ArtistsLabel.vue'
import { useAPI } from '@/composables/useAPI'
import Comment from '@/components/elements/includes/Comment.vue'
import { useAuthStore } from '@/stores/useAuth.ts'

const { getData, addReview } = useAPI()
const authStore = useAuthStore()

const route = useRoute()
const song = ref<null | Song>(null)

const comment = ref('')
const songComments = ref('')

async function sendReview(id: number) {
  if (comment.value && authStore.user) {
    const response = await addReview(id, comment.value, authStore.user.token)
    songComments.value = await getData(`songs/${id}/reviews/`)
    comment.value = ''
  } else {
    alert('Missing comment')
  }
}

onMounted(async () => {
  const song_pk = route.params['song_pk']
  song.value = await getData(`songs/${song_pk}/`)
  songComments.value = await getData(`songs/${song_pk}/reviews/`)
})
</script>

<template>
  <div v-if="song">
    <ItemHeader :img="song.cover" :title="song.title" :id="song.id" :type="'song'">
      <ArtistsLabel :artists="song.artists" />
    </ItemHeader>

    <div class="row">
      <div class="col-9">
        <p class="h4">Reviews</p>
        <form id="comment-input" class="mb-3" @submit.prevent="sendReview(song.id)" v-if="authStore.isAuthenticated">
          <div class="form-floating">
            <input type="text" name="comment" id="comment" class="from-control mb-2" v-model="comment">
            <label for="comment">Your comment...</label>
          </div>
          <input class="btn btn-primary" type="submit" value="Send" />
        </form>

        <div id="comments-container">
          <div v-if="songComments.length > 0">
            <Comment v-for="(comment, index) in songComments" :key="index" :comment="comment"></Comment>
          </div>
          <div v-else class="alert alert-primary">No comments yet. Write the first one! :)</div>
        </div>
      </div>
      <div class="col-3">
        <UrlsContainer :item_type="'song'" :item_id="song.id" :lbz_link="song.lbz_url"/>
        <StatsContainer :likes="song.likes" :comments="0">Stats</StatsContainer>
      </div>
    </div>
  </div>

  <p v-else>Loading song</p>
</template>
