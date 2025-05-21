<script setup lang="ts">
const { img, type, id } = defineProps<{
    id: number
    img: string
    type: 'songs'|'albums'
}>()
</script>

<template>
    <div class="col-lg-3 col-xl-2 col-5 fw-bold text-decoration-none">
        <div class="card border-0">
            <RouterLink :to="`/${type}/${id}`">
                <img :src="img" :alt="`${type} ${id} image`" class="img-fluid rounded-5 shadow">
            </RouterLink>
        </div>
        <div class="card-body text-center mt-3">
            <RouterLink :to="`/${type}/${id}`" class="text-black text-decoration-none">
                <h5><slot></slot></h5>
            </RouterLink>
            <slot name="extra"></slot>
        </div>
    </div>
</template>

<style scoped lang="scss">
.card {
    transition: 0.3s;
    &:hover {
        transform: scale(1.05);
    }
}
</style>