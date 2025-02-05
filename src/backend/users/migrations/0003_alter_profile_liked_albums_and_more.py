# Generated by Django 5.1.5 on 2025-02-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0003_alter_artist_profile'),
        ('playlists', '0003_alter_playlist_songs'),
        ('songs', '0003_delete_genre_alter_song_genre'),
        ('users', '0002_profile_token_alter_profile_liked_albums_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='liked_albums',
            field=models.ManyToManyField(blank=True, related_name='hearts', to='albums.album'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_artists',
            field=models.ManyToManyField(blank=True, related_name='hearts', to='artists.artist'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_playlist',
            field=models.ManyToManyField(blank=True, related_name='hearts', to='playlists.playlist'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_songs',
            field=models.ManyToManyField(blank=True, related_name='hearts', to='songs.song'),
        ),
    ]
