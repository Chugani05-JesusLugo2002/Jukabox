from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')