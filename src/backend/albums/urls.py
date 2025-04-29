from django.urls import path

from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.album_list, name='album-list'),
    path('<int:album_pk>/', views.album_detail, name='album-detail'),
    path('<int:album_pk>/songs/', views.album_songs, name='album-songs'),
    path('latest/', views.latest_albums, name='latest-albums')
]