import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '@/views/auth/LoginView.vue'
import SignupView from '@/views/auth/SignupView.vue'

import HomeView from '@/views/HomeView.vue'
import SongsView from '@/views/SongsView.vue'
import ArtistsView from '@/views/ArtistsView.vue'
import ExploreView from '@/views/ExploreView.vue'
import ProfileView from '@/views/ProfileView.vue'

import SongDetail from '@/views/details/SongDetail.vue'
import ArtistDetail from '@/views/details/ArtistDetail.vue'
import AlbumDetail from '@/views/details/AlbumDetail.vue'
import ImporterView from '@/views/ImporterView.vue'

const routes = [
  { path: '/', redirect: 'home' },
  { path: '/home', component: HomeView, name: 'home' },

  { path: '/login', component: LoginView, name: 'login' },
  { path: '/signup', component: SignupView, name: 'signup' },

  { path: '/explore', component: ExploreView, name: 'explore' },

  { path: '/songs', component: SongsView, name: 'song-list' },
  { path: '/songs/:song_pk', component: SongDetail, name: 'song-detail' },

  { path: '/artists', component: ArtistsView, name: 'artist-list' },
  { path: '/artists/:artist_pk', component: ArtistDetail, name: 'artist-detail' },

  { path: '/albums/:album_pk', component: AlbumDetail, name: 'album-detail' },

  { path: '/profile', component: ProfileView, name: 'my-profile' },

  { path: '/importer', component: ImporterView, name: 'importer' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
