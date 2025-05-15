<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col">
        <h1 class="display-5 fw-bold text-body-emphasis text-center mb-3">
          <i class="bi bi-boombox-fill"></i> Welcome to Jukabox
        </h1>
        <p class="lead text-center">
          Discover, share, and connect through music. Explore your favorite songs, albums, and artists — all in one place. Jukabox is the ultimate social experience for music lovers.
        </p>
        <div class="mt-3 d-flex flex-column align-items-center mt-5">
          <router-link to="/login" class="btn btn-primary w-50">
            <i class="bi bi-box-arrow-in-right"></i> Login
          </router-link>
          <router-link to="/signup" class="btn btn-outline-primary w-50 mt-2">
            <i class="bi bi-person-fill-add"></i> Register
          </router-link>
        </div>
      </div>
      <div class="col">
        <img src="" class="img-fluid rounded" alt="" />
      </div>
    </div>

    <!-- <div class="row mt-5">
      <div class="col">
        <img src="" class="img-fluid rounded" alt="User profile example" />
      </div>
      <div class="col text-center align-items-center">
        <h2 class="fw-bold"><i class="bi bi-vinyl-fill"></i> As a listener...</h2>
        <p class="lead">
          Search and save the songs you love, follow your favorite artists, and create playlists that match your mood. Share your discoveries with the community and see what your friends are listening to.
        </p>
      </div>
    </div> -->

    <div class="row mt-5">
      <div class="col">
        <img src="\public\imgs\explorer.png" class="img-fluid rounded" alt="Explorer example" />
      </div>
      <div class="col text-center align-items-center mt-5">
        <h2 class="fw-bold"><i class="bi bi-search-heart"></i> Discover music you love</h2>
        <p class="lead">
          Use the Explorer to search for your favorite songs, artists, or albums. Discover new music, follow other users who share your taste, and share your favorite discoveries with your friends.
        </p>
      </div>
    </div>

    <div class="row mt-5">
      <div class="col text-center align-items-center mt-5">
        <h2 class="fw-bold"><i class="bi bi-cloud-download"></i> Can't find an artist?</h2>
        <p class="lead">
          Use the Importer to bring in artists not yet available on Jukabox. Our integration with <strong>MusicBrainz</strong> lets you fetch artist profiles directly from a global music database.
        </p>
      </div>
      <div class="col">
        <img src="\public\imgs\importer.png" class="img-fluid rounded" alt="Importer example" />
      </div>
    </div>
  </div>
</template>
