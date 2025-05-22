<script setup lang="ts">
import ArtistLabel from '../shared/ArtistLabel.vue'
import ItemList from './ItemList.vue'
import LikesCounter from '@/components/gui/LikesCounter.vue'
import ReviewsCounter from '@/components/gui/ReviewsCounter.vue'

const { result } = defineProps(['result'])
</script>

<template>
  <div class="list-group" v-if="result.result.hasOwnProperty('artists')">
    <ItemList
      v-for="artist in result.result.artists"
      :key="artist.id"
      :id="artist.id"
      :img="artist.avatar"
      :type="'artist'"
      :lbzUrl="artist.lbz_url"
    >
      <template #default>{{ artist.name }}</template>
      <template #stats>
        <LikesCounter :likes="artist.likes" />
      </template>
    </ItemList>
  </div>
  <div class="list-group" v-if="result.result.hasOwnProperty('albums')">
    <ItemList
      v-for="album in result.result.albums"
      :key="album.id"
      :id="album.id"
      :img="album.cover"
      :type="'album'"
      :lbzUrl="album.lbz_url"
    >
      <template #default>{{ album.title }}</template>
      <template #credits v-if="album.artists.length > 0">
        by <ArtistLabel :artist="album.artists[0]" />
      </template>
      <template #stats>
        <LikesCounter :likes="album.likes" />
      </template>
    </ItemList>
  </div>
  <div class="list-group" v-if="result.result.hasOwnProperty('songs')">
    <ItemList
      v-for="song in result.result.songs"
      :key="song.id"
      :id="song.id"
      :img="song.cover"
      :type="'song'"
      :lbzUrl="song.lbz_url"
    >
      <template #default>{{ song.title }}</template>
      <template #credits v-if="song.artists.length > 0">
        by <ArtistLabel :artist="song.artists[0]" />
      </template>
      <template #stats>
        <LikesCounter :likes="song.likes" />
        <ReviewsCounter :reviews="song.reviews" />
      </template>
    </ItemList>
  </div>
</template>
