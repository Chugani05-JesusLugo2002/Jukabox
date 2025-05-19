from django.urls import path

from . import views

app_name = 'importer'

urlpatterns = [
    path('', views.import_artist, name='import-artist'),
]
