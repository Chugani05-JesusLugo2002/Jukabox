<script setup lang="ts">
import { useAPI } from '@/composables/useAPI'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import ItemsSection from '@/components/elements/shared/ItemsSection.vue'
import MusicItem from '@/components/elements/shared/MusicItem.vue'
import AlertComp from '@/components/gui/AlertComp.vue'
import StatCounter from '@/components/elements/ProfileView/StatCounter.vue'

const route = useRoute()
const { getData } = useAPI()
const user = ref()

const likedAlbums = ref()
const likedSongs = ref()

onMounted(async () => {
  const userSlug = route.params['profile_slug']
  user.value = await getData(`users/${userSlug}/`)
  likedAlbums.value = await getData(`users/${userSlug}/liked_albums/`)
  likedSongs.value = await getData(`users/${userSlug}/liked_songs/`)
})
</script>

<template>
  <div v-if="user" class="container py-4">
    <div class="row">
      <div class="col-lg-2 col-4">
        <img :src="user.avatar" alt="profile picture" class="img-fluid rounded-circle"/>
      </div>
      <div class="col">
        <div class="row d-flex justify-content-between">
          <h1 class="col-11 mb-0">@{{ user.username }}</h1>
          <RouterLink :to="'/settings/'" class="col text-reset text-end">
            <i class="bi bi-gear" id="settings-icon" style="font-size: 2.5rem"></i>
          </RouterLink>
        </div>
        <div class="row h-100 d-flex justify-content-between mt-5">
          <StatCounter :stat="user.reviews_count">{{ $t('profile-page.reviews') }}</StatCounter>
          <StatCounter :stat="user.liked_songs_count">{{ $t('profile-page.songs') }}</StatCounter>
          <StatCounter :stat="user.liked_albums_count">{{ $t('profile-page.albums') }}</StatCounter>
          <StatCounter :stat="user.liked_artists_count">{{ $t('profile-page.artists') }}</StatCounter>
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
          <div v-if="likedAlbums.length > 0" class="row">
            <MusicItem
              v-for="album in likedAlbums"
              :key="album.id"
              :id="album.id"
              :img="album.cover"
              :type="'albums'"
            >
              {{ album.title }}
            </MusicItem>
          </div>
          <AlertComp :style="'info'" v-else>{{ $t('profile-page.placeholder1') }}</AlertComp>
        </div>
      </template>
    </ItemsSection>

    <ItemsSection class="my-5">
      <template #header>
        <p class="display-6">{{ $t('profile-page.songs') }}</p>
      </template>
      <template #default>
        <div v-if="likedSongs">
          <div v-if="likedSongs.length > 0" class="row">
            <MusicItem
              v-for="song in likedSongs"
              :key="song.id"
              :id="song.id"
              :img="song.cover"
              :type="'songs'"
            >
              {{ song.title }}
            </MusicItem>
          </div>
          <AlertComp v-else :style="'info'">{{ $t('profile-page.placeholder2') }}</AlertComp>
        </div>
      </template>
    </ItemsSection>
  </div>

  <div class="alert alert-warning text-center" v-else>El usuario no existe!</div>
</template>
