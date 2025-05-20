<script setup lang="ts">
import ViewHeader from '@/components/ViewHeader.vue'
import { useAPI } from '@/composables/useAPI'
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale, t } = useI18n()
const { importArtist } = useAPI()

const mbid = ref('')
const modalMessage = ref('')

async function importToAPI(mbid: string) {
  if (mbid) {
    const response = await importArtist(mbid)
    modalMessage.value = response.message
  }
}
</script>

<template>
  <ViewHeader>{{ $t('importer-page.title') }}</ViewHeader>

  <div class="d-flex justify-content-center my-4">
    <div class="border rounded p-4 text-center bg-light" style="min-width: 300px">
      <h4>{{ $t('importer-page.tag1') }}</h4>
    </div>
  </div>

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

    <input
      class="form-control mb-4"
      type="text"
      id="floatingInput"
      v-model="mbid"
      :placeholder="$t('importer-page.placeholder')"
      required
    />

    <div class="text-center">
      <button
        type="button"
        class="btn btn-primary"
        @click="importToAPI(mbid)"
        data-bs-toggle="modal"
        data-bs-target="#importerModal"
      >
        {{ $t('importer-page.button') }}
      </button>
    </div>

    <div
      class="modal fade"
      id="importerModal"
      tabindex="-1"
      aria-labelledby="importerModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="importerModalLabel">Importing artist...</h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            {{ modalMessage }}
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Ok!</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
