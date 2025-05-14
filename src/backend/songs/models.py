from django.db import models


class Song(models.Model):
    mbid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField('artists.Artist', related_name='songs')
    albums = models.ManyToManyField('albums.Album', related_name='songs')
    genre = models.ManyToManyField('genres.Genre', related_name='songs')
    added_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    
    @property
    def cover(self):
        first_album = self.albums.first()
        return first_album.cover if first_album else 'covers/default-song.png'
    