<script setup lang="ts">
import { ref } from 'vue';

const { id, title, type } = defineProps(['id', 'title', 'type'])

const toastColor = ref(type)
const toastIcon = ref('')

switch (type) {
  case 'success':
    toastIcon.value = 'bi bi-check-lg'
    break;
  case 'danger':
    toastIcon.value = 'bi bi-slash-circle'
    break;
  default:
    toastIcon.value = 'bi bi-vinyl'
    break;
}
</script>

<template>
    <div class="toast-container position-fixed top-0 end-0 p-3">
      <div :id="id" :class="'toast text-bg-' + toastColor" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header d-flex">
          <i :class="'h5 my-0 ' + toastIcon"></i>
          <strong class="me-auto mx-2">{{ title }}</strong>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
          <slot></slot>
        </div>
      </div>
    </div>
</template>