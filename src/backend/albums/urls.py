from django.urls import path

from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.album_list, name='album-list'),
    path('<int:album_pk>/', views.album_detail, name='album-detail'),
    path('<int:album_pk>/songs/', views.album_songs, name='album-songs'),
    path('<int:album_pk>/like/', views.like_album, name='like-album'),
    path('<int:album_pk>/links/', views.album_links, name='album-links'),
    path('latest/', views.latest_albums, name='latest-albums'),
    path('most-liked/', views.most_liked_albums, name='most-liked-albums'),
]