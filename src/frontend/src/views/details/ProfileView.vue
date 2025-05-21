<script setup lang="ts">
import { useAPI } from '@/composables/useAPI'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import ItemsSection from '@/components/elements/shared/ItemsSection.vue'
import MusicItem from '@/components/elements/shared/MusicItem.vue'
import AlertComp from '@/components/gui/AlertComp.vue'

const route = useRoute()
const { getData } = useAPI()
const user = ref()
const userFound = ref(false)

const likedAlbums = ref()
const likedSongs = ref()

onMounted(async () => {
  const userSlug = route.params['profile_slug']
  user.value = await getData(`users/${userSlug}/`)
  userFound.value = !user.value.hasOwnProperty('error')
  likedAlbums.value = await getData(`users/${userSlug}/liked_albums/`)
  likedSongs.value = await getData(`users/${userSlug}/liked_songs/`)
})
</script>

<template>
  <div v-if="userFound" class="container py-4">
    <div class="row">
      <img :src="user.avatar" alt="profile picture" class="col-2 rounded-circle" />
      <div class="col">
        <div class="d-flex justify-content-between align-items-center">
          <h1 class="mb-0">@{{ user.username }}</h1>
          <RouterLink :to="'/settings/'" class="text-reset">
            <i class="bi bi-gear" id="settings-icon" style="font-size: 2.5rem;"></i>
          </RouterLink>
        </div>
        <div class="row mt-5">
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.reviews_count }}</h4>
            <h5 class="text-secondary">{{ $t('profile-page.reviews') }}</h5>
          </div>
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.liked_songs_count }}</h4>
            <h5 class="text-secondary">{{ $t('profile-page.songs') }}</h5>
          </div>
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.liked_albums_count }}</h4>
            <h5 class="text-secondary">{{ $t('profile-page.albums') }}</h5>
          </div>
          <div class="col-1 d-flex flex-column align-items-center mx-2">
            <h4>{{ user.liked_artists_count }}</h4>
            <h5 class="text-secondary">{{ $t('profile-page.artists') }}</h5>
          </div>
        </div>
      </div>
    </div>

    <div class="mt-4 lead">
      <p v-if="user.bio">
        {{ user.bio }}
      </p>
    </div>

    <ItemsSection class="my-5">
      <template #header>
        <p class="display-6">{{ $t('profile-page.albums') }}</p>
      </template>
      <template #default>
        <div v-if="likedAlbums">
          <MusicItem v-for="album in likedAlbums" :key="album.id" :id="album.id" :img="album.cover" :type="'albums'">
            {{ album.title }}
          </MusicItem>
        </div>
        <AlertComp :style="'info'">{{ $t('profile-page.placeholder1') }}</AlertComp>
      </template>
    </ItemsSection>

    <ItemsSection class="my-5">
      <template #header>
        <p class="display-6">{{ $t('profile-page.songs') }}</p>
      </template>
      <template #default>
        <div v-if="likedSongs">
          <MusicItem v-for="song in likedSongs" :key="song.id" :id="song.id" :img="song.cover" :type="'songs'">
            {{ song.title }}
          </MusicItem>
        </div>
        <AlertComp :style="'info'">{{ $t('profile-page.placeholder2') }}</AlertComp>
      </template>
    </ItemsSection>
  </div>

  <div class="alert alert-warning text-center" v-else>El usuario no existe!</div>
</template>
