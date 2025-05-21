<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuth'
import LikeButton from './shared/LikeButton.vue'

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
    <div class="col-3" v-if="img">
      <img :src="img" :alt="title + ' image'" class="rounded-3 img-fluid" />
    </div>
    <div class="col d-flex flex-column justify-content-center">
      <h1 class="display-4">{{ title }}</h1>
      <p class="text-muted h5"><slot></slot></p>
    </div>
    <div class="col-1 display-5 d-flex align-items-center" v-if="authStore.isAuthenticated">
      <LikeButton :id="id" :type="type" />
    </div>
  </div>
</template>
