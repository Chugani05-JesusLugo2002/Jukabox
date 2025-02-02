import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SongsView from '@/views/SongsView.vue'
import ArtistsView from '@/views/ArtistsView.vue'
import ExploreView from '@/views/ExploreView.vue'
import SongDetailView from '@/views/SongDetailView.vue'
import CommunityView from '@/views/CommunityView.vue'

const routes = [
  { path: '/', redirect: 'home' },
  { path: '/home', component: HomeView, name: 'home' },
  { path: '/explore', component: ExploreView, name: 'explore' },
  { path: '/songs', component: SongsView, name: 'song-list' },
  { path: '/songs/:song_pk/', component: SongDetailView, name: 'song-detail' },
  { path: '/artists', component: ArtistsView, name: 'artist-list' },
  { path: '/community', component: CommunityView, name: 'community' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
