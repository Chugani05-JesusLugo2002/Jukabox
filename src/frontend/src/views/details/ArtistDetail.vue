<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import { useAPI } from '@/composables/useAPI'

import ItemHeader from '@/components/elements/ItemHeader.vue'
import ItemsSection from '@/components/elements/shared/ItemsSection.vue'
import MusicItem from '@/components/elements/shared/MusicItem.vue'
import SectionHeader from '@/components/elements/ArtistDetailView/SectionHeader.vue'
import ListenBrainzButton from '@/components/elements/ArtistDetailView/ListenBrainzButton.vue'
import StatifyButton from '@/components/elements/ArtistDetailView/StatifyButton.vue'

const { getData } = useAPI()
const route = useRoute()

const artist = ref()
const topAlbums = ref()
const topSongs = ref()
const statifyUrl = ref()

onMounted(async () => {
  const artist_pk = route.params['artist_pk']
  artist.value = await getData(`artists/${artist_pk}/`)
  topAlbums.value = await getData(`artists/${artist_pk}/albums/top/`)
  topSongs.value = await getData(`artists/${artist_pk}/songs/top/`)

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  artist.value.links.forEach((link: any) => {
    if (link['url_type'] == 'statify') {
      statifyUrl.value = link['url']
    }
  });
})
</script>

<template>
  <div v-if="artist">
    <ItemHeader :title="artist.name" :id="artist.id" :type="'artist'">
      <ListenBrainzButton :lbzUrl="artist.lbz_url" />
      <StatifyButton v-if="statifyUrl" :statifyUrl="statifyUrl"></StatifyButton>
    </ItemHeader>

    <ItemsSection v-if="topAlbums" class="my-5">
      <template #header>
        <SectionHeader :id="artist.id" :type="'albums'" />
      </template>
      <template #default>
        <MusicItem
          v-for="album in topAlbums"
          :key="album.id"
          :id="album.id"
          :img="album.cover"
          :type="'albums'"
        >
          {{ album.title }}
        </MusicItem>
      </template>
    </ItemsSection>

    <ItemsSection v-if="topSongs" class="my-5">
      <template #header>
        <SectionHeader :id="artist.id" :type="'songs'" />
      </template>
      <template #default>
        <MusicItem
          v-for="song in topSongs"
          :key="song.id"
          :id="song.id"
          :img="song.cover"
          :type="'songs'"
        >
          {{ song.title }}
        </MusicItem>
      </template>
    </ItemsSection>
  </div>

  <p v-else>Loading artist</p>
</template>
