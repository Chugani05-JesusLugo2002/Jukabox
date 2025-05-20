<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuth'

const authStore = useAuthStore()
</script>

<template>
  <div class="container">
    <div class="row mt-5 justify-content-center">
      <div class="col-10 text-center">
        <h1 class="display-5 fw-bold text-body-emphasis mb-3">
          <i class="bi bi-boombox-fill"></i> {{ $t('home-page.tag1') }}
        </h1>
        <p class="lead">
          {{ $t('home-page.text1') }}
        </p>
        <div v-if="!authStore.isAuthenticated" class="mt-3 d-flex flex-column align-items-center">
          <router-link to="/login" class="btn btn-primary w-50">
            <i class="bi bi-box-arrow-in-right"></i> {{ $t('home-page.button1') }}
          </router-link>
          <router-link to="/signup" class="btn btn-outline-primary w-50 mt-2">
            <i class="bi bi-person-fill-add"></i> {{ $t('home-page.button2') }}
          </router-link>
        </div>
      </div>
    </div>

    <!-- <div class="row mt-5">
      <div class="col">
        <img src="" class="img-fluid rounded" alt="User profile example" />
      </div>
      <div class="col text-center align-items-center">
        <h2 class="fw-bold"><i class="bi bi-vinyl-fill"></i> As a listener...</h2>
        <p class="lead">
          Search and save the songs you love, follow your favorite artists, and create playlists that match your mood. Share your discoveries with the community and see what your friends are listening to.
        </p>
      </div>
    </div> -->

    <div class="row mt-5">
      <div class="col-md-6">
        <img src="/imgs/explorer.png" class="img-fluid rounded" alt="Explorer example" />
      </div>
      <div class="col-md-6 text-center d-flex flex-column justify-content-center mt-5">
        <h2 class="fw-bold"><i class="bi bi-search-heart"></i> {{ $t('home-page.tag2') }}</h2>
        <p class="lead">
          {{ $t('home-page.text2') }}
        </p>
      </div>
    </div>

    <div class="row mt-5">
      <div
        class="col-md-6 text-center d-flex flex-column justify-content-center order-2 order-md-1 mt-5"
      >
        <h2 class="fw-bold"><i class="bi bi-cloud-download"></i> {{ $t('home-page.tag3') }}</h2>
        <p class="lead">
          {{ $t('home-page.text3') }}
        </p>
      </div>
      <div class="col-md-6 order-1">
        <img src="/imgs/importer.png" class="img-fluid rounded" alt="Importer example" />
      </div>
    </div>
  </div>
</template>
