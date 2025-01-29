from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    liked_songs = models.ManyToManyField('songs.Song', blank=True)
    liked_albums = models.ManyToManyField('albums.Album', blank=True)
    liked_playlist = models.ManyToManyField('playlists.Playlist', blank=True)
    liked_artists = models.ManyToManyField('artists.Artist', blank=True)

    def __str__(self, *args, **kwargs):
        return self.user
    