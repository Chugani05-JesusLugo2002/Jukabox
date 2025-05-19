import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '@/views/auth/LoginView.vue'
import SignupView from '@/views/auth/SignupView.vue'

import HomeView from '@/views/HomeView.vue'
import MusicView from '@/views/MusicView.vue'
import ExploreView from '@/views/ExploreView.vue'

import ProfileView from '@/views/details/ProfileView.vue'
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
  
  { path: '/music', component: MusicView, name: 'artist-list' },

  { path: '/songs/:song_pk', component: SongDetail, name: 'song-detail' },

  { path: '/artists/:artist_pk', component: ArtistDetail, name: 'artist-detail' },

  { path: '/albums/:album_pk', component: AlbumDetail, name: 'album-detail' },

  { path: '/profiles/:profile_slug', component: ProfileView, name: 'profile-detail' },

  { path: '/importer', component: ImporterView, name: 'importer' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
