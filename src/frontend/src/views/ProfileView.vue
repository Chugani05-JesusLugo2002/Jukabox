<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuth'
import ViewHeader from '@/components/ViewHeader.vue'

const { user } = useAuthStore()
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
          <p class="text-dark">@{{ user.username }}</p>

          <div class="mt-4 row text-center">
            <div class="col">
              <!-- <div class="fw-bold fs-4">{{ user.followers.length }}</div> -->
              <small class="text-secondary">Followers:</small>
            </div>
            <div class="col">
              <!-- <div class="fw-bold fs-4">{{ user.following.length }}</div> -->
              <small class="text-secondary">Following:</small>
            </div>
          </div>
          
        </div>
      </div>
    </ViewHeader>

    <!-- Biografía -->
    <div class="mt-4">
      <h2 class="h5">Biography</h2>
      <p class="text-secondary">
        <!-- {{ user.bio || "Este usuario aún no ha escrito una biografía." }} -->
      </p>
    </div>

    <!-- Estadísticas -->
    <div class="mt-4 row text-center">
      <div class="col">
        <!-- <div class="fw-bold fs-4">{{ user.songs.length }}</div> -->
        <small class="text-secondary">Featured Songs</small>
      </div>
    </div>
  </div>

  <ViewHeader v-else>
    <div class="alert alert-warning text-center">
      No deberías estar aquí :(
    </div>
  </ViewHeader>
</template>
