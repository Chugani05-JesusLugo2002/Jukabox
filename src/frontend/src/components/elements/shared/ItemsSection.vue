<template>
  <section>
    <slot name="header"></slot>
    <div class="row justify-content-center mt-3">
      <slot></slot>
    </div>
  </section>
</template>

<style scoped>
.mix-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: flex-start;
}
</style>
