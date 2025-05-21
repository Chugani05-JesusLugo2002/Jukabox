from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('change-profile/', views.change_profile, name='change-profile'),
    path('leave/', views.user_leave, name='user-leave'),
    path('<slug:user_slug>/', views.user_detail, name='user-detail'),
    path('<slug:user_slug>/liked_songs/', views.liked_songs, name='liked-songs'),
    path('<slug:user_slug>/liked_albums/', views.liked_albums, name='liked-albums'),
    path('<slug:user_slug>/liked_artists/', views.liked_artists, name='liked-artists'),
    path('<slug:user_slug>/reviews/', views.user_reviews, name='user-reviews'),
]
