from django.db import models

class ArtistLink(models.Model):
    url = models.URLField()
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE, related_name='links', blank=True, null=True)

    @property
    def url_type(self):
        return 'spotify'
    
class AlbumLink(models.Model):
    url = models.URLField()
    album = models.ForeignKey('albums.Album', on_delete=models.CASCADE, related_name='links', blank=True, null=True)

    @property
    def url_type(self):
        return 'spotify'