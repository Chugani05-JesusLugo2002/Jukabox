from django.urls import path

from . import views

urlpatterns = [
    path('', views.genre_list, name='genre-list'),
    path('<slug:genre_slug>/songs/', views.genre_songs, name='genre-songs')
]
