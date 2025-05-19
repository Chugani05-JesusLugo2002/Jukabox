from django.urls import path

from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.artist_list, name='artist-list'),
    path('<int:artist_pk>/', views.artist_detail, name='artist-detail'),
    path('<int:artist_pk>/albums/', views.artist_albums, name='artist-albums'),
    path('<int:artist_pk>/like/', views.like_artist, name='like-artist'),
]
