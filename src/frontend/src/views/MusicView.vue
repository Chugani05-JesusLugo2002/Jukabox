<script setup lang="ts">
import { inject } from 'vue'

import type { Album } from '@/components/classes/Album'
import type { Song } from '@/components/classes/Song'

import ViewHeader from '@/components/layout/ViewHeader.vue'
import ItemsSection from '@/components/elements/shared/ItemsSection.vue'
import MusicItem from '@/components/elements/shared/MusicItem.vue'
import ArtistLabel from '@/components/elements/shared/ArtistLabel.vue'

const mostLikedAlbums = inject<Album[]>('mostLikedAlbums')
const mostLikedSongs = inject<Song[]>('mostLikedSongs')
const latestAlbums = inject<Album[]>('latestAlbums')
</script>

<template>
  <ViewHeader>{{ $t('music-page.title') }}</ViewHeader>

  <ItemsSection v-if="mostLikedAlbums">
    <template #header>
      <h2 class="display-5 my-3">{{ $t('music-page.tag1') }}</h2>
    </template>
    <template #default>
      <MusicItem v-for="album in mostLikedAlbums" :key="album.id" :id="album.id" :img="album.cover" :type="'albums'">
        <template #default>
          {{ album.title }}
        </template>
        <template #extra>
          <ArtistLabel v-if="album.artists.length > 0" :artist="album.artists[0]"/>
        </template>
      </MusicItem>
    </template>
  </ItemsSection>

  <ItemsSection v-if="mostLikedSongs">
    <template #header>
      <h2 class="display-5 my-3">{{ $t('music-page.tag2') }}</h2>
    </template>
    <template #default>
      <MusicItem v-for="song in mostLikedSongs" :key="song.id" :id="song.id" :img="song.cover" :type="'songs'">
        <template #default>
          {{ song.title }}
        </template>
        <template #extra>
          <ArtistLabel v-if="song.artists.length > 0" :artist="song.artists[0]"/>
        </template>
      </MusicItem>
    </template>
  </ItemsSection>

  <ItemsSection v-if="latestAlbums">
    <template #header>
      <h2 class="display-5 my-3">{{ $t('music-page.tag3') }}</h2>
    </template>
    <template #default>
      <MusicItem v-for="album in latestAlbums" :key="album.id" :id="album.id" :img="album.cover" :type="'albums'">
        <template #default>
          {{ album.title }}
        </template>
        <template #extra>
          <ArtistLabel v-if="album.artists.length > 0" :artist="album.artists[0]"/>
        </template>
      </MusicItem>
    </template>
  </ItemsSection>
</template>
