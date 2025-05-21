<script setup lang="ts">
const { stat } = defineProps<{
    stat: number
}>()

</script>

<template>
    <div class="col-2 d-flex flex-column align-items-center mx-2">
        <h4>{{ stat }}</h4>
        <h5 class="text-secondary"><slot></slot></h5>
    </div>
</template>