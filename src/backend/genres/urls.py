from django.urls import path

from . import views

app_name = 'genres'

urlpatterns = [
    path('', views.genre_list, name='genre-list'),
    path('<slug:genre_slug>/', views.genre_detail, name='genre-detail'),
    path('<slug:genre_slug>/songs/', views.genre_songs, name='genre-songs')
]
