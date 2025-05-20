<script setup lang="ts">
const emit = defineEmits(['changeTheme'])
const { themeIconClass } = defineProps(['themeIconClass'])
</script>

<template>
    <div class="btn-group text-success px-2">
          <button
            type="button"
            class="btn btn-outline-primary dropdown-toggle"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <i :class="themeIconClass"></i>
          </button>
          <ul class="dropdown-menu">
            <li class="dropdown-item" @click="emit('changeTheme', 'light')">
              <i class="bi bi-brightness-high-fill"></i> {{ $t('footer.light') }}
            </li>
            <li class="dropdown-item" @click="emit('changeTheme', 'dark')">
              <i class="bi bi-moon-stars-fill"></i> {{ $t('footer.dark') }}
            </li>
          </ul>
        </div>
</template>

<style scoped lang="scss">
.dropdown-item {
  cursor: pointer;
}</style>