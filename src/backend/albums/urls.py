from django.urls import path

from . import views

urlpatterns = [
    path('', views.album_list, name='album-list'),
    path('<int:album_pk>/', views.album_detail, name='album-detail'),
    path('latest/', views.latest_albums, name='latest-albums')
]