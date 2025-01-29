from django.contrib import admin

from .models import Playlist

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at')