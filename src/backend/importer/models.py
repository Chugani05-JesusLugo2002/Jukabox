from django.db import models

class ArtistLink(models.Model):
    url = models.URLField()
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE, related_name='links', blank=True, null=True)

    @property
    def url_type(self):
        POSSIBLE_TYPES = ['spotify', 'deezer', 'youtube', 'statify', 'bandcamp']
        for type in POSSIBLE_TYPES:
            if type in self.url:
                return type
        return 'undefined'
    
    
class AlbumLink(models.Model):
    url = models.URLField()
    album = models.ForeignKey('albums.Album', on_delete=models.CASCADE, related_name='links', blank=True, null=True)

    @property
    def url_type(self):
        POSSIBLE_TYPES = ['spotify', 'deezer', 'youtube', 'statify', 'bandcamp']
        for type in POSSIBLE_TYPES:
            if type in self.url:
                return type
        return 'undefined'
        
