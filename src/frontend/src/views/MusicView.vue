<script setup lang="ts">
import { inject } from 'vue'

import type { Album } from '@/components/classes/Album'
import type { Song } from '@/components/classes/Song'

import ViewHeader from '@/components/layout/ViewHeader.vue'
import ItemsSection from '@/components/elements/MusicView/ItemsSection.vue'
import AlbumItem from '@/components/elements/MusicView/AlbumItem.vue'
import SongItem from '@/components/elements/MusicView/SongItem.vue'

const mostLikedAlbums = inject<Album[]>('mostLikedAlbums')
const mostLikedSongs = inject<Song[]>('mostLikedSongs')
const latestAlbums = inject<Album[]>('latestAlbums')
</script>

<template>
  <ViewHeader>{{ $t('music-page.title') }}</ViewHeader>

  <ItemsSection :title="$t('music-page.tag1')" v-if="mostLikedAlbums">
    <AlbumItem v-for="(album, index) in mostLikedAlbums" :key="index" :album="album" />
  </ItemsSection>

  <ItemsSection :title="$t('music-page.tag2')" v-if="mostLikedSongs">
    <SongItem v-for="(song, index) in mostLikedSongs" :key="index" :song="song" />
  </ItemsSection>

  <ItemsSection :title="$t('music-page.tag3')" v-if="latestAlbums">
    <AlbumItem v-for="(album, index) in latestAlbums" :key="index" :album="album" />
  </ItemsSection>
</template>
