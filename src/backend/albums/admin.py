from django.contrib import admin

from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'released_at', 'added_at')