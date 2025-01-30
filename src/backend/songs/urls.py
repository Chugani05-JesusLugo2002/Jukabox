from django.urls import path

from . import views

urlpatterns = [
    path('', views.song_list, name='song-list'),
    path('<int:song_pk>/', views.song_detail, name='song-detail'),
    path('latest/', views.latest_songs, name='latest-songs')
]
