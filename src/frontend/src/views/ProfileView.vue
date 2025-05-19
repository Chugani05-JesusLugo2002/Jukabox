<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuth'
import { useAPI } from '@/composables/useAPI'
import ViewHeader from '@/components/ViewHeader.vue'
import { onMounted } from 'vue'

const { user } = useAuthStore()
const { getData } = useAPI()

const likedSongs = await getData(`users/${user?.id}/liked_songs/`)


</script>

<template>
  <div v-if="user" class="container py-4">
    <ViewHeader>
      <div class="d-flex align-items-center gap-4">
        <img
          :src="user.avatar"
          alt="Foto de perfil"
          class="rounded-circle border border-white shadow"
          style="width: 250px; height: 250px; object-fit: cover;"
        />
        <div>
          <div>
            <p class="text-dark">@{{ user.username }}</p>
          </div>

          <div class="mt-4 row text-center">
            <div class="col">
              <!-- <div class="fw-bold fs-4">{{ user.followers.length }}</div> -->
              <small class="text-secondary">{{ $t('profile-page.followers') }}:</small>
            </div>
            <div class="col">
              <!-- <div class="fw-bold fs-4">{{ user.following.length }}</div> -->
              <small class="text-secondary">{{ $t('profile-page.following') }}:</small>
            </div>
          </div>
          
        </div>
      </div>
    </ViewHeader>

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
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div v-for="song in likedSongs" class="carousel-item">
            <img :src="song.cover" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{ song.title }}</h5>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </div>

  <ViewHeader v-else>
    <div class="alert alert-warning text-center">
      No deberías estar aquí :(
    </div>
  </ViewHeader>
</template>
