<template>
    <div class="d-flex flex-column">
        <h4><slot></slot></h4>
        <a href="https://open.spotify.com/" class="h5"><i class="bi bi-spotify px-2"></i><span>Spotify</span></a>
        <a href="https://music.youtube.com/" class="h5"><i class="bi bi-youtube px-2"></i><span>Youtube Music</span></a>
        <a href="https://music.apple.com/" class="h5"><i class="bi bi-apple px-2"></i><span>Apple Music</span></a>
    </div>
</template>

<style scoped lang="scss">
a {
    color: black;
    span {
        font-style: italic;
    }
}
</style>