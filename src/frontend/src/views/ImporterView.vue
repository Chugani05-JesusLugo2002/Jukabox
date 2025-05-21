<script setup lang="ts">
import { ref } from 'vue'
import { useToast } from 'vue-toast-notification'

import { useAPI } from '@/composables/useAPI'
import { useAuthStore } from '@/stores/useAuth'

import ViewHeader from '@/components/layout/ViewHeader.vue'
import AlertComp from '@/components/gui/AlertComp.vue'

const { importArtist } = useAPI()
const toast = useToast()
const authStore = useAuthStore()

const mbid = ref('')

async function importToAPI(mbidInput: string) {
  if (mbidInput) {
    const response = await importArtist(mbidInput)
    if (response) {
      toast.success(response.message)
      mbid.value = ''
    }
  }
}
</script>

<template>
  <ViewHeader>{{ $t('importer-page.title') }}</ViewHeader>

  <AlertComp :style="'info'">{{ $t('importer-page.alert1') }}</AlertComp>

  <div class="mb-4 px-3">
    <div class="mb-3" v-html="$t('importer-page.paragraph1')"></div>
    <div class="mb-3" v-html="$t('importer-page.paragraph2')"></div>
    <div class="mb-3">
      <ol>
        <li v-html="$t('importer-page.step1')"></li>
        <li>{{ $t('importer-page.step2') }}</li>
        <li>{{ $t('importer-page.step3') }}</li>
        <li v-html="$t('importer-page.step4')"></li>
      </ol>
    </div>
    <div class="mb-3">
      {{ $t('importer-page.paragraph3') }}
    </div>

    <form @submit.prevent="importToAPI(mbid)" v-if="authStore.isAuthenticated">
      <input
        class="form-control mb-4"
        type="text"
        id="floatingInput"
        v-model="mbid"
        :placeholder="$t('importer-page.placeholder')"
        required
      />
      <div class="text-center">
        <button type="submit" class="btn btn-primary">
          <i class="bi bi-cloud-arrow-up"></i> | {{ $t('importer-page.button') }}
        </button>
      </div>
    </form>

    <AlertComp :style="'warning'" v-else>{{ $t('importer-page.alert2') }}</AlertComp>
  </div>
</template>
