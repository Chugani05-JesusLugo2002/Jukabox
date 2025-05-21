from django.urls import path

from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.artist_list, name='artist-list'),
    path('<int:artist_pk>/', views.artist_detail, name='artist-detail'),
    path('<int:artist_pk>/albums/', views.artist_albums, name='artist-albums'),
    path('<int:artist_pk>/albums/top/', views.artist_top_albums, name='artist-top-albums'),
    path('<int:artist_pk>/songs/', views.artist_songs, name='artist-songs'),
    path('<int:artist_pk>/songs/top/', views.artist_top_songs, name='artist-top-songs'),
    path('<int:artist_pk>/like/', views.like_artist, name='like-artist'),
    path('<int:artist_pk>/links/', views.artist_links, name='artist-links'),
]
