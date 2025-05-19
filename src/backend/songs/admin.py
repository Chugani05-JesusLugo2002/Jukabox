from django.contrib import admin

from .models import Song, Review

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
