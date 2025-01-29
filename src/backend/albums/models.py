from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=250)
    artists = models.ManyToManyField('artists.Artist', related_name='albums')
    released_at = models.DateField()
    cover = models.ImageField(upload_to='covers/', default='covers/default.jpg')