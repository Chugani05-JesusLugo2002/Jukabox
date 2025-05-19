from django.urls import path

from . import views

app_name = 'songs'

urlpatterns = [
    path('', views.song_list, name='song-list'),
    path('<int:song_pk>/', views.song_detail, name='song-detail'),
    path('<int:song_pk>/like/', views.like_song, name='like-song'),
    path('<int:song_pk>/add_review/', views.add_review, name='add-review'),
    path('<int:song_pk>/reviews/', views.review_list, name='review-list'),
    path('latest/', views.latest_songs, name='latest-songs'),
]
