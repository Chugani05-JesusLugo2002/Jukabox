<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuth'
import LikeButton from './LikeButton.vue'

const authStore = useAuthStore()

const { id, img, title, type } = defineProps<{
  id: number
  title: string
  type: 'artist' | 'album' | 'song'
  img?: string
}>()
</script>

<template>
  <div class="row pb-3">
    <div class="col-sm-3 col-4" v-if="img">
      <img :src="img" :alt="title + ' image'" class="rounded-3 img-fluid w-100" />
    </div>
    <div class="col d-flex flex-column justify-content-center">
      <h1 class="display-5">{{ title }}</h1>
      <p class="text-muted h5"><slot></slot></p>
    </div>
    <div class="col-sm-2 col-1 fs-1 d-flex align-items-center justify-content-end" v-if="authStore.isAuthenticated">
      <LikeButton :id="id" :type="type" />
    </div>
  </div>
</template>
