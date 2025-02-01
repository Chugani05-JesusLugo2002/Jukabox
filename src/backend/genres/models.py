from django.db import models
from colorfield.fields import ColorField


class Genre(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    color = ColorField(default='#ffffff')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name