from django.urls import path

from . import views

urlpatterns = [
    path('', views.song_list, name='song-list'),
    path('latest/', views.latest_songs, name='latest-songs')
]
