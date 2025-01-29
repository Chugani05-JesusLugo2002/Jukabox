# Generated by Django 5.1.5 on 2025-01-29 22:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0001_initial'),
        ('playlists', '0001_initial'),
        ('songs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='avatars/default.jpg', upload_to='avatars/')),
                ('liked_albums', models.ManyToManyField(blank=True, to='albums.album')),
                ('liked_artists', models.ManyToManyField(blank=True, to='artists.artist')),
                ('liked_playlist', models.ManyToManyField(blank=True, to='playlists.playlist')),
                ('liked_songs', models.ManyToManyField(blank=True, to='songs.song')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
