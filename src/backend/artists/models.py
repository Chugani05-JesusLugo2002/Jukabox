from django.db import models

class Artist(models.Model):
    mbid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    added_at = models.DateField(auto_now_add=True)
    avatar = models.ImageField(default='/avatars/default.jpg', upload_to='avatars/')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    @property
    def lbz_url(self):
        return f'https://listenbrainz.org/artist/{self.mbid}/'