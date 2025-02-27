from django.db import models

from shared.validators import validate_year_range


class Song(models.Model):
    mbid = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=250)
    artists = models.ManyToManyField('artists.Artist', related_name='songs')
    released_at = models.SmallIntegerField(validators=[validate_year_range])
    album = models.ForeignKey('albums.Album', on_delete=models.PROTECT, related_name='songs', null=True, blank=True)
    genre = models.ManyToManyField('genres.Genre', related_name='songs')
    cover = models.ImageField(upload_to='covers/', default='covers/default.jpg')
    added_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    