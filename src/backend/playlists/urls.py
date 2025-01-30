from django.urls import path

from . import views

urlpatterns = [
    path('', views.playlist_list, name='playlist-list')
]