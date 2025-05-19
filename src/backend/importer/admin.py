from django.contrib import admin

from .models import ArtistLink, AlbumLink

@admin.register(AlbumLink)
class AlbumLinkAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtistLink)
class ArtistLinkAdmin(admin.ModelAdmin):
    pass