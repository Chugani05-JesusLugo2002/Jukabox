<script setup lang="ts">
import { ref, onMounted } from 'vue'

import { useToast } from 'vue-toast-notification'
import type { Song } from '@/components/classes/Song'
import type { Album } from '@/components/classes/Album'
import type { Artist } from '@/components/classes/Artist'
import { useSocial } from '@/composables/useSocial'
import { useAuthStore } from '@/stores/useAuth'

const social = useSocial()
const toast = useToast()
const { user } = useAuthStore()
const { id, type } = defineProps<{
  id: number
  type: 'artist' | 'album' | 'song'
}>()

const heartColor = ref('')

async function likeItem() {
  const response = await social.likeItem(id, type)
  if (response) {
    toast.info(response.message)
    heartColor.value = heartColor.value ? '' : 'text-danger'
  }
}

onMounted(async () => {
  if (user) {
    const likedItems = await social.getLikedItems(user.slug, type)
    if (likedItems) {
      likedItems.every((item: Song | Artist | Album) => {
        if (item.id == id) {
          heartColor.value = 'text-danger'
          return false
        }
      })
    }
  }
})
</script>

<template>
  <i :class="'bi bi-heart-fill likeButton ' + heartColor" @click="likeItem"></i>
</template>

<style scoped lang="scss">
i {
  cursor: pointer;
}
</style>
