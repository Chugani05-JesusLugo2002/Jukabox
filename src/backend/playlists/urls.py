from django.urls import path

from . import views

urlpatterns = [
    path('', views.playlist_list, name='playlist-list'),
    path('<int:playlist_pk>/', views.playlist_songs, name='playlist-songs'),
    path('latest/', views.latest_playlist, name='latest-playlists')
]