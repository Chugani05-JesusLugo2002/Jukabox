import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SongsView from '@/views/SongsView.vue'
import ArtistListView from '@/views/ArtistListView.vue'

const routes = [
  { path: '/', component: HomeView, name: 'home' },
  { path: '/songs', component: SongsView, name: 'song-list' },
  { path: '/artists', component: ArtistListView, name: 'artist-list' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
