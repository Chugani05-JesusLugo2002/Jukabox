# Generated by Django 5.1.5 on 2025-05-19 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0002_albumlink_album_artistlink_artist_songlink_song'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SongLink',
        ),
    ]
