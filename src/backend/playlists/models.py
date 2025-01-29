from django.db import models


class Playlist(models.Model):
    title = models.CharField(max_length=250)
    songs = models.ManyToManyField('songs.Song', blank=True)
    creator = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name='playlists')
    created_at = models.DateField(auto_now_add=True)