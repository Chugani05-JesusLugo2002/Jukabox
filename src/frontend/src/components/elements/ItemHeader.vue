<script setup lang="ts">
import { useAPI } from '@/composables/useAPI';
import { useAuthStore } from '@/stores/useAuth';
import { onMounted, ref } from 'vue';

const props = defineProps(['itemId', 'image', 'name', 'isRounded', 'itemType'])

const imgClass = props.isRounded ? 'img-fluid rounded-circle' : 'img-fluid rounded'

const { like } = useAPI()
const { user, isAuthenticated } = useAuthStore()

const heartColor = ref('')

switch (props.itemType) {
  case 'song':
    user?.liked_songs.forEach(song => {
      if (song.id == props.itemId) {
        heartColor.value = 'text-danger'
      }
    });
    break;
  case 'album':
    user?.liked_albums.forEach(song => {
        if (song.id == props.itemId) {
          heartColor.value = 'text-danger'
        }
      });
    break;
  case 'artist':
    user?.liked_artists.forEach(song => {
        if (song.id == props.itemId) {
          heartColor.value = 'text-danger'
        }
      });
    break;

  default:
    break;
}

async function likeItem() {
  if (user) {
    try {
      const response = await like(props.itemId, props.itemType, user.token)
      heartColor.value = heartColor.value ? '' : 'text-danger'
    } catch (error) {
      console.error(error)
    }
  }
}
</script>

<template>
  <div class="row pb-3">
    <div class="col-3" v-if="image">
      <img :src="image" :alt="name + ' image'" :class="imgClass" />
    </div>
    <div class="col d-flex flex-column justify-content-center">
      <h1 class="display-5 fw-bold">{{ name }}</h1>
      <p class="text-muted h5"><slot></slot></p>
    </div>
    <div class="col-1 display-5 d-flex align-items-center" v-if="isAuthenticated">
      <i :class="'bi bi-heart-fill likeButton ' + heartColor" @click="likeItem"></i>
    </div>
  </div>
</template>

<style scoped lang="scss">
.likeButton {
  cursor: pointer;
}
</style>
