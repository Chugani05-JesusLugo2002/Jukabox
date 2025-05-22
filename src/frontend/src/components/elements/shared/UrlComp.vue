<script setup lang="ts">
type Link = {
  url: string
  url_type: string
}

const { link } = defineProps<{
  link: Link
}>()
</script>

<template>
  <a
    :href="link.url"
    :class="`btn btn-light py-2 my-1 w-100 fw-bold border d-flex justify-content-center align-items-center ${link.url_type}`"
    target="_blank"
  >
    <i v-if="link.url_type == 'spotify'" class="bi bi-spotify h4 px-2 m-0"></i>
    <i v-else-if="link.url_type == 'youtube'" class="bi bi-youtube h3 m-0 px-2"></i>
    <img
      v-else-if="link.url_type == 'deezer'"
      src="/imgs/deezer-logo.svg"
      style="height: 32px"
      class="mx-2"
    />
    <img
      v-else-if="link.url_type == 'bandcamp'"
      src="/imgs/bandcamp-logo.png"
      style="height: 32px"
      class="mx-2"
    />
    <img
      v-else-if="link.url_type == 'statify'"
      src="/imgs/statify-icon.png"
      style="height: 32px"
      class="mx-2"
    />
    <i v-else class="bi bi-music-note h3 px-2 m-0 h4"></i>
    <slot></slot>
  </a>
</template>

<style scoped lang="scss">
a {
  transition: 0.5s;
  background-color: white;
  color: black;
  &:hover {
    transform: scale(1.05);
  }
}
.spotify {
  i {
    color: #1db954;
  }
  &:hover {
    background: linear-gradient(to left, #1db954, #191414);
    color: white;
  }
  &:hover i {
    color: white
  }
}
.statify:hover {
  background: linear-gradient(to right, #2d0036, #004d00);
  color: white;
}
.deezer:hover {
  background: linear-gradient(to left, #5d1c63, #c92b68);
  color: white;
}
.bandcamp:hover {
  background: linear-gradient(to right, #315b66, #ffffff);
}
.youtube {
  i {
    color: #ff0000;
  }
  &:hover {
    background: linear-gradient(to right, #ff0000, #282828);
    color: white;
  }
  &:hover i {
    color: white;
  }
}
</style>
