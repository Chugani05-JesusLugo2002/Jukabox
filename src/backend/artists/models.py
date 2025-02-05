from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    added_at = models.DateField(auto_now_add=True)
    profile = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, null=True, blank=True, related_name='artist_profile')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name