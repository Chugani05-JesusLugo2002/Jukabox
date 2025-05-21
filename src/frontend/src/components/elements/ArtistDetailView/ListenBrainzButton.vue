<script setup lang="ts">
const { lbzUrl } = defineProps(['lbzUrl'])
</script>

<template>
    <div>
        <img src="/imgs/listenbrainz-logo.svg" alt="ListenBrainz logo" class="img-fluid col-2"/>
        <a :href="lbzUrl" class="col py-3 mx-3 my-1 text-black" target="_blank">Play in ListenBrainz</a>
    </div>
</template>

<style scoped lang="scss">
img {
    width: 32px;
}
</style>
