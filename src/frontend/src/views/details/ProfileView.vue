<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuth'
import { useAPI } from '@/composables/useAPI'
import ViewHeader from '@/components/layout/ViewHeader.vue'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const { getData } = useAPI()
const user = ref()
const userFound = ref(false)

onMounted(async () => {
  user.value = await getData(`users/${route.params['profile_slug']}/`)
  userFound.value = !user.value.hasOwnProperty('error')
})
</script>

<template>
  <div v-if="userFound" class="container py-4">
    <div class="row">
      <img :src="user.avatar" alt="Foto de perfil" class="col-2 rounded-circle" />
      <div class="col">
        <h1 class="row">@{{ user.username }}</h1>
        <div class="row mt-5">
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.reviews_count }}</h4>
            <h5 class="text-secondary">Reviews</h5>
          </div>
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.liked_songs_count }}</h4>
            <h5 class="text-secondary">Liked songs</h5>
          </div>
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.liked_albums_count }}</h4>
            <h5 class="text-secondary">Liked albums</h5>
          </div>
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.liked_artists_count }}</h4>
            <h5 class="text-secondary">Liked artists</h5>
          </div>
        </div>
      </div>
    </div>

    <div class="mt-4">
      <p v-if="user.bio" class="text-secondary">
        {{ user.bio }}
      </p>
      <p v-else>
        {{ $t('profile-page.nobiomessage') }}
      </p>
    </div>

    <div class="mt-4 row text-center">
      <div class="col">
        <!-- <div class="fw-bold fs-4">{{ user.songs.length }}</div> -->
        <small class="text-secondary">{{ $t('profile-page.featuredsongs') }}</small>
      </div>
      <div id="carouselExampleCaptions" class="carousel slide">
        <div class="carousel-indicators">
          <button
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide-to="0"
            class="active"
            aria-current="true"
            aria-label="Slide 1"
          ></button>
          <button
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide-to="1"
            aria-label="Slide 2"
          ></button>
          <button
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide-to="2"
            aria-label="Slide 3"
          ></button>
        </div>
        <div class="carousel-inner">
          <div v-for="song in likedSongs" class="carousel-item">
            <img :src="song.cover" class="d-block w-100" alt="..." />
            <div class="carousel-caption d-none d-md-block">
              <h5>{{ song.title }}</h5>
            </div>
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </div>

  <div class="alert alert-warning text-center" v-else>El usuario no existe!</div>
</template>
