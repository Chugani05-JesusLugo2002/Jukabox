from django.contrib import admin

from .models import ArtistLink, AlbumLink

@admin.register(AlbumLink)
class AlbumLinkAdmin(admin.ModelAdmin):
    list_display = ['url_type', 'album']

@admin.register(ArtistLink)
class ArtistLinkAdmin(admin.ModelAdmin):
    list_display = ['url_type', 'artist']