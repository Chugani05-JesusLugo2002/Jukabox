<script setup lang="ts">
const { statifyUrl } = defineProps(['statifyUrl'])
</script>

<template>
  <div class="my-2">
    <img src="/imgs/statify-icon.png" alt="Statify logo" class="img-fluid col-2" />
    <a :href="statifyUrl" class="col py-3 mx-3 text-black" target="_blank">View in Statify</a>
  </div>
</template>

<style scoped lang="scss">
img {
  width: 32px;
}
</style>
