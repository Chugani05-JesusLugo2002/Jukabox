from django.db import models
from colorfield.fields import ColorField

class Genre(models.Model):
    name = models.CharField(max_length=250)
    color = ColorField(default='#ffffff')

    class Meta:
        ordering = ('name',)

    def __str__(self, *args, **kwargs):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=250)
    artists = models.ManyToManyField('artists.Artist')
    released_at = models.DateField()
    album = models.ForeignKey('albums.Album', on_delete=models.PROTECT, related_name='songs', null=True, blank=True)
    url = models.URLField(max_length=250)
    genre = models.ManyToManyField(Genre, related_name='songs') 

    class Meta:
        ordering = ('title',)

    def __str__(self, *args, **kwargs):
        return self.title