from django.contrib import admin

from .models import Song, Genre

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'released_at')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass