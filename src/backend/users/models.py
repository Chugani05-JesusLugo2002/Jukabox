from django.db import models
from django.conf import settings
import uuid

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    token = models.UUIDField(default=uuid.uuid4)
    bio = models.TextField(blank=True)
    liked_songs = models.ManyToManyField('songs.Song', blank=True, related_name='likes')
    liked_albums = models.ManyToManyField('albums.Album', blank=True, related_name='likes')
    liked_artists = models.ManyToManyField('artists.Artist', blank=True, related_name='likes')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username