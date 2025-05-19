from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('<int:user_id>/', views.user_detail, name='user-detail'),
    path('<int:user_id>/liked_songs/', views.liked_songs, name='liked-songs'),
    path('<int:user_id>/liked_albums/', views.liked_albums, name='liked-albums'),
    path('<int:user_id>/liked_artists/', views.liked_artists, name='liked-artists'),
    path('<int:user_id>/reviews/', views.user_reviews, name='user-reviews'),
    path('my-profile/', views.my_profile, name='my-profile')
]
