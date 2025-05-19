from django.contrib import admin

from .models import SongLink, ArtistLink, AlbumLink

@admin.register(SongLink)
class SongLinkAdmin(admin.ModelAdmin):
    pass

@admin.register(AlbumLink)
class AlbumLinkAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtistLink)
class ArtistLinkAdmin(admin.ModelAdmin):
    pass