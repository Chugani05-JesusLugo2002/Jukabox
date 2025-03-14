from django.db import models

from shared.validators import validate_year_range

class Album(models.Model):
    mbid = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=250)
    artists = models.ManyToManyField('artists.Artist', related_name='albums')
    released_at = models.SmallIntegerField(validators=[validate_year_range])
    cover = models.ImageField(upload_to='covers/', default='covers/default.jpg')
    added_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title 