from django.db import models


class Album(models.Model):
    mbid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField('artists.Artist', related_name='albums')
    released_at = models.DateField()
    cover = models.ImageField(upload_to='covers/', default='covers/default.jpg')
    added_at = models.DateField(auto_now_add=True)
    lbz_url = models.URLField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title 