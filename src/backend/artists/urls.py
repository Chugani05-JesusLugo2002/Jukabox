from django.urls import path

from . import views

urlpatterns = [
    path('', views.artist_list, name='artist-list'),
    path('<int:artist_pk>/', views.artist_detail, name='artist-detail'),
    path('latest/', views.latest_artists, name='latest-artists')
]
