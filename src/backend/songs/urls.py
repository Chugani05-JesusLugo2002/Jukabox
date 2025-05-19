from django.urls import path

from . import views

app_name = 'songs'

urlpatterns = [
    path('', views.song_list, name='song-list'),
    path('<int:song_pk>/', views.song_detail, name='song-detail'),
    path('<int:song_pk>/like/', views.like_song, name='like-song'),
    path('<int:song_pk>/links/', views.song_links, name='song-links'),
    path('<int:song_pk>/add-review/', views.add_review, name='add-review'),
    path('<int:song_pk>/reviews/', views.song_reviews, name='song-reviews'),
    path('latest/', views.latest_songs, name='latest-songs'),
]
