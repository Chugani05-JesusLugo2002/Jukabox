<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import type { Song } from '@/components/classes/Song'
import ItemHeader from '@/components/elements/ItemHeader.vue'
import UrlsContainer from '@/components/elements/includes/UrlsContainer.vue'
import StatsContainer from '@/components/elements/includes/StatsContainer.vue'
import ArtistsLabel from '@/components/elements/includes/ArtistsLabel.vue'
import { useAPI } from '@/composables/useAPI'

const { getData } = useAPI()
const route = useRoute()
const song = ref<null | Song>(null)

let comment = ref('')

function sendReview() {
  if (comment.value) {
    alert(comment.value)
  } else {
    alert('Escribe algo pendejito')
  }
}

onMounted(async () => {
  const song_pk = route.params['song_pk']
  song.value = await getData(`songs/${song_pk}/`)
})
</script>

<template>
  <div v-if="song">
    <ItemHeader :image="song.cover" :name="song.title" :isRounded="false" :itemId="song.id" :itemType="'song'">
      <ArtistsLabel :artists="song.artists" />
    </ItemHeader>

    <div class="row">
      <div class="col-9">
        <p class="h4">Reviews</p>
        <form id="comment-input" class="mb-3" @submit.prevent="sendReview">
          <div class="form-floating">
            <textarea
              v-model="comment"
              class="form-control mb-2"
              name="comment"
              id="comment"
            ></textarea>
            <label for="comment">Your comment...</label>
          </div>
          <input class="btn btn-primary" type="submit" value="Send" />
        </form>

        <div id="comments-container">
          <div class="alert alert-primary">No comments yet. Write the first one! :)</div>
        </div>
      </div>
      <div class="col-3">
        <UrlsContainer>Where to listen</UrlsContainer>
        <StatsContainer :likes="song.likes" :comments="0">Stats</StatsContainer>
      </div>
    </div>
  </div>

  <p v-else>Loading song</p>
</template>
