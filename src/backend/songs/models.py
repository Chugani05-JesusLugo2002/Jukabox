from django.db import models


class Song(models.Model):
    mbid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField('artists.Artist', related_name='songs')
    albums = models.ManyToManyField('albums.Album', related_name='songs')
    added_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    
    @property
    def cover(self):
        first_album = self.albums.first()
        return first_album.cover if first_album else 'covers/default-song.png'
    
    @property
    def lbz_url(self):
        return f'https://listenbrainz.org/player/?recording_mbids={self.mbid}'
    

class Review(models.Model):
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name='reviews')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} in {self.song}'
    