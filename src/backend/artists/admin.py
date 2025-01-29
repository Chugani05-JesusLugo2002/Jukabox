from django.contrib import admin

from .models import Artist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass