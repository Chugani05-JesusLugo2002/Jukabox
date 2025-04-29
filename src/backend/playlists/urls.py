from django.urls import path

from . import views

app_name = 'playlists'

urlpatterns = [
    path('', views.playlist_list, name='playlist-list'),
    path('<int:playlist_pk>/', views.playlist_songs, name='playlist-songs'),
    path('latest/', views.latest_playlist, name='latest-playlists')
]