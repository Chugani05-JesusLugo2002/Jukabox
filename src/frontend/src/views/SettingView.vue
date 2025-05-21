<script setup lang="ts">
import { ref } from 'vue'
import { Modal } from 'bootstrap'
import { useAPI } from '@/composables/useAPI'
import { useToast } from 'vue-toast-notification'
import { useAuthStore } from '@/stores/useAuth'

import ViewHeader from '@/components/layout/ViewHeader.vue'

const api = useAPI()
const toast = useToast()
const authStore = useAuthStore()

const bio = ref('')
const image = ref('')

async function updateProfile() {
  const response = await api.updateProfile(bio.value)
  if (response) {
    toast.success(response.message)
  }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function imageUpload(event: any) {
  image.value = event.target.files[0]
}

async function confirmLeave() {
  const response = await api.deleteProfile()
  if (response) {
    toast.success(response.message)
    Modal.getOrCreateInstance('#confirmLeaveModal').hide()
    authStore.logout()
  }
}
</script>

<template>
  <div class="container mt-4">
    <ViewHeader>{{ $t('setting-page.title') }}</ViewHeader>

    <form @submit.prevent="updateProfile" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="avatar" class="form-label fs-5 lead">{{ $t('setting-page.pic') }}</label>
        <input
          type="file"
          id="avatar"
          class="form-control"
          @change="imageUpload"
          accept="image/*"
        />
      </div>

      <div class="mb-3">
        <label for="bio" class="form-label fs-5 lead">Bio</label>
        <textarea
          id="bio"
          v-model="bio"
          class="form-control"
          rows="4"
          :placeholder="$t('setting-page.placeholder')"
        ></textarea>
      </div>

      <div class="d-flex justify-content-between">
        <button type="submit" class="btn btn-primary">{{ $t('setting-page.button1') }}</button>
        <button
          type="button"
          class="btn btn-danger"
          data-bs-toggle="modal"
          data-bs-target="#confirmLeaveModal"
        >
          {{ $t('setting-page.button2') }}
        </button>
      </div>
    </form>

    <div
      class="modal fade"
      id="confirmLeaveModal"
      tabindex="-1"
      aria-labelledby="modalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalLabel">{{ $t('setting-page.modaltitle') }}</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            {{ $t('setting-page.modaltext') }}
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
              {{ $t('setting-page.modalbutton1') }}
            </button>
            <button @click="confirmLeave" type="button" class="btn btn-danger">
              {{ $t('setting-page.modalbutton2') }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
